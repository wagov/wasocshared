## Cisco Critical Advisory - 20240125002

## Overview

Cisco has released software updates that addresses a vulnerability in multiple Cisco Unified Communications and Contact Center Solutions products could allow an unauthenticated, remote attacker to execute arbitrary code on an affected device.

## What is vulnerable?

| CVE ID                                                            | Product(s) Affected                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Summary                                                                         | Severity     | CVSS |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ | ---- |
| [CVE-2024-20253](https://nvd.nist.gov/vuln/detail/CVE-2024-20253) | - Packaged Contact Center Enterprise (PCCE) ([CSCwe18830](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64245)) **versions before** 12.0 - Unified Communications Manager (Unified CM) ([CSCwd64245](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64245)) **versions before** 11.5 - Unified Communications Manager IM & Presence Service (Unified CM IM&P) ([CSCwd64276](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64276)) **versions before** 11.5 - Unified Communications Manager Session Management Edition (Unified CM SME) ([CSCwd64245](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64245)) **versions before** 11.5 -  Unified Contact Center Enterprise (UCCE) ([CSCwe18830](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64245)) **versions before** 12.0 -  Unified Contact Center Express (UCCX) ([CSCwe18773](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64245)) **versions before** 12.0 - Unity Connection ([CSCwd64292](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64245)) **versions before** 11.5 - Virtualized Voice Browser (VVB) ([CSCwe18840](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd64245)) **versions before** 12.0 | Cisco Unified Communications Products Remote Code Execution (RCE) Vulnerability | **Critical** | 9.9  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Cisco Security](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-rce-bWNzQcUm#fs)

## Additional References

- [IT News](https://www.itnews.com.au/news/cisco-unified-comms-systems-patched-against-rce-604400)
