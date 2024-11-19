# Paloalto Publishes Critical Advisory - 20241119001

## Overview

The WA SOC has been made aware of a privilege escalation vulnerability in Palo Alto Networks' PAN-OS software. This vulnerability allows a PAN-OS administrator with access to the management web interface to perform actions on the firewall with root privileges.

## What is vulnerable?

| Product(s) Affected            | Version(s)                                                                                                                    | CVE                                                               | CVSS | Severity     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| Palo Alto Networks PAN-OS | \< 11.2.4-h1 <br> \< 11.1.5-h1 <br> \< 11.0.6-h1 <br> \< 10.2.12-h2 <br>  |[CVE-2024-0012](https://nvd.nist.gov/vuln/detail/CVE-2024-0012) | 9.3  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Paloalto: <https://security.paloaltonetworks.com/CVE-2024-0012>
