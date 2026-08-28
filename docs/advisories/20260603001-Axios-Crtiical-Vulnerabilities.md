# Axios Critical Vulnerabilities - 20260603001

## Overview

Axios has issued an advisory regarding critical vulnerabilities in Axios, the promise-based HTTP client for browsers and Node.js. Both vulnerabilities allow remote attackers to compromise applications without requiring authentication or user interaction.

## What is vulnerable?

| Product(s) Affected | Version(s)                                        | CVE #                                                                                                                                    | CVSS          | Severity               |
| ------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------- |
| axios               | 0.x prior to 0.31.1, and <br> 1.x prior to 1.15.2 | [CVE-2026-42043](https://nvd.nist.gov/vuln/detail/CVE-2026-42043) <br> [CVE-2026-42044](https://nvd.nist.gov/vuln/detail/CVE-2026-42044) | 10.0 <br> 9.1 | Critical <br> Critical |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- axios: <https://github.com/axios/axios/security/advisories/GHSA-pmwg-cvhr-8vh7>
- axios: <https://github.com/axios/axios/security/advisories/GHSA-3w6x-2g7m-8v23>
