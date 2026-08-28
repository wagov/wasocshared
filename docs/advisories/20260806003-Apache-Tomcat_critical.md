# Apache Tomcat Critical Vulnerability - 20260806003

## Overview

The WASOC has been made aware of a vulnerability in Apache Tomcat where encryption handling allows the EncryptInterceptor to be bypassed, potentially exposing sensitive data that should have been protected. CISA has added the vulnerability to the Known Exploited Vulnerabilities Catalog and the Apache organisation is encouraging affected organisations to apply the relevant security patches.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Apache Tomcat      | versions prior to 11.0.21, 10.1.54 or 9.0.117  | [CVE-2026-34486](https://nvd.nist.gov/vuln/detail/CVE-2026-34486)                                                                        | 9.8          | **Critical**                                   |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Apache: <https://lists.apache.org/thread/9510k5p5zdvt9pkkgtyp85mvwxo2qrly>

## Additional References

- GitHub Advisory Database: <https://github.com/advisories/GHSA-69r9-qgr7-g2wj>
