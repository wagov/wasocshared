# Actively Exploited Chrome Zero-Day Patch Released - 20231002003

## Overview

Google have released a patch for Chrome that addresses a number of serious vulnerabilities, including an actively exploited zero-day that would allow a remote attacker to potentially exploit heap corruption via a crafted HTML page. Google notes that the exploit for CVE-2023-5217 exists in the wild, and recommends users update as soon as possible.

## What are the vulnerabilities?

- [**CVE-2023-5217**](https://www.cve.org/CVERecord?id=CVE-2023-5217) - CVSS v3 Base Score: ***8.8***
- [**CVE-2023-5186**](https://www.cve.org/CVERecord?id=CVE-2023-5186) - CVSS v3 Base Score: ***8.8***
- [**CVE-2023-5187**](https://www.cve.org/CVERecord?id=CVE-2023-5187) - CVSS v3 Base Score: ***8.8***

## What is vulnerable?

Google Chrome versions before 117.0.5938.132

## What has been observed?

Google has publicly stated that the vulnerabilities addresses in this patch are being actively exploited in the wild and that the exploit is publicly available. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours* (refer [Patch Management](../guidelines/patch-management.md)):

- [Google Blog](https://chromereleases.googleblog.com/2023/09/stable-channel-update-for-desktop_27.html)