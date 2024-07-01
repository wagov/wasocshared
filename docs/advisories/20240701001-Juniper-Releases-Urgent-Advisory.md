# Juniper Releases Urgent Advisory - 20240701001

## Overview

Juniper Networks has released an emergency update to address a maximum severity vulnerability that leads to authentication bypass in Session Smart Router (SSR), Session Smart Conductor, and WAN Assurance Router products. Exploitation of this vulnerability could allow an attacker to take full control of the device.

## What is vulnerable?

| Products Affected           | Versions                                                                                          | CVE                                                             | CVSS | Severity     |
| --------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---- | ------------ |
| **Session Smart Router**    | - ***All versions before*** 5.6.15<br/>- from 6.0 before 6.1.9-lts<br>- from 6.2 before 6.2.5-sts | [CVE-2024-2973](https://nvd.nist.gov/vuln/detail/CVE-2024-2973) | 10.0 | **Critical** |
| **Session Smart Conductor** | - ***All versions before*** 5.6.15<br/>- from 6.0 before 6.1.9-lts<br>- from 6.2 before 6.2.5-sts | [CVE-2024-2973](https://nvd.nist.gov/vuln/detail/CVE-2024-2973) | 10.0 | **Critical** |
| **WAN Assurance Router**    | - ***6.0 versions before*** 6.1.9-lts<br/>- 6.2 versions before 6.2.5-sts                         | [CVE-2024-2973](https://nvd.nist.gov/vuln/detail/CVE-2024-2973) | 10.0 | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- Session Smart Router: SSR-5.6.15, SSR-6.1.9-lts, SSR-6.2.5-sts, and subsequent releases.

- WAN Assurance Routers are patched automatically when connected to the Mist Cloud, but administrators of High-Availability clusters need to upgrade to SSR-6.1.9 or SSR-6.2.5.

- Juniper also notes that upgrading Conductor nodes is enough to apply the fix automatically to connected routers, but routers should still be upgraded to the latest available version.

## Additional References

- [Session Smart Router(SSR): On redundant router deployments API authentication can be bypassed (CVE-2024-2973) (juniper.net)](https://supportportal.juniper.net/s/article/2024-06-Out-Of-Cycle-Security-Bulletin-Session-Smart-Router-SSR-On-redundant-router-deployments-API-authentication-can-be-bypassed-CVE-2024-2973?language=en_US)
- [Juniper releases out-of-cycle fix for max severity auth bypass flaw (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/juniper-releases-out-of-cycle-fix-for-max-severity-auth-bypass-flaw/)
