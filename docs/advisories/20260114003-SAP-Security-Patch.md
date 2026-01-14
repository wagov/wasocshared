# SAP Security Patch - 20260114003

## Overview

SAP has released security patches as part of the January 2026 Security Patch Day, including four critical vulnerabilities. These vulnerabilities introduce risks such as SQL injection, remote code execution (RCE), code injection, and privilege escalation, potentially allowing attackers to fully compromise affected systems

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| SAP S/4HANA      | S4CORE 102, 103, 104, 105, 106, 107, 108, 109    | [CVE-2026-0501](https://nvd.nist.gov/vuln/detail/CVE-2026-0501)  <br> [CVE-2026-0498](https://nvd.nist.gov/vuln/detail/CVE-2026-0498) | 9.9 <br> 9.1 | **Critical** <br> **Critical** |
| SAP Wily Introscope Enterprise Manager (WorkStation)      | 10.8    | [CVE-2026-0500](https://nvd.nist.gov/vuln/detail/CVE-2026-0500)                                                                        | 9.6          | **Critical** |
| SAP Landscape Transformation      | DMIS 2011_1_700, 2011_1_710, 2011_1_730, 2011_1_731, 2018_1_752, 2020    | [CVE-2026-0491](https://nvd.nist.gov/vuln/detail/CVE-2026-0491)                                                                        | 9.1          | **Critical**| 


## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- SAP: <https://support.sap.com/en/my-support/knowledge-base/security-notes-news/january-2026.html>
