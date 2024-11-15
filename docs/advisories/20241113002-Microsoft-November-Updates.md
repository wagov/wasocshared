# Microsoft Monthly Updates - 20241113002

## Overview

Microsoft has released security updates to address vulnerabilities in multiple products. A Cyber threat actor could leverage some of these vulnerabilities to exploit the affected system.

## What is vulnerable?

### Critical Vulnerabilities

| Product(s) Affected    | CVE                                                               | CVSS | Severity |
| ---------------------- | ----------------------------------------------------------------- | ---- | -------- |
| .NET and Visual Studio | [CVE-2024-43498](https://nvd.nist.gov/vuln/detail/cve-2024-43498) | 9.8  | High     |
| Azure CycleCloud       | [CVE-2024-43602](https://nvd.nist.gov/vuln/detail/CVE-2024-43602) | 9.9  | High     |
| Windows Kerberos       | [CVE-2024-43639](https://nvd.nist.gov/vuln/detail/CVE-2024-43639) | 9.8  | High     |

### Known Exploitation

| Product(s) Affected    | Version(s)                                                        | CVE | CVSS |
| ---------------------- | ----------------------------------------------------------------- | --- | ---- |
| Windows NTLM           | [CVE-2024-43451](https://nvd.nist.gov/vuln/detail/CVE-2024-43451) | 6.5 | High |
| Windows Task Scheduler | [CVE-2024-49039](https://nvd.nist.gov/vuln/detail/CVE-2024-49039) | 8.8 | High |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft November 2024 Security Updates: <https://msrc.microsoft.com/update-guide/releaseNote/2024-Nov>
