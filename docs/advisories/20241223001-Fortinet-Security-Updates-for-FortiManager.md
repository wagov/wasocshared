# Fortinet Security Updates for FortiManager - 20241223001

## Overview

Fortinet has released security updates for FortiManager to address a vulnerability where a remote threat actor could exploit the vulnerability to take control of an affected system.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE| CVSS| Severity|
| ------------------- | :---------- | ---------------------------- | ------------ | ----------------------------- |
| FortiManager        | ***7.6.0*** <br> ***7.4.0 through 7.4.4*** <br> ***Cloud 7.4.1 through 7.4.4*** <br> ***7.2.3 through 7.2.7*** <br> ***Cloud 7.2.1 through 7.2.7*** <br> ***7.0.5 through 7.0.12*** <br> ***Cloud 7.0.1 through 7.0.12*** <br> ***6.4.10 through 6.4.14*** | [CVE-2024-48889](https://nvd.nist.gov/vuln/detail/CVE-2024-48889)| 7.2 | High|

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Fortinet: <https://www.fortiguard.com/psirt/FG-IR-24-425>

| **Product** | **Affected Versions** | **Solution** |
|---|---|---|
| FortiManager 7.6 | **_7.6.0_** | Upgrade to 7.6.1 or above |
| FortiManager 7.4 | **_7.4.0 through 7.4.4_** | Upgrade to 7.4.5 or above |
| FortiManager 7.4 | **_Cloud 7.4.1 through 7.4.4_** | Upgrade to 7.4.5 or above |
| FortiManager 7.2 | **_7.2.3 through 7.2.7_** | Upgrade to 7.2.8 or above |
| FortiManager 7.2 | **_Cloud 7.2.1 through 7.2.7_** | Upgrade to 7.2.8 or above |
| FortiManager 7.0 | **_7.0.5 through 7.0.12_** | Upgrade to 7.0.13 or above |
| FortiManager 7.0 | **_Cloud 7.0.1 through 7.0.12_** | Upgrade to 7.0.13 or above |
| FortiManager 6.4 | **_6.4.10 through 6.4.14_** | Upgrade to 6.4.15 or above |

## Additional References

- CISA Cybersecurity Advisories: <https://www.cisa.gov/news-events/alerts/2024/12/20/fortinet-releases-security-updates-fortimanager>
