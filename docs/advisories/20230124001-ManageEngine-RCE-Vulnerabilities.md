# ManageEngine RCE Vulnerability Known Exploitation - 20230124001

## Overview
ManageEngine has released an advisory to address unauthenticated remote code execution (RCE) vulnerabilities across multiple ManageEngine OnPremise products due to the usage of an outdated third party dependency.

## What is the vulnerability?
[**CVE-2022-47966**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47966) - CVSS Score 8.1: Multiple Zoho ManageEngine on-premise products, such as ServiceDesk Plus through 14003, allow remote code execution due to use of Apache xmlsec (aka XML Security for Java) 1.4.1, because the xmlsec XSLT features, by design in that version, make the application responsible for certain security protections, and the ManageEngine applications did not provide those protections.

## What is vulnerable? 
ManageEngine has noted the following products and versions to be impacted by the vulnerability:

| Product | Impacted Version(s) | Note |
| --- | --- | --- |
| Access Manager Plus | 4307 and below | [1] |
| Active Directory 360 | 4309 and below | [2] |
| ADAudit Plus | 7080 and below | [2] |
| ADManager Plus | 7161 and below | [2] |
| ADSelfService Plus | 6210 and below | [2] |
| Analytics Plus | 5140 and below | [1] |
| Application Control Plus | 10.1.2220.17 and below | [1] |
| Asset Explorer | 6982 and below | [2] |
| Browser Security Plus | 11.1.2238.5 and below | [1] |
| Device Control Plus | 10.1.2220.17 and below | [1] |
| Endpoint Central | 10.1.2228.10 and below | [1] |
| Endpoint Central MSP | 10.1.2228.10 and below | [1] |
| Endpoint DLP | 10.1.2137.5 and below | [1] |
| Key Manager Plus | 6400 and below | [1] |
| OS Deployer | 1.1.2243.0 and below | [1] |
| PAM 360 | 5712 and below | [1] |
| Password Manager Pro | 12123 and below | [1] |
| Patch Manager Plus | 10.1.2220.17 and below | [1] |
| Remote Access Plus | 10.1.2228.10 and below | [1] |
| Remote Monitoring and Management (RMM) | 10.1.40 and below | [1] |
| ServiceDesk Plus | 14003 and below | [2] |
| ServiceDesk Plus MSP | 13000 and below | [2] |
| SupportCenter Plus | 11017 to 11025 | [2] |
| Vulnerability Manager Plus | 10.1.2220.17 and below | [1] |

   [1] Applicable only if configured SAML-based SSO and it is currently active.

   [2] Applicable only if configured SAML-based SSO at least once in the past, regardless of the current SAML-based SSO status.

## What has been observed?
CISA has listed this vulnerabilty in their [Known Exploited Vulnerabilties](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog.

## Recommendation
Due to the report of active exploitation, it is strongly recommended to patch this vulnerability within 2 weeks across all affected platforms as per vendor instructions: [https://www.manageengine.com/security/advisory/CVE/cve-2022-47966.html](https://www.manageengine.com/security/advisory/CVE/cve-2022-47966.html)