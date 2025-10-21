# VMWare Active Exploitation - 20251021001

## Overview

Broadcom has reported multiple vulnerabilities in VMware Aria Operations and VMware Tools. A non-administrative user on a virtual machine could escalate privileges to root if VMware Tools is installed and the VM is managed by Aria Operations with SDMP (Software-Defined Management Platform) enabled.

The WASOC has observed alleged reports of exploitation in the wild for one or more the the mentioned CVEs.

## What is vulnerable?

| Product(s) Affected         | Version(s)                           | CVE                                                                    | CVSS | Severity  |
| --------------------------- | ------------------------------------ | ---------------------------------------------------------------------- | ---- | --------- |
| VMware Tools <br> VMWare Aria Operations | [Vendor listed affected products and versions](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36149) | [CVE-2025-41244](https://nvd.nist.gov/vuln/detail/CVE-2025-41244) <br> [CVE-2025-41245](https://nvd.nist.gov/vuln/detail/CVE-2025-41245) <br> [CVE-2025-41246](https://nvd.nist.gov/vuln/detail/CVE-2025-41246) | 7.8 <br> 7.1 <br> 7.1 | High <br> High <br> High |

## What has been observed?

The WASOC has observed alleged reports of exploitation in the wild for one or more the the mentioned vulnerabilities.
The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Broadcom: <https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36149>

## Additional References

- BleepingComputer: <https://www.bleepingcomputer.com/news/security/chinese-hackers-exploiting-vmware-zero-day-since-october-2024/>
