# Delinea Secret Server Authentication Bypass Vulnerability - 20240429003

## Overview

The WA SOC has been made aware of an authentication bypass vulnerability in Delinea Secret Server.

Delinea Secret Server versions before 11.7.000001 are vulnerable to a serious authentication bypass attack that may allow attackers to gain Admin access and to retrieve stored secrets, due to a hardcoded key used in the authentication process. Delinea is urging all on premises customers running the vulnerable versions to upgrade.

## What is vulnerable?

| CVE    | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ------ | ------------ | ---- | ------------------- | ------- | ----- |
| [CVE-2024-33891](https://nvd.nist.gov/vuln/detail/CVE-2024-33891) | **High** | 8.8  | Delinea Secret Server **versions before** 11.7.000001| Authentication bypass vulnerabilty due to a hardcoded key.       | 28/04/2024      |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 2 weeks (refer [Patch Management](../guidelines/patch-management.md)):

- [Delinea - Trust Center Updates](https://trust.delinea.com/?tcuUid=17aaf4ef-ada9-46d5-bf97-abd3b07daae3)

## Additional References

- [“All Your Secrets Are Belong To Us” — A Delinea Secret Server AuthN/AuthZ Bypass](https://straightblast.medium.com/all-your-secrets-are-belong-to-us-a-delinea-secret-server-authn-authz-bypass-adc26c800ad3)
