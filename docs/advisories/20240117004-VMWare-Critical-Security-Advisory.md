# VMWare Critical Security Advisory - 20240117004

## Overview

VMWare have released a security advisory for CVE-2023-34063 affecting Aria Automation (formerly vRealize Automation) and Cloud Foundation.

## What is vulnerable?

| Product(s) Affected                                                                | Summary                                                                                                                                                                                                | Severity     | CVSS |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ---- |
| VMware Aria Automation (formerly vRealize Automation) **all versions before** 8.16 | Aria Automation contains a Missing Access Control vulnerability. An authenticated malicious actor may exploit this vulnerability leading to unauthorized access to remote organizations and workflows. | **Critical** | 9.9  |
| VMware Cloud Foundation (Aria Automation) versions 4.x, 5.x                        | Aria Automation contains a Missing Access Control vulnerability. An authenticated malicious actor may exploit this vulnerability leading to unauthorized access to remote organizations and workflows. | **Critical** | 9.9  |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *One Month...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://www.vmware.com/security/advisories/VMSA-2024-0001.html>
