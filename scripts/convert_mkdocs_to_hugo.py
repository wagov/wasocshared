"""Convert the MkDocs source tree into Hugo/Docsy input files.

The script is intentionally idempotent so the Hugo preview branch can be rebuilt
from the latest `main` branch content in CI without committing generated files.
"""

from __future__ import annotations

import argparse
import json
import os
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
    "TTP_Hunt": "Threat Hunting (TTPs)",
    "sentinel-101": "Sentinel 101",
    "ADS_forms": "Detection Analytics",
}

# Sections whose child pages should be hidden from the sidebar navigation
# (they are browsed via shortcodes like date_index instead).
# Supports both top-level ("advisories") and nested ("guidelines/TTP_Hunt/ADS_forms").
SIDEBAR_HIDDEN_CHILDREN: frozenset[str] = frozenset({
    "advisories",
    "guidelines/TTP_Hunt/ADS_forms",
})

# Section display order in the left sidebar (matches mkdocs.yml nav).
SECTION_WEIGHTS: dict[str, int] = {
    "onboarding": 10,
    "advisories": 20,
    "baselines": 50,
    "guidelines": 60,
    "training": 70,
}

# Per-page ordering within their section (relative path stem → weight).
PAGE_WEIGHTS: dict[str, int] = {
    "baselines/data-sources": 1,
    "baselines/security-operations": 2,
    "baselines/vulnerability-management": 3,
    "guidelines/incident-reporting": 1,
    "guidelines/playbooks": 2,
    "guidelines/network-management": 3,
    "guidelines/patch-management": 4,
    "guidelines/secure-configuration": 5,
    "guidelines/annual-implementation-reporting": 6,
    "guidelines/e8-assessment": 7,
    "guidelines/further-five": 8,
    "guidelines/TTP_Hunt/ttp-detection-guidelines": 9,
    "training/analyst-induction": 1,
    "training/azure-basics": 2,
    "training/devsecops-induction": 3,
    "training/sentinel-101": 4,
}

# Pages hidden from the sidebar (not in the mkdocs.yml nav).
NAV_HIDDEN: frozenset[str] = frozenset({
    "threat-activity",
    "guidelines/collecting-evidence",
    "guidelines/config-wombat-test",
    "guidelines/runzero-ot",
    "guidelines/workstations",
    "guidelines/supply-chain-risk-mgmt",
    "training/sentinel-101/update-analytic-rule-alert-overrides",
    "training/sentinel-101/update-analytic-rule-entity-mapping",
    "training/sentinel-101/update-analytic-rule-custom-details",
    "training/sentinel-101/update-analytic-rule-incident-grouping",
    "training/sentinel-101/update-analytic-rule-query",
})


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
    stem = relative.stem
    parent = source.parent
    if (parent / stem).is_dir():
        return content_dir / relative.parent / stem / "_index.md"
    if relative.name == "README.md":
        return content_dir / relative.parent / "_index.md"
    return content_dir / relative


def hugo_url_path(source: Path, docs_dir: Path) -> str:
    """Return the Hugo output URL path for a source markdown file."""
    relative = source.relative_to(docs_dir)
    if relative == Path("README.md"):
        return ""
    stem = relative.stem
    if (source.parent / stem).is_dir():
        url = (relative.parent / stem).as_posix()
        return f"{url}/" if url else ""
    if relative.name == "README.md":
        url = relative.parent.as_posix()
        return f"{url}/" if url else ""
    # Hugo strips () from URLs
    url = relative.with_suffix("").as_posix().replace("(", "").replace(")", "")
    return url + "/"


LINK_ANGLE_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(<([^>]+)>\)")
LINK_PLAIN_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)<]+(?:\([^)<]*\)[^)<]*)*)\)")


def rewrite_links(markdown: str, source: Path, docs_dir: Path) -> str:
    """Rewrite relative .md links to correct relative URLs for Hugo's URL scheme."""
    source_url = hugo_url_path(source, docs_dir)

    def replace_link(match: re.Match[str]) -> str:
        text = match.group(1)
        url = match.group(2)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        parts = url.split("#", 1)
        path_part = parts[0].split()[0] if " " in parts[0] else parts[0]
        fragment = parts[1] if len(parts) > 1 else ""

        if not path_part.endswith(".md"):
            return match.group(0)

        target_file = (source.parent / path_part).resolve()
        if not target_file.exists() or not target_file.is_file():
            return match.group(0)

        target_url = hugo_url_path(target_file, docs_dir)
        if not source_url:
            rel = target_url
        else:
            rel = os.path.relpath(
                target_url.rstrip("/"), source_url.rstrip("/")
            ).replace(os.sep, "/")
            rel += "/"
        if fragment:
            rel += "#" + fragment
        return f"[{text}]({rel})"

    markdown = LINK_ANGLE_RE.sub(replace_link, markdown)
    return LINK_PLAIN_RE.sub(replace_link, markdown)


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


def convert_markdown(markdown: str, source: Path, docs_dir: Path) -> str:
    markdown = rewrite_links(markdown, source, docs_dir)
    return strip_first_h1(convert_admonitions(convert_macros(markdown)))


def page_title(markdown: str, source: Path) -> str:
    if source.name == "advisories.md":
        return "Advisories (TLP:CLEAR)"
    if match := TITLE_RE.search(markdown):
        return re.sub(r"\s+-\s+\d{11}$", "", match.group("title")).strip()
    return source.stem.replace("-", " ").replace("_", " ").title()


def nav_metadata(source: Path, docs_dir: Path) -> dict[str, str | int | bool]:
    """Compute weight, linkTitle, toc_hide for a page based on its source path."""
    relative = source.relative_to(docs_dir)
    rel_stem = relative.with_suffix("").as_posix()
    section = relative.parts[0] if relative.parts else ""

    meta: dict[str, str | int | bool] = {}

    if rel_stem in NAV_HIDDEN:
        meta["toc_hide"] = True

    # Don't hide section index pages themselves
    is_section_index = (
        relative.name == "README.md"
        or relative.name == f"{section}.md"
        or (source.parent / relative.stem).is_dir()
    )

    # Hide individual pages in large sections (advisories, ADS_forms)
    if not is_section_index:
        if section in SIDEBAR_HIDDEN_CHILDREN:
            meta["toc_hide"] = True

        # Check nested hidden children like guidelines/TTP_Hunt/ADS_forms
        rel_dir = "/".join(relative.parts[:-1])
        parent_stem = rel_stem.rsplit("/", 1)[0]
        if (
            rel_dir in SIDEBAR_HIDDEN_CHILDREN
            or parent_stem in SIDEBAR_HIDDEN_CHILDREN
        ):
            meta["toc_hide"] = True

    if rel_stem in PAGE_WEIGHTS:
        meta["weight"] = PAGE_WEIGHTS[rel_stem]

    if section in SECTION_TITLES and relative.name == f"{section}.md":
        meta["linkTitle"] = SECTION_TITLES[section]

    return meta


def with_front_matter(
    markdown: str, source: Path, title: str, docs_dir: Path
) -> str:
    if markdown.startswith(("---\n", "+++\n")):
        return markdown
    meta = nav_metadata(source, docs_dir)
    lines = ["---", f"title: {json.dumps(title)}", "type: docs"]
    for key in ("weight", "linkTitle", "toc_hide"):
        if key in meta:
            val = meta[key]
            if isinstance(val, str):
                lines.append(f"{key}: {json.dumps(val)}")
            elif isinstance(val, bool):
                lines.append(f"{key}: {str(val).lower()}")
            else:
                lines.append(f"{key}: {val}")
    lines.append("---\n")
    return "\n".join(lines) + markdown


def pretty_section_name(name: str) -> str:
    if name in SECTION_TITLES:
        return SECTION_TITLES[name]
    return name.replace("-", " ").replace("_", " ").title()


def generate_section_indexes(content_dir: Path) -> None:
    """Create _index.md for directories, hide large sections, list children."""
    for section_dir in sorted(content_dir.rglob("*")):
        if not section_dir.is_dir():
            continue
        index_path = section_dir / "_index.md"
        section_name = section_dir.name

        if not index_path.exists():
            title = pretty_section_name(section_name)
            lines = ["---", f"title: {json.dumps(title)}", "type: docs"]
            # Hide section index for hidden children directories
            rel = section_dir.relative_to(content_dir).as_posix()
            if rel in SIDEBAR_HIDDEN_CHILDREN:
                lines.append("toc_hide: true")
            if section_name in SECTION_WEIGHTS:
                lines.append(f"weight: {SECTION_WEIGHTS[section_name]}")
            if section_name in SECTION_TITLES:
                lines.append(f"linkTitle: {json.dumps(SECTION_TITLES[section_name])}")
            lines.append("---\n")

            if True:
                child_md_pages = sorted(section_dir.glob("*.md"))
                child_dirs = sorted(
                    d for d in section_dir.iterdir() if d.is_dir()
                )
                if child_md_pages or child_dirs:
                    lines.append("## Pages in this section\n")

            index_path.write_text("\n".join(lines), encoding="utf-8")
        else:
            existing = index_path.read_text(encoding="utf-8")
            changed = False
            # Remove old cascade if present
            if "cascade:" in existing and "toc_hide" in existing:
                existing = re.sub(
                    r"\ncascade:\n  (?:build:\n    list: never\n|toc_hide: true\n)",
                    "",
                    existing,
                )
                changed = True
            # Only apply section weight/title to top-level directories
            rel_parts = section_dir.relative_to(content_dir).parts
            is_top_level = len(rel_parts) == 1
            lookup_name = rel_parts[0] if is_top_level else section_name
            if lookup_name in SECTION_WEIGHTS and "weight:" not in existing:
                existing = existing.replace(
                    "type: docs\n",
                    f"type: docs\nweight: {SECTION_WEIGHTS[lookup_name]}\n",
                    1,
                )
                changed = True
            if lookup_name in SECTION_TITLES and "linkTitle:" not in existing:
                lt = json.dumps(SECTION_TITLES[lookup_name])
                existing = existing.replace(
                    "type: docs\n",
                    f"type: docs\nlinkTitle: {lt}\n",
                    1,
                )
                changed = True
            if changed:
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
            with_front_matter(
                convert_markdown(markdown, source, docs_dir), source, title, docs_dir
            ),
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
