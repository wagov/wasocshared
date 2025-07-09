# Fortinet Critical Update - 20250709002

## Overview

Fortinet have released critical update addressing an improper neutralization of special elements used in an SQL command ('SQL Injection') vulnerability in FortiWeb, which may allow an unauthenticated attacker to execute unauthorized SQL code or commands via crafted HTTP or HTTPs requests.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| FortiWeb 7.6 <br/> FortiWeb 7.4 <br/> FortiWeb 7.2 <br/> FortiWeb 7.0| 7.6.0 - 7.6.3  <br/> 7.4.0 - 7.4.7 <br/> 7.2.0 - 7.2.10 <br/> 7.0.0 - 7.0.10| [CVE-2025-25257](https://nvd.nist.gov/vuln/detail/CVE-2025-25257)                                                                        | 9.6        | **Critical**            |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- FortiGuard: [PSIRT | FortiGuard Labs ](https://www.fortiguard.com/psirt/FG-IR-25-151)

