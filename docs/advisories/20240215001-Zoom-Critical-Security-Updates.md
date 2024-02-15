# Zoom Critical Security Updates - 20240215001

## Overview

Zoom has released updates to patch critical privilege elevation flaw in Windows based Zoom apps. The Zoom desktop and VDI clients and the Meeting SDK for Windows are vulnerable to an improper input validation flaw that could allow an unauthenticated attacker to conduct privilege escalation on the target system over the network.

## What is vulnerable?

| Product(s) Affected                                                                           | CVE                                                               | Severity     | CVSS |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------ | ---- |
| Zoom Desktop Client for Windows  **versions before** ***5.16.5***                             | [CVE-2024-24691](https://nvd.nist.gov/vuln/detail/CVE-2024-24691) | **Critical** | 9.6  |
| Zoom VDI Client for Windows **versions before** ***5.16.10 (excluding 5.14.14 and 5.15.12)*** | [CVE-2024-24691](https://nvd.nist.gov/vuln/detail/CVE-2024-24691) | **Critical** | 9.6  |
| Zoom Rooms Client for Windows **versions before** ***5.17.0***                                | [CVE-2024-24691](https://nvd.nist.gov/vuln/detail/CVE-2024-24691) | **Critical** | 9.6  |
| Zoom Meeting SDK for Windows **versions before** ***5.16.5***                                 | [CVE-2024-24691](https://nvd.nist.gov/vuln/detail/CVE-2024-24691) | **Critical** | 9.6  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Security Update - ZSB-24008 | Zoom](https://www.zoom.com/en/trust/security-bulletin/ZSB-24008/)

## Additional References

- [Zoom patches critical privilege elevation flaw in Windows apps (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/zoom-patches-critical-privilege-elevation-flaw-in-windows-apps/)
- [NVD - CVE-2024-24691 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2024-24691)
