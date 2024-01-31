# Cisco Critical Advisory - 20240125002

## Overview

Cisco has released software updates that addresses a vulnerability in multiple Cisco Unified Communications and Contact Center Solutions products could allow an unauthenticated, remote attacker to execute arbitrary code on an affected device.

## What is the vulnerability?

| CVE                                                               | Severity     | CVSS |
| ----------------------------------------------------------------- | ------------ | ---- |
| [CVE-2024-20253](https://nvd.nist.gov/vuln/detail/CVE-2024-20253) | **Critical** | 9.9  |

## What is vulnerable?

| Product(s) Affected                                                        |                          |
| -------------------------------------------------------------------------- | ------------------------ |
| Packaged Contact Center Enterprise (PCCE)                                  | **versions before** 12.0 |
| Unified Communications Manager (Unified CM)                                | **versions before** 11.5 |
| Unified Communications Manager IM & Presence Service (Unified CM IM&P)     | **versions before** 11.5 |
| Unified Communications Manager Session Management Edition (Unified CM SME) | **versions before** 11.5 |
| Unified Contact Center Enterprise (UCCE)                                   | **versions before** 12.0 |
| Unified Contact Center Express (UCCX)                                      | **versions before** 12.0 |
| Unity Connection                                                           | **versions before** 11.5 |
| Virtualized Voice Browser(VVB)                                             | **versions before** 12.0 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Cisco Security](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-rce-bWNzQcUm#fs)

## Additional References

- [IT News](https://www.itnews.com.au/news/cisco-unified-comms-systems-patched-against-rce-604400)
