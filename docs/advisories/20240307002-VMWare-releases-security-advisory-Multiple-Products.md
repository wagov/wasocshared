# VMware Releases Security Advisory for Multiple Products - 20240307002

## Overview

VMware released a security advisory to address multiple vulnerabilities in ESXi, Workstation, Fusion, and Cloud Foundation. A cyber threat actor could exploit one of these vulnerabilities to take control of an affected system.

## What is vulnerable?

| Product(s) Affected                           | Severity | Version  | CVEs                                                                                                                                                                                                                                                                                           | CVSS                                                            | Dated       |
| --------------------------------------------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------- |
| VMware ESXi                                   | Critical | 7.0, 8.0 | <br>- [CVE-2024-22252](https://nvd.nist.gov/vuln/detail/CVE-2024-22252) <br>- [CVE-2024-22253](https://nvd.nist.gov/vuln/detail/CVE-2024-22253) <br>-[CVE-2024-22254](https://nvd.nist.gov/vuln/detail/CVE-2024-22254) <br>- [CVE-2024-22255](https://nvd.nist.gov/vuln/detail/CVE-2024-22255) | <br>-Vmware 9.3 <br>-Vmware 9.3 <br>-Vmware 7.9 <br>-Vmware 7.1 | 5 Mar, 2024 |
| VMware Workstation Pro / Player (Workstation) | Critical | 17.x     | <br>- [CVE-2024-22252](https://nvd.nist.gov/vuln/detail/CVE-2024-22252) <br>- [CVE-2024-22253](https://nvd.nist.gov/vuln/detail/CVE-2024-22253) <br>- [CVE-2024-22255](https://nvd.nist.gov/vuln/detail/CVE-2024-22255)                                                                        | -Vmware 9.3 <br>-Vmware 9.3 <br>-Vmware 7.1                     | 5 Mar, 2024 |
| VMware Fusion Pro / Fusion (Fusion)           | Critical | 13.x     | <br>- [CVE-2024-22252](https://nvd.nist.gov/vuln/detail/CVE-2024-22252) <br>- [CVE-2024-22253](https://nvd.nist.gov/vuln/detail/CVE-2024-22253) <br>-[CVE-2024-22255](https://nvd.nist.gov/vuln/detail/CVE-2024-22255)                                                                         | -Vmware 9.3 <br>-Vmware 9.3 <br>-Vmware 7.1                     | 5 Mar, 2024 |
| VMware Cloud Foundation (Cloud Foundation)    | Critical | 5.x/4.x  | <br>- [CVE-2024-22252](https://nvd.nist.gov/vuln/detail/CVE-2024-22252) <br>- [CVE-2024-22253](https://nvd.nist.gov/vuln/detail/CVE-2024-22253)<br>- [CVE-2024-22254](https://nvd.nist.gov/vuln/detail/CVE-2024-22254) <br>- [CVE-2024-22255](https://nvd.nist.gov/vuln/detail/CVE-2024-22255) | -Vmware 9.3 <br>-Vmware 9.3 <br>-Vmware 7.9 <br>-Vmware 7.1     | 5 Mar, 2024 |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- [VMware advisory VMSA-2024-0006.1](https://www.vmware.com/security/advisories/VMSA-2024-0006.html)

## Additional References

- [CISA - VMware Releases Security Advisory for Multiple Products](https://www.cisa.gov/news-events/alerts/2024/03/06/vmware-releases-security-advisory-multiple-products)
