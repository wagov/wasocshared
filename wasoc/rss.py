"""RSS and Atom feed generation."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from subprocess import CalledProcessError

from feedgen.feed import FeedGenerator

from .common import (
    CONTACT_EMAIL,
    CONTACT_NAME,
    DOCS_DIR,
    SITE_DIR,
    SITE_URL,
    document_title,
    git,
    titled_section,
)

RECENT_DAYS = 180
EXCLUDED_PARTS = {"ADS_forms", "markdown-templates"}


@dataclass(frozen=True)
class FeedEntry:
    title: str
    url: str
    overview: str
    updated: str
    category: str


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def recently_changed_markdown(days: int = RECENT_DAYS) -> list[Path]:
    """Return unique markdown files changed in git within the lookback window."""
    try:
        output = git(
            "log",
            f"--since={days} days ago",
            "--name-only",
            "--pretty=format:",
            "--",
            str(DOCS_DIR),
        )
    except CalledProcessError as exc:
        raise SystemExit(
            f"Failed to collect recently changed files: {exc.stderr.strip()}"
        ) from exc

    recent: list[Path] = []
    seen: set[Path] = set()
    for line in output.splitlines():
        path = Path(line.strip())
        if (
            path.suffix == ".md"
            and path.is_file()
            and not is_excluded(path)
            and path not in seen
        ):
            recent.append(path)
            seen.add(path)
    return recent


def last_updated(path: Path) -> str:
    updated = git("log", "-1", "--pretty=format:%ci", "--", str(path))
    if not updated:
        raise ValueError(f"No git history found for {path}")
    return updated


def document_metadata(path: Path) -> FeedEntry:
    if is_excluded(path):
        raise ValueError(f"Excluded path: {path}")

    markdown_text = path.read_text(encoding="utf-8-sig")
    title = document_title(markdown_text)
    overview = titled_section(markdown_text, "overview")
    if not title:
        raise ValueError(f"Title not found: {path}")
    if not overview:
        raise ValueError(f"Overview section not found: {path}")

    url_path = path.relative_to(DOCS_DIR).with_suffix("")
    return FeedEntry(
        title=title,
        url=f"{SITE_URL}/{url_path}",
        overview=overview,
        updated=last_updated(path),
        category=url_path.parts[0],
    )


def feed_updated(entries: list[FeedEntry]) -> str:
    if entries:
        return max(entry.updated for entry in entries)
    fallback_updated = git("log", "-1", "--pretty=format:%ci", "--", str(DOCS_DIR))
    if not fallback_updated:
        raise SystemExit("No git history found for docs; cannot timestamp feed")
    return fallback_updated


def build_feed(paths: list[Path]) -> FeedGenerator:
    fg = FeedGenerator()
    fg.id(SITE_URL)
    fg.title("WA SOC Alerts & Updates")
    fg.description(
        "This site contains technical information to support WA Government "
        "Cyber Security "
        "activities. Please propose updates directly via the edit link on each page or "
        f"email {CONTACT_EMAIL} with any feedback."
    )
    fg.author({"name": CONTACT_NAME, "email": CONTACT_EMAIL})
    fg.link(href=SITE_URL, rel="alternate")
    fg.language("en")

    entries = []
    for path in reversed(paths):
        try:
            entries.append(document_metadata(path))
        except ValueError as exc:
            print(f"Skipping {path}: {exc}", file=sys.stderr)

    fg.updated(feed_updated(entries))
    for entry in entries:
        fe = fg.add_entry()
        fe.id(entry.url)
        fe.title(entry.title)
        fe.author({"name": CONTACT_NAME, "email": CONTACT_EMAIL})
        fe.description(entry.overview)
        fe.category(term=entry.category)
        fe.updated(entry.updated)
        fe.link(href=entry.url)

    return fg


def write_feeds(output_dir: Path = SITE_DIR) -> None:
    output_dir.mkdir(exist_ok=True)
    feed = build_feed(recently_changed_markdown())
    feed.atom_file(str(output_dir / "atom.xml"))
    feed.rss_file(str(output_dir / "rss.xml"))


if __name__ == "__main__":
    write_feeds()
