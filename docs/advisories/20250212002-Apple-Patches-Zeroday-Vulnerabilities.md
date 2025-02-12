# Apple Patches Zero Day Vulnerabilities - 20250212002

## Overview

Apple has released patches for an actively exploited iOS zero-day vulnerabilities. The vulnerability could lead to an authorisation issue, allowing a malicious actor to disable USB Restricted Mode on a locked device, potentially enabling a cyber-physical attack.

## What is vulnerable?

| Product(s) Affected                                    | CVE                                                               | CVSS | Severity |
| ------------------------------------------------------ | ----------------------------------------------------------------- | ---- | -------- |
| iOS < 18.3.1 <br> iPadOS < 18.3.1 <br> iPadOS < 17.7.5 | [CVE-2025-24200](https://nvd.nist.gov/vuln/detail/CVE-2025-24200) | 4.6  | Medium   |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *1 Month...* (refer [Patch Management](../guidelines/patch-management.md)):

- Apple iOS/iPadOS 18.3.1 : <https://support.apple.com/en-us/122174>
- Apple iOS 17.7.5 : <https://support.apple.com/en-us/122173>

### Additional Resources

- Apple security releases: <https://support.apple.com/en-us/100100>
