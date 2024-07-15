# Junos OS Evolved: Parameter Processing Issues Allowing Privilege Escalation Resolved - 20240715001

## Overview

Multiple instances of Improper Neutralization of Special Elements vulnerabilities exist in Juniper Networks Junos OS Evolved commands, which allow a local, authenticated attacker with low privileges to escalate their privileges to 'root' leading to a full compromise of the system.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                                                                                                                                                                                           | CVE                                                                                                                                                                                                                                                                                                                                                            | CVSS | Severity |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | -------- |
| Junos OS Evolved    | -   All version before 20.4R3-S7-EVO <br> -   21.2-EVO versions before 21.2R3-S8-EVO <br> - 21.4-EVO versions before 21.4R3-S7-EVO <br> - 22.2-EVO versions before 22.2R3-EVO <br>- 22.3-EVO versions before 22.3R2-EVO <br> -   22.4-EVO versions before 22.4R2-EVO | [CVE-2024-39520](https://nvd.nist.gov/vuln/detail/CVE-2024-39520) <br>  [CVE-2024-39521](https://nvd.nist.gov/vuln/detail/CVE-2024-39521) <br> [CVE-2024-39522](https://nvd.nist.gov/vuln/detail/CVE-2024-39522) <br> [CVE-2024-39523](https://nvd.nist.gov/vuln/detail/CVE-2024-39523) <br> [CVE-2024-39524](https://nvd.nist.gov/vuln/detail/CVE-2024-39524) | 8.5  | High     |

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [2024-07 Security Bulletin: Junos OS Evolved: Multiple CLI parameter processing issues allowing privilege escalation resolved](https://supportportal.juniper.net/s/article/2024-07-Security-Bulletin-Junos-OS-Evolved-Multiple-CLI-parameter-processing-issues-allowing-privilege-escalation-resolved?language=en_US)
