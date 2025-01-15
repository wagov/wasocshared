# SAP Critical Vulnerabilities - 20250115001

## Overview

SAP released 14 new security notes during its monthly Security Patch Day. This release includes several critical and high-severity vulnerabilities affecting core SAP systems such as NetWeaver, BusinessObjects, and SAP GUI platforms.

## What is vulnerable?

| Product(s) Affected                                                            | Version(s)                                                                                                                                                                                                                                                                                                                    | CVE                                                             | CVSS | Severity     |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---- | ------------ |
| SAP NetWeaver AS for ABAP and ABAP Platform (Internet Communication Framework) | SAP_BASIS 700 <br> SAP_BASIS 701 <br> SAP_BASIS 702 <br> SAP_BASIS 731 <br> SAP_BASIS 740 <br> SAP_BASIS 750 <br> SAP_BASIS 751 <br> SAP_BASIS 752 <br> SAP_BASIS 753 <br> SAP_BASIS 754 <br> SAP_BASIS 755 <br> SAP_BASIS 756 <br> SAP_BASIS 757 <br> SAP_BASIS 758 <br> SAP_BASIS 912 <br> SAP_BASIS 913 <br> SAP_BASIS 914 | [CVE-2025-0066](https://nvd.nist.gov/vuln/detail/CVE-2025-0066) | 9.9  | **Critical** |
| SAP NetWeaver Application Server for ABAP and ABAP Platform                    | KRNL64NUC 7.22 <br> 7.22EXT <br> KRNL64UC 7.22 <br> 7.53 <br> 8.04 <br> KERNEL 7.22 <br> 7.54 <br> 7.77 <br> 7.89 <br> 7.93 <br> 7.97 <br> 9.12 <br> 9.13 <br> 9.14                                                                                                                                                           | [CVE-2025-0070](https://nvd.nist.gov/vuln/detail/CVE-2025-0070) | 9.9  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- SAP Security Patch Day – January 2025: <https://support.sap.com/en/my-support/knowledge-base/security-notes-news/january-2025.html>

## Additional References

- SecurityOnline: <https://securityonline.info/critical-sap-flaws-revealed-cve-2025-0070-and-cve-2025-0066-with-cvss-9-9-demand-immediate-action/>
