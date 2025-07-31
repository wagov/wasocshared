# Apple Critical OS Security Updates - 20250731002

## Overview

Since the publication of [Advisory 20250716003](https://soc.cyber.wa.gov.au/advisories/20250716003-Google-Chrome-Zero-Day-Vulnerability/), Apple has released OS-specific updates to address the known exploited vulnerability in multiple products.

## What is vulnerable?

| Product(s) Affected                                                                              | Version(s)                                                           | CVE                                                             | CVSS | Severity |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------- | ---- | -------- |
| iOS and iPadOS <br> macOS Sequoia <br> macOS Sonoma <br> macOS Ventura <br> visionOS <br> Safari | < 18.6 <br> < 15.6 <br> < 14.7.7 <br> < 13.7.7<br> < 2.6 <br> < 18.6 | [CVE-2025-6558](https://nvd.nist.gov/vuln/detail/CVE-2025-6558) | 8.8  | **High** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Apple security release notes: <https://support.apple.com/en-us/100100>

## Additional References

- securityaffairs: <https://securityaffairs.com/180595/security/apple-fixed-a-zero-day-exploited-in-attacks-against-google-chrome-users.html>
