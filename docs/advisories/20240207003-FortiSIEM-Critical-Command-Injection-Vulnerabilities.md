# FortiSIEM - Citical Command Injection Vulnerabilities - 20240207003

## Overview

An improper neutralization of special elements used in an os command ('os command injection') in Fortinet FortiSIEM can allow attacker to execute unauthorized code or commands via crafted API requests.

## What is vulnerable?

| Product(s) Affected                                                                                                                                                                                                                                                          | CVE                                                                                                                                   | Severity     | CVSS |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---- |
| Fortinet FortiSIEM versions <br />- **versions 7.1.0 through 7.1.1** <br />- **version 7.0.0 through 7.0.2** <br />- **version 6.7.0 through 6.7.8** <br />- **version 6.6.0 through 6.6.3** <br />- **version 6.5.0 through 6.5.2** <br />- **version 6.4.0 through 6.4.2** | [CVE-2024-23108](https://nvd.nist.gov/vuln/detail/CVE-2024-23108) , [CVE-2024-23109](https://nvd.nist.gov/vuln/detail/CVE-2024-23109) | **Critical** | 10.0 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions. (refer [Patch Management](../guidelines/patch-management.md)):

- [FortiGuard](https://www.fortiguard.com/psirt/FG-IR-23-130)
