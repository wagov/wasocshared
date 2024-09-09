# Veeam Releases Critical Updates - 20240909001

## Overview

Veeam has released a security advisory detailing multiple vulnerabilities affecting Veeam ONE, a comprehensive monitoring solution for virtual and data protection environments. These vulnerabilities exposes systems to remote code execution (RCE), credential theft, and configuration tampering.

## What is vulnerable?

| Product(s) Affected        | Version(s)     | CVE #                                                                                                                                   | CVSS v4/v3    | Severity               |
| -------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------- |
| Veeam Backup & Replication | \< 12.2.0.334  | [CVE-2024-40711](https://nvd.nist.gov/vuln/detail/CVE-2024-40711)                                                                       | 9.8           | Critical               |
| Veeam ONE                  | \< 12.2.0.4093 | [CVE-2024-42024](https://nvd.nist.gov/vuln/detail/CVE-2024-42024) <br>[CVE-2024-42019](https://nvd.nist.gov/vuln/detail/CVE-2024-42019) | 9.1  <br> 9.0 | Critical <br> Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Veeam Security Advisory: <https://www.veeam.com/kb4649>

## Additional References

- SecurtyNewsOnline article: <https://securityonline.info/critical-flaws-in-veeam-one-expose-systems-to-rce-cve-2024-42024-and-credential-theft-cve-2024-42019>
