# Security Vulnerabilities fixed in Firefox for iOS 131.2 - 20241017001

## Overview

Opening an external link to an HTTP website when Firefox iOS was previously closed and had an HTTPS tab open could in some cases result in the padlock icon showing an HTTPS indicator incorrectly.

## What is vulnerable?

| Product(s) Affected | Version(s)            | CVE                                                               | CVSS | Severity     |
| ------------------- | --------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| Firefox for iOS     | Versions before 131.2 | [CVE-2024-10004](https://nvd.nist.gov/vuln/detail/CVE-2024-10004) | 9.1  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla - <https://www.mozilla.org/en-US/security/advisories/mfsa2024-54>

## Additional References

- Tenable - <https://www.tenable.com/cve/CVE-2024-10004>
