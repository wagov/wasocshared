# HPE Aruba Network Products Critical Remote Code Execution (RCE) Vulnerabilities - 20240502001

## Overview

The WA SOC has been made aware of Critical Remote Code Execution (RCE) Vulnerabilities affecting multiple ArubaOS versions in HPE Aruba Network Products.

## What is vulnerable?

Products affected by the listed vulnerabilities:

Mobility Conductor,Mobility Controllers,WLAN Gateways and SD-WAN Gateways managed by Aruba Central with OS versions: <br> - ArubaOS 10.5.1.0 and below <br> - ArubaOS 10.4.1.0 and below <br> - ArubaOS 8.11.2.1 and below <br> - ArubaOS 8.10.0.10 and below <br> <br>
Products affected by these vulnerabilities and are not patched by this advisory: <br>  - ArubaOS 10.3.x.x:          all <br> - ArubaOS 8.9.x.x:           all <br> - ArubaOS 8.8.x.x:           all <br> - ArubaOS 8.7.x.x:           all <br> - ArubaOS 8.6.x.x:           all <br> - ArubaOS 6.5.4.x:           all <br> - SD-WAN 8.7.0.0-2.3.0.x:    all <br> - SD-WAN 8.6.0.4-2.2.x.x:    all

| CVE                                                                                                                                                                                                             | Severity     | CVSS | Summary                                                                                                                           | Dated      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---- | --------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [CVE-2024-26305](https://nvd.nist.gov/vuln/detail/CVE-2024-26305)                                                                                                                                               | **Critical** | 9.8  | Buffer overflow vulnerability in the underlying Utility daemon that could lead to unauthenticated RCE                             | 30/04/2024 |
| [CVE-2024-26304](https://nvd.nist.gov/vuln/detail/CVE-2024-26304)                                                                                                                                               | **Critical** | 9.8  | Buffer overflow vulnerability in the underlying L2/L3 Management service that could lead to unauthenticated RCE                   | 30/04/2024 |
| [CVE-2024-33511](https://nvd.nist.gov/vuln/detail/CVE-2024-33511)                                                                                                                                               | **Critical** | 9.8  | Buffer overflow vulnerability in the underlying Automatic Reporting service that could lead to unauthenticated RCE                | 30/04/2024 |
| [CVE-2024-33512](https://nvd.nist.gov/vuln/detail/CVE-2024-33512)                                                                                                                                               | **Critical** | 9.8  | Buffer overflow vulnerability in the underlying Local User Authentication Database service that could lead to unauthenticated RCE | 30/04/2024 |
| [CVE-2024-33513](https://nvd.nist.gov/vuln/detail/CVE-2024-33513) <br> [CVE-2024-33514](https://nvd.nist.gov/vuln/detail/CVE-2024-33514) <br> [CVE-2024-33515](https://nvd.nist.gov/vuln/detail/CVE-2024-33515) | **Medium**   | 5.9  | Unauthenticated Denial-of-Service (DoS Vulnerabilities in the AP Management Service Accessed via the PAPI Protocol                | 30/04/2024 |
| [CVE-2024-33516](https://nvd.nist.gov/vuln/detail/CVE-2024-33516)                                                                                                                                               | **Medium**   | 5.3  | Unauthenticated Denial-of-Service (DoS) Vulnerability in Auth Service Accessed via the PAPI Protocol                              | 30/04/2024 |
| [CVE-2024-33517](https://nvd.nist.gov/vuln/detail/CVE-2024-33517)                                                                                                                                               | **Medium**   | 5.3  | Unauthenticated Denial-of-Service (DoS) Vulnerability in the Radio Frequency Manager Service Accessed via the PAPI Protocol       | 30/04/2024 |
| [CVE-2024-33518](https://nvd.nist.gov/vuln/detail/CVE-2024-33518)                                                                                                                                               | **Medium**   | 5.3  | Unauthenticated Denial-of-Service (DoS) Vulnerabilities in the Radio Frequency daemon via the PAPI protocol                       | 30/04/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [HPE Aruba Networking Product Security Advisory](https://www.arubanetworks.com/assets/alert/ARUBA-PSA-2024-004.txt)

## Additional References

- N/A
