# Grafana Releases Critical Update - 20241021002

## Overview

The WA SOC has been made aware of a critical vulnerability in Grafana's SQL Expressions experimental feature where insufficient query sanitisation could lead to command injection and local file inclusion from any user with VIEWER or higher permissions.

The 'duckdb' binary must be present in Grafana's $PATH for this attack to function; by default, this binary is not installed in Grafana distributions.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                                                                                   | CVE                                                             | CVSS | Severity     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ---- | ------------ |
| Grafana             | \< 11.0.5+security-01 <br> \< 11.1.6+security-01 <br> \< 11.2.1+security-01 <br> \< 11.0.6+security-01 <br> \< 11.1.7+security-01 <br> \< 11.2.2+security-01 | [CVE-2024-9264](https://nvd.nist.gov/vuln/detail/CVE-2024-9264) | 9.9  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- Grafana: <https://grafana.com/blog/2024/10/17/grafana-security-release-critical-severity-fix-for-cve-2024-9264/>
