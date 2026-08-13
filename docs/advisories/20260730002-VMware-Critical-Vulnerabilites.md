# Multiple VMware Critical Vulnerabilities - 20260730002

## Overview

Broadcom has released a security advisory addressing multiple critical vulnerabilities affecting several VMware products. Successful exploitation could allow an attacker to compromise affected systems through authentication bypass, remote code execution, or virtual machine escape.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |Active Exploitation | Dated |
|----------------------|------------|-----|------|----------|-|-|
| VMware Cloud Foundation | 9.1.x.x, 9.0.x.x, 5.x | [CVE-2026-59309](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-59310](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-47876](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) | 9.8<br>9.8<br>9.3 | **Critical** | / <br> Yes <br> / | Aug 12, 2026 | 
| VMware vSphere Foundation | 9.1.x.x, 9.0.x.x | [CVE-2026-59309](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-59310](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-47876](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) | 9.8<br>9.8<br>9.3 | **Critical** | / <br> Yes <br> /  | Aug 12, 2026 | 
| VMware vCenter | 8.0 | [CVE-2026-59309](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-59310](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) | 9.8<br>9.8 | **Critical** | / <br> Yes   | Aug 12, 2026 | 
| VMware ESX | 8.0 | [CVE-2026-47876](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) | 9.3 | **Critical** | / | |
| VMware Telco Cloud Platform | 3.0, 4.x, 5.0.x, 5.1.x | [CVE-2026-59309](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-59310](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-47876](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) | 9.8<br>9.8<br>9.3 | **Critical** | / <br> Yes <br> /  | Aug 12, 2026 | 
| VMware Telco Cloud Infrastructure | 3.0 | [CVE-2026-59309](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)<br>[CVE-2026-59310](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) | 9.8<br>9.8 | **Critical** | / <br> Yes | Aug 12, 2026 | 
## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- BROADCOM: <https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017>

