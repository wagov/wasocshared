# VirtualBox Privilege Escalation Vulnerability - 20240423001

## Overview

An easily exploitable vulnerability in Oracle VM VirtualBox allows a low privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox. Successful attacks of this vulnerability can result in takeover of Oracle VM VirtualBox and the Windows system running it.

## What is vulnerable?

| CVE                                                               | Severity | CVSS | Product(s) Affected                                 | Summary                                                                                                 | Dated      |
| ----------------------------------------------------------------- | -------- | ---- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------- |
| [CVE-2024-21111](https://nvd.nist.gov/vuln/detail/CVE-2024-21111) | **High** | 7.8  | Oracle VM VirtualBox prior to 7.0.16 - Windows only | Allows attackers with basic access to a Windows system running VirtualBox to escalate their privileges. | 16/04/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of one month (refer [Patch Management](../guidelines/patch-management.md)):

- [Oracle Critical Patch Update Advisory - April 2024](https://www.oracle.com/security-alerts/cpuapr2024.html#AppendixOVIR)

## Additional References

- [Oracle VirtualBox Elevation of Privilege Vulnerability (CVE-2024-21111): PoC Published](https://securityonline.info/oracle-virtualbox-elevation-of-privilege-vulnerability-cve-2024-21111-poc-published/)
