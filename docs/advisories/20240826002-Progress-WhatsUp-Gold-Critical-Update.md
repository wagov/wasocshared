# Progress WhatsUp Gold Critical Update - 20240826002

## Overview

The Progress WhatsUp Gold team has recently disclosed multiple critical vulnerabilities affecting all versions of the software released before 2024.0.0. These vulnerabilities, identified as CVE-2024-6670, CVE-2024-6671, and CVE-2024-6672, pose significant risks to organizations using outdated versions of the network monitoring tool.

## What is vulnerable?

| Product(s) Affected | Version(s)          | CVE                                                 | CVSS                  | Severity                                     |
| ------------------- | ------------------- | --------------------------------------------------- | --------------------- | -------------------------------------------- |
| Progress WhatsUp    | **Gold < 2024.0.0** | CVE-2024-6670 <br> CVE-2024-6671 <br> CVE-2024-6672 | 9.8 <br> 9.8 <br> 8.8 | **Critical** <br> **Critical** <br> **High** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

Since publication, there has been evidence of exploitation in the wild.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Progress Community article: <https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2024>

## Additional References

- Cybersecurity News article: <https://securityonline.info/critical-vulnerabilities-uncovered-in-progress-whatsup-gold-cve-2024-6670-cve-2024-6671/>
- Protecting Against RCE Attacks Abusing WhatsUp Gold Vulnerabilities: https://www.trendmicro.com/en_us/research/24/i/whatsup-gold-rce.html

### Change log

- 2024-08-26: Advisory created.
- 2024-09-13: Update of “What has been observed” with evidence of exploitation and secondary additional reference link.
