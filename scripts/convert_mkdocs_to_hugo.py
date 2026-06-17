"""Convert the MkDocs source tree into Hugo/Docsy input files.

The script is intentionally idempotent so the Hugo preview branch can be rebuilt
from the latest `main` branch content in CI without committing generated files.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

ADMONITION_RE = re.compile(
    r'^(?P<indent> *)(?P<kind>!!!|\?\?\?)\s+'
    r'(?P<type>[A-Za-z0-9_-]+)(?:\s+"(?P<title>[^"]+)")?\s*$'
)
DATE_INDEX_RE = re.compile(r'\{\{\s*date_index\((?P<args>.*?)\)\s*\}\}')
INCLUDE_RE = re.compile(r"\{%\s*include\s+['\"](?P<path>[^'\"]+)['\"]\s*%\}")
MITRE_RE = re.compile(r'\{\{\s*mitre\(\s*["\']?(?P<id>[A-Za-z0-9.]+)["\']?\s*\)\s*\}\}')
TITLE_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.MULTILINE)

EXCLUDED_DIRS = frozenset({"markdown-templates"})

SECTION_TITLES: dict[str, str] = {
    "advisories": "Advisories (TLP:CLEAR)",
    "baselines": "Baselines",
    "guidelines": "Guidelines",
    "onboarding": "Connecting to the WASOC",
    "training": "Training",
}

# Sections whose child pages should be hidden from the sidebar navigation
# (they are browsed via shortcodes like date_index instead).
SIDEBAR_HIDDEN_CHILDREN: frozenset[str] = frozenset({"advisories"})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        type=Path,
        default=Path("."),
        help="Repository root containing mkdocs.yml and docs/.",
    )
    parser.add_argument(
        "--target-root",
        type=Path,
        default=Path("."),
        help="Hugo branch checkout root to write generated content/static files into.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help=(
            "Remove generated Hugo content/static asset directories before "
            "converting."
        ),
    )
    return parser.parse_args()


def hugo_page_path(source: Path, docs_dir: Path, content_dir: Path) -> Path:
    relative = source.relative_to(docs_dir)
    if relative == Path("README.md"):
        return content_dir / "_index.md"
    # If docs/Foo.md has a matching docs/Foo/ directory, make it the section index
    stem = relative.stem
    parent = source.parent
    if (parent / stem).is_dir():
        return content_dir / relative.parent / stem / "_index.md"
    if relative.name == "README.md":
        return content_dir / relative.parent / "_index.md"
    return content_dir / relative


def shortcode_attrs(**attrs: str | int) -> str:
    return " ".join(f'{key}="{value}"' for key, value in attrs.items())


def convert_macros(markdown: str) -> str:
    def date_index(match: re.Match[str]) -> str:
        args = match.group("args")
        attrs: dict[str, str] = {}
        for key in ("expand", "include"):
            key_match = re.search(rf"{key}\s*=\s*(\d+)", args)
            if key_match:
                attrs[key] = key_match.group(1)
        if not attrs:
            return "{{% date_index %}}"
        return f"{{{{% date_index {shortcode_attrs(**attrs)} %}}}}"

    def include_page(match: re.Match[str]) -> str:
        page_path = Path(match.group("path")).with_suffix("").as_posix()
        return f'{{{{< include-page path="{page_path}" >}}}}'

    def mitre(match: re.Match[str]) -> str:
        return f'{{{{< mitre id="{match.group("id")}" >}}}}'

    markdown = DATE_INDEX_RE.sub(date_index, markdown)
    markdown = INCLUDE_RE.sub(include_page, markdown)
    return MITRE_RE.sub(mitre, markdown)


def dedent_admonition_body(lines: list[str], indent_width: int) -> str:
    prefix = " " * (indent_width + 4)
    fallback = " " * indent_width
    dedented: list[str] = []
    for line in lines:
        if not line.strip():
            dedented.append("")
        elif line.startswith(prefix):
            dedented.append(line[len(prefix) :])
        elif line.startswith(fallback):
            dedented.append(line[len(fallback) :])
        else:
            dedented.append(line)
    return "\n".join(dedented).strip("\n")


def convert_admonitions(markdown: str) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        match = ADMONITION_RE.match(lines[index])
        if not match:
            output.append(lines[index])
            index += 1
            continue

        indent = match.group("indent")
        indent_width = len(indent)
        body: list[str] = []
        index += 1
        while index < len(lines):
            line = lines[index]
            if line.strip() and not line.startswith(" " * (indent_width + 4)):
                break
            body.append(line)
            index += 1

        attrs: dict[str, str] = {"type": match.group("type")}
        if title := match.group("title"):
            attrs["title"] = title
        if match.group("kind") == "???":
            attrs["collapsible"] = "true"

        output.append(f"{indent}{{{{< admonition {shortcode_attrs(**attrs)} >}}}}")
        converted_body = convert_admonitions(dedent_admonition_body(body, indent_width))
        if converted_body:
            output.extend(converted_body.splitlines())
        output.append(f"{indent}{{{{< /admonition >}}}}")
    return "\n".join(output) + ("\n" if markdown.endswith("\n") else "")


def strip_first_h1(markdown: str) -> str:
    """Remove the first H1 heading from markdown (it's in front matter title)."""
    return re.sub(r"\A\s*#\s+.+\n?", "", markdown, count=1)


def convert_markdown(markdown: str) -> str:
    return strip_first_h1(convert_admonitions(convert_macros(markdown)))


def page_title(markdown: str, source: Path) -> str:
    if source.name == "advisories.md":
        return "Advisories (TLP:CLEAR)"
    if match := TITLE_RE.search(markdown):
        return re.sub(r"\s+-\s+\d{11}$", "", match.group("title")).strip()
    return source.stem.replace("-", " ").replace("_", " ").title()


def with_front_matter(markdown: str, source: Path, title: str) -> str:
    if markdown.startswith(("---\n", "+++\n")):
        return markdown
    return f"---\ntitle: {json.dumps(title)}\ntype: docs\n---\n\n{markdown}"


def generate_section_indexes(content_dir: Path) -> None:
    """Create _index.md for section directories, and add cascade to hide large ones."""
    for section_dir in sorted(content_dir.iterdir()):
        if not section_dir.is_dir():
            continue
        index_path = section_dir / "_index.md"
        name = section_dir.name
        needs_cascade = name in SIDEBAR_HIDDEN_CHILDREN

        if not index_path.exists():
            title = SECTION_TITLES.get(
                name, name.replace("-", " ").replace("_", " ").title()
            )
            lines = ["---", f"title: {json.dumps(title)}"]
            if needs_cascade:
                lines.append("type: docs")
                lines.append("cascade:")
                lines.append("  build:")
                lines.append("    list: never")
            lines.append("---\n")
            index_path.write_text("\n".join(lines), encoding="utf-8")
        elif needs_cascade:
            existing = index_path.read_text(encoding="utf-8")
            if "list: never" not in existing:
                existing = existing.replace(
                    "type: docs\n",
                    "type: docs\ncascade:\n  build:\n    list: never\n",
                    1,
                )
                index_path.write_text(existing, encoding="utf-8")


def copy_tree(source: Path, target: Path) -> None:
    if not source.exists():
        return
    shutil.copytree(source, target, dirs_exist_ok=True)


def clean_generated(target_root: Path) -> None:
    for relative in (
        Path("content/en"),
        Path("static/images"),
        Path("static/pdfs"),
        Path("static/stylesheets"),
    ):
        shutil.rmtree(target_root / relative, ignore_errors=True)


def convert(source_root: Path, target_root: Path, clean: bool) -> None:
    source_root = source_root.resolve()
    target_root = target_root.resolve()
    docs_dir = source_root / "docs"
    content_dir = target_root / "content" / "en"
    if not docs_dir.is_dir():
        raise SystemExit(f"docs directory not found: {docs_dir}")

    if clean:
        clean_generated(target_root)
    content_dir.mkdir(parents=True, exist_ok=True)

    for source in sorted(docs_dir.rglob("*.md")):
        if any(part in EXCLUDED_DIRS for part in source.parts):
            continue
        target = hugo_page_path(source, docs_dir, content_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        markdown = source.read_text(encoding="utf-8-sig")
        title = page_title(markdown, source)
        target.write_text(
            with_front_matter(convert_markdown(markdown), source, title),
            encoding="utf-8",
        )

    generate_section_indexes(content_dir)

    copy_tree(docs_dir / "images", target_root / "static" / "images")
    copy_tree(docs_dir / "pdfs", target_root / "static" / "pdfs")
    copy_tree(docs_dir / "stylesheets", target_root / "static" / "stylesheets")


def main() -> None:
    args = parse_args()
    convert(args.source_root, args.target_root, args.clean)


if __name__ == "__main__":
    main()
