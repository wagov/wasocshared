# Microsoft Releases Critical Security Updates - 20241009001

## Overview

Microsoft has released security updates to address vulnerabilities in multiple products. A Cyber threat actor could leverage some of these vulnerabilities to exploit the affected system.

## What is vulnerable?

This release consists of the following 117 Microsoft CVEs:

- [May 2024 Security Updates](https://msrc.microsoft.com/update-guide/releaseNote/2024-Oct)

| Product(s) Affected             | CVE                                                                             | Severity     | CVSS | Exploited |
| ------------------------------- | ------------------------------------------------------------------------------- | ------------ | ---- | --------- |
| Microsoft Configuration Manager | [CVE-2024-43468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43468) | **Critical** | 9.8  | Yes       |
| Windows Server 2019             | [CVE-2024-38124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38124) | **Critical** | 9.0  | No        |
| Windows 10 Version 1809         | [CVE-2024-43572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43572) | **High**     | 7.8  | Yes       |
| Windows 10 Version 22H2         | [CVE-2024-43573](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43573) | **Medium**   | 6.5  | Yes       |

## What has been observed?

CISA added one or more of the above vulnerabilities in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks*, or *48 hours* where exploited (refer [Patch Management](../guidelines/patch-management.md)).

- Microsoft Security Update Release Notes: <https://www.cisa.gov/news-events/alerts/2024/10/08/cisa-adds-three-known-exploited-vulnerabilities-catalog>

## Additional References

- CISA Known Exploited Vulnerabilities Update: <https://www.cisa.gov/news-events/alerts/2026/02/12/cisa-adds-four-known-exploited-vulnerabilities-catalog>

### Change log

- 2024-10-09: Initial Publication
- 2026-12-13: Added known exploitation
