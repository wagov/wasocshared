# IBM Critical Update - 20241031002

## Overview

A critical vulnerability has been identified in IBM Power Systems servers. The IBM Flexible Service Processor (FSP) contains static credentials that could enable network users to obtain service privileges on the FSP.

## What is vulnerable?

| Product(s) Affected            | Version(s)                                                                                                                    | CVE                                                               | CVSS | Severity     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| IBM Flexible Service Processor | FW1060.00 - FW1060.10 <br> FW1050.00 - FW1050.21 <br> FW1030.00 - FW1030.61 <br> FW950.00 - FW950.C0 <br> FW860.00 - FW860.B3 | [CVE-2024-45656](https://nvd.nist.gov/vuln/detail/CVE-2024-45656) | 9.8  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- IBM: <https://www.ibm.com/support/pages/node/7174183>
