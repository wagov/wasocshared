# Administrative FortiCloud SSO Authentication Bypass Vulnerability - 20260129001

## Overview

An authentication bypass vulnerability in FortiOS, FortiManager, FortiAnalyzer, FortiProxy, FortiWeb may allow an attacker with a FortiCloud account and a registered device to log into other devices registered to other accounts, if FortiCloud SSO authentication is enabled on those devices.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| FortiAnalyzer | [Vendor listed affected versions](https://fortiguard.fortinet.com/psirt/FG-IR-26-060)    | [CVE-2026-24858](https://nvd.nist.gov/vuln/detail/CVE-2026-24858)  | 9.8         | **Critical**                                   |
| FortiManager      | [Vendor listed affected versions](https://fortiguard.fortinet.com/psirt/FG-IR-26-060)    | [CVE-2026-24858](https://nvd.nist.gov/vuln/detail/CVE-2026-24858) | 8.8 | **Critical** |
| FortiOS      | [Vendor listed affected versions](https://fortiguard.fortinet.com/psirt/FG-IR-26-060)    | [CVE-2026-24858](https://nvd.nist.gov/vuln/detail/CVE-2026-24858) | 9.8 | **Critical** |
| FortiProxy      | [Vendor listed affected versions](https://fortiguard.fortinet.com/psirt/FG-IR-26-060)    | [CVE-2026-24858](https://nvd.nist.gov/vuln/detail/CVE-2026-24858) | 9.8 | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- FortiGuard Labs: <https://fortiguard.fortinet.com/psirt/FG-IR-26-060>

## Additional References

- CISA Known Exploited Vulnerabilities Catalog: <https://www.cisa.gov/news-events/alerts/2026/01/27/cisa-adds-one-known-exploited-vulnerability-catalog>
