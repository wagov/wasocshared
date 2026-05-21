"""Shared configuration and small helpers for site automation."""

from __future__ import annotations

import re
from pathlib import Path
from subprocess import run

SITE_URL = "https://soc.cyber.wa.gov.au"
CONTACT_EMAIL = "cybersecurity@dpc.wa.gov.au"
CONTACT_NAME = "WA SOC"
DOCS_DIR = Path("docs")
SITE_DIR = Path("site")
ADVISORY_DIR = DOCS_DIR / "advisories"
ADVISORY_BASE_URL = f"{SITE_URL}/advisories/"
EMAIL_TEMPLATE_PATH = Path("templates/tlp-clear-email-template.html")


def git(*args: str) -> str:
    """Run git and return stripped stdout, raising on failure."""
    return run(
        ["git", *args], capture_output=True, check=True, text=True
    ).stdout.strip()


def first_heading_text(path: Path) -> str:
    """Return the first markdown heading in a file, falling back to the stem."""
    with path.open(encoding="utf-8-sig") as handle:
        for line in handle:
            if line.startswith("#"):
                return line.lstrip("#").strip()
    return path.stem


def document_title(markdown_text: str) -> str | None:
    """Return the first level-1 markdown heading from text."""
    for line in markdown_text.lstrip("\ufeff").splitlines():
        if line.startswith("# "):
            return line.lstrip("#").strip()
    return None


def titled_section(markdown_text: str, title: str) -> str | None:
    """Return the body under a markdown heading with the given title."""
    pattern = re.compile(
        rf"^##+\s+(?:\d+(?:\.\d+)*\.?\s+)?{re.escape(title)}\s*\n"
        rf"(?P<body>.*?)(?=\n##+\s+|\Z)",
        re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(markdown_text)
    if not match:
        return None

    paragraphs = [
        part.strip() for part in match.group("body").split("\n\n") if part.strip()
    ]
    return "\n\n".join(
        paragraph
        for paragraph in paragraphs
        if not paragraph.startswith(("!!!", "???"))
    )
