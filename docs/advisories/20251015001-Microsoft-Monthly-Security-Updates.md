# Microsoft Monthly Security Updates - 20251015001

## Overview

Microsoft has released its October 2025 Monthly Security Update, addressing a total of 172 vulnerabilities across its product suite, including six zero-day vulnerabilities. This update includes critical patches for remote code execution and elevation of privilege vulnerabilities affecting core Windows components, Microsoft Office, and Azure services.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Windows Server 2019      | Versions between 10.0.17763.0 and 10.0.17763.7919    | [CVE-2025-59287](https://nvd.nist.gov/vuln/detail/CVE-2025-59287)                                                                        | 9.8          | **Critical**                                   |
| ASP.NET Core 8.0      | Versions between 8.0 and 8.0.21    | [CVE-2025-55315](https://nvd.nist.gov/vuln/detail/CVE-2025-55315)                                                                        | 9.9          | **Critical**                                   |
| Windows 10 Version 1809      | Versions between 10.0.17763.0 and 10.0.17763.7919    | [CVE-2025-49708](https://nvd.nist.gov/vuln/detail/CVE-2025-49708)                                                                        | 9.9          | **Critical**                                   |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft: <https://msrc.microsoft.com/update-guide/releaseNote/2025-Oct>