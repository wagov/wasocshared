# Google Chrome Critical Updates - 20241031001

## Overview

Google has released a new stable channel update for their Chrome browser addressing multiple vulnerabilities. Successful exploitation could allow a remote attacker to perform malicious activity via a crafted HTML page.

## What is vulnerable?

| Product(s) Affected | Affected Version(s)              | CVE                                                                                                                                      | CVSS         | Severity                       |
| ------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------ |
| Google Chrome       | All versions below 130.0.6723.92 | [CVE-2024-10487](https://nvd.nist.gov/vuln/detail/CVE-2024-10487) <br> [CVE-2024-10488](https://nvd.nist.gov/vuln/detail/CVE-2024-10488) | 9.8 <br> 9.8 | **Critical** <br> **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Google: <https://chromereleases.googleblog.com/2024/10/stable-channel-update-for-desktop_29.html>

## Additional References

- SecurityOnline article: <https://securityonline.info/new-chrome-security-patch-targets-critical-cve-2024-10487-10488-flaws-update-immediately/>
