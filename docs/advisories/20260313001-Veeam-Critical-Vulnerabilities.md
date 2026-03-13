# Veeam Critical Vulnerabilities - 20260313001

## Overview

Veeam has released a patch addressing multiple vulnerabilities in its Backup & Replication solution. These vulnerabilities could allow low-privileged domain users to execute remote code on vulnerable backup servers through low-complexity attacks, and could also allow a Backup Viewer to achieve remote code execution as the PostgreSQL user.

## What is vulnerable?

| Product(s) Affected        | Version(s)                                    | CVE                                                                                                                                                                                                                                                                                                                                                          | CVSS                                    | Severity                                                            |
| -------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------- |
| Veeam Backup & Replication | 12.3.2.4165 and all earlier version 12 builds | [CVE-2026-21666](https://nvd.nist.gov/vuln/detail/CVE-2026-21666) <br> [CVE-2026-21667](https://nvd.nist.gov/vuln/detail/CVE-2026-21667) <br>[CVE-2026-21708](https://nvd.nist.gov/vuln/detail/CVE-2026-21708) <br> [CVE-2026-21668](https://nvd.nist.gov/vuln/detail/CVE-2026-21668) <br> [CVE-2026-21672](https://nvd.nist.gov/vuln/detail/CVE-2026-21672) | 9.9 <br> 9.9 <br> 9.9 <br> 8.8 <br> 8.8 | **Critical** <br> **Critical** <br> **Critical**<br> High <br> High |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Veeam: <https://www.veeam.com/kb4830>
