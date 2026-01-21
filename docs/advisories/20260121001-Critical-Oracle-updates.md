# Critical Oracle updates - 20260121001

## Overview

Oracle has released critical patch updates addressing multiple security vulnerabilities in Oracle code and in third party components included in Oracle products. These vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.

## What is vulnerable?

| Product(s) Affected                                | Version(s)            | CVE                                                               | CVSS | Severity     |
| -------------------------------------------------- | --------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| Oracle Communications Order and Service Management | Versions 7.5.0, 8.0.0 | [CVE-2025-66516](https://nvd.nist.gov/vuln/detail/CVE-2025-66516) | 9.9  | **Critical** |
| Oracle Communications Operations Monitor           | Version 5.2           | [CVE-2025-49844](https://nvd.nist.gov/vuln/detail/CVE-2025-49844) | 9.9  | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- ORACLE: <https://www.oracle.com/security-alerts/cpujan2026.html>
