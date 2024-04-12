# Chrome Security Update - 20240412001

## Overview

A security update to address multiple vulnerabilities in Chrome has been released.
The Stable channel has been updated to 123.0.6312.122/.123 for Windows 123.0.6312.122/.123/.124 for Mac and 123.0.6312.122 to Linux which will roll out over the coming days/weeks.

## What is vulnerable?

| CVE                                                                           | Severity | CVSS | Product(s) Affected | Summary                                 | Dated       |
| ----------------------------------------------------------------------------- | -------- | ---- | ------------------- | --------------------------------------- | ----------- |
| [CVE-2024-3157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3157) | **High** | N/A  | **versions before** | Out of bounds write in Compositing      | 10-Apr-2024 |
| [CVE-2024-3516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3516) | **High** | N/A  | **versions before** | Heap buffer overflow in ANGLE           | 09-Apr-2024 |
| [CVE-2024-3515](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3515) | **High** | N/A  | **versions before** | Heap corruption via a crafted HTML page | 09-Apr-2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

## Additional References

- [Stable Channel Update for Desktop - Google](https://chromereleases.googleblog.com/2024/04/stable-channel-update-for-desktop_10.html)
