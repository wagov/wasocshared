# GitPython Critical Vulnerabilities - 20260603002

## Overview

GitPython is a python library used to interact with Git repositories. Prior to version 3.1.47, _clone() validates multi_options as the original list, then executes shlex.split(” ”.join(multi_options)). A string like ”--branch main --config core.hooksPath=/x” passes validation (starts with --branch), but after split becomes [”--branch”, “main”, ”--config”, “core.hooksPath=/x”]. Git applies the config and executes attacker hooks during clone.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                               | CVSS         | Severity                               |
| ------------------- | ---------- | ----------------------------------------------------------------- | ------------ | -------------------------------------- |
| GitPython     | Versions prior to 3.1.47   | [CVE-2026-42284](https://nvd.nist.gov/vuln/detail/CVE-2026-42284) | 9.8          | **Critical**           |

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- GitPython: <https://github.com/gitpython-developers/GitPython/releases/tag/3.1.47>

## Additional References

- GitPython Advisories: <https://github.com/gitpython-developers/GitPython/security/advisories/GHSA-x2qx-6953-8485>
- Ubuntu Security Advisory: <https://ubuntu.com/security/CVE-2026-42284>
