# Ivanti Critical Patch for Multiple Products - 20240209001

## Overview

Ivanti has published an urgent patch for a new authentication bypass vulnerability impacting Connect Secure, Policy Secure, and ZTA gateways. Ivanti is urging admins to secure their appliances immediately.

The 'low complexity' attack allows an attacker to access restricted resources without authentication.

## What is vulnerable?

| Product(s) Affected | Summary | Severity     | CVSS |
| ------------------- | ------- | ------------ | ---- |
| **Ivanti Connect Secure** `9.1R14.4, 9.1R17.2, 9.1R18.3, 22.4R2.2 and 22.5R1.1`, **Ivanti Policy Secure** `22.5R1.1` and **ZTA** `22.6R1.3` | **CVE-2024-22024** An XML external entity or XXE vulnerability in the SAML component of Ivanti Connect Secure (9.x, 22.x), Ivanti Policy Secure (9.x, 22.x) and ZTA gateways which allows an attacker to access certain restricted resources without authentication.        | **Critical** | 8.3  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing. As of writing, Ivanti states 'We have no evidence of any customers being exploited by CVE-2024-22024'.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of **48 hours** (refer [Patch Management](../guidelines/patch-management.md)):

- [Ivanti - CVE-2024-22024 (XXE) for Ivanti Connect Secure and Ivanti Policy Secure
](https://forums.ivanti.com/s/article/CVE-2024-22024-XXE-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure?language=en_US)

## Additional References

- [BleepingComputer - Ivanti: Patch new Connect Secure auth bypass bug immediately](https://www.bleepingcomputer.com/news/security/ivanti-patch-new-connect-secure-auth-bypass-bug-immediately/)
