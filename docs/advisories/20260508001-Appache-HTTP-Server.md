# Apache HTTP Server Vulnerability - 20260508001

## Overview

The WASOC has been made aware of a vulnerability for Apache HTTP Server with the HTTP/2 protocol that may lead to a Denial of Service attack, or under certain conditions, allow for remote code execution.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Apache HTTP Server      | 2.4.66    | [CVE-2026-23918](https://nvd.nist.gov/vuln/detail/CVE-2026-23918)                                                                        | 8.8          | High                    |


## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Apache: <https://httpd.apache.org/security/vulnerabilities_24.html>

## Additional References

- THN: <https://thehackernews.com/2026/05/critical-apache-http2-flaw-cve-2026.html>
