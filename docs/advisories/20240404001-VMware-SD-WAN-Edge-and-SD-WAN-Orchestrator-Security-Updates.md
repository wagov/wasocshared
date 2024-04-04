# VMware SD-WAN Edge and SD-WAN Orchestrator Multiple Security Updates - 20240404001

## Overview

Multiple vulnerabilities in VMware SD-WAN were privately reported to VMware. Patches and instructions are available to remediate the vulnerabilities in affected VMware products.

## What is vulnerable?

| CVE                                                               | Severity   | CVSS | Product(s) Affected                                    |
| ----------------------------------------------------------------- | ---------- | ---- | ------------------------------------------------------ |
| [CVE-2024-22246](https://nvd.nist.gov/vuln/detail/CVE-2024-22246) | **High**   | 7.4  | VMware SD-WAN (Edge) **versions before 5.0.1 & 4.5.1** |
| [CVE-2024-22247](https://nvd.nist.gov/vuln/detail/CVE-2024-22247) | **Medium** | 4.8  | VMware SD-WAN (Edge) **versions before 5.0.1 & 4.5.1** |
| [CVE-2024-22248](https://nvd.nist.gov/vuln/detail/CVE-2024-22248) | **High**   | 7.1  | VMware SD-WAN (Orchestrator) **versions before 5.0.1** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [VMWare: VMSA-2024-0008](https://www.vmware.com/security/advisories/VMSA-2024-0008.html)
