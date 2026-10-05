# 20261005002 - CPython Vulnerability

## Overview

The WASOC has been made aware a critical vulnerabilty affecting CPython, which is used in multiple Operating Systems and perimeter devices.

The vulnerability could allow for remote, unauthenticated TLS client can make a server crash or call through a freed pointer if its sni_callback assigns a different context to SSLSocket.context.

## What is vulnerable?

 Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity				|
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------------|
| CPython      | - 0 < 3.10.22 (python)<br>- 3.11.0 < 3.11.17 (python)<br>- 3.12.0 < 3.12.15 (python)<br>- 3.13.0 < 3.13.16 (python)<br>- 3.14.0 < 3.14.8 (python)<br>- 3.15.0a1 < 3.15.0rc3 (python)             |[CVE-2026-19445](https://nvd.nist.gov/vuln/detail/cve-2026-19445)                                                        | 9.2          | **Critical**         |


## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- GitHub Advisory DB: <https://github.com/advisories/GHSA-7jvw-f348-84gq>

## Additional References

- Vulnerability Disclosure: <https://github.com/abraxas/cve-2026-19445-sni-uaf>