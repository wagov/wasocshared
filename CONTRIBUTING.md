# Development

The development environment and CI use [mise](https://mise.jdx.dev/).

```sh
mise install
mise run install
mise run serve
```

Run the same checks as CI with `mise run ci`. Format Markdown with
`mise run format`, and build the site and feeds with `mise run feeds`.

VS Code and GitHub Codespaces users can reopen the repository in its dev
container; it installs mise, Python, and the locked dependencies automatically.
