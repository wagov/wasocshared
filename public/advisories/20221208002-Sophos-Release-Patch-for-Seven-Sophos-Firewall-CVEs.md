# **Sophos Release Patch for Seven "Sophos Firewall" CVE's** - 20221208003

## Overview
Sophos has released a security [advisory](https://www.sophos.com/en-us/security-advisories/sophos-sa-20221201-sfos-19-5-0) and patch addressing seven vulnerabilities including a 'critical' Remote Code Execution (RCE) vulnerability previously remediated via a [hotfix](https://www.sophos.com/en-us/security-advisories/sophos-sa-20220923-sfos-rce) and three rated **'High'**.

## What is the threat?
Describe the threat to organisation's application/ environment/ security/ operational continuity

## What is the vulnerability ?

[CVE-2022-3236:](https://nvd.nist.gov/vuln/detail/CVE-2022-3236) **CVSS 9.8** - A code injection vulnerability in the User Portal and Webadmin allows a remote attacker to conduct RCE in Sophos Firewall. This CVE was subject to a [previous advisory and hotfix](https://www.sophos.com/en-us/security-advisories/sophos-sa-20220923-sfos-rce), which has now officially been rolled out in a new patch.

[CVE-2022-3713:](https://nvd.nist.gov/vuln/detail/CVE-2022-3713) **CVSS 8.8** - A code injection vulnerability that can allow an adjacent attacker to execute code in the Wi-Fi controller of Sophos Firewall.

[CVE-2022-3709:](https://nvd.nist.gov/vuln/detail/CVE-2022-3709) **CVSS 8.4** - A stored XSS vulnerability allows an administrator to super-administrator privilege escalation in the Webadmin import group wizard of Sophos Firewall.

[**CVE-2022-3696:**](https://nvd.nist.gov/vuln/detail/CVE-2022-3696) CVSS 7.2 - A post-authentication code injection vulnerability that allows administrators to execute code in Webadmin of Sophos Firewall.

[**CVE-2022-3226:**](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2022-3226&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7C48c8a0a205ae4fd7602e08dad8be68c7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638060609568583660%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=59nyC7DXv5c7swYbHcpFgpky4odkZOqDcgRJtchZDs0%3D&reserved=0) CVSS 7.2 - An OS command injection vulnerability allows admins to execute code via SSL VPN configuration uploads in Sophos Firewall.

[**CVE-2022-3711:**](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2022-3711&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7C48c8a0a205ae4fd7602e08dad8be68c7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638060609568583660%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=Rafw9phHwYPaenFgydKk7hbcr1N1yRfr4IeHKX0RQEc%3D&reserved=0) CVSS 4.3 - A post-auth read-only SQL injection vulnerability allows users to read non-sensitive configuration database contents in the User Portal of Sophos Firewall.

## What is vulnerable ? 
-   [Name of vulnerable application/ platform/ tools] - [Version]
- Log4j 2.17.1
- VMware Foundation ver. 3.11

## What has been observed ?
Describe what has been observed in state of WA sector.

## Recommendation
Patch Sophos Firewall immediately to avoid exploitation

### Reference:
* reference and URL link