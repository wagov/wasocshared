# Google Chrome Zero Day - 20240513001

## Overview

A number of vulnerabilities in Google Chrome V8 have been addressed, including a Zero Day that potentially has an exploit in the wild.

## What is vulnerable?

| CVE  | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ---- | ------------ | ---- | ------------------- | ------- | ----- |
| Google Chrome | **High** | 8.8 | **versions before** Mac 120.0.6099.234; Linux and Win 120.0.6099.224/225 |    Out of bounds memory access in V8 in Google Chrome allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page.     |    16 Jan 2024   |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://chromereleases.googleblog.com/2024/01/stable-channel-update-for-desktop_16.html

## Additional References

- https://nvd.nist.gov/vuln/detail/CVE-2024-0519
