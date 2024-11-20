# Paloalto Publishes Critical Advisory - 20241119001

## Overview

Palo Alto Networks has released a critical advisory relating to a a vulnerability affecting their PAN-OS software. This vulnerability enables an unauthenticated attacker with network access to the management web interface to gain PAN-OS administrator privileges to perform administrative actions, tamper with the configuration, or exploit other authenticated privilege escalation vulnerabilities.

The risk is highest when you allow access to the management interface from external IP addresses on the internet.

## What is vulnerable?

| Product(s) Affected       | Version(s)                                                                               | CVE                                                             | CVSS | Severity     |
| ------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---- | ------------ |
| Palo Alto Networks PAN-OS | 11.2 < 11.2.4-h1 <br> 11.1 < 11.1.5-h1 <br> 11.0 < 11.0.6-h1 <br> 10.2 < 10.2.12-h2 <br> | [CVE-2024-0012](https://nvd.nist.gov/vuln/detail/CVE-2024-0012) | 9.3  | **Critical** |

## What has been observed?

Palo Alto Networks observed threat activity that exploits this vulnerability against a limited number of management web interfaces that are exposed to internet traffic coming from outside the network.
There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Paloalto: <https://security.paloaltonetworks.com/CVE-2024-0012>
