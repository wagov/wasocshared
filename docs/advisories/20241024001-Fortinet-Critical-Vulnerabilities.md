# Fortinet FortiManager Critical Vulnerability - 20241024001

## Overview

The WA SOC has been made aware of a critical vulnerability in Fortinet FortiManager devices that is currently being actively exploited. A missing authentication for critical function vulnerability in FortiManager fgfmd daemon may allow a remote unauthenticated attacker to execute arbitrary code or commands via specially crafted requests.

**Reports have shown this vulnerability has been seen to be exploited in the wild**

## What is vulnerable?

| Product(s) Affected | Affected Version(s)                                                                                 | CVE                                                               | CVSS | Severity |
| ------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| FortiManager        | 7.6 - 7.6.0 <br> 7.4 - 7.4.4 <br> 7.2 - 7.2.7 <br> 7.0 - 7.0.12 <br> 6.4 - 6.4.14 <br> 6.2 - 6.2.12 | [CVE-2024-47575](https://nvd.nist.gov/vuln/detail/CVE-2024-47575) | 9.8  | Critical |
| Fortimanager Cloud  | 7.4.1 - 7.4.4 <br> 7.2.1 - 7.2.7 <br> 7.0.1 - 7.0.12 <br> all versions 6.4.x                        | [CVE-2024-47575](https://nvd.nist.gov/vuln/detail/CVE-2024-47575) | 9.8  | Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

Fortinet has updated their security advisory addressing this vulnerability to include additional workarounds and indicators of compromise (IOCs).

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Fortinet: <https://www.fortiguard.com/psirt/FG-IR-24-423>

## Other Information

- ACSC: <https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/vulnerability-in-fortinets-fortimanager>

### Change Log

- 2024-10-24: Advisory initial creation.
- 2024-10-31: Update "What has been observed" with new information from vendor. Update "What is vulnerable" version information.
