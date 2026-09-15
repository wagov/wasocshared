# Canonical LXD Command Execution as Root - 20260915003

## Overview

Canonical have published updates to address multiple critical vulnerabilities affecting their LXD products. Successful exploitation could allow a remote attacker to achieve root command execution on the host system.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Canonical LXD     | - 6.x prior to 6.10 <br> - 5.21.x prior to 5.21.7 <br> - 5.0.x proir to 5.0.9 <br> - All versions prior to 4.0.13    | [CVE-2026-66897](hhttps://nvd.nist.gov/vuln/detail/CVE-2026-66897) <br> [CVE-2026-66898](https://nvd.nist.gov/vuln/detail/cve-2026-66898) <br> [CVE-2026-63300](https://nvd.nist.gov/vuln/detail/cve-2026-63300) <br> [CVE-2026-63299](https://nvd.nist.gov/vuln/detail/cve-2026-63299) <br> [CVE-2026-63297](https://nvd.nist.gov/vuln/detail/cve-2026-63297) <br> [CVE-2026-63296](https://nvd.nist.gov/vuln/detail/cve-2026-63296) <br> [CVE-2026-63294](https://nvd.nist.gov/vuln/detail/cve-2026-63294) <br> [CVE-2026-62420](https://nvd.nist.gov/vuln/detail/cve-2026-62420) | 9.9 <br> 9.9 <br> 9.9 <br> 9.9 <br> 9.9 <br> 9.9 <br> 9.9 <br> 9.9 | **Critical** <br> **Critical** <br> **Critical** <br> **Critical** <br> **Critical** <br> **Critical** <br> **Critical** <br> **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Canonical Github Security Advisories: <https://github.com/canonical/lxd/security/advisories>