# Cisco Releases New Security Advisories - 20240718003

## Overview

The WA SOC has been made aware of a number of critical-to-medium vulnerabilites released by Cisco across a range of products.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                       | CVSS          | Severity                                                         |
| ------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
| Cisco Smart Software Manager      | Versions before 8-202212   | [CVE-2024-20419](https://nvd.nist.gov/vuln/detail/CVE-2024-20419)                                      | 10            | **Critical**  |
| Cisco Secure Email Gateway      | The Content Scanner Tools version is earlier than 23.3.0.4823   | [CVE-2024-20401](https://nvd.nist.gov/vuln/detail/CVE-2024-20401)        | 9.8           | **Critical**                                     |
| Cisco Secure Web Appliance      | Versions before 14.5.3 MR (Jul 2024), 15.0 MR (Aug 2024), and 15.2.0-164    | [CVE-2024-20435](https://nvd.nist.gov/vuln/detail/CVE-2024-20435)            | 8.8           | High |
| RADIUS Protocol      | RFC 2865    | [CVE-2024-3596](https://nvd.nist.gov/vuln/detail/CVE-2024-3596)                                                                     | 8.1           | High  |
| Cisco Intelligent Node      | Cisco iNode Software versions before 4.0.0 <br>  Cisco iNode Manager Software versions before 24.1  | [CVE-2024-20323](https://nvd.nist.gov/vuln/detail/CVE-2024-20323)                                                                         | 7.5            | High  |
| Cisco Small Business RV Series Router Firmware for RV340 and RV345 Dual WAN Gigabit VPN Routers     | 1.0.03.24 or later (has reached end-of-life)    | [CVE-2024-20416](https://nvd.nist.gov/vuln/detail/CVE-2024-20416)                                                                         | 6.5           | Medium  |
| Cisco Secure Email Gateway       | Versions before 14.2.3-027, and 15.0.0-097   | [CVE-2024-20429](https://nvd.nist.gov/vuln/detail/CVE-2024-20429)                                                                         | 6.5           | Medium |
| Cisco Webex App      | Cloud-based software   | [	CVE-2024-20395](https://nvd.nist.gov/vuln/detail/CVE-2024-20395) <br> [CVE-2024-20396](https://nvd.nist.gov/vuln/detail/CVE-2024-20396)                | 6.4 <br>  5.3         | Medium <br> Medium |
| Cisco Identity Services Engine Software      | Versions before 3.1P10 (Jan 2025), 3.2P7 (Sep 2024), and 3.3P3 | [CVE-2024-20296](https://nvd.nist.gov/vuln/detail/CVE-2024-20296)            | 4.7            | Medium |
| Cisco Expressway Series     | Versions before 15.0.2    | [CVE-2024-20400](https://nvd.nist.gov/vuln/detail/CVE-2024-20400)                                                                         | 3.1            | Medium  |



## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Cisco Security](https://sec.cloudapps.cisco.com/security/center/Search.x?publicationTypeIDs=1&firstPublishedStartDate=2024%2F07%2F17&firstPublishedEndDate=2024%2F07%2F17&lastPublishedStartDate=2024%2F07%2F17&lastPublishedEndDate=2024%2F07%2F17&pageNum=1&isRenderingBugList=false)
