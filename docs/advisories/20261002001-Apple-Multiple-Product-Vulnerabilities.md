# Apple Multiple Products Out-of-Bounds Write Vulnerability - 20261002001


## Overview

Apple have released security updates addressing an out-of-bounds write vulnerability in CoreGraphics affecting iOS, macOS and iPadOS that may lead to arbitrary code execution.


## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
|---------------------|------------|-----|------|----------|
| Apple iOS and iPadOS | 26.x.x prior to 26.7.1 | [CVE-2026-86950](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) | 8.8 | High |
| Apple macOS | 15.x.x prior to 15.8.1<br>26.x.x prior to 26.7.1 | [CVE-2026-86950](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) | 8.8 | High |
## What has been observed?

CISA has added one or more of the mentioned items to their [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Apple <https://support.apple.com/en-us/149226>
- Apple <https://support.apple.com/en-us/149228>
- Apple <https://support.apple.com/en-us/149229>
