# SAP Security Advisory April 2024 - 20240416002

## Overview

The WA SOC has become aware of a security misconfiguration vulnerability in SAP NetWeaver AS Java User Management Engine. Self-Registration and Modify your own profile in User Admin Application of NetWeaver AS Java does not enforce proper security requirements for the content of the newly defined security answer. This can be leveraged by an attacker to cause profound impact on confidentiality and low impact on both integrity and availability

## What is vulnerable?

| CVE                                                                | Severity | CVSS | Product(s) Affected                                                                                                           | Dated      |
| ------------------------------------------------------------------ | -------- | ---- | ----------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [CVE-2024-27899,](https://nvd.nist.gov/vuln/detail/CVE-2024-27899) | **High** | 8.8  | SAP NetWeaver AS Java User Management Engine Versions: ***<br>- SERVERCORE 7.50, <br>- J2EE-APPS 7.50, <br>- UMEADMIN 7.50*** | 04/09/2024 |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Patch Notes](https://me.sap.com/notes/3434839)

## Additional References

- [SAP's April 2024 Updates Patch High-Severity Vulnerabilities - SecurityWeek](https://www.securityweek.com/saps-april-2024-updates-patch-high-severity-vulnerabilities/)

- [CVE-2024-27899 | Tenable®](https://www.tenable.com/cve/CVE-2024-27899)

- [SAP Security Patch Day -- April 2024](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/april-2024.html)
