# SolarWinds Releases Critical Update - 20240823001

## Overview

The SolarWinds Web Help Desk (WHD) software is affected by a hardcoded credential vulnerability, allowing remote unauthenticated user to access internal functionality and modify data.

## What is vulnerable?

| Product(s) Affected      | Version(s)                              | CVE                                                               | CVSS | Severity     |
| ------------------------ | --------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| SolarWinds Web Help Desk | **all versions before** 12.8.3 Hotfix 2 | [CVE-2024-28987](https://nvd.nist.gov/vuln/detail/CVE-2024-28987) | 9.1  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- SolarWinds article: <https://support.solarwinds.com/SuccessCenter/s/article/SolarWinds-Web-Help-Desk-12-8-3-Hotfix-2>

## Additional References

- Cybersecurity News article: <https://securityonline.info/solarwinds-web-help-desk-hit-by-critical-vulnerability-cve-2024-28987>
