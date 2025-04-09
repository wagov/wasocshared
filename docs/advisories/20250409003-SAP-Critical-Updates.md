# SAP Critical Updates - 20250409003

## Overview

SAP has released security updates to address multiple vulnerabilities. It is crucial to apply the latest fixes, as several of them address severe code injection vulnerabilities that pose a significant threat to SAP systems.

## What is vulnerable?

| Product(s) Affected                              | Version(s)                                              | CVE                                                                | CVSS | Severity     |
| ------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------ | ---- | ------------ |
| SAP S/4HANA                                      | S4CORE 102 through 108                                  | [CVE-2025-27429](https://www.cve.org/CVERecord?id=CVE-2025-27429)  | 9.9  | **Critical** |
| SAP Landscape Transformation (Analysis Platform) | DMIS 2011_1_700, 2011_1_710, 2011_1_730, and 2011_1_731 | [CVE-2025-31330](https://www.cve.org/CVERecord?id=CVE-2025-31330)  | 9.9  | **Critical** |
| SAP Financial Consolidation                      | FINANCE 1010                                            | [CVE-2025-30016](https://www.cve.org/CVERecord?id=CVE-2025-30016)  | 9.8  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected products within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- SAP advisory: <https://support.sap.com/en/my-support/knowledge-base/security-notes-news/april-2025.html>

## Additional References

- SecurityOnline: <https://securityonline.info/sap-april-2025-patch-day-critical-code-injection-risks/>
