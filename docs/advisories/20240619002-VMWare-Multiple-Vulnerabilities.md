# VMWare Multiple Vulnerabilities - 20240619002

## Overview

The WA SOC has been made aware of heap-overflow and privilege escalation vulnerabilities affecting VMware vCenter Server.

## What is vulnerable?

| Products Affected.                            | CVE                                                               | CVSSv3 | Severity     |
| --------------------------------------------- | ----------------------------------------------------------------- | ------ | ------------ |
| VMware vCenter Server: </br> **versions before 8.0 U2d, 8.0 U1e, 7.0 U3r** | [CVE-2024-37079](https://nvd.nist.gov/vuln/detail/CVE-2024-37079) </br> [CVE-2024-37080](https://nvd.nist.gov/vuln/detail/CVE-2024-37080) </br> [CVE-2024-37081](https://nvd.nist.gov/vuln/detail/CVE-2024-37081) | 9.8 </br> 9.8 </br> 7.8  | **Critical** </br> **Critical** </br>  **High** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48h...* (refer [Patch Management](../guidelines/patch-management.md)):

- Broadcom Advisory: <https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24453>

## Additional References

- Security Affairs article: <https://securityaffairs.com/164659/hacking/vmware-fixed-vcenter-server-flaws.html>
- The Cyber Throne article: <https://thecyberthrone.in/2024/06/18/vmware-fixes-critical-vulnerabilities-in-its-products/>
