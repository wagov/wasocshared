# Mozilla Critical Advisory - 20250328001

## Overview

Mozilla has released a critical-rated advisory relating to a security vulnerability in their Firefox products which could cause the parent process to return an unintentionally powerful handle, leading to a sandbox escape.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                | CVE                                                             | CVSS | Severity |
| ------------------- | --------------------------------------------------------- | --------------------------------------------------------------- | ---- | -------- |
| Firefox             | versions prior to Firefox 136.0.4                         | [CVE-2025-2857](https://nvd.nist.gov/vuln/detail/CVE-2025-2857) | TBD  | TBD      |
| Firefox ESR         | versions prior to 115.21.1 <br> versions prior to 128.8.1 | [CVE-2025-2857](https://nvd.nist.gov/vuln/detail/CVE-2025-2857) | TBD  | TBD      |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla: <https://www.mozilla.org/en-US/security/advisories/mfsa2025-19/#CVE-2025-2857>

## Additional References

- Bleeping Comptuer: <https://www.bleepingcomputer.com/news/security/mozilla-warns-windows-users-of-critical-firefox-sandbox-escape-flaw/>
