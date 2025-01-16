# Microsoft Monthly Updates - 20250115004

## Overview

Microsoft has released security updates to address 159 vulnerabilities in multiple products. A Cyber threat actor could leverage some of these vulnerabilities to exploit the affected system.

## What is vulnerable?

### Critical Severity

| Product(s) Affected                          | CVE                                                               | CVSS | Severity |
| -------------------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| Windows NTLM                                 | [CVE-2025-21311](https://nvd.nist.gov/vuln/detail/CVE-2025-21311) | 9.8  | Critical |
| Windows OLE                                  | [CVE-2025-21298](https://nvd.nist.gov/vuln/detail/CVE-2025-21298) | 9.8  | Critical |
| Reliable Multicast Transport Driver (RMCAST) | [CVE-2025-21307](https://nvd.nist.gov/vuln/detail/CVE-2025-21307) | 9.8  | Critical |

### Known Exploited

| Product(s) Affected                          | CVE                                                               | CVSS | Severity |
| -------------------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| Windows Hyper-V | [CVE-2025-21333](https://nvd.nist.gov/vuln/detail/CVE-2025-21333) | 7.8 | High |
| Windows Hyper-V | [CVE-2025-21334](https://nvd.nist.gov/vuln/detail/CVE-2025-21334) | 7.8 | High |
| Windows Hyper-V | [CVE-2025-21335](https://nvd.nist.gov/vuln/detail/CVE-2025-21335) | 7.8 | High |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft January 2025 Security Updates: <https://msrc.microsoft.com/update-guide/releaseNote/2025-Jan>

### Change Log
- 2025-01-15: Initial Publication
- 2025-01-16: Added "Known Exploited" CVEs
