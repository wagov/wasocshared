# Cisco Addresses Apache Struts 2 Critical RCE Vulnerability - 20231214001

## Overview

Since the release of [Advisory 20231213001](https://soc.cyber.wa.gov.au//advisories/20231213001-Apache-Struts-2-crit-vuln/), Cisco have released a [public advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-struts-C2kCMkmT) regarding the Apache Struts vulnerability affecting Cisco Products.

Cisco is investigating its product line to determine which products may be affected by this vulnerability and the impact on each affected product. As the investigation progresses, Cisco will update their advisory with information about affected products.

## What is the vulnerability?

| CVE ID                                                                | CVSS Score | Overview                                                                                                                                                                                             |
| --------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**CVE-2023-50164**](https://nvd.nist.gov/vuln/detail/CVE-2023-50164) | 9.8        | An attacker can manipulate file upload params to enable paths traversal and under some circumstances this can lead to uploading a malicious file which can be used to perform Remote Code Execution. |

## What is vulnerable?

Only products listed in the Vulnerable Products section of the advisory are known to be affected by this vulnerability

| Usage                                    | Product                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Collaboration and Social Media           | Customer Collaboration Platform, formerly SocialMiner                                                                    |
| Network and Content Security Devices     | Identity Services Engine (ISE)                                                                                           |
| Network Management and Provisioning      | Prime Access Registrar                                                                                                   |
|                                          | Prime Collaboration Assurance                                                                                            |
|                                          | Prime Collaboration Provisioning                                                                                         |
|                                          | Prime License Manager                                                                                                    |
|                                          | Prime Service Catalog                                                                                                    |
| Voice and Unified Communications Devices | Computer Telephony Integration Object Server (CTIOS)                                                                     |
|                                          | Emergency Responder                                                                                                      |
|                                          | Finesse                                                                                                                  |
|                                          | Unified Communications Manager (Unified CM) / Unified Communications Manager Session Management Edition (Unified CM SME) |
|                                          | Unified Communications Manager IM & Presence Service (Unified CM IM&P)                                                   |
|                                          | Unified Contact Center Enterprise (Unified CCE)                                                                          |
|                                          | Unified Contact Center Enterprise - Live Data server (Unified CCE - Live Data Server)                                    |
|                                          | Unified Contact Center Express (Unified CCX)                                                                             |
|                                          | Unified Intelligence Center                                                                                              |
|                                          | Unified Intelligent Contact Management Enterprise                                                                        |
|                                          | Unified SIP Proxy Software                                                                                               |
|                                          | Unity Connection                                                                                                         |
|                                          | Virtualized Voice Browser                                                                                                |

## What has been observed?

The Cisco Product Security Incident Response Team (PSIRT) is aware that proof-of-concept exploit code is available for the vulnerability described in this advisory.

## Recommendation

The WA SOC recommends administrators apply the workarounds and solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-struts-C2kCMkmT>
