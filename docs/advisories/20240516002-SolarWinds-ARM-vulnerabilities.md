# SolarWinds ARM Vulnerabilities - 20240516002

## Overview

A Critical and a High vulnerability in SolarWinds ARM have been addressed by a new service update.


## What is vulnerable?

| CVE  | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ---- | ------------ | ---- | ------------------- | ------- | ----- |
| CVE-2024-23473 | **High** | 8.6  | **versions before** 2023.2.4 |    A hard-coded credential authentication bypass vulnerability that allows access to the RabbitMQ management console.     |   14 May 2024    |
| CVE-2024-28075 | **Critical** | 9.0  | **versions before** 2023.2.4 |    This vulnerability allows an authenticated user to abuse SolarWinds service resulting in remote code execution.     |    14 May 2024   |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2023-2-4_release_notes.htm


## Additional References

- https://nvd.nist.gov/vuln/detail/CVE-2024-23473
- https://nvd.nist.gov/vuln/detail/CVE-2024-28075
