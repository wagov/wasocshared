# N8N Multiple Critical Vulnerabilities - 20260115001

## Overview

A critical vulnerability has been identified in n8n, an open‑source workflow automation platform, that enables unauthenticated remote code execution and unauthorized access to files.

## What is vulnerable?

| Product(s) Affected                                                                   | Version(s)                                                                     | CVE                                                               | CVSS | Severity     |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ---- | ------------ |
| n8n  | affected at >= 0.211.0, < 1.120.4   <br>affected at = 1.121.0 | [CVE-2025-68613](https://nvd.nist.gov/vuln/detail/CVE-2025-68613) | 9.9   | **Critical** |
| | affected at < 1.121.3  | [CVE-2026-21877](https://nvd.nist.gov/vuln/detail/CVE-2026-21877) | 9.9   | **Critical** |
| | affected at >= 1.65.0, < 1.121.0  | [CVE-2026-21858](https://nvd.nist.gov/vuln/detail/CVE-2026-21858) | 10.0   | **Critical** |
|

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Cyera: <https://www.cyera.com/research-labs/ni8mare-unauthenticated-remote-code-execution-in-n8n-cve-2026-21858>
- Rapid7: <https://www.rapid7.com/blog/post/etr-ni8mare-n8scape-flaws-multiple-critical-vulnerabilities-affecting-n8n/>
