# Google Chrome Security Updates - 20240205002

## Overview

Google has released new updates for Google Chrome to address a Use-After-Free in Network vulnerability which could allow a threat actor to potentially exploit heap corruption via a malicious file.

## What is vulnerable?

| Product(s) Affected | Summary | Severity     | CVSS |
| ------------------- | ------- | ------------ | ---- |
| **Google Chrome** <br /> Versions Prior to: 121.0.6167.139  | This vulnerability could allow a remote attacker to potentially exploit heap corruption via a malicious file. | **NA**       | N.A  |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Chrome Releases: Stable Channel Update for Desktop (googleblog.com)](https://chromereleases.googleblog.com/2024/01/stable-channel-update-for-desktop_30.html)

## Additional References

- [NVD - CVE-2024-1077 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2024-1077)
- [CVE-2024-1077 - Security Update Guide - Microsoft - Chromium: CVE-2024-1077 Use after free in Network](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-1077)