# Cisco Critical Vulnerabilities - 20250207001

## Overview

Multiple vulnerabilities in Cisco Identity Services Engine (ISE) could allow an authenticated, remote attacker to execute arbitrary commands and elevate privileges on an affected device.

## What is vulnerable?

| Product(s) Affected                                                                      | Version(s)                                                                                | CVE                                                                                                                                      | CVSS         | Severity                       |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------ |
| Cisco Identity Services Engine (ISE) <br> Cisco ISE Passive Identity Connector (ISE-PIC) | 3.0 all versions <br> 3.1 prior to 3.1P10 <br> 3.2 prior to 3.2P7 <br> 3.3 prior to 3.3P4 | [CVE-2025-20124](https://nvd.nist.gov/vuln/detail/CVE-2025-20124) <br> [CVE-2025-20125](https://nvd.nist.gov/vuln/detail/CVE-2025-20125) | 9.9 <br> 9.1 | **Critical** <br> **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Cisco: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multivuls-FTW9AOXF>
