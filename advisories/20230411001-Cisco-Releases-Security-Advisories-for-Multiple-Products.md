# Cisco Releases Security Advisories for Multiple Products - 20230411001

## Overview
Cisco has released security advisories for vulnerabilities affecting multiple Cisco products.

These vulnerabilities could allow authenticated remote attackers to execute arbitrary commands as root or administrative accounts.


## What is the vulnerability?
[**CVE-2023-20102**](https://nvd.nist.gov/vuln/detail/CVE-2023-20102) - Cisco Secure Network Analytics Remote Code Execution Vulnerability
- **CVSS Score:** 8.8 (High)

[**CVE-2023-20117**](https://nvd.nist.gov/vuln/detail/CVE-2023-20117) & [**CVE-2023-20128**](https://nvd.nist.gov/vuln/detail/CVE-2023-20128) - Cisco Small Business RV320 and RV325 Dual Gigabit WAN VPN Routers Command Injection Vulnerabilities
- **CVSS Score:** 7.2 (High)

[**CVE-2023-20121**](https://nvd.nist.gov/vuln/detail/CVE-2023-20121) & [**CVE-2023-20122**](https://nvd.nist.gov/vuln/detail/CVE-2023-20122) - Cisco Evolved Programmable Network Manager, Cisco Identity Services Engine, and Cisco Prime Infrastructure Command Injection Vulnerabilities
- **CVSS Score:** 7.8 (High)



## What is vulnerable? 
The vulnerability affects the following products:

| No 	| Vulnerability                                             | Affected Products                                                     | Additional Info                                               |
|----	|--------------------------------------------------------	|-------------------------------------------------------------------	|--------------------------------------------------------------	|
| 1  	| Cisco Secure Network Analytics Remote Code Execution Vulnerability                   	| - Secure Network Analytics Manager<br>- Secure Network Analytics Virtual Manager<br>- Stealthwatch Management Console 2200<br>    | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-stealthsmc-rce-sfNBPjcS)      	|
| 2  	| Cisco Small Business RV320 and RV325 Dual Gigabit WAN VPN Routers Command Injection Vulnerabilities             	| These vulnerabilities affect Cisco Small Business RV320 and RV325 Dual Gigabit WAN VPN Routers.                                                                                                                                                                                       	| [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sb-rv32x-cmdinject-cKQsZpxL) 	|
| 3  	| Cisco Evolved Programmable Network Manager, Cisco Identity Services Engine, and Cisco Prime Infrastructure Command Injection Vulnerabilities                                             	| - **CVE-2023-20121** affects Cisco EPNM, Cisco ISE, and Cisco Prime Infrastructure<br>- **CVE-2023-20122** affects Cisco ISE.<br>                                                                                      	| [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-adeos-MLAyEcvk)      	|

## Recommendation
The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected products.
- Cisco Secure Network Analytics Remote Code Execution Vulnerability | [**Patch Available**](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-stealthsmc-rce-sfNBPjcS)
- Cisco Small Business RV320 and RV325 Dual Gigabit WAN VPN Routers Command Injection Vulnerabilities | [**No patch will be made available due to product end-of-life.**](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sb-rv32x-cmdinject-cKQsZpxL)
- Cisco Evolved Programmable Network Manager, Cisco Identity Services Engine, and Cisco Prime Infrastructure Command Injection Vulnerabilities | [**Patch Available**](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-adeos-MLAyEcvk)



