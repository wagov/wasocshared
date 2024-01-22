# Trend Micro Deep Security Local Privilege Escalation Vulnerabilities - 20240122001

## Overview

Trend Micro has released a new agent update for Trend Micro Deep Security and Trend Micro Cloud One - Endpoint and Workload Security that resolves two local privilege escalation vulnerabilities.

## What is vulnerable?

| CVE ID                                                            | Product(s) Affected                                                                                                    | Summary                                                                                                                                                                                                                                                        | Severity | CVSS |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---- |
| [CVE-2023-52338](https://nvd.nist.gov/vuln/detail/CVE-2023-52338) | Deep Security Agent (Including Cloud One - Endpoint and Workload Security), **versions before** 20.0, Windows Platform | This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Deep Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. | **High** | 7.8  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Trend Micro solutions](https://success.trendmicro.com/dcx/s/solution/000296337?language=en_US)

## Additional References

- [Zeroday Initiative Advisories](https://www.zerodayinitiative.com/advisories/published/)
