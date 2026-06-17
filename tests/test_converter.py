"""Tests for the MkDocs → Hugo conversion script."""

from __future__ import annotations

import importlib.util
from pathlib import Path

# Load the converter module from scripts/ (not a package)
_spec = importlib.util.spec_from_file_location(
    "convert",
    Path(__file__).resolve().parent.parent
    / "scripts"
    / "convert_mkdocs_to_hugo.py",
)
convert = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(convert)


# --- Admonition conversion ---

class TestAdmonitions:
    def test_basic_note(self):
        md = '!!! note\n\n    Body text here.'
        result = convert.convert_admonitions(md)
        assert '{{< admonition type="note"' in result
        assert "Body text here." in result

    def test_titled_admonition(self):
        md = '!!! warning "Custom Title"\n\n    Danger zone.'
        result = convert.convert_admonitions(md)
        assert 'type="warning"' in result
        assert 'title="Custom Title"' in result
        assert "Danger zone." in result

    def test_collapsible_admonition(self):
        md = '??? note "Click to expand"\n\n    Hidden content.'
        result = convert.convert_admonitions(md)
        assert 'collapsible="true"' in result
        assert "Hidden content." in result

    def test_nested_admonition(self):
        md = '!!! note\n\n    Outer text.\n\n    !!! warning\n\n        Inner text.'
        result = convert.convert_admonitions(md)
        assert result.count("{{< admonition") == 2
        assert "Outer text." in result
        assert "Inner text." in result

    def test_admonition_preserves_trailing_newline(self):
        md = '!!! note\n\n    Body.\n'
        result = convert.convert_admonitions(md)
        assert result.endswith("\n")


# --- Macro conversion ---

class TestMacros:
    def test_mitre_macro(self):
        md = '{{ mitre("T1059") }}'
        result = convert.convert_macros(md)
        assert '{{< mitre id="T1059" >}}' in result

    def test_mitre_no_quotes(self):
        md = '{{mitre("T1003.001")}}'
        result = convert.convert_macros(md)
        assert '{{< mitre id="T1003.001" >}}' in result

    def test_date_index_simple(self):
        md = '{{ date_index("docs/advisories") }}'
        result = convert.convert_macros(md)
        assert "{{% date_index %}}" in result

    def test_date_index_with_args(self):
        md = (
            '{{ date_index("docs/advisories",'
            ' prefix="advisories/", expand=1, include=2) }}'
        )
        result = convert.convert_macros(md)
        assert '{{% date_index' in result
        assert 'expand="1"' in result
        assert 'include="2"' in result

    def test_include_macro(self):
        md = "{% include 'threat-activity.md' %}"
        result = convert.convert_macros(md)
        assert '{{< include-page path="threat-activity" >}}' in result

    def test_include_double_quotes(self):
        md = '{% include "threat-activity.md" %}'
        result = convert.convert_macros(md)
        assert '{{< include-page path="threat-activity" >}}' in result


# --- Link rewriting ---

class TestLinkRewriting:
    def test_relative_md_link_rewritten(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# Page\n")
        target = docs / "target.md"
        target.write_text("# Target\n")

        md = "[link](target.md)"
        result = convert.rewrite_links(md, source, docs)
        assert "target/" in result
        assert "target.md" not in result

    def test_external_link_preserved(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# Page\n")

        md = "[link](https://example.com)"
        result = convert.rewrite_links(md, source, docs)
        assert "https://example.com" in result

    def test_anchor_link_preserved(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# Page\n")

        md = "[link](#section)"
        result = convert.rewrite_links(md, source, docs)
        assert "#section" in result

    def test_link_with_fragment(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# Page\n")
        target = docs / "other.md"
        target.write_text("# Other\n")

        md = "[link](other.md#section)"
        result = convert.rewrite_links(md, source, docs)
        assert "#section" in result

    def test_angle_bracket_link(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# Page\n")
        target = docs / "file(test).md"
        target.write_text("# File\n")

        md = "[link](<file(test).md>)"
        result = convert.rewrite_links(md, source, docs)
        assert "test" in result
        assert ".md" not in result


# --- Front matter ---

class TestFrontMatter:
    def test_title_from_h1(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# My Page Title\n\nBody.")

        title = convert.page_title("# My Page Title\n", source)
        assert title == "My Page Title"

    def test_title_strips_advisory_suffix(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "advisory.md"
        source.write_text("# Critical Vulnerability - 20260610001\n")

        title = convert.page_title("# Critical Vulnerability - 20260610001\n", source)
        assert title == "Critical Vulnerability"

    def test_with_front_matter_adds_type(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# Title\n")
        result = convert.with_front_matter("body", source, "Title", docs)
        assert "type: docs" in result
        assert 'title: "Title"' in result

    def test_existing_front_matter_preserved(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "page.md"
        source.write_text("# Title\n")
        result = convert.with_front_matter(
            "---\ntitle: Existing\n---\nbody",
            source, "Title", docs,
        )
        assert "Existing" in result


# --- H1 stripping ---

class TestStripH1:
    def test_strips_first_h1(self):
        md = "# Title\n\n## Section\n\nBody."
        result = convert.strip_first_h1(md)
        assert not result.strip().startswith("# Title")
        assert "## Section" in result

    def test_preserves_h2_and_below(self):
        md = "# Title\n\n## Subtitle\n\n### Sub-subtitle"
        result = convert.strip_first_h1(md)
        assert "## Subtitle" in result
        assert "### Sub-subtitle" in result


# --- URL path computation ---

class TestUrlPath:
    def test_regular_page(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "guidelines" / "patch-management.md"
        source.parent.mkdir(parents=True)
        source.write_text("# Test\n")

        result = convert.hugo_url_path(source, docs)
        assert result == "guidelines/patch-management/"

    def test_readme_becomes_root(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "README.md"
        source.write_text("# Home\n")

        result = convert.hugo_url_path(source, docs)
        assert result == ""

    def test_section_index(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "onboarding.md"
        source.write_text("# Onboarding\n")
        (docs / "onboarding").mkdir()

        result = convert.hugo_url_path(source, docs)
        assert result == "onboarding/"

    def test_parentheses_stripped(self, tmp_path):
        docs = tmp_path / "docs"
        docs.mkdir()
        source = docs / "file(test).md"
        source.write_text("# Test\n")

        result = convert.hugo_url_path(source, docs)
        assert "(" not in result
        assert ")" not in result
