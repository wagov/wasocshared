# SolarWinds Product Advisories - 20240611004

## Overview

The WA SOC has been made aware of multiple SolarWinds product advisories which could be exploited by unauthenticated attackers to access sensitive files on the host machine.

## What is vulnerable?

| CVE                                                               | Severity | CVSS | Product(s) Affected                                       |
| ----------------------------------------------------------------- | -------- | ---- | --------------------------------------------------------- |
| [CVE-2024-28995](https://nvd.nist.gov/vuln/detail/CVE-2024-28995) | **High** | 8.6  | **SolarWinds Serv-U 15.4.2 HF 1 and previous versions**   |
| [CVE-2024-28996](https://nvd.nist.gov/vuln/detail/CVE-2024-28996) | **High** | 8.1  | **SolarWinds Platform 2024.1 SR 1 and previous versions** |

## What has been observed?

There are currently no reports of these vulnerabilities being exploited in the wild at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 48 hours (refer [Patch Management](../guidelines/patch-management.md)):

- [SolarWinds Security Advisory - CVE-2024-28995](https://www.solarwinds.com/trust-center/security-advisories/cve-2024-28995)
- [SolarWinds Security Advisory - CVE-2024-28996](https://www.solarwinds.com/trust-center/security-advisories/cve-2024-28996)

## Additional References

- Center for Internet Security: <https://www.cisecurity.org/advisory/a-vulnerability-in-solarwinds-serv-u-could-allow-for-path-transversal_2024-068>
