# Sophos Firewall Addresses Multiple Vulnerabilities - 20241223002

## Overview

Sophos has addressed three vulnerabilities, that could lead to SQL injection, privileged SSH access to devices, and remote code execution..

## What is vulnerable?

| Product(s) Affected | Version(s)                                           | CVE                                                                                                                                                                                                             | CVSS                  | Severity                                     |
| ------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------------- |
| Sophos Firewall     | Sophos Firewall v21.0 GA (21.0.0) and older versions | [CVE-2024-12727](https://www.cve.org/CVERecord?id=CVE-2024-12727) <br> [CVE-2024-12728](https://www.cve.org/CVERecord?id=CVE-2024-12728) <br> [CVE-2024-12729](https://www.cve.org/CVERecord?id=CVE-2024-12729) | 9.8 <br> 9.8 <br> 8.8 | **Critical** <br> **Critical** <br> **High** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Sophos: <https://www.sophos.com/en-us/security-advisories/sophos-sa-20241219-sfos-rce>

## 3rd Party Article(s):

- Security Affairs: <https://securityaffairs.com/172179/security/sophos-firewall-critical-vulnerabilities.html>
