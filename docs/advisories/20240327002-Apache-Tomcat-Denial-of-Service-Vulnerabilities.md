# Apache Tomcat Denial of Service Vulnerabilities - 20240327002

## Overview

Denial of Service via incomplete cleanup vulnerability in Apache Tomcat. It was possible for WebSocket clients to keep WebSocket connections open leading to increased resource consumption.

## What is vulnerable?

| CVE                                                               | Severity     | CVSS | Product(s) Affected                                                                                                             | Summary | Dated |
| ----------------------------------------------------------------- | ------------ | ---- | ------------------------------------------------------------------------------------------------------------------------------- | ------- | ----- |
| [CVE-2024-23672](https://nvd.nist.gov/vuln/detail/CVE-2024-23672) | **Critical** | N/A  | **From 11.0.0-M1 through 11.0.0-M16, from 10.1.0-M1 through 10.1.18, from 9.0.0-M1 through 9.0.85, from 8.5.0 through 8.5.98**  |         |       |
| [CVE-2024-24549](https://nvd.nist.gov/vuln/detail/CVE-2024-24549) | **Critical** | N/A  | **From 11.0.0-M1 through 11.0.0-M16, from 10.1.0-M1 through 10.1.18, from 9.0.0-M1 through 9.0.85, from 8.5.0 through 8.5.98.** |         |       |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [CVE-2024-24549 Apache Tomcat - Denial of Service](https://lists.apache.org/thread/4c50rmomhbbsdgfjsgwlb51xdwfjdcvg)
- [CVE-2024-23672 Apache Tomcat - Denial of Service](https://lists.apache.org/thread/cmpswfx6tj4s7x0nxxosvfqs11lvdx2f)

## Additional References

- NIST -  [CVE-2024-23672 Detail
    ](https://nvd.nist.gov/vuln/detail/CVE-2024-23672)

- NIST -  [CVE-2024-24549 Detail
    ](https://nvd.nist.gov/vuln/detail/CVE-2024-24549)
