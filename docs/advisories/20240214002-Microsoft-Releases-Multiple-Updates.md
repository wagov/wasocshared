# Microsoft Releases Security Updates for Multiple Products - 20240214002

## Overview

Microsoft has released security updates to address vulnerabilities in multiple products including active exploits. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is vulnerable?

| Product(s) Affected                                                                                | Summary                                                                                | Severity     | CVSS | Active Exploitation | Dated        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------ | ---- | ------------------- | ------------ |
| [**February 2024 Security Updates**](https://msrc.microsoft.com/update-guide/releaseNote/2024-Feb) |                                                                                        |              |      |                     | 13 Feb, 2024 |
| **Internet Shortcut Files Security Feature Bypass Vulnerability**                                  | [CVE-2024-21412](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21412) | **High**     | 8.1  | **Yes**             | 15 Feb, 2024 |
| **Windows SmartScreen Security Feature Bypass Vulnerability**                                      | [CVE-2024-21351](https://nvd.nist.gov/vuln/detail/CVE-2024-21351)                      | **High**     | 7.6  | **Yes**             | 13 Feb, 2024 |
| **Microsoft Exchange Server Elevation of Privilege Vulnerability**                                 | [CVE-2024-21410](https://nvd.nist.gov/vuln/detail/CVE-2024-21410)                      | **Critical** | 9.8  | **Yes**             | 15 Feb, 2024 |

## What has been observed?

CISA added this vulnerability in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks* (refer [Patch Management](../guidelines/patch-management.md)).

## Additional References

- [CISA - Microsoft Releases Security Updates for Multiple Products](https://www.cisa.gov/news-events/alerts/2024/02/13/microsoft-releases-security-updates-multiple-products)
- [Internet Shortcut Files Security Feature Bypass Vulnerability](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-21412)
- [CISA Known Exploited Vulnerabilities ](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
