# CISA Releases New ICS Advisories - 20240801002

## Overview

The WA SOC has been made aware of vulnerabilities discovered in the Philips Vue PACS image management and communication system, which can be remotely exploited in a low-complexity attack. Successful exploitation of these vulnerabilities may allow threat actors to remotely execute code, install unauthorised software, eavesdrop, view, or modify data, or negatively impact the system.

## What is vulnerable?
The 13 vulnerabilities affect all versions prior to 12.2.8.410.
| CVE |Type                                | CVSS                    |  
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | 
| [CVE-2017-17485](https://nvd.nist.gov/vuln/detail/CVE-2017-17485)      | Deserialization of untrusted data | 9.8 </br>  |
| [CVE-2020-11113](https://nvd.nist.gov/vuln/detail/CVE-2020-11113)      | Deserialization of untrusted data | 8.8 </br>  |
| [CVE-2020-10673](https://nvd.nist.gov/vuln/detail/CVE-2020-10673)      | Deserialization of untrusted data | 8.8 </br>  |
| [CVE-2023-40159](https://nvd.nist.gov/vuln/detail/CVE-2023-40159)      | Exposure of sensitive information to an unauthorized actor | 8.8 </br>  |
| [CVE-2023-40704](https://nvd.nist.gov/vuln/detail/CVE-2023-40704)      | Use of default credentials | 8.4 </br>  |
| [CVE-2020-35728](https://nvd.nist.gov/vuln/detail/CVE-2020-35728)      | Deserialization of untrusted data | 8.1 </br>  |
| [CVE-2021-20190](https://nvd.nist.gov/vuln/detail/CVE-2021-20190)      | Deserialization of untrusted data | 8.1 </br>  |
| [CVE-2020-14061](https://nvd.nist.gov/vuln/detail/CVE-2020-14061)      | Deserialization of untrusted data | 8.1 </br>  |
| [CVE-2021-28165](https://nvd.nist.gov/vuln/detail/CVE-2021-28165)      | Uncontrolled resource consumption | 7.5 </br>  |
| [CVE-2020-36518](https://nvd.nist.gov/vuln/detail/CVE-2020-36518)      | Out-of-bounds write data | 7.5 </br>  |
| [CVE-2019-12814](https://nvd.nist.gov/vuln/detail/CVE-2019-12814)      | Deserialization of untrusted data | 5.9 </br>  |
| [CVE-2023-40223](https://nvd.nist.gov/vuln/detail/CVE-2023-40223)      | Improper privilege management | 4.8 </br>  |
| [CVE-2023-40539](https://nvd.nist.gov/vuln/detail/CVE-2023-40539)      | Weak password requirements  | 4.8 </br>  |


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *1 month* (refer [Patch Management](../guidelines/patch-management.md)):

- Philips Security Advisories: <https://www.philips.com/a-w/security/security-advisories.html#security_advisories>

## Reference

- CISA: <https://www.cisa.gov/news-events/ics-medical-advisories/icsma-24-200-01>
