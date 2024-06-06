# New Chrome Zero-Day Vulnerability Under Active Exploitation - 20240516005

## Overview

Google has issued an urgent security update for its Chrome web browser, responding to a newly discovered “zero-day” vulnerability that is actively being exploited by malicious actors.

## What is vulnerable?

| CVE           | Severity |     | Product(s) Affected                                                                                 | Summary                                                                                                                                      | Dated       |
| ------------- | -------- | --- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Google Chrome | **High** |     | **versions before** Chrome 120.0.6099.234 (Linux) 120.0.6099.224 (Mac) 120.0.6099.224/225 (Windows) | Out of bounds memory access in V8 in Google Chrome allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. | 16 Jan 2024 |
| Google Chrome | **High** |     | **versions before** Chrome 125.0.6422.60 (Linux)  125.0.6422.60/.61( Windows, Mac)                  | Type Confusion in V8 in Google Chrome allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page.          | 15 May 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://chromereleases.googleblog.com/2024/01/stable-channel-update-for-desktop_16.html
- https://chromereleases.googleblog.com/2024/05/stable-channel-update-for-desktop_15.html

## Additional References

- https://nvd.nist.gov/vuln/detail/CVE-2024-0519
- https://nvd.nist.gov/vuln/detail/CVE-2024-4947
