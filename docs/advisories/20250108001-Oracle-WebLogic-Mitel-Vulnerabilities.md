# Known Exploited Oracle WebLogic and Mitel Vulnerabilities - 20250108001

## Overview

The WA SOC has been made aware of exploits released for a high vulnerabilities in Oracle WebLogic and Mitel products.

The Oracle vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle WebLogic. Authentication is not required to exploit this vulnerability.

The Mitel MiCollab vulnerability could allow an unauthenticated attacker to conduct a path traversal attack due to insufficient input validation.
A successful exploit of this vulnerability could allow an attacker to gain unauthorised access, with potential impacts to the confidentiality, integrity, and availability of the system.

## What is vulnerable?

| Product(s) Affected    | Version(s)                                    | CVE                                                                                                                                      | CVSS         | Severity              |
| ---------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------- |
| Oracle WebLogic Server | Version 10.3.6.0.0 <br> Version \<=12.2.1.4.0 | [CVE-2020-2883](https://www.cve.org/CVERecord?id=CVE-2020-2883)                                                                          | 9.8          | **Critical**          |
| Mitel MiCollab         | Version 9.8 SP1 FP2 (9.8.1.201) and earlier   | [CVE-2024-41713](https://www.cve.org/CVERecord?id=CVE-2024-41713) <br> [CVE-2024-55550](https://www.cve.org/CVERecord?id=CVE-2024-55550) | 9.8 <br> 2.7 | **Critical** <br> Low |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Oracle: <https://www.oracle.com/security-alerts/cpuapr2020.html>
- Mitel: <https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2024-0029>

## Additional References

- Zero Day Initiative: \<https://www.zerodayinitiative.com/advisories/ZDI-20-504/
