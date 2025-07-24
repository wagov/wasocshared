# Cisco Critical Security Vulnerabilities - 20250718001

## Overview

Multiple vulnerabilities in Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) could allow an unauthenticated, remote attacker to issue commands on the underlying operating system as the root user.

## What is vulnerable?

| Product(s) Affected               | Version(s)                                     | CVE                                                                                                                                                                                                             | CVSS               | Severity                                         |
| --------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------ |
| Cisco ISE, and <br> Cisco ISE-PIC | 3.3 prior to Patch 7 <br> 3.4 prior to Patch 2 | [CVE-2025-20337](https://nvd.nist.gov/vuln/detail/CVE-2025-20337) <br> [CVE-2025-20281](https://nvd.nist.gov/vuln/detail/CVE-2025-20281) <br> [CVE-2025-20282](https://nvd.nist.gov/vuln/detail/CVE-2025-20282) | 10 <br> 10 <br> 10 | **Critical** <br> **Critical** <br> **Critical** |

## What has been observed?

Cisco have updated their advisory since initial publication to indicate active exploitation attempts in the wild.
The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Cisco: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-unauth-rce-ZAd2GnJ6>

## Additional References

- Security Week: <https://www.securityweek.com/cisco-patches-another-critical-ise-vulnerability/>

### Change Log

- 2025-07-18: Initial publication.
- 2025-07-24: Updated to indicate active exploitation attempts in the wild.
