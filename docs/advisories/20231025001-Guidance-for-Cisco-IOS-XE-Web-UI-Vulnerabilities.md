# Guidance for Addressing Cisco IOS XE Web UI Vulnerabilities - 20231025001

## Overview

Cisco has released guidance for addressing Cisco IOS XE Web UI Vulnerabilities, where an unauthenticated remote actor could exploit these vulnerabilities to take control of an affected system. Exploiting these vulnerabilities allow actors to create privileged accounts that provides complete control over a device.

## What is the vulnerability?

[**CVE-2023-20198**](https://nvd.nist.gov/vuln/detail/CVE-2023-20198) - CVSS v3 Base Score: ***10.0***
    - Successfully exploiting this vulnerability allows a threat actor to gain initial access and execute privilege commands to create local user accounts and passwords.

[**CVE-2023-20273**](https://nvd.nist.gov/vuln/detail/CVE-2023-20273) - CVSS v3 Base Score: ***7.2***
    - Allows an actor to leverage newly created local user account (from previous exploit) to elevate privilege to root and write implants to the file system.

## What is vulnerable?

The vulnerability affects the following products:

- Cisco IOS XE Software if the web UI feature is enabled


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):


| **Cisco IOS XE Software Release Train** | **First Fixed Release** | **Available** |
|-----------------------------------------|-------------------------|---------------|
| 17.9                                    | 17.9.4a                 | Yes           |
| 17.6                                    | 17.6.6a                 | TBD           |
| 17.3                                    | 17.3.8a                 | TBD           |
| 16.12 (Catalyst 3650 and 3850 only)     | 16.12.10a               | TBD           |

- [Multiple Vulnerabilities in Cisco IOS XE Software Web UI Feature](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z)

Additional steps for mitigation or for determining if Cisco systems are vulnerable are listed in the [Cisco Security Advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z).

## Additional References

- [CISA Updates Guidance for Addressing Cisco IOS XE Web UI Vulnerabilities | CISA](https://www.cisa.gov/news-events/alerts/2023/10/23/cisa-updates-guidance-addressing-cisco-ios-xe-web-ui-vulnerabilities)
- [Guidance for Addressing Cisco IOS XE Web UI Vulnerabilities | CISA](https://www.cisa.gov/guidance-addressing-cisco-ios-xe-web-ui-vulnerabilities)
- [Active exploitation of Cisco IOS XE Software Web Management User Interface vulnerabilities (talosintelligence.com)](https://blog.talosintelligence.com/active-exploitation-of-cisco-ios-xe-software/)
- [Multiple Vulnerabilities in Cisco IOS XE Software Web UI Feature](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z)

#### Previous WASOC advisories related to Cisco IOS XE Vulnerabilities: 
 - [Cisco IOS and IOS XE HTTP WebUI](./20231018001-Cisco-IOS-XE-HTTP-WebUI.md)
 - [Cisco IOS and IOS XE Group Encrypted Transport VPN Out-of-Bounds Write Vulnerability](./20231011004-Cisco-IOS-Software-Out-of-Bounds-Write-Vulnerability.md)