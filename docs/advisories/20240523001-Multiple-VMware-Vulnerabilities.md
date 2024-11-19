# Broadcom Security Advisory Addresses Multiple VMware Vulnerabilities - 20240523001

## Overview

Broadcom has issued an important security advisory detailing several vulnerabilities discovered in various VMware products. These vulnerabilities, if exploited, could lead to severe security breaches, including denial of service, unauthorized code execution, and exposure of sensitive data. The affected products include VMware ESXi, Workstation, Fusion, and vCenter Server.

## What is vulnerable?

| CVE                                                               | Severity     | CVSS | Product(s) Affected                                                  | Dated      |
| ----------------------------------------------------------------- | ------------ | ---- | -------------------------------------------------------------------- | ---------- |
| [CVE-2024-22267](https://nvd.nist.gov/vuln/detail/CVE-2024-22267) | **Critical** | 9.3  | [versions affected](https://www.cve.org/CVERecord?id=CVE-2024-22267) | 14/05/2024 |
| [CVE-2024-22268](https://nvd.nist.gov/vuln/detail/CVE-2024-22268) | **High**     | 7.1  | [versions affected](https://www.cve.org/CVERecord?id=CVE-2024-22268) | 14/05/2024 |
| [CVE-2024-22269](https://nvd.nist.gov/vuln/detail/CVE-2024-22269) | **High**     | 7.1  | [versions affected](https://www.cve.org/CVERecord?id=CVE-2024-22269) | 14/05/2024 |
| [CVE-2024-22270](https://nvd.nist.gov/vuln/detail/CVE-2024-22270) | **High**     | 7.1  | [versions affected](https://www.cve.org/CVERecord?id=CVE-2024-22270) | 14/05/2024 |
| [CVE-2024-22273](https://nvd.nist.gov/vuln/detail/CVE-2024-22273) | **High**     | 8.1  | [versions affected](https://www.cve.org/CVERecord?id=CVE-2024-22273) | 21/05/2024 |
| [CVE-2024-22274](https://nvd.nist.gov/vuln/detail/CVE-2024-22274) | **High**     | 7.2  | [versions affected](https://www.cve.org/CVERecord?id=CVE-2024-22274) | 21/05/2024 |
| [CVE-2024-22275](https://nvd.nist.gov/vuln/detail/CVE-2024-22275) | **Medium**   | 4.9  | [versions affected](https://www.cve.org/CVERecord?id=CVE-2024-22275) | 21/05/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Broadcom support portal: VMSA-2024-0010](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24280)
- [Broadcom support portal: VMSA-2024-0011](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24308)

## Additional References

- https://securityonline.info/broadcom-security-alert-vmware-vulnerabilities-expose-data-enable-attacks/
- https://www.zerodayinitiative.com/advisories/ZDI-24-494/
