# Veeam Exploitation PoC Published - 20240611002

## Overview

Since the publication of [Advisory 20240522003](https://soc.cyber.wa.gov.au//advisories/20240522003-Critical-Veeam-Backup-Enterprise-Manager-Vulnerability/), a proof-of-concept (PoC) exploit for a Veeam Backup Enterprise Manager ulnerability is now publicly available.

## What is vulnerable?

| Product(s) Affected                                                      | CVE                                                                                                                                                                                                                                                                                       | Severity                                     | CVSS                              |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------- |
| Veeam Backup Enterprise Manager: </br> All versions **below 12.1.2.172** | [CVE-2024-29849](https://nvd.nist.gov/vuln/detail/CVE-2024-29849) </br> [CVE-2024-29850](https://nvd.nist.gov/vuln/detail/CVE-2024-29850) </br> [CVE-2024-29851](https://nvd.nist.gov/vuln/detail/CVE-2024-29851) </br> [CVE-2024-29852](https://nvd.nist.gov/vuln/detail/CVE-2024-29852) | **Critical** </br> High </br> High </br> Low | 9.8 </br> 8.8 </br> 7.2 </br> 2.7 |

## Recommendation

The WA SOC recommends administrators apply the latest solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://www.veeam.com/kb4581>

### Additional Resources

- Tenable CVE article: <https://www.tenable.com/cve/CVE-2024-29849>
- BleepingComputer article: <https://www.bleepingcomputer.com/news/security/exploit-for-critical-veeam-auth-bypass-available-patch-now/>
