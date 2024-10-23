# Fortinet Zero-Day Vulnerability - 20241023001

## Overview

The WA SOC has been made aware of a zero-day vulnerability in FortiGate devices that is currently being actively exploited. This vulnerability allows threat actor to execute malicious code on affected systems. The issue seems to stem from a FortiManager default setting that permits devices with unknown or unauthorised serial numbers to register in an organization’s FortiManager dashboard.

## What is vulnerable?

| Product(s) Affected | Affected Version(s)                                                                                                               | Severity |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------- |
| FortiManager        | all versions \< 7.6.0 <br> all versions \< 7.4.4 <br>all versions \< 7.2.7  <br>all versions \< 7.0.12 <br>all versions \< 6.4.14 | Zero-Day |
|                     |                                                                                                                                   |          |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- arstechnica: <https://arstechnica.com/security/2024/10/fortinet-stays-mum-on-critical-0-day-reportedly-under-active-exploitation/>
- Fortinet: <https://www.fortiguard.com/psirt?filter=1&product=FortiManager&version=>
