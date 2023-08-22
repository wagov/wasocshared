# Cisco Releases Security Advisories for Multiple Products - 20230822002

## Overview

Cisco has released security advisories for vulnerabilities affecting multiple Cisco products. A cyber threat actor can exploit some of these vulnerabilities to take control of an affected system or cause a denial-of service condition.

## What is the vulnerability?

- [**CVE-2023-20224**](https://nvd.nist.gov/vuln/detail/CVE-2023-20224) - CVSS v3 Base Score: ***7.8***
- [**CVE-2023-20229**](https://nvd.nist.gov/vuln/detail/CVE-2023-20229) - CVSS v3 Base Score: ***7.1***
- [**CVE-2023-20212**](https://nvd.nist.gov/vuln/detail/CVE-2023-20212) - CVSS v3 Base Score: ***7.5***
- [**CVE-2023-20211**](https://nvd.nist.gov/vuln/detail/CVE-2023-20211) - CVSS v3 Base Score: ***8.1***
- [**CVE-2023-20197**](https://nvd.nist.gov/vuln/detail/CVE-2023-20197) - CVSS v3 Base Score: ***7.5***

## What is vulnerable?

The vulnerability affects the following products:

-   [ThousandEyes Enterprise Agent](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-thoueye-privesc-NVhHGwb3): This vulnerability is due to insufficient input validation of user-supplied CLI arguments. An attacker could exploit this vulnerability by authenticating to an affected device and using crafted commands at the prompt. A successful exploit could allow the attacker to execute arbitrary commands as root. The attacker must have valid credentials on the affected device.

-   [Duo Device Health Application](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-duo-dha-filewrite-xPMBMZAK): This vulnerability is due to insufficient input validation. An attacker could exploit this vulnerability by executing a directory traversal attack on an affected host. A successful exploit could allow an attacker to use a cryptographic key to overwrite arbitrary files with SYSTEM-level privileges, resulting in a denial of service (DoS) condition or data loss on the affected system.

-   [Unified CM](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-injection-g6MbwH2): This vulnerability is due to improper validation of user-supplied input. An attacker could exploit this vulnerability by authenticating to the application as a user with read-only or higher privileges and sending crafted HTTP requests to an affected system. A successful exploit could allow the attacker to read or modify data in the underlying database or elevate their privileges.

-   [ClamAV HFS+](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-clamav-rNwNEEee): This vulnerability is due to an incorrect check for completion when a file is decompressed, which may result in a loop condition that could cause the affected software to stop responding. An attacker could exploit this vulnerability by submitting a crafted HFS+ filesystem image to be scanned by ClamAV on an affected device. A successful exploit could allow the attacker to cause the ClamAV scanning process to stop responding, resulting in a DoS condition on the affected software and consuming available system resources.

-   [ClamAV](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-clamav-dos-FTkhqMWZ): This vulnerability is due to a logic error in the memory management of an affected device. An attacker could exploit this vulnerability by submitting a crafted AutoIt file to be scanned by ClamAV on the affected device. A successful exploit could allow the attacker to cause the ClamAV scanning process to restart unexpectedly, resulting in a DoS condition.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per the above vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md))
