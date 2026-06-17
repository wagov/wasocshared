# Hugo Preview Authoring Guide

This document explains how content authored in MkDocs format renders in the
Hugo/Docsy preview at `/hugo-preview/`.

## Supported MkDocs Features

All features below are automatically converted by `scripts/convert_mkdocs_to_hugo.py`
and render correctly in the Hugo preview.

### Admonitions

MkDocs `!!!` and `???` syntax works as-is:

```markdown
!!! note "Optional Title"

    Admonition body text.

??? warning "Collapsible Block"

    Hidden until clicked.
```

Supported types: `note`, `tip`, `info`, `abstract`, `warning`, `danger`,
`success`, `quote`.

### Task Lists

Standard GitHub-style checkboxes:

```markdown
- [ ] Unchecked item
- [x] Checked item
```

### Code Blocks with Highlighting

Fenced code blocks with language hints:

````markdown
```python
def hello():
    print("world")
```
````

### Tables, Images, Footnotes

Standard Markdown — all work without conversion.

### Macros (converted to Hugo shortcodes)

| MkDocs macro | What it does | Hugo equivalent |
|---|---|---|
| `{{ date_index("docs/advisories") }}` | Month-grouped advisory listing | `{{% date_index %}}` |
| `{{ mitre("T1059") }}` | MITRE ATT&CK link | `{{< mitre id="T1059" >}}` |
| `{% include 'file.md' %}` | Inline page include | `{{< include-page path="file" >}}` |

### Internal Links

Relative `.md` links are automatically rewritten to correct Hugo URLs:

```markdown
[Patch Management](guidelines/patch-management.md)     → works
[Advisories](../advisories.md)                          → works
[ADS Form](./ADS_forms/T1059-Netcat.md)                 → works
[Quishing](<./ADS_forms/T1566.001-QR-Code(Quishing).md>) → works (angle brackets)
```

## Not Supported

These MkDocs features have no Hugo equivalent:

- `mkdocs-material` tabbed content (`=== "Tab"`) — convert to Docsy `{{< tabpane >}}`
- `pymdownx.keys` (`++ctrl+c++`) — use inline code instead
- `pymdownx.snippets` (`--8<-- "file.md"`) — use `{{< include-page >}}` instead

## Running the Hugo Preview Locally

```bash
# Install tools (first time)
mise install

# Build once
mise run hugo-build

# Live preview with auto-reload
mise run hugo-serve

# Run converter tests
mise run unit

# Validate Hugo config/templates
mise run hugo-check
```

## Creating New Content

Use Hugo archetypes (from the hugo branch):

```bash
hugo new advisory --kind advisory
hugo new guidelines/my-guideline --kind guideline
hugo new training/my-module --kind training
```

## How the Dual-Build Works

1. Content is authored on `main` in MkDocs format
2. On push to `main`, CI builds the MkDocs site (primary) and also:
   - Checks out the `hugo` branch
   - Runs the converter against the latest `main` content
   - Builds the Hugo preview into `/hugo-preview/`
3. The converter is idempotent — it can run any time without side effects
4. When Hugo quality is sufficient, content can be migrated to native Hugo
   syntax and the converter deleted
