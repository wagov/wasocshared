# Arcserve UDP Software Critical Vulnerabilities - 20240318001

## Overview

An authentication bypass vulnerability, path traversal vulnerability, and denial of service vulnerability has been reported in Arcserve Unified Data Protection 9.2 and 8.1 alongside proof-of-concepts.

## What is vulnerable?

| CVE | Severity | CVSS | Product(s) Affected | Dated |
| --- | -------- | ---- | ------------------- | ----- |
|  [CVE-2024-0799](https://nvd.nist.gov/vuln/detail/CVE-2024-0799)  |      **Critical**    |    9.8  | **versions 9.2 and 8.1** | 13/03/2024  |
|  [CVE-2024-0800](https://nvd.nist.gov/vuln/detail/CVE-2024-0800)  |     **High**     |   8.8   | **versions 9.2 and 8.1** | 13/03/2024    |
|  [CVE-2024-0801](https://nvd.nist.gov/vuln/detail/CVE-2024-0801)  |    **High**      |   7.5   | **versions 9.2 and 8.1** | 13/03/2024   |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Arcserve UDP 9.2 | Console Vulnerabilities: CVE-2024-0801, CVE-2024-0800, CVE-2024-0799](https://support.arcserve.com/s/article/P00003050?language=en_US)
- [Arcserve UDP 8.1 | Console & Agent Vulnerabilities: CVE-2024-0801, CVE-2024-0800, CVE-2024-0799](https://support.arcserve.com/s/article/P00003059?language=en_US)


## Additional References

- [Arcserve Unified Data Protection 9.2 Multiple Vulnerabilities PoC](https://www.tenable.com/security/research/tra-2024-07)
