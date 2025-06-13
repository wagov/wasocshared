# Trend Micro Critical Vulnerabilties - 20250613001

## Overview

The WA SOC has been made aware of a critical vulnerability in Trend Micro products.

This vulnerability allows remote threat actor to escalate privileges on affected installations of Trend Micro Endpoint Encryption. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed.

## What is vulnerable?

| Product(s) Affected                                 | Version(s)       | CVE                                                                                                                                           | CVSS             | Severity                  |
| --------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------- |
| Trend Micro Endpoint Encryption (TMEE) PolicyServer | prior 6.0.0.4013 | <br> [CVE-2025-49212](https://nvd.nist.gov/vuln/detail/CVE-2025-49212) <br>[ CVE-2025-49213](https://nvd.nist.gov/vuln/detail/CVE-2025-49213) | <br> 9.8 <br>9.8 | <br>Critical <br>Critical |
| Apex Central                                        | 2019 (On-prem)   | [CVE-2025-49219](https://nvd.nist.gov/vuln/detail/CVE-2025-49219)                                                                             | 9.8              | Critical                  |
| Apex Central as a Service\*                         | SaaS             | [CVE-2025-49220](https://nvd.nist.gov/vuln/detail/CVE-2025-49220)                                                                             | 9.8              | Critical                  |
|                                                     |                  |                                                                                                                                               |                  |                           |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australia Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- [Trend Micro EndPoint: (trendmicro.com)](https://success.trendmicro.com/en-US/solution/KA-0019928)
- [Trend Micro Apex Central: (trendmicro.com)](https://success.trendmicro.com/en-US/solution/KA-0019926)

## Additional References

- bleepingcomputer: <https://www.bleepingcomputer.com/news/security/trend-micro-fixes-six-critical-flaws-on-apex-central-endpoint-encryption-policyserver/>
