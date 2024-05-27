# May 2024 Cisco ASA, FMC, and FTD Software Security Advisory Bundled Publication - 20240527002

## Overview

Cisco released its semiannual Cisco ASA, FMC, and FTD Software Security Advisory Bundled Publication on May 22, 2024. 

The May 22, 2024, release of the Cisco ASA, FMC, and FTD Software Security Advisory Bundled Publication includes 6 Cisco Security Advisories that describe 6 vulnerabilities in Cisco ASA, FMC, and FTD. Cisco has released software updates that address these vulnerabilities.


## What is vulnerable?

| CVE  | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ---- | ------------ | ---- | ------------------- | ------- | ----- |
| CVE-2024-20360 | **High** | 8.8  | Cisco FMC |     A vulnerability in the web-based management interface of Cisco Firepower Management Center (FMC) Software could allow an authenticated, remote attacker to conduct SQL injection attacks on an affected system.    |   22 May 2024    |
| CVE-2024-20293 | **Medium** | 5.8 | Cisco ASA and FTD | A vulnerability in the activation of an access control list (ACL) could allow an unauthenticated, remote attacker to bypass the protection that is offered by a configured ACL on an affected device. | 22 May 2024 |
| CVE-2024-20361 | **Medium** | 5.8 | Cisco FMC and FTD | A vulnerability in the Object Groups for ACLs feature of Cisco FMC Software could allow an unauthenticated, remote attacker to bypass configured access controls on managed devices that are running Cisco FTD Software. | 22 May 2024 |
| CVE-2024-20261 | **Medium** | 5.8 | Cisco FTD | A vulnerability in the file policy feature that is used to inspect encrypted archive files of Cisco FTD could allow an unauthenticated, remote attacker to bypass a configured file policy to block an encrypted archive file. | 22 May 2024 |
| CVE-2024-20363 | **Medium** | 5.8 | Multiple Cisco Products (see link below) | Multiple Cisco products are affected by a vulnerability in the Snort Intrusion Prevention System (IPS) rule engine that could allow an unauthenticated, remote attacker to bypass the configured rules on an affected system. | 22 May 2024 |
| CVE-2024-20355 | **Medium** | 5.0 | Cisco ASA and FTD | A vulnerability in the implementation of SAML 2.0 single sign-on (SSO) for remote access VPN services could allow an authenticated, remote attacker to successfully establish a VPN session on an affected device. | 22 May 2024 |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://sec.cloudapps.cisco.com/security/center/viewErp.x?alertId=ERP-75298


## Additional References

- [Cisco Firepower Management Center Software SQL Injection Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-sqli-WFFDnNOs)
- [Cisco Adaptive Security Appliance and Firepower Threat Defense Software Inactive-to-Active ACL Bypass Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ogsnsg-aclbyp-3XB8q6jX)
- [Cisco Firepower Management Center Software Object Group Access Control List Bypass Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-object-bypass-fTH8tDjq)
- [Cisco Firepower Threat Defense Software Encrypted Archive File Policy Bypass Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-archive-bypass-z4wQjwcN)
- [Multiple Cisco Products Snort 3 HTTP Intrusion Prevention System Rule Bypass Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort3-ips-bypass-uE69KBMd)
- [Cisco Adaptive Security Appliance and Firepower Threat Defense Software Authorization Bypass Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-saml-bypass-KkNvXyKW)