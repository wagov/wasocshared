# ISC Releases Multiple BIND 9 Security Advisories - 20240725001

## Overview

The Internet Systems Consortium (ISC) released security advisories to address vulnerabilities affecting multiple versions of ISC’s Berkeley Internet Name Domain (BIND) 9. A cyber threat actor could exploit one of these vulnerabilities to cause a denial-of-service condition.

## What is the vulnerability?

| CVE #                                                           | Product(s) and Version(s) Affected                                                                                                                                                                                                                                                                                                                                   | CVSS v4/v3 | Severity |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| [CVE-2024-4076](https://nvd.nist.gov/vuln/detail/CVE-2024-4076) | BIND </br> - 9.16.13 -> 9.16.50 </br> - 9.18.0 -> 9.18.27 </br> - 9.19.0 -> 9.19.24 </br> </br> BIND Supported Preview Edition </br> - 9.11.33-S1 -> 9.11.37-S1 </br> - 9.16.13-S1 -> 9.16.50-S1 </br> - 9.18.11-S1 -> 9.18.27-S1                                                                                                                                    | 7.5        | High     |
| [CVE-2024-1975](https://nvd.nist.gov/vuln/detail/CVE-2024-1975) | BIND </br> - 9.0.0 -> 9.11.37 </br> - 9.16.0 -> 9.16.50 </br> - 9.18.0 -> 9.18.27 </br> - 9.19.0 -> 9.19.24 </br> (Versions prior to 9.16.48 were not assessed.) </br>  </br> BIND Supported Preview Edition </br> - 9.9.3-S1 -> 9.11.37-S1 </br> - 9.16.8-S1 -> 9.16.49-S1 </br> - 9.18.11-S1 -> 9.18.27-S1 </br> (Versions prior to 9.16.48-S1 were not assessed.) | 7.5        | High     |
| [CVE-2024-1737](https://nvd.nist.gov/vuln/detail/CVE-2024-1737) | BIND </br> - 9.11.0 -> 9.11.37 </br> - 9.16.0 -> 9.16.50 </br> - 9.18.0 -> 9.18.27 </br> - 9.19.0 -> 9.19.24 </br> (Versions prior to 9.11.0 were not assessed.) </br> </br> BIND Supported Preview Edition </br> - 9.11.4-S1 -> 9.11.37-S1 </br> - 9.16.8-S1 -> 9.16.50-S1 </br> - 9.18.11-S1 -> 9.18.27-S1 </br> (Versions prior to 9.11.4-S1 were not assessed.)  | 7.5        | High     |
| [CVE-2024-0760](https://nvd.nist.gov/vuln/detail/CVE-2024-0760) | BIND </br> - 9.18.1 -> 9.18.27 </br> - 9.19.0 -> 9.19.24 </br> (Versions prior to 9.18.1 were not assessed.) </br> </br> BIND Supported Preview Edition </br> - 9.18.11-S1 -> 9.18.27-S1 </br> (Versions prior to 9.18.24-S1 were not assessed.)                                                                                                                     | 7.5        | High     |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of one month (refer [Patch Management](../guidelines/patch-management.md)):

ISC Advisories:

- <https://kb.isc.org/docs/cve-2024-4076>
- <https://kb.isc.org/docs/cve-2024-1975>
- <https://kb.isc.org/docs/cve-2024-1737>
- <https://kb.isc.org/docs/cve-2024-0760>

## Additional References

- CISA Advisory: <https://www.cisa.gov/news-events/alerts/2024/07/24/isc-releases-security-advisories-bind-9>
