# SQL-based Critical Vulnerabilities - 20240926001

## Overview

The WA SOC has been made aware that a severe security flaw has been uncovered in pgAdmin, allowing  attackers to execute malicious code on servers running pgAdmin, potentially compromising the entire database system.

sqlite-vec v0.1.1 was discovered to contain a heap buffer overflow via the npy_token_next function. This vulnerability allows attackers to cause a Denial of Service (DoS) via a crafted file.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                       | CVSS          | Severity                                                         |
| ------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
| pgAdmin       | <=8.11    | [CVE-2024-9014](https://nvd.nist.gov/vuln/detail/CVE-2024-9014)                                                                         | 9.9           | **Critical**                                     |
| sqlLite     | v0.1.1    | [CVE-2024-46488](https://nvd.nist.gov/vuln/detail/CVE-2024-46488) </br> | 9.1 </br> | **Critical**
## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

Given the severity of this vulnerability and its potential impact on data security, the WA SOC recomends update to the latest version, pgAdmin 4 version 8.12, as soon as possible.
- pgAdmin: <https://www.pgadmin.org/docs/pgadmin4/development/release_notes_8_12.html>

## Additional References

3rd Party Reference
- <https://nvd.nist.gov/vuln/detail/CVE-2024-9014>
- <https://nvd.nist.gov/vuln/detail/CVE-2024-46488>
