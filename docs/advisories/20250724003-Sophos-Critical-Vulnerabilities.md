# Sophos Critical Vulnerabilities - 20250724003

## Overview

Sophos has issued a security advisory addressing multiple vulnerabilities in the products. Successful exploitation could potentially lead to remote code execution.

## What is vulnerable?

| Product(s) Affected    | Version(s)                  | CVE                                                             | CVSS | Severity     |
| ---------------------- | --------------------------- | --------------------------------------------------------------- | ---- | ------------ |
| Sophos Firewall | all versions prior to v21.0 MR2 (21.0.2) | [CVE-2025-6704](https://nvd.nist.gov/vuln/detail/CVE-2025-6704) <br> [CVE-2025-7624](https://nvd.nist.gov/vuln/detail/CVE-2025-7624) | 9.8 <br> 9.8 | **Critical** <br> **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Sophos: <https://www.sophos.com/en-us/security-advisories/sophos-sa-20250721-sfos-rce>

## Additional References

- Securityaffairs: <https://securityaffairs.com/180283/security/sophos-addressed-five-sophos-firewall-vulnerabilities.html>
