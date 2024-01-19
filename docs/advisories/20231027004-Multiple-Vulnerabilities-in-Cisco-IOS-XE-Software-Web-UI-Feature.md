# Multiple Vulnerabilities in Cisco IOS XE Software Web UI Feature - 20231027004

## Overview

Cisco is providing an update for the ongoing investigation into observed exploitation of the web UI feature in Cisco IOS XE Software.

## What is the vulnerability?

[**CVE-2023-20198**](https://nvd.nist.gov/vuln/detail/CVE-2023-20198) - CVSS v3 Base Score: ***10.0***
\- Successfully exploiting this vulnerability allows a threat actor to gain initial access and execute privilege commands to create local user accounts and passwords.

[**CVE-2023-20273**](https://nvd.nist.gov/vuln/detail/CVE-2023-20273) - CVSS v3 Base Score: ***7.2***
\- Allows an actor to leverage newly created local user account (from previous exploit) to elevate privilege to root and write implants to the file system.

## What is vulnerable?

The vulnerability affects the following products:

- Cisco IOS XE Software with the web UI feature enabled.

**Products Confirmed Not Vulnerable**
Cisco has confirmed that these vulnerabilities do not affect the following Cisco products:

- Adaptive Security Appliance (ASA) Software
- Firepower Threat Defense (FTD) Software
- IOS Software
- IOS XE Software prior to Release 16
- NX-OS Software

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

| **Cisco IOS XE Software Release Train** | **First Fixed Release** | **Available** |
| --------------------------------------- | ----------------------- | ------------- |
| 17.9                                    | 17.9.4a                 | Yes           |
| 17.6                                    | 17.6.6a                 | TBD           |
| 17.3                                    | 17.3.8a                 | TBD           |
| 16.12 (Catalyst 3650 and 3850 only)     | 16.12.10a               | TBD           |

IOS XE Software Maintenance Upgrade (SMU):

| **Cisco IOS XE Software Release Train** | **Base Release** | **SMU Available** |
| --------------------------------------- | ---------------- | ----------------- |
| 17.9                                    | 17.9.4           | Yes               |
| 17.6                                    | 17.6.5           | TBD               |

Cisco strongly recommends that customers disable the HTTP Server feature on all internet-facing systems or restrict its access to trusted source addresses. To disable the HTTP Server feature, use the no ip http server or no ip http secure-server command in global configuration mode. If both the HTTP server and HTTPS server are in use, both commands are required to disable the HTTP Server feature.

***Note***: A list of IOC's (Indicators of Compromise) provided in [Cisco's advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z) that can be used to determine if a system have been compromised.

## Additional References

- [Multiple Vulnerabilities in Cisco IOS XE Software Web UI Feature](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z)
