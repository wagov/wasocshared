# Ricoh Critical Updates - 20241105001

## Overview

A critical vulnerability has been discovered in Ricoh's Web Image Monitor, impacting a wide range of their printer and MFP products. If this vulnerability is exploited, receiving a specially crafted request created and sent by an attacker may lead to arbitrary code execution and/or a denial-of-service (DoS) condition.

## What is vulnerable?

| Product(s) Affected                                                                                               | CVE                                                               | CVSS | Severity     |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| [List of Products and versions](https://www.ricoh.com/products/security/vulnerabilities/vul?id=ricoh-2024-000011) | [CVE-2024-47939](https://nvd.nist.gov/vuln/detail/CVE-2024-47939) | 9.8  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- Ricoh: <https://www.ricoh.com/products/security/vulnerabilities/vul?id=ricoh-2024-000011>

## Additional References

- SecurityOnline article: <https://securityonline.info/ricoh-printers-and-mfps-vulnerable-to-remote-code-execution-cve-2024-47939-cvss-9-8/>
