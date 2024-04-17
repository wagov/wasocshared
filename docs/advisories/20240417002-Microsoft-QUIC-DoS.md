# Microsoft QUIC Denial of Service Vulnerability - 20240417002

## Overview

Microsoft has previously released information regarding QUIC Denial of Service vulnerabilities. However, it has recently updated this to include further vulnerabe software versions. The product does not properly control the allocation and maintenance of a limited resource, thereby enabling an actor to influence the amount of resources consumed, eventually leading to the exhaustion of available resources.

## What is vulnerable?

| CVE                                                               | Severity | CVSS | Product(s) Affected               | Dated                       |
| ----------------------------------------------------------------- | -------- | ---- | --------------------------------- | --------------------------- |
| [CVE-2024-26190](https://nvd.nist.gov/vuln/detail/CVE-2024-26190) | **High** | 7.5  | See vendor link in Recommendation | 12/03/24 (Updated 16/04/24) |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-26190

## Additional References

- https://www.cve.org/CVERecord?id=CVE-2024-26190
