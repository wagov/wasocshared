# Apple Releases Security Updates for Multiple Products - 20230627004

## Overview

Apple has released security updates to address vulnerabilities in multiple products. An attacker could exploit some of these vulnerabilities to take control of an affected device.

## What is the vulnerability?

- **Integer Overflow** - [**CVE-2023-32434**](https://nvd.nist.gov/vuln/detail/CVE-2023-32434) - CVSS v3 Base Score: ***N/A***
- **WebKit Memory Corruption** - [**CVE-2023-32435**](https://nvd.nist.gov/vuln/detail/CVE-2023-32435) - CVSS v3 Base Score: ***N/A***
- **WebKit Type Confusion** - [**CVE-2023-32439**](https://nvd.nist.gov/vuln/detail/CVE-2023-32439) - CVSS v3 Base Score: ***N/A***

## What is vulnerable?

The vulnerability affects the following products:

- [watchOS 8.8.1](https://support.apple.com/en-us/HT213808 "About the security content of watchOS 8.8.1") ***- Integer Overflow***
- [macOS Big Sur 11.7.8](https://support.apple.com/en-us/HT213809 "About the security content of macOS Big Sur 11.7.8") ***- Integer Overflow***
- [macOS Monterey 12.6.7](https://support.apple.com/en-us/HT213810 "About the security content of macOS Monterey 12.6.7") ***- Integer Overflow***
- [iOS 15.7.7 and iPadOS 15.7.7](https://support.apple.com/en-us/HT213811 "About the security content of iOS 15.7.7 and iPadOS 15.7.7") ***- Integer Overflow, WebKit Memory Corruption, WebKit Type confusion***
- [watchOS 9.5.2](https://support.apple.com/en-us/HT213812 "About the security content of watchOS 9.5.2") ***- Integer Overflow***
- [macOS Ventura 13.4.1](https://support.apple.com/en-us/HT213813 "About the security content of macOS Ventura 13.4.1") ***- Integer Overflow,  WebKit Type Confusion***
- [iOS 16.5.1 and iPadOS 16.5.1](https://support.apple.com/en-us/HT213814 "About the security content of iOS 16.5.1 and iPadOS 16.5.1") ***- Integer Overflow, WebKit Type Confusion***

## What has been observed?

CISA added this vulnerabilty to their [Known Exploited Vulnerabilties](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog on 22 June 2023.

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of one month (refer [Patch Management](../guidelines/patch-management.md)):

- [**Apple Security Updates**](https://support.apple.com/en-us/HT201222)

## Additional references

- [**CISA Advisory 22/06/2023**](https://www.cisa.gov/news-events/alerts/2023/06/22/apple-releases-security-updates-multiple-products)
