# SonicWall GMS Virtual Appliance Windows Multiple vulnerabilities - 20240514003

## Overview

The WA SOC has been made aware of multiple vulnerabilities affecting SonicWall GMS (Virtual Appliance, Windows) version 9.3.4 and earlier versions.

## What is vulnerable?

| CVE  | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ---- | ------------ | ---- | ------------------- | ------- | ----- |
| [CVE-2024-29010](https://nvd.nist.gov/vuln/detail/CVE-2024-29010) | **High** | 7.1  | **versions before 9.3.4** | GMS ECM Policy XML External Entity Processing Information Disclosure Vulnerability | 01/05/2024|
| [CVE-2024-29011](https://nvd.nist.gov/vuln/detail/CVE-2024-29011) | **High** | 7.5  | **versions before 9.3.4** | GMS ECM Hard-Coded Credential Authentication Bypass Vulnerability | 01/05/2024|

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0007

## Additional References

- NA
