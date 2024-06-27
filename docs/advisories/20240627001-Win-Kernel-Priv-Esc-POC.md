# Windows Kernel Elevation of Privilege PoC Released - 20240627001

## Overview

The WA SOC has been made aware of the release of proof-of-concept (PoC) code targeting a recent high-severity vulnerability (CVE-2024-30088) in Microsoft Windows. By using a relatively simple race condition vulnerability, an attacker can gain SYSTEM privileges.

Organisations are encouraged to review the information regarding the vulnerability and apply the relevant security fixes as soon as possible.

## What is vulnerable?

| Products Affected.                         | CVE                                                               | CVSS | Severity |
| ------------------------------------------ | ----------------------------------------------------------------- | ---- | -------- |
| Windows 10, 11 and Server 2016, 2019, 2022 | [CVE-2024-30088](https://nvd.nist.gov/vuln/detail/CVE-2024-30088) | 7.0  | **High** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of one month (refer [Patch Management](../guidelines/patch-management.md)):

- [Microsoft - Windows Kernel Elevation of Privilege Vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30088)

## Additional References

- [GitHub - CVE-2024-30088 PoC](https://github.com/tykawaii98/CVE-2024-30088)
