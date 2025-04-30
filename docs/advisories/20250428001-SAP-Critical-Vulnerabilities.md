# SAP New Critical Vulnerabilities - 20250428001

## Overview

Since the initial publication of [Advisory #20250409003](https://soc.cyber.wa.gov.au//advisories/20250409003-SAP-Critical-Updates), SAP has updated their monthly patch release notes to include three new critical severity vulnerabilities. Successful exploitation could allow an unauthenticated agent to upload potentially malicious executable binaries that could severely harm the host system.

## What is vulnerable?

| Product(s) Affected                                | Version(s)                                          | CVE                                                               | CVSS | Severity     |
| -------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| SAP NetWeaver (Visual Composer development server) | VCFRAMEWORK 7.50                                    | [CVE-2025-31324](https://nvd.nist.gov/vuln/detail/CVE-2025-31324) | 10   | **Critical** |
| SAP S/4HANA (Private Cloud or On-Premise)          | S4CORE 102, 103, 104, 105, 106, 107, 108            | [CVE-2025-27429](https://nvd.nist.gov/vuln/detail/CVE-2025-27429) | 9.9  | **Critical** |
| SAP Landscape Transformation (Analysis Platform)   | DMIS 2011_1_700, 2011_1_710, 2011_1_730, 2011_1_731 | [CVE-2025-31330](https://nvd.nist.gov/vuln/detail/CVE-2025-31330) | 9.9  | **Critical** |

## What has been observed?

CISA added CVE-2025-31324 vulnerability in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- SAP: <https://support.sap.com/en/my-support/knowledge-base/security-notes-news/april-2025.html>

### Additional Resources

- The Register: <https://www.theregister.com/2025/04/25/sap_netweaver_patch/>
