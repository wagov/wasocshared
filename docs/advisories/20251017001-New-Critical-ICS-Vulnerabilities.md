# New Critical ICS Vulnerabilities - 20251017001

## Overview

CISA has released multiple advisories for Industrial Control Systems (ICS) related vendors.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS        | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| SIMATIC ET 200SP     | CP 1542SP-1, CP 1542SP-1 IRC and CP 1543SP-1, incl. SIPLUS variants    | [CVE-2025-40771](https://nvd.nist.gov/vuln/detail/CVE-2025-40771)                                                                        | CVSS v3.1:	9.8 <br> CVSS v4.0:	9.3  | **Critical**                                   |
| TeleControl Server Basic V3.1      |  All versions >= V3.1.2.2 < V3.1.2.3   | [CVE-2025-40765](https://nvd.nist.gov/vuln/detail/CVE-2025-40765)  | CVSS v3.1:	9.8 <br> CVSS v4.0: 9.3 | **Critical** |


## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- SIEMENS: <ol><li><https://cert-portal.siemens.com/productcert/html/ssa-486936.html> </li><li> <https://cert-portal.siemens.com/productcert/html/ssa-062309.html> </li></ol>

## Additional References

- CISA: <https://www.cisa.gov/news-events/alerts/2025/10/16/cisa-releases-thirteen-industrial-control-systems-advisories>
