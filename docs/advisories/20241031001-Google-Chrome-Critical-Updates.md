# Google Chrome Critical Updates - 20241031001

## Overview

Google has just released an urgent update for its Chrome browser, addressing two serious security vulnerabilities that could potentially allow attackers to take control of users' systems. The WA SOC has been made aware of some vulnerabilities being classified as critical.

## What is vulnerable?


| Product(s) Affected | Source                   | CVE                                                                 | CVSS  | Severity     |
| ------------------- | ------------------------ | ------------------------------------------------------------------- | ----- | ------------ |
| Out-of-Bounds Write | *Dawn* - Google Chrome   | [CVE-2024-10487](https://nvd.nist.gov/vuln/detail/CVE-2024-10487)   |  9.8  | **Critical** |
| Use After Free      | *WebRTC* - Google Chrome | [CVE-2024-10488](https://nvd.nist.gov/vuln/detail/CVE-2024-10488)   |  9.8  | **Critical** |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- New Chrome Security Patch Targets Critical CVE-2024-10487 & 10488 Flaws -- Update Immediately: <https://securityonline.info/new-chrome-security-patch-targets-critical-cve-2024-10487-10488-flaws-update-immediately/>

## Additional References

- Stable Channel Update for Desktop: <https://chromereleases.googleblog.com/2024/10/stable-channel-update-for-desktop_29.html>