# FortiOS & FortiProxy - Heap buffer overflow in sslvpn pre-authentication - 20230620004

## Overview

A heap-based buffer overflow vulnerability \[CWE-122\] in FortiOS and FortiProxy SSL-VPN may allow a remote attacker to execute arbitrary code or commands via specifically crafted requests.

## What is the vulnerability?

[**CVE-2023-27997**](https://nvd.nist.gov/vuln/detail/CVE-2023-27997) - CVSS v3 Base Score: ***9.2***

## What is vulnerable?

The vulnerability affects the following products:

[FortiOS & FortiProxy Affected Products](https://www.fortiguard.com/psirt/FG-IR-23-097)

## What has been observed?

This CVE is in [CISA's Known Exploited Vulnerabilities Catalog](https://cisa.gov/known-exploited-vulnerabilities-catalog) (added 13 June 2023). There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within 2 weeks: [FortiGuard PSIRT FG-IR-23-097 Solutions](https://www.fortiguard.com/psirt/FG-IR-23-097)
