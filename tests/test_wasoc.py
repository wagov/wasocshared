from pathlib import Path

import pytest

import wasoc.macros as macros
import wasoc.rss as rss
from wasoc.advisory import (
    advisory_uid_from_name,
    advisory_uid_from_url,
    parse_advisory,
    paths_from_source,
)
from wasoc.common import document_title, first_heading_text, titled_section


class UndefinedLike:
    _undefined_name = "T1505"


def test_document_title_and_titled_section():
    text = "# Example - 20260101001\n\n## Overview\nBody text\n\n## Advice\nPatch"
    assert document_title(text) == "Example - 20260101001"
    assert titled_section(text, "overview") == "Body text"
    assert titled_section(text, "missing") is None


def test_first_heading_text_falls_back_to_stem(tmp_path: Path):
    with_heading = tmp_path / "with.md"
    with_heading.write_text("intro\n# Heading\n", encoding="utf-8")
    without_heading = tmp_path / "without.md"
    without_heading.write_text("body\n", encoding="utf-8")

    assert first_heading_text(with_heading) == "Heading"
    assert first_heading_text(without_heading) == "without"


def test_mitre_link_and_url_are_deterministic():
    assert macros.attack_url("TA0001") == "https://attack.mitre.org/tactics/TA0001/"
    assert (
        macros.attack_url("T1505.003")
        == "https://attack.mitre.org/techniques/T1505/003/"
    )
    assert macros.attack_url("X0000") is None
    assert (
        macros.attack_link("T1047")
        == "[T1047](https://attack.mitre.org/techniques/T1047/)"
    )


def test_normalise_mitre_id_accepts_jinja_undefined_names():
    assert macros.normalise_mitre_id(UndefinedLike()) == "T1505"
    assert macros.normalise_mitre_id("T1047") == "T1047"


def test_advisory_uid_parsing():
    assert advisory_uid_from_name("20260430002-cPanel.md") == "20260430002"
    assert (
        advisory_uid_from_url(
            "https://soc.cyber.wa.gov.au/advisories/20260430002-cPanel/"
        )
        == "20260430002"
    )
    with pytest.raises(ValueError):
        advisory_uid_from_name("not-an-advisory.md")


def test_parse_advisory(tmp_path: Path):
    path = tmp_path / "20260430002-cPanel-Critical-Vulnerability.md"
    path.write_text(
        "# cPanel Critical Vulnerability - 20260430002\n\n"
        "## Overview\n"
        "Patch immediately.\n\n"
        "## Advice\n"
        "Update systems.",
        encoding="utf-8",
    )

    advisory = parse_advisory(path)

    assert advisory.uid == "20260430002"
    assert advisory.title == "cPanel Critical Vulnerability"
    assert advisory.overview == "Patch immediately."
    assert advisory.url.endswith(
        "/advisories/20260430002-cPanel-Critical-Vulnerability/"
    )


def test_paths_from_existing_markdown(tmp_path: Path):
    path = tmp_path / "20260430002-cPanel.md"
    path.write_text("# title", encoding="utf-8")
    assert paths_from_source(str(path)) == [path]


def test_document_metadata(monkeypatch, tmp_path: Path):
    docs = tmp_path / "docs"
    advisory = docs / "advisories" / "20260430002-test.md"
    advisory.parent.mkdir(parents=True)
    advisory.write_text(
        "# Test Advisory\n\n## Overview\n\nSummary text\n\n## Advice\n\nPatch",
        encoding="utf-8",
    )
    monkeypatch.setattr(rss, "DOCS_DIR", docs)
    monkeypatch.setattr(rss, "last_updated", lambda path: "2026-04-30 00:00:00 +0000")

    entry = rss.document_metadata(advisory)

    assert entry.title == "Test Advisory"
    assert entry.url == "https://soc.cyber.wa.gov.au/advisories/20260430002-test"
    assert entry.overview == "Summary text"
    assert entry.updated == "2026-04-30 00:00:00 +0000"
    assert entry.category == "advisories"


def test_feed_updated_uses_latest_entry():
    entries = [
        rss.FeedEntry("a", "u", "o", "2026-01-01 00:00:00 +0000", "c"),
        rss.FeedEntry("b", "u", "o", "2026-02-01 00:00:00 +0000", "c"),
    ]
    assert rss.feed_updated(entries) == "2026-02-01 00:00:00 +0000"
