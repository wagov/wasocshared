# SAP Monthly Security Patch - 20250813002

## Overview

SAP has released security updates to address critical vulnerabilities in S/4HANA and Landscape Transformation. These vulnerabilities, patched this month, include three code injection flaws that could allow attackers to execute arbitrary code with elevated privileges.

## What is vulnerable?

| Product(s) Affected                              | Version(s)                                                            | CVE                                                               | CVSS | Severity     |
| ------------------------------------------------ | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| SAP S/4HANA (Private Cloud or On-Premise)        | S4CORE 102, 103, 104, 105, 106, 107, 108                              | [CVE-2025-42957](https://www.cve.org/CVERecord?id=CVE-2025-42957) | 9.9  | **Critical** |
| SAP Landscape Transformation (Analysis Platform) | DMIS 2011_1_700, 2011_1_710, 2011_1_730, 2011_1_731, 2011_1_752, 2020 | [CVE-2025-42950](https://www.cve.org/CVERecord?id=CVE-2025-42950) | 9.9  | **Critical** |
| SAP S/4HANA (Private Cloud or On-Premise)        | S4CORE 102, 103, 104, 105, 106, 107, 108                              | [CVE-2025-27429](https://www.cve.org/CVERecord?id=CVE-2025-27429) | 9.9  | **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- SAP: <https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2025.html>
