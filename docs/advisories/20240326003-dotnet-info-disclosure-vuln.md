# .NET Framework Information Disclosure Vulnerability - 20240326003

## Overview

The WA SOC has been made aware of a high severity vulnerability in the .NET framework.

An attacker who successfully exploits this vulnerability could obtain the ObjRef URI which could lead to Remote Code Execution. There are no recommended workarounds, Microsoft recommends patching to address the vulnerability.

## What is vulnerable?

| CVE    | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ------ | ------------ | ---- | ------------------- | ------- | ----- |
| [CVE-2024-29059](https://nvd.nist.gov/vuln/detail/CVE-2024-29059) | **High** | 7.5  | Please review the affected versions [here](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29059) | .NET Framework Information Disclosure Vulnerability        | 22/03/2024      |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* or *48 hours* for internet facing services (refer [Patch Management](../guidelines/patch-management.md)):

- [MSRC - .NET Framework Information Disclosure Vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29059)