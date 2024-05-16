# HPE Aruba Networking Multiple Critical Vulnerabilities - 20240516001

## Overview

HPE Aruba Networking has issued an urgent security advisory, urging customers to patch their Aruba Access Points running InstantOS and ArubaOS 10 due to the discovery of multiple critical vulnerabilities. These flaws could allow unauthenticated attackers to execute malicious code remotely, potentially leading to a complete takeover of the affected devices.

## What is vulnerable?

| CVE                                                                                                                                   | Severity     | CVSS | Summary                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---- | ------------------------------------------------------------------------- |
| [CVE-2024-31466](https://nvd.nist.gov/vuln/detail/CVE-2024-31466) , [CVE-2024-31467](https://nvd.nist.gov/vuln/detail/CVE-2024-31467) | **Critical** | 9.8  | Buffer Overflow Vulnerabilities in CLI Service                            |
| [CVE-2024-31468](https://nvd.nist.gov/vuln/detail/CVE-2024-31468) , [CVE-2024-31469](https://nvd.nist.gov/vuln/detail/CVE-2024-31469) | **Critical** | 9.8  | Buffer Overflow Vulnerabilities in Central Communications Service         |
| [CVE-2024-31470](https://nvd.nist.gov/vuln/detail/CVE-2024-31470)                                                                     | **Critical** | 9.8  | Buffer Overflow Vulnerability in SAE Service                              |
| [CVE-2024-31471](https://nvd.nist.gov/vuln/detail/CVE-2024-31471)                                                                     | **Critical** | 9.8  | Command Injection Vulnerability in Central Communications Service         |
| [CVE-2024-31472](https://nvd.nist.gov/vuln/detail/CVE-2024-31472)                                                                     | **Critical** | 9.8  | Command Injection Vulnerabilities in Soft AP Daemon Service               |
| [CVE-2024-31473](https://nvd.nist.gov/vuln/detail/CVE-2024-31473)                                                                     | **Critical** | 9.8  | Command Injection Vulnerability in Deauthentication Service               |
| [CVE-2024-31474](https://nvd.nist.gov/vuln/detail/CVE-2024-31474)                                                                     | **High**     | 8.2  | Arbitrary File Deletion in CLI Service                                    |
| [CVE-2024-31475](https://nvd.nist.gov/vuln/detail/CVE-2024-31475)                                                                     | **High**     | 8.2  | Arbitrary File Deletion in Central Communications Service                 |
| [CVE-2024-31476](https://nvd.nist.gov/vuln/detail/CVE-2024-31476) , [CVE-2024-31477](https://nvd.nist.gov/vuln/detail/CVE-2024-31477) | **High**     | 9.8  | Authenticated Command Injection in CLI Interface                          |
| [CVE-2024-31478](https://nvd.nist.gov/vuln/detail/CVE-2024-31478)                                                                     | **Medium**   | 5.3  | Denial-of-Service (DoS) Vulnerabilities in Soft AP Daemon Service         |
| [CVE-2024-31479](https://nvd.nist.gov/vuln/detail/CVE-2024-31479)                                                                     | **Medium**   | 5.3  | Denial-of-Service (DoS) Vulnerabilities in Central Communications Service |
| [CVE-2024-31480](https://nvd.nist.gov/vuln/detail/CVE-2024-31480) , [CVE-2024-31481](https://nvd.nist.gov/vuln/detail/CVE-2024-31481) | **Medium**   | 5.3  | Denial-of-Service (DoS) Vulnerabilities in CLI Service                    |
| [CVE-2024-31482](https://nvd.nist.gov/vuln/detail/CVE-2024-31482)                                                                     | **Medium**   | 5.3  | Denial-of-Service (DoS) Vulnerabilities in ANSI Escape Code Service       |
| [CVE-2024-31483](https://nvd.nist.gov/vuln/detail/CVE-2024-31483)                                                                     | **Medium**   | 4.9  | Sensitive Information Disclosure in CLI Service                           |

**Affected Software Versions:**

- ArubaOS:
    - 10.5.x.x: 10.5.1.0 and below
    - 10.4.x.x: 10.4.1.0 and below
- InstantOS:
    - 8.11.x.x: 8.11.2.1 and below
    - 8.10.x.x: 8.10.0.10 and below
    - 8.6.x.x: 8.6.0.23 and below

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [**Aruba Access Points Multiple Vulnerabilities**](https://www.arubanetworks.com/assets/alert/ARUBA-PSA-2024-006.txt)

## Additional References

- [Security Online: HPE Aruba Networking Patches Critical Vulnerabilities in Access Points](https://securityonline.info/hpe-aruba-networking-patches-critical-vulnerabilities-in-access-points/)
