# QNAP Zero-Day Vulnerability - 20241030002

## Overview

An OS command injection vulnerability has been reported to affect HBS 3 Hybrid Backup Sync. If exploited, the vulnerability could allow remote attackers to execute arbitrary commands.

## What is vulnerable?

| Product(s) Affected      | Version(s)         | CVE                                                               | CVSS | Severity     |
| ------------------------ | ------------------ | ----------------------------------------------------------------- | ---- | ------------ |
| HBS 3 Hybrid Backup Sync | 25.1 \< 25.1.1.673 | [CVE-2024-50388](https://nvd.nist.gov/vuln/detail/CVE-2024-50388) | TBA  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- QNAP: <https://www.qnap.com/en-us/security-advisory/qsa-24-41>

## Additional References

- Tenable: <https://www.tenable.com/cve/CVE-2024-50388>
