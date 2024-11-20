# WordPress's Bricks Builder RCE Flaw - 20240220001

## Overview

A critical remote code execution (RCE) vulnerability [CVE-2024-25600](https://www.cve.org/CVERecord?id=CVE-2024-25600) has been discovered in the widely used WordPress site builder, Bricks Builder. This vulnerability is actively being exploited, rendering affected websites at significant risk.

This vulnerability allows any unauthenticated user to execute arbitrary PHP code on the WordPress site.

## What is vulnerable?

| Product(s) Affected                                                        |     | Severity     | CVSS                                                                                           |
| -------------------------------------------------------------------------- | --- | ------------ | ---------------------------------------------------------------------------------------------- |
| [Bricks Builder](https://wpscan.com/theme/bricks/) versions before 1.9.6.1 |     | **Critical** | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/) |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

## Additional References

- [Bricks < 1.9.6.1 - Unauthenticated Remote Code Execution](https://wpscan.com/vulnerability/8bab5266-7154-4b65-b5bc-07a91b28be42/)
- [patchstack](https://patchstack.com/articles/critical-rce-patched-in-bricks-builder-theme/)
- [snicco.io](https://snicco.io/vulnerability-disclosure/bricks/unauthenticated-rce-in-bricks-1-9-6)
- [BleeingComouter](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-rce-flaw-in-bricks-wordpress-site-builder/)
