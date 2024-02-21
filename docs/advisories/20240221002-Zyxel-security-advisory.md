# Zyxel security advisory for multiple vulnerabilities in firewalls and APs - 20240221002

## Overview

Zyxel has released a security advisory relating to multiple vulnerabilities present in select firewall and access point models. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is vulnerable?

| Product(s) Affected                                             | Summary         | Severity                                                                                                                                                                | CVSS |
| --------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| [CVE-2023-6397](https://www.cve.org/CVERecord?id=CVE-2023-6397) | Firewalls       | **[MEDIUM](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2023-6397&vector=AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H&version=3.1&source=Zyxel%20Corporation)** | 6.5  |
| [CVE-2023-6398](https://www.cve.org/CVERecord?id=CVE-2023-6398) | Firewalls & APs | **[HIGH](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2023-6398&vector=AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H&version=3.1&source=Zyxel%20Corporation)**   | 7.2  |
| [CVE-2023-6399](https://www.cve.org/CVERecord?id=CVE-2023-6399) | Firewalls       | **[MEDIUM](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2023-6399&vector=AV:A/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H&version=3.1&source=Zyxel%20Corporation)** | 5.7  |
| [CVE-2023-6764](https://www.cve.org/CVERecord?id=CVE-2023-6764) | Firewalls       | **[HIGH](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2023-6764&vector=AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1&source=Zyxel%20Corporation)**   | 8.1  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Zyxel security advisory for multiple vulnerabilities in firewalls and APs](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-multiple-vulnerabilities-in-firewalls-and-aps-02-20-2024)

## Additional References

- [Multiple vulnerabilities in Zyxel firewalls and APs](https://www.cybersecurity-help.cz/vdb/SB2024022031)
- [Zyxel Security Vulnerabilities: DoS, Command Injection & More](https://securityonline.info/zyxel-security-vulnerabilities-dos-command-injection-more/)
