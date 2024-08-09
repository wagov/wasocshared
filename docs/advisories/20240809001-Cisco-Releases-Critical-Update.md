# Cisco Releases Critical Update - 20240809001

## Overview

A vulnerability in the authentication system of Cisco Smart Software Manager On-Prem (SSM On-Prem) could allow an unauthenticated, remote attacker to change the password of any user, including administrative users. This vulnerability is due to improper implementation of the password-change process. An attacker could exploit this vulnerability by sending crafted HTTP requests to an affected device. A successful exploit could allow an attacker to access the web UI or API with the privileges of the compromised user.

## What is vulnerable?

| Product(s) Affected                                                                            | Version(s)                  | CVE                                                               | CVSS | Severity     |
| ---------------------------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| Cisco SSM On-Prem and Cisco SSM Satellite (the same product with different naming conventions) | All versions below 8-202212 | [CVE-2024-20419](https://nvd.nist.gov/vuln/detail/CVE-2024-20419) | 10.0 | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [CISCO Advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cssm-auth-sLw3uhUy)

## Additional References

- SecurityOnline article: <https://securityonline.info/cisco-warns-of-public-poc-exploit-code-of-critical-cve-2024-20419-cvss-10-flaw/#google_vignette>

- Bleeping Computer article: <https://www.bleepingcomputer.com/news/security/exploit-released-for-cisco-ssm-bug-allowing-admin-password-changes/>
