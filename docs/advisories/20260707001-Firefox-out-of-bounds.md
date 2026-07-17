# Mozilla Firefox Out-of-bounds Write - 20260707001

## Overview

The WASOC has been made aware of memory safety bugs present in Firefox.

Mozilla has stated that exploitation of these bugs may lead to arbitrary code execution and has provided patches to address the vulnerabilities.

## What is vulnerable?

| Product(s) Affected | Version(s)  | CVE                                                               | CVSS | Severity     |
| ------------------- | ----------- | ----------------------------------------------------------------- | ---- | ------------ |
| Mozilla Firefox     | \<= 152.0.3 | [CVE-2026-14241](https://nvd.nist.gov/vuln/detail/CVE-2026-14241) | 9.8  | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla: <https://www.mozilla.org/en-GB/security/advisories/mfsa2026-62/>
