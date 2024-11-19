# Juniper Junos OS EX / SRX vulnerabilities - 20231114002

## Overview

Juniper has released updates to five known vulnerabilities in Juniper's Junos OS, that are being actively exploited.

## What is the vulnerability?

[**CVE-2023-36844**](https://nvd.nist.gov/vuln/detail/CVE-2023-36844) - CVSS v3 Base Score: ***5.3*** - Juniper Junos OS EX Series PHP External Variable Modification Vulnerability:

- A PHP External Variable Modification vulnerability in J-Web of Juniper Networks Junos OS on EX Series allows an unauthenticated, network-based attacker to control certain, important environment variables.

[**CVE-2023-36845**](https://nvd.nist.gov/vuln/detail/CVE-CVE-2023-36845) - CVSS v3 Base Score: ***9.8*** - Juniper Junos OS EX Series and SRX Series PHP External Variable Modification Vulnerability:

- A PHP External Variable Modification vulnerability in J-Web of Juniper Networks Junos OS on EX Series and SRX Series allows an unauthenticated, network-based attacker to control an important environment variable.

[**CVE-2023-36846**](https://nvd.nist.gov/vuln/detail/CVE-2023-36846) - CVSS v3 Base Score: ***5.3*** - Juniper Junos OS SRX Series Missing Authentication for Critical Function Vulnerability:

- A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on SRX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity.

[**CVE-2023-36847**](https://nvd.nist.gov/vuln/detail/CVE-2023-36847) - CVSS v3 Base Score: ***5.3*** - Juniper Junos OS EX Series Missing Authentication for Critical Function Vulnerability:

- A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on EX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity.

[**CVE-2023-36851**](https://nvd.nist.gov/vuln/detail/CVE-2023-36851) - CVSS v3 Base Score: ***5.3*** - Juniper Junos OS SRX Series Missing Authentication for Critical Function Vulnerability:

- A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on SRX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity.

## What is vulnerable?

The vulnerability affects Juniper Networks Junos OS on SRX Series and EX Series:

- All versions prior to 20.4R3-S9;
- 21.1 version 21.1R1 and later versions;
- 21.2 versions prior to 21.2R3-S7;
- 21.3 versions prior to 21.3R3-S5;
- 21.4 versions prior to 21.4R3-S5;
- 22.1 versions prior to 22.1R3-S4;
- 22.2 versions prior to 22.2R3-S2;
- 22.3 versions prior to 22.3R2-S2, 22.3R3-S1;
- 22.4 versions prior to 22.4R2-S1, 22.4R3;
- 23.2 versions prior to 23.2R1-S1, 23.2R2.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- The following software releases have been updated to prevent the code execution in CVE-2023-36845 vulnerability:

    - 20.4R3-S9, 21.2R3-S7\*, 21.3R3-S5, 21.4R3-S5\*, 22.1R3-S4, 22.2R3-S2, 22.3R2-S2, 22.3R3-S1, 22.4R2-S1, 22.4R3\*, 23.2R1-S1, 23.2R2\*, 23.4R1\*, and all subsequent releases.

- More updates are to be released to address the remaining vulnerabilities.

#### Recommended Workarounds:

- Disable J-Web, or limit access to only trusted hosts.

## Additional References

- [CISA Adds Six Known Exploited Vulnerabilities to Catalog | CISA](https://www.cisa.gov/news-events/alerts/2023/11/13/cisa-adds-six-known-exploited-vulnerabilities-catalog)
- [2023-08 Out-of-Cycle Security Bulletin: Junos OS: SRX Series and EX Series: Multiple vulnerabilities in J-Web can be combined to allow a preAuth Remote Code Execution (juniper.net)](https://supportportal.juniper.net/s/article/2023-08-Out-of-Cycle-Security-Bulletin-Junos-OS-SRX-Series-and-EX-Series-Multiple-vulnerabilities-in-J-Web-can-be-combined-to-allow-a-preAuth-Remote-Code-Execution?language=en_US)
- [Known Exploited Vulnerabilities Catalog | CISA](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=&sort_by=field_date_added)
