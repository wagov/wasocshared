# SolarWinds Critical Update - 20240913001

## Overview

SolarWinds has reported two vulnerabilities affecting their Access Rights Manager (ARM) software. The vulnerabilities have the potential to compromise the security of networks utilising ARM, with impacts ranging from unauthorized access to remote code execution.

## What is vulnerable?

| Product(s) Affected | Version(s)              | CVE                                                                                                                                       | CVSS          | Severity                  |
| ------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------- |
| SolarWinds ARM      | Version before 2024.3.1 | [CVE-2024-28991](https://nvd.nist.gov/vuln/detail/CVE-2024-28991) </br> [CVE-2024-28990](https://nvd.nist.gov/vuln/detail/CVE-2024-28990) | 9.0 </br> 6.3 | **Critical** </br> Medium |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48hrs* (refer [Patch Management](../guidelines/patch-management.md)):

- Solarwinds ARM Release notes: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2024-3-1_release_notes.htm
