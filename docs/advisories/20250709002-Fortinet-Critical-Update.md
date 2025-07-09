# Fortinet Critical Update - 20250709002

## Overview

Fortinet have addressed a critical vulnerability affecting FortiWeb products. Successful exploitation may allow an unauthenticated attacker to execute unauthorized SQL code or commands via crafted HTTP or HTTPs requests.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                              | CVE                                                               | CVSS | Severity     |
| ------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| FortiWeb            | 7.6.x prior to 7.6.4 <br/> 7.4.x prior to 7.4.8 <br/> 7.2.x prior to 7.2.11 <br/> 7.0.x prior to 7.0.11 | [CVE-2025-25257](https://nvd.nist.gov/vuln/detail/CVE-2025-25257) | 9.6  | **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Fortinet: <https://www.fortiguard.com/psirt/FG-IR-25-151>
