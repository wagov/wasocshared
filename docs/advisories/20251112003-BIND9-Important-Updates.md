# BIND9 Important Updates - 20251112003

## Overview

Internet Systems Consortium (ISC) have released a security advisory relating to a vulnerability identified in BIND9's DNS solution via its cache, poisoning attacks with unsolicited RRs. Successful exploitation could allow an attacker to remotely inject forged records data into the cache during a query, which can potentially affect resolution of future queries.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                                        | CVE                                                                                                                                                                                                           | CVSS                  | Severity                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------ |
| BIND                | 9.11.x prior to 9.16.50 </br> 9.18.x prior to 9.18.39 </br> 9.20.x prior to 9.20.13 </br> 9.21.x prior to 9.21.12 | [CVE-2025-8677](https://nvd.nist.gov/vuln/detail/CVE-2025-8677) <br> [CVE-2025-40778](https://nvd.nist.gov/vuln/detail/CVE-2025-40778) <br> [CVE-2025-40780](https://nvd.nist.gov/vuln/detail/CVE-2025-40780) | 8.6 <br> 8.6 <br> 8.6 | High <br> High <br> High |

## What has been observed?

ISC have noted "Versions prior to 9.11.0 were not specifically assessed but are also believed to be affected" within their advisory.
Tenable has noted one or more of the mentioned vulnerabilities as having an exploitation maturity of "Exploitation Available".
The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- ISC: <https://kb.isc.org/docs/cve-2025-40778>
