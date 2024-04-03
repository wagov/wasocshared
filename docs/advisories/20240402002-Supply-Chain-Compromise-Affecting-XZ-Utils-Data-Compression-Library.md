# Supply Chain Compromise Affecting XZ Utils Data Compression Library - 20240402002

## Overview

Red Hat Linux has released security advisories to address malicious code discovered in the upstream tarballs of xz. This vulnerability is a result of a supply chain compromise impacting the XZ Utils. XZ Utils is data compression software and may be present in Linux distributions. The malicious code may allow unauthorized access to affected systems.

## What is vulnerable?

| CVE                                                             | Severity     | CVSS | Product(s) Affected                 |
| --------------------------------------------------------------- | ------------ | ---- | ----------------------------------- |
| [CVE-2024-3094](https://nvd.nist.gov/vuln/detail/CVE-2024-3094) | **Critical** | 10.0 | **xz**  All versions starting 5.6.0 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

## Additional References

- [NVD - CVE-2024-3094 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2024-3094 "https://nvd.nist.gov/vuln/detail/CVE-2024-3094") (Critical CVSS 10.0)
- [CVE-2024-3094 (tenable.com)](https://www.tenable.com/cve/CVE-2024-3094)
