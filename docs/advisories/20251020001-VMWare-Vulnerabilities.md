# VMWare Multiple Vulnerabilities - 20251020001

## Overview

Broadcom reported multiple vulnerabilities in VMware Aria Operations and VMware Tools. A non-administrative user on a virtual machine could escalate privileges to root if VMware Tools is installed and the VM is managed by Aria Operations with SDMP (Software-Defined Management Platform) enabled.

## What is vulnerable?

| Product(s) Affected               | Version(s)                           | CVE                                                                    | CVSS | Severity  |
| --------------------------------- | ------------------------------------ | ---------------------------------------------------------------------- | ---- | --------- |
| VMware Tools                      | 12.5.x < 12.5.4 <br> 13.x < 13.0.5.0 | [CVE-2025-41244](https://nvd.nist.gov/vuln/detail/CVE-2025-41244)      | 7.8  | High      |
| VMware Aria Operations            | 8.18.x < 8.18.5                      | [CVE-2025-41244](https://nvd.nist.gov/vuln/detail/CVE-2025-41244) <br> | 7.8  | High <br> |
| VMware Cloud Foundation           | 4.x/5.x < 8.18.5                     | [CVE-2025-41244](https://nvd.nist.gov/vuln/detail/CVE-2025-41244) <br> | 7.8  | High <br> |
| VMware Telco Cloud Platform       | 2.x/3.x/4.x/5.x <br> < 8.18.5        | [CVE-2025-41244](https://nvd.nist.gov/vuln/detail/CVE-2025-41244) <br> | 7.8  | High <br> |
| VMware Telco Cloud Infrastructure | 2.x/3.x/4.x/5.x <br> < 8.18.5        | [CVE-2025-41244](https://nvd.nist.gov/vuln/detail/CVE-2025-41244) <br> | 7.8  | High      |

## What has been observed?

This vulnerability arises due to unsafe privilege definitions and has been confirmed to be exploited in the wild, making it a critical concern for environments using affected VMware products

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Broadcom: <https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36149#:~:text=Broadcom%20would%20like%20to%20thank%20Maxime%20Thiebaut%20(NVISO)%20for%20reporting%20this%20issue%20to%20us>

## Additional References

- BleepingComputer: <https://www.bleepingcomputer.com/news/security/chinese-hackers-exploiting-vmware-zero-day-since-october-2024/>
