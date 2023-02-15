# Apple Releases Security Updates for Multiple Products - 20230215001

## Overview
Apple has released security updates to address vulnerabilities in multiple products. 

## What is the vulnerability?
- [**CVE-2023-23529**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23529)
- [**CVE-2023-23514**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23514)
- [**CVE-2023-23522**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23522)

## What is vulnerable? 
An attacker could exploit these vulnerabilities to take control of an affected device.
 - Safari 16.3*:
   - **Webkit:** Processing maliciously crafted web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited.

- iOS 16.3.1 and iPadOS 16.3.1:
  - **Kernel:** An app may be able to execute arbitrary code with kernel privileges.
  - **Webkit:** Processing maliciously crafted web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited.
  
- macOS Ventura 13.2.1:
    - **Kernel:** An app may be able to execute arbitrary code with kernel privileges.
    - **Shortcut:** An app may be able to observe unprotected user data.
    - **Webkit:** Processing maliciously crafted web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited.
## Recommendation
The WA SOC encourages users and administrators to review the Apple security updates page for the following products and apply the necessary updates as soon as possible.

-   [Safari 16.3.1](https://support.apple.com/kb/HT213638)\
-   [iOS 16.3.1 and iPadOS 16.3.1](https://support.apple.com/kb/HT213635)\
-   [macOS 13.2.1](https://support.apple.com/kb/HT213633)

