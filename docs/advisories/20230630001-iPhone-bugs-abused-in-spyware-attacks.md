# iPhone bugs abused in spyware attacks - 20230630001

## Overview

The WA SOC has observed security vulnerabilities exploited as zero-days to deploy Triangulation spyware on iPhones via iMessage zero-click exploits. Spywares are malwares that infiltrates your device, gain root privileges through vulnerabilioty in the Kernel and covertly gathers intel about you.

Multiple apple products with vulnerabilities can process maliciously crafted web content, which may lead to arbitrary code execution on unpatched devices. Apple is aware of a report that this issue may have been actively exploited. This issue is fixed in iOS 16.5.1 and iPadOS 16.5.1, Safari 16.5.1, macOS Ventura 13.4.1, iOS 15.7.7 and iPadOS 15.7.7.

## What is the vulnerability?

These Vulnerabilities are still undergoing analysis.

- [**CVE-2023-32434**](https://nvd.nist.gov/vuln/detail/CVE-2023-32434) - CVSS v3 Base Score: ***N/A***

  Apple Multiple Products Integer Overflow Vulnerability

- [**CVE-2023-32435**](https://nvd.nist.gov/vuln/detail/CVE-2023-32435) - CVSS v3 Base Score: ***N/A***

  Apple iOS and iPadOS WebKit Memory Corruption Vulnerability

- [**CVE-2023-32439**](https://nvd.nist.gov/vuln/detail/CVE-2023-32439) - CVSS v3 Base Score: ***N/A***

  Apple Multiple Products WebKit Type Confusion Vulnerability

## What is vulnerable?

The vulnerability affects the following products:

iOS and iPadOS before 15.7:
- iPhone 7 (all models)
- iPhone 6s (all models)
- iPhone SE (1st generation)
- iPad Air 2
- iPad mini (4th generation)
- iPod touch (7th generation)

iOS and iPadOS before 16.5:
- iPhone 8 and later
- iPad Pro (all models)
- iPad Air 3rd generation and later
- iPad 5th generation and later
- iPad mini 5th generation and later

macOS before 13.4
- Macs running macOS Big Sur, Monterey, and Ventura

watchOS before 9.5.2
- Apple Watch Series 4 and later
- Apple Watch Series 3, Series 4, Series 5, Series 6, Series 7, and SE++

## What has been observed?

CISA added this vulnerabilty in their [Known Exploited Vulnerabilties](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog on 23/06/2023. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

Due to the report of active exploitation, it is strongly recommended to patch this vulnerability within 2 weeks across all affected platforms as per vendor instructions (refer [Patch Management](../guidelines/patch-management.md)):

- [https://support.apple.com/en-us/HT201222](https://support.apple.com/en-us/HT201222)
- [https://support.apple.com/en-us/HT204204](https://support.apple.com/en-us/HT204204)
- [https://support.apple.com/en-us/HT213811](https://support.apple.com/en-us/HT213811)
- [https://support.apple.com/en-us/HT213814](https://support.apple.com/en-us/HT213814)
- [https://support.apple.com/en-us/HT213813](https://support.apple.com/en-us/HT213813)
- [https://support.apple.com/en-us/HT213812](https://support.apple.com/en-us/HT213812)
