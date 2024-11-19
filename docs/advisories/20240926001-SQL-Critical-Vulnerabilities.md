# SQL-based Critical Vulnerabilities - 20240926001

## Overview

The WA SOC has been made aware of reports of critical vulnerabilities relating to SQLite and pgAdmin (open-source management tool for PostgreSQL databases). Successful exploitation could allow attackers to execute malicious code on servers running pgAdmin, potentially compromising the entire database system. Aditionally, sqlite-vec v0.1.1 was discovered to contain a heap buffer overflow via the npy_token_next function, which could allow attackers to cause a Denial of Service (DoS) via a crafted file.

## What is vulnerable?

| Product(s) Affected    | Version(s) | CVE                                                               | CVSS | Severity     |
| ---------------------- | ---------- | ----------------------------------------------------------------- | ---- | ------------ |
| pgAdmin for PostgreSQL | < 8.12     | [CVE-2024-9014](https://nvd.nist.gov/vuln/detail/CVE-2024-9014)   | 9.9  | **Critical** |
| sqlLite                | \<= 0.1.1  | [CVE-2024-46488](https://nvd.nist.gov/vuln/detail/CVE-2024-46488) | 9.1  | **Critical** |

## What has been observed?

CISA is aware of exploitation in the wild for CVE-2024-46488. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- pgAdmin for PostgreSQL: <https://www.pgadmin.org/docs/pgadmin4/development/release_notes_8_12.html>
- SQLite: <https://github.com/VulnSphere/LLMVulnSphere/blob/main/VectorDB/sqlite-vec/OOBR_2.md>

## Additional References

- SecurityOnline: <https://securityonline.info/cve-2024-9014-cvss-9-9-pgadmins-critical-vulnerability-puts-user-data-at-risk/>
