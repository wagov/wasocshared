# SolarWinds Releases Critical Update - 20240814002

## Overview

SolarWinds has released an urgent security advisory regarding a critical vulnerability in its Web Help Desk software. The vulnerability allows for Java Deserialization Remote Code Execution, potentially granting unauthorized users the ability to run arbitrary commands on the affected system

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE # | CVSS v4/v3 | Severity |
|---------------------|------------|-------|------------|----------|
| SolarWinds Web Help Desk (WHD) | all versions before 12.8.3 Hotfix 1 | [CVE-2024-28986](https://nvd.nist.gov/vuln/detail/CVE-2024-28986) |  9.8 | Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- SolarWinds: <https://support.solarwinds.com/SuccessCenter/s/article/WHD-12-8-3-Hotfix-1>

## Additional References

- Tenable: <https://www.tenable.com/cve/CVE-2024-28986>
- SecurityOnline: <https://securityonline.info/cve-2024-28986-cvss-9-8-solarwinds-web-help-desk-users-must-patch-now/>
