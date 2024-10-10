# Fortinet Critical Vulnerabilities - 20241010002

## Overview

Fortinet has released advisory on a critical vulnerability affecting multiple Fortinet products. Exploitation of this vulnerability will allow a remote unauthenticated attacker to execute arbitrary code or commands via specially crafted requests.

## What is vulnerable?

| Product(s) Affected | Affected Version(s)  | CVE            | CVSS | Severity |
|---------------------|----------------------|----------------|------|----------|
| FortiOS  | 7.4 <= 7.4.2 <br> 7.2 <= 7.2.6 <br> 7.0 <= 7.0.13  | [CVE-2024-23113](https://nvd.nist.gov/vuln/detail/CVE-2024-23113) |  9.8 | Critical |
| FortiPAM | 1.2 all versions <br> 1.1 all versions <br> 1.0 all versions | [CVE-2024-23113](https://nvd.nist.gov/vuln/detail/CVE-2024-23113) |  9.8 | Critical |
| FortiProxy | 7.4 <= 7.4.2 <br> 7.2 <= 7.2.8 <br> 7.0 <= 7.0.15 | [CVE-2024-23113](https://nvd.nist.gov/vuln/detail/CVE-2024-23113) |  9.8 | Critical |
| FortiWeb | 7.4.0 <= 7.4.2  | [CVE-2024-23113](https://nvd.nist.gov/vuln/detail/CVE-2024-23113) |  9.8 | Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Fortinet advisory <https://www.fortiguard.com/psirt/FG-IR-24-029>

