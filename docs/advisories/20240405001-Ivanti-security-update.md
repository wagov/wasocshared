# Ivanti Releases Security Update for Ivanti Connect Secure and Policy Secure Gateways - 20240405001

## Overview

Ivanti has released security updates to address vulnerabilities in all supported versions (9.x and 22.x) of Ivanti Connect Secure and Policy Secure gateways. A cyber threat actor could exploit one of these vulnerabilities to take control of an affected system.

## What is vulnerable?

| CVE            | Severity   | CVSS | Product(s) Affected          | Summary                                                                                                                                                                               | Dated      |
| -------------- | ---------- | ---- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| CVE-2024-21894 | **High**   | 8.2  | ICS and Ivanti Policy Secure | An unauthenticated malicious user may send specially crafted requests to crash the service thereby causing a DoS. In certain conditions this may lead to execution of arbitrary code. | 04/04/2024 |
| CVE-2024-22052 | **High**   | 7.5  | ICS and Ivanti Policy Secure | Allows an unauthenticated malicious user to send specially crafted requests to crash the service thereby causing a DoS attack.                                                        | 04/04/2024 |
| CVE-2024-22053 | **High**   | 8.2  | ICS and Ivanti Policy Secure | Allows an unauthenticated malicious user to send specially crafted requests to crash the service thereby causing a DoS attack or in certain conditions read contents from memory.     | 04/04/2024 |
| CVE-2024-22023 | **Medium** | 5.3  | ICS and Ivanti Policy Secure | Allows an unauthenticated attacker to send specially crafted XML requests to temporarily cause resource exhaustion thereby resulting in a limited-time DoS.                           | 04/04/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://forums.ivanti.com/s/article/SA-CVE-2024-21894-Heap-Overflow-CVE-2024-22052-Null-Pointer-Dereference-CVE-2024-22053-Heap-Overflow-and-CVE-2024-22023-XML-entity-expansion-or-XXE-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US

## Additional References

- [NVD - CVE-2024-21894 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2024-21894)

- [NVD - CVE-2024-22052 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2024-22052)

- [NVD - CVE-2024-22053 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2024-22053)

- [NVD - CVE-2024-22023 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2024-22023)
