# Juniper Critical Vulnerability - 20250218001

## Overview

The WA SOC has been made aware of a critical authentication bypass flaw in Juniper Session Smart Routers.

The identified Authentication Bypass use an Alternate Path or Channel vulnerability in Juniper Networks Session Smart Router may allow a network-based attacker to bypass authentication and take administrative control of the device.

## What is vulnerable?

| Product(s) Affected                                                                | Version(s)                                                                                                                       | CVE                                                               | CVSS | Severity     |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| Session Smart Router <br> Session Smart Conductor <WAN Assurance Managed Routers > | from 5.6.7 before 5.6.17 <br> from 6.0.8<br>from 6.1 before 6.1.12-lts <br>from 6.2 before 6.2.8-lts<br>from 6.3 before 6.3.3-r2 | [CVE-2025-21589](https://nvd.nist.gov/vuln/detail/CVE-2025-21589) | 9.8  | **Critical** |
|                                                                                    |                                                                                                                                  |                                                                   |      |              |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 48 hours:

- Juniper Network: <https://supportportal.juniper.net/s/article/2025-02-Out-of-Cycle-Security-Bulletin-Session-Smart-Router-Session-Smart-Conductor-WAN-Assurance-Router-API-Authentication-Bypass-Vulnerability-CVE-2025-21589?language=en_US>

## Additional References

- AttackerKB: <https://www.tenable.com/cve/CVE-2025-21589>
