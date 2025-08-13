# SAP Monthly Security Patch - 20250813002

## Overview

SAP has released security updates to address critical vulnerabilities affecting multiple products. These vulnerabilities include code injection flaws that could allow attackers to execute arbitrary code with elevated privileges.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
| ------------------- | ---------- | --- | ---- | -------- |
| SAP S/4HANA | S4CORE 102 <br> 103 <br> 104 <br> 105 <br> 106 <br> 107 <br> 108 | [CVE-2025-42957](https://www.cve.org/CVERecord?id=CVE-2025-42957) <br> [CVE-2025-27429](https://www.cve.org/CVERecord?id=CVE-2025-27429) | 9.9 <br> 9.9 | **Critical** <br> **Critical** |
| SAP Landscape Transformation | DMIS 2011_1_700 <br> 2011_1_710 <br> 2011_1_730 <br> 2011_1_731 <br> 2011_1_752 <br> 2020 | [CVE-2025-42950](https://www.cve.org/CVERecord?id=CVE-2025-42950) | 9.9  | **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- SAP: <https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2025.html>
