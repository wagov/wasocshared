# F5 Security Advisory Addresses Multiple Vulnerabilities - 20240510001

## Overview

F5 Product Development has released their quarterly security advisory for the month of May 2024, addressing multiple vulnerabilitites. An unauthenticated attacker can exploit these vulnerabilities if left unpatched.

## What is vulnerable?

| CVE                                                               | Severity | CVSS | Product(s) Affected                                                                              | Summary                                                                                                                                                                                                                                                                                                     | Dated       |
| ----------------------------------------------------------------- | -------- | ---- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [CVE-2024-26026](https://nvd.nist.gov/vuln/detail/CVE-2024-26026) | **High** | 7.5  | BIG-IP Next Central Manager **versions 20.0.1 - 20.1.0**                                         | An SQL injection vulnerability exists in the BIG-IP Next Central Manager API (URI). Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated                                                                                                                            | 8 May, 2024 |
| [CVE-2024-21793](https://nvd.nist.gov/vuln/detail/CVE-2024-21793) | **High** | 7.5  | BIG-IP Next Central Manager **versions 20.0.1 - 20.1.0**                                         | An OData injection vulnerability exists in the BIG-IP Next Central Manager API (URI). Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.                                                                                                                         | 8 May, 2024 |
| [CVE-2024-31156](https://nvd.nist.gov/vuln/detail/CVE-2024-31156) | **High** | 7.5  | BIG-IP (all modules)**versions <br/>17.1.0 - 17.1.1,<br/>16.1.0 - 16.1.4,<br/>15.1.0 - 15.1.10** | A stored cross-site scripting (XSS) vulnerability exists in an undisclosed page of the BIG-IP Configuration utility that allows an attacker to run JavaScript in the context of the currently logged-in user. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated. | 8 May, 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [MyF5 Quarterly Security Notification](https://my.f5.com/manage/s/article/K000139404)
