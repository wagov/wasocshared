# Cisco Expressway Series Cross-Site Request Forgery Vulnerabilities - 20240208003

## Overview

Cisco has released a security advisory relating to multiple vulnerabilities for their Cisco Expressway product that could allow an unauthenticated, remote attacker to conduct cross-site request forgery (CSRF) attacks and perform arbitrary actions on an affected device.

## What is vulnerable?

| Product(s) Affected                                               | Summary | Severity                                                                                                                                                                       | CVSS |
| ----------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| **[CVE-2024-20252](https://cve.org/CVERecord?id=CVE-2024-20252)** |         | **[CRITICAL](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2024-20252&vector=AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H&version=3.1&source=Cisco%20Systems,%20Inc.)** | 9.6  |
| **[CVE-2024-20254](https://cve.org/CVERecord?id=CVE-2024-20254)** |         | **[CRITICAL](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2024-20254&vector=AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H&version=3.1&source=Cisco%20Systems,%20Inc.)** | 9.6  |
| **[CVE-2024-20255](https://cve.org/CVERecord?id=CVE-2024-20255)** |         | **[HIGH](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2024-20255&vector=AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:H/A:L&version=3.1&source=Cisco%20Systems,%20Inc.)**     | 8.2  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

## Additional References

- [Cisco Security Advisory(cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-expressway-csrf-KnnZDMj3)
