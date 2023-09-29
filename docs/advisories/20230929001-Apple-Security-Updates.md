# Apple Releases Security Updates for Multiple Products - 20230929001

## Overview

Apple have released 2 advisories regarding high vulnerabilities across multiple products. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

- [**CVE-2023-40417**](https://nvd.nist.gov/vuln/detail/CVE-2023-40417) - CVSS v3 Base Score: ***5.4 MEDIUM***: A window management issue was addressed with improved state management. This issue is fixed in Safari 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. Visiting a website that frames malicious content may lead to UI spoofing..
- [**CVE-2023-40451**](https://nvd.nist.gov/vuln/detail/CVE-2023-40451) - CVSS v3 Base Score: ***8.8 HIGH***: This issue was addressed with improved iframe sandbox enforcement. This issue is fixed in Safari 17. An attacker with JavaScript execution may be able to execute arbitrary code
- [**CVE-2023-41074**](https://nvd.nist.gov/vuln/detail/CVE-2023-41074) - CVSS v3 Base Score: ***8.8 HIGH***: The issue was addressed with improved checks. This issue is fixed in tvOS 17, Safari 17, watchOS 10, iOS 17 and iPadOS 17, macOS Sonoma 14. Processing web content may lead to arbitrary code execution.
- [**CVE-2023-35074**](https://nvd.nist.gov/vuln/detail/CVE-2023-35074) - CVSS v3 Base Score: ***8.8 HIGH***: The issue was addressed with improved memory handling. This issue is fixed in tvOS 17, Safari 17, watchOS 10, iOS 17 and iPadOS 17, macOS Sonoma 14. Processing web content may lead to arbitrary code execution.
- [**CVE-2023-41993**](https://nvd.nist.gov/vuln/detail/CVE-2023-41993) - CVSS v3 Base Score: ***9.8 CRITICAL***: The issue was addressed with improved checks. This issue is fixed in Safari 17, iOS 16.7 and iPadOS 16.7, macOS Sonoma 14. Processing web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited against versions of iOS before iOS 16.7.
- [**CVE-2023-40384**](https://nvd.nist.gov/vuln/detail/CVE-2023-40384) - CVSS v3 Base Score: ***TBA***: A permissions issue was addressed with improved redaction of sensitive information. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, macOS Sonoma 14. An app may be able to read sensitive location information.
- [**CVE-2023-32377**](https://nvd.nist.gov/vuln/detail/CVE-2023-32377) - CVSS v3 Base Score: ***7.8 HIGH***: A buffer overflow issue was addressed with improved memory handling. This issue is fixed in macOS Sonoma 14. An app may be able to execute arbitrary code with kernel privileges.
- [**CVE-2023-38615**](https://nvd.nist.gov/vuln/detail/CVE-2023-38615) - CVSS v3 Base Score: ***7.8 HIGH***: The issue was addressed with improved memory handling. This issue is fixed in macOS Sonoma 14. An app may be able to execute arbitrary code with kernel privileges.
- [**CVE-2023-40448**](https://nvd.nist.gov/vuln/detail/CVE-2023-40448) - CVSS v3 Base Score: ***8.6 HIGH***s: The issue was addressed with improved handling of protocols. This issue is fixed in tvOS 17, iOS 16.7 and iPadOS 16.7, watchOS 10, iOS 17 and iPadOS 17, macOS Sonoma 14. A remote attacker may be able to break out of Web Content sandbox.
- [**CVE-2023-40432**](https://nvd.nist.gov/vuln/detail/CVE-2023-40432) - CVSS v3 Base Score: ***7.8 HIGH***s: The issue was addressed with improved memory handling. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. An app may be able to execute arbitrary code with kernel privileges.
- [**CVE-2023-40399**](https://nvd.nist.gov/vuln/detail/CVE-2023-40399) - CVSS v3 Base Score: ***5.5 MEDIUM***s: The issue was addressed with improved memory handling. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. An app may be able to disclose kernel memory
- [**CVE-2023-40410**](https://nvd.nist.gov/vuln/detail/CVE-2023-40410) - CVSS v3 Base Score: ***5.5 MEDIUM***s: An out-of-bounds read was addressed with improved input validation. This issue is fixed in macOS Ventura 13.6, tvOS 17, macOS Monterey 12.7, watchOS 10, iOS 17 and iPadOS 17, macOS Sonoma 14. An app may be able to disclose kernel memory.
- [**CVE-2023-32361**](https://nvd.nist.gov/vuln/detail/CVE-2023-32361) - CVSS v3 Base Score: ***5.5 MEDIUM***s: The issue was addressed with improved handling of caches. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. An app may be able to access user-sensitive data.
- [**CVE-2023-35984**](https://nvd.nist.gov/vuln/detail/CVE-2023-35984) - CVSS v3 Base Score: ***4.3 MEDIUM***s: The issue was addressed with improved checks. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. An attacker in physical proximity can cause a limited out of bounds write.
- [**CVE-2023-40402**](https://nvd.nist.gov/vuln/detail/CVE-2023-40402) - CVSS v3 Base Score: ***5.5 MEDIUM***s: A permissions issue was addressed with additional restrictions. This issue is fixed in macOS Sonoma 14. An app may be able to access sensitive user data.
- [**CVE-2023-40426**](https://nvd.nist.gov/vuln/detail/CVE-2023-40426) - CVSS v3 Base Score: ***5.5 MEDIUM***s: A permissions issue was addressed with additional restrictions. This issue is fixed in macOS Sonoma 14. An app may be able to bypass certain Privacy preferences.
- [**CVE-2023-41065**](https://nvd.nist.gov/vuln/detail/CVE-2023-41065) - CVSS v3 Base Score: ***3.3 LOW***s: A privacy issue was addressed with improved private data redaction for log entries. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. An app may be able to read sensitive location information.
- [**CVE-2023-29497**](https://nvd.nist.gov/vuln/detail/CVE-2023-29497) - CVSS v3 Base Score: ***3.3 LOW***s: A privacy issue was addressed with improved handling of temporary files. This issue is fixed in macOS Sonoma 14. An app may be able to access calendar data saved to a temporary directory.
- [**CVE-2023-38596**](https://nvd.nist.gov/vuln/detail/CVE-2023-38596) - CVSS v3 Base Score: ***5.5 MEDIUM***s: The issue was addressed with improved handling of protocols. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. An app may fail to enforce App Transport Security.
- [**CVE-2023-40406**](https://nvd.nist.gov/vuln/detail/CVE-2023-40406) - CVSS v3 Base Score: ***5.5 MEDIUM***s: The issue was addressed with improved checks. This issue is fixed in macOS Monterey 12.7, macOS Ventura 13.6, macOS Sonoma 14. An app may be able to read arbitrary files.
- [**CVE-2023-40420**](https://nvd.nist.gov/vuln/detail/CVE-2023-40420) - CVSS v3 Base Score: ***6.5 MEDIUM***s: The issue was addressed with improved memory handling. This issue is fixed in macOS Ventura 13.6, tvOS 17, iOS 16.7 and iPadOS 16.7, macOS Monterey 12.7, watchOS 10, iOS 17 and iPadOS 17, macOS Sonoma 14. Processing web content may lead to a denial-of-service.
- [**CVE-2023-40407**](https://nvd.nist.gov/vuln/detail/CVE-2023-40407) - CVSS v3 Base Score: ***7.5 HIGH***s: The issue was addressed with improved bounds checks. This issue is fixed in macOS Sonoma 14. A remote attacker may be able to cause a denial-of-service.
- [**CVE-2023-32396**](https://nvd.nist.gov/vuln/detail/CVE-2023-32396) - CVSS v3 Base Score: ***7.8 HIGH***s: This issue was addressed with improved checks. This issue is fixed in Xcode 15, tvOS 17, watchOS 10, iOS 17 and iPadOS 17, macOS Sonoma 14. An app may be able to gain elevated privileges.
- [**CVE-2023-41980**](https://nvd.nist.gov/vuln/detail/CVE-2023-41980) - CVSS v3 Base Score: ***5.5 MEDIUM***s: A permissions issue was addressed with additional restrictions. This issue is fixed in iOS 17 and iPadOS 17, macOS Sonoma 14. An app may be able to bypass Privacy preferences.
- [**CVE-2023-40395**](https://nvd.nist.gov/vuln/detail/CVE-2023-40395) - CVSS v3 Base Score: ***3.3 LOW***s: The issue was addressed with improved handling of caches. This issue is fixed in tvOS 17, iOS 16.7 and iPadOS 16.7, macOS Monterey 12.7, watchOS 10, iOS 17 and iPadOS 17, macOS Sonoma 14. An app may be able to access contacts.
- [**CVE-2023-40391**](https://nvd.nist.gov/vuln/detail/CVE-2023-40391) - CVSS v3 Base Score: ***TBA***s: The issue was addressed with improved memory handling. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, macOS Sonoma 14, Xcode 15. An app may be able to disclose kernel memory.
- [**CVE-2023-40441**](https://nvd.nist.gov/vuln/detail/CVE-2023-40441) - CVSS v3 Base Score: ***TBA***s: A resource exhaustion issue was addressed with improved input validation. This issue is fixed in iOS 17 and iPadOS 17, macOS Sonoma 14. Processing web content may lead to a denial-of-service.
- [**CVE-2023-23495**](https://nvd.nist.gov/vuln/detail/CVE-2023-23495) - CVSS v3 Base Score: ***5.5 MEDIUM***s: A permissions issue was addressed with improved redaction of sensitive information. This issue is fixed in macOS Sonoma 14. An app may be able to access sensitive user data.
- [**CVE-2023-40434**](https://nvd.nist.gov/vuln/detail/CVE-2023-40434) - CVSS v3 Base Score: ***3.3 LOW***s: A configuration issue was addressed with additional restrictions. This issue is fixed in iOS 17 and iPadOS 17, macOS Sonoma 14. An app may be able to access a user's Photos Library.



## What is vulnerable?

The vulnerability affects the following products:

- macOS Sonoma 14
- Safari 17 

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Safari 17](https://support.apple.com/en-us/HT213941)
- [macOS Sonoma 14](https://support.apple.com/en-us/HT213940/)
