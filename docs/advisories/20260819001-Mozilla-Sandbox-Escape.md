# Mozilla Sandbox Escape Vulnerability - 20260819001

## Overview

The WASOC has observed updates from Mozilla relating to a maximum severity vulnerability affecting their Firefox and Thunderbird products. An unauthenticated attacker with access to a system running the affected browser can break out of the sandbox environment and execute code outside the sandbox restrictions.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Mozilla Firefox <br> Mozilla Thunderbird | All versions prior to 154 | [CVE-2026-75874](https://nvd.nist.gov/vuln/detail/CVE-2026-75874) | 10 | **Critical** |

## What has been observed?


The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla Firefox: <https://www.mozilla.org/en-GB/security/advisories/mfsa2026-74/>
- Mozilla Thunderbird: <https://www.mozilla.org/en-GB/security/advisories/mfsa2026-78/>
