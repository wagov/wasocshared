# Fortinet fixes critical RCE in Fortigate SSL-VPN devices - 20230612001

## Overview

Fortinet has released new Fortigate firmware updates that fix an undisclosed, critical pre-authentication remote code execution vulnerability in SSL VPN devices.

## What is the vulnerability?

[**CVE-2023-27997**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27997) - **Remote Code Execution vulnerability in SSL VPN**

## What is vulnerable?

The vulnerability affects the following products:

- **All FortiOS firmware Versions**

The flaw would allow a hostile agent to interfere via the VPN, even if the MFA is activated.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices (within 48 hours if exposed to the internet, 2 weeks otherwise).

Security fixes to address this vulnerability has been released in:

- **FortiOS firmware Version** ***6.0.17, 6.2.15, 6.4.13, 7.0.12, and 7.2.5***

## Additional References

- [Critical severity vulnerability in Fortinet Fortigate SSL-VPN devices (ACSC)](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/critical-severity-vulnerability-fortinet-fortigate-ssl-vpn-devices)
- [Fortinet fixes critical RCE flaw in Fortigate SSL-VPN devices, patch now (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/fortinet-fixes-critical-rce-flaw-in-fortigate-ssl-vpn-devices-patch-now/)
