# Juniper Announce RCE Chain Vulnerability Variation - 20231009002

## Overview

Juniper published an update to an existing advisory regarding a variation of the exploit for the code execution vulnerability (CVE-2023-36845).

## What is the vulnerability?

- [**CVE-2023-36844**](https://nvd.nist.gov/vuln/detail/CVE-2023-36844) - CVSS v3 Base Score: ***5.3***: A PHP External Variable Modification vulnerability in J-Web of Juniper Networks Junos OS on EX Series allows an unauthenticated, network-based attacker to control certain, important environment variables. Using a crafted request an attacker is able to modify certain PHP environment variables leading to partial loss of integrity, which may allow chaining to other vulnerabilities.
- [**CVE-2023-36845**](https://nvd.nist.gov/vuln/detail/CVE-2023-36845) - CVSS v3 Base Score: ***9.8***: A PHP External Variable Modification vulnerability in J-Web of Juniper Networks Junos OS on EX Series and SRX Series allows an unauthenticated, network-based attacker to remotely execute code. Using a crafted request which sets the variable PHPRC an attacker is able to modify the PHP execution environment allowing the injection und execution of code.
- [**CVE-2023-36846**](https://nvd.nist.gov/vuln/detail/CVE-2023-36846) - CVSS v3 Base Score: ***5.3***: A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on SRX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity. With a specific request to user.php that doesn't require authentication an attacker is able to upload arbitrary files via J-Web, leading to a loss of integrity for a certain  part of the file system, which may allow chaining to other vulnerabilities.
- [**CVE-2023-36847**](https://nvd.nist.gov/vuln/detail/CVE-2023-36847) - CVSS v3 Base Score: ***5.3***: A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on EX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity. With a specific request to installAppPackage.php that doesn't require authentication an attacker is able to upload arbitrary files via J-Web, leading to a loss of integrity for a certain part of the file system, which may allow chaining to other vulnerabilities.
- [**CVE-2023-36851**](https://nvd.nist.gov/vuln/detail/CVE-2023-36851) - CVSS v3 Base Score: ***5.3***: A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on SRX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity. With a specific request to webauth_operation.php that doesn't require authentication, an attacker is able to upload arbitrary files via J-Web, leading to a loss of integrity for a certain part of the file system, which may allow chaining to other vulnerabilities.

## What is vulnerable?

The vulnerability affects the following products:

- Juniper Networks Junos OS on EX Series and SRX Series: 
  - All versions prior to 20.4R3-S9
  - 21.1 versions 21.1R1 and later
  - 22.1 versions prior to 22.1R3-S4 
  - 21.2 versions prior to 21.2R3-S7
  - 21.3 versions prior to 21.3R3-S5
  - 21.4 versions prior to 21.4R3-S5
  - 22.1 versions prior to 22.1R3-S4
  - 22.2 versions prior to 22.2R3-S2 
  - 22.3 versions prior to 22.3R2-S2, 22.3R3-S1
  - 22.4 versions prior to 22.4R2-S1, 22.4R3
  - 23.2 versions prior to 23.2R1-S1, 23.2R2

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://supportportal.juniper.net/s/article/2023-08-Out-of-Cycle-Security-Bulletin-Junos-OS-SRX-Series-and-EX-Series-Multiple-vulnerabilities-in-J-Web-can-be-combined-to-allow-a-preAuth-Remote-Code-Execution?language=en_US&ref=labs.watchtowr.com>