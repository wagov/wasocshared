# **Sophos Release Patch for Seven "Sophos Firewall" CVE's** - 20221208003

## Overview

Sophos has released a security [advisory](https://www.sophos.com/en-us/security-advisories/sophos-sa-20221201-sfos-19-5-0) and patch addressing seven vulnerabilities including a 'critical' Remote Code Execution (RCE) vulnerability previously remediated via a [hotfix](https://www.sophos.com/en-us/security-advisories/sophos-sa-20220923-sfos-rce) and three rated **'High'**.

## What is the vulnerability ?

[**CVE-2022-3236:**](https://nvd.nist.gov/vuln/detail/CVE-2022-3236) **CVSS 9.8** - A code injection vulnerability in the User Portal and Webadmin allows a remote attacker to conduct RCE in Sophos Firewall. This CVE was subject to a [previous advisory and hotfix](https://www.sophos.com/en-us/security-advisories/sophos-sa-20220923-sfos-rce), which has now officially been rolled out in a new patch.

[**CVE-2022-3713:**](https://nvd.nist.gov/vuln/detail/CVE-2022-3713) **CVSS 8.8** - A code injection vulnerability that can allow an adjacent attacker to execute code in the Wi-Fi controller of Sophos Firewall.

[**CVE-2022-3709:**](https://nvd.nist.gov/vuln/detail/CVE-2022-3709) **CVSS 8.4** - A stored XSS vulnerability allows an administrator to super-administrator privilege escalation in the Webadmin import group wizard of Sophos Firewall.

[**CVE-2022-3696:**](https://nvd.nist.gov/vuln/detail/CVE-2022-3696) **CVSS 7.2** - A post-authentication code injection vulnerability that allows administrators to execute code in Webadmin of Sophos Firewall.

[**CVE-2022-3226:**](https://nvd.nist.gov/vuln/detail/CVE-2022-3226) **CVSS 7.2** - An OS command injection vulnerability allows admins to execute code via SSL VPN configuration uploads in Sophos Firewall.

[**CVE-2022-3711:**](https://nvd.nist.gov/vuln/detail/CVE-2022-3711) **CVSS 4.3** - A post-auth read-only SQL injection vulnerability allows users to read non-sensitive configuration database contents in the User Portal of Sophos Firewall.

## What is vulnerable ?

All versions of Sophos Firewall **prior to v19.5 GA** are considered vulnerable.

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

- Review the [Sophos Advisory](https://www.sophos.com/en-us/security-advisories/sophos-sa-20221201-sfos-19-5-0).
- Ascertain if your version of Sophos Firewall is vulnerable.
- If vulnerable, patch immediately to avoid exploitation.
