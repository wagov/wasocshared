# Trend Releases Critical Update - 20241021001

## Overview

Trend Micro has released updates to address a critical command injection vulnerability in the Cloud Edge appliance. This vulnerability could allow a threat actor to execute Remote Code on affected devices without authentication.

## What is vulnerable?

| Product(s) Affected | Version(s)                                      | CVE #                                                             | CVSS v4/v3 | Severity |
| ------------------- | ----------------------------------------------- | ----------------------------------------------------------------- | ---------- | -------- |
| Cloud Edge          | - 5.6SP2 < build 3228 <br> - 7.0 < build 1081 | [CVE-2024-48904](https://nvd.nist.gov/vuln/detail/CVE-2024-48904) | 9.8        | Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Trend Micro: <https://success.trendmicro.com/en-US/solution/KA-0017998>

## Additional References

- Cybersecurity News: <https://securityonline.info/cve-2024-48904-cvss-9-8-critical-command-injection-vulnerability-in-trend-micro-cloud-edge/>
