# Windows Vulnerabilities Added to CISA Known Exploited Catalog - 20240710001

## Overview

Microsoft has released security advisories for known exploited vulnerabilities impacting Windows systems. The advisories relate to a Windows MSHTML Platform Spoofing Vulnerability and a Windows Hyper-V Elevation of Privilege Vulnerability that could result in an attacker gaining SYSTEM privileges if exploited.

## What is vulnerable?

| Product(s) Affected | CVE | Severity | CVSS |
| ------------------- | --- | -------- | ---- |
| Windows 11, Server 2022 | [CVE-2024-38080](https://nvd.nist.gov/vuln/detail/CVE-2024-38080) - Windows Hyper-V Elevation of Privilege Vulnerability| **High** | 7.8  |
| Windows 11, 10, multiple Server versions | [CVE-2024-38112](https://nvd.nist.gov/vuln/detail/CVE-2024-38112) - Windows MSHTML Platform Spoofing Vulnerability| **High** | 7.5  |

## What has been observed?

CISA added this vulnerability in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 48 Hours (refer [Patch Management](../guidelines/patch-management.md)):

- [Windows Hyper-V Elevation of Privilege Vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38080)
- [Windows MSHTML Platform Spoofing Vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38112)
