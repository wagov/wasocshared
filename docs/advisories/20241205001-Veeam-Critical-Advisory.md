# Veeam Critical Advisory - 20241205001

## Overview

Veeam has released a security advisory detailing a vulnerability discovered within the Veeam Service Provider Console (VSPC) that could allow Remote Code Execution (RCE) and remove arbitrary files on the VSPC server machine.

## What is vulnerable?

| Product(s) Affected                   | Version(s)                 | CVE #                                                             | CVSS v4/v3 | Severity |
| ------------------------------------- | -------------------------- | ----------------------------------------------------------------- | ---------- | -------- |
| Veeam Service Provider Console (VSPC) | All versions < 8.1.0.21999 | [CVE-2024-42448](https://nvd.nist.gov/vuln/detail/CVE-2024-42448) | 9.9        | Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Veeam: <https://www.veeam.com/kb4679>

## 3rd Party Article(s):

- Tenable: <https://www.tenable.com/cve/CVE-2024-42448>
