# Siemens Critical Vulnerabilities - 20250912001

## Overview

Siemens has released multiple critical vulnerabilities that could allow an unauthenticated remote attacker to execute arbitrary code, cause a DoS condition, or exploit a flaw that exposes a network share without authentication. 

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
|  SIMATIC (SIVaaS)     | All versions    | [CVE-2025-40804](https://nvd.nist.gov/vuln/detail/CVE-2025-40804)                                                                        | 9.3          | **Critical**                                   |
| User Management Component (UMC)      |  < V2.15.1.3    | [CVE-2025-40795](https://nvd.nist.gov/vuln/detail/CVE-2025-40795)  | 9.8 | **Critical**

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Siemens: <https://cert-portal.siemens.com/productcert/html/ssa-722410.html>

## Additional References

- CISA: <https://www.cisa.gov/news-events/alerts/2025/09/11/cisa-releases-eleven-industrial-control-systems-advisories>
