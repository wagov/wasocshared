# Palo Alto Critical Vulnerabilities - 20241010003

## Overview

Palo Alto have published an advisory regarding multiple vulnerabilities in Palo Alto Networks Expedition. Sucesful exploitation could allow an attacker to read Expedition database contents and arbitrary files, as well as write arbitrary files to temporary storage locations on the Expedition system. Combined, these include information such as usernames, cleartext passwords, device configurations, and device API keys of PAN-OS firewalls.

## What is vulnerable?

| Product(s) Affected           | Version(s)             | CVE #                                                                                                                                                                                                     | CVSS v4/v3            | Severity                             |
| ----------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------ |
| Palo Alto Networks Expedition | all versions \< 1.2.96 | [CVE-2024-9463](https://nvd.nist.gov/vuln/detail/CVE-2024-9463) <br> [CVE-2024-9464](https://nvd.nist.gov/vuln/detail/CVE-2024-9464) <br> [CVE-2024-9465](https://nvd.nist.gov/vuln/detail/CVE-2024-9465) | 9.9 <br> 9.3 <br> 9.2 | Critical <br> Critical <br> Critical |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

## Reference

- Palo Alto advisory: <https://security.paloaltonetworks.com/PAN-SA-2024-0010>
