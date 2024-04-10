# Fortinet Releases Security Updates for Multiple Products - 20240410002

## Overview

Fortinet released security updates to address vulnerabilities in multiple products, including OS and FortiProxy. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is vulnerable?

| CVE                                                                                                                                                                 | Severity     | CVSS | Product(s) Affected                                                                                                         | Summary                                                                                                                                                                                             | Dated         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [CVE-2023-45588](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45588) <br>[CVE-2024-31492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-31492) | **High**     | 7.8  | [FortiClientMac](https://www.fortiguard.com/psirt/FG-IR-23-345)                                                             | Lack of configuration file validation may allow a local attacker to execute arbitrary code or commands via writing a malicious configuration file in /tmp before starting the installation process. | 9 April, 2024 |
| [CVE-2023-45590](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45590)                                                                                     | **Critical** | 9.4  | [FortiClient Linux](https://www.fortiguard.com/psirt/FG-IR-23-087)                                                          | Remote Code Execution due to dangerous nodejs configuration may allow an unauthenticated attacker to execute arbitrary code via tricking a FortiClientLinux user into visiting a malicious website. | 9 April, 2024 |
|                                                                                                                                                                     | **TBD**      | TBD  | [FortiOS & FortiProxy](https://www.fortiguard.com/psirt/FG-IR-23-345%20%20%20https://www.fortiguard.com/psirt/FG-IR-23-493) | Administrator cookie leakage                                                                                                                                                                        | 9 April, 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [CISA](https://www.cisa.gov/news-events/alerts/2024/04/09/fortinet-releases-security-updates-multiple-products)
