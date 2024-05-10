# Google Chrome Arbitrary Code Execution Multiple Vulnerabilities - 20240509001

## Overview

Use after free in ANGLE and Heap buffer overflow in WebAudio in Google Chrome prior to 124.0.6367.155 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page.

## What is vulnerable?

| CVE                                                             | Severity | CVSS | Product(s) Affected                  |
| --------------------------------------------------------------- | -------- | ---- | ------------------------------------ |
| [CVE-2024-4558](https://nvd.nist.gov/vuln/detail/CVE-2024-4558) | **High** | 8.8  | **versions prior to 124.0.6367.155** |
| [CVE-2024-4559](https://nvd.nist.gov/vuln/detail/CVE-2024-4559) | **High** | 8.8  | **versions prior to 124.0.6367.155** |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- https://chromereleases.googleblog.com/2024/05/stable-channel-update-for-desktop_7.html
