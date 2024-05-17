# Git Patches Critical RCE Vulnerabilities - 20240517005

## Overview

The Git project has recently addressed a series of critical security vulnerabilities that could expose users to remote code execution and unauthorized data manipulation.

## What is vulnerable?

| CVE  | Severity     | CVSS | Product(s) Affected |
| ---- | ------------ | ---- | ------------------- |
| [CVE-2024-32002](https://nvd.nist.gov/vuln/detail/CVE-2024-32002) | **Critical** | 9.0  | **versions before** 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4 |
| [CVE-2024-32004](https://nvd.nist.gov/vuln/detail/CVE-2024-32004) | **High** | 8.1  | **versions before** 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [**Git Security**](https://github.com/git/git/security)

## Additional References

- [Git Patches Critical RCE Vulnerabilities](https://securityonline.info/git-patches-critical-rce-vulnerabilities-cve-2024-32002-cve-2024-32004/)
