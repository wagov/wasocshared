# Bitdefender Critical Vulnerabilities in GravityZone and Endpoint Security - 20240415002

## Overview

Bitdefender has released a security advisory to address a Path Traversal vulnerability in the UpdateServer component of Bitdefender GravityZone. The vulnerability could allow an attacker to excute arbitrary code on vulnerable instance of affected products.

## What is vulnerable?

| Product(s) Affected                                                                                                                                                                                          | CVE                                                               | Severity   | CVSS |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ---------- | ---- | --- |
| Bitdefender Endpoint Security for Linux version 7.0.5.200089 <br>Bitdefender Endpoint Security for Windows version 7.9.9.380 <br>GravityZone Control Center (On Premises) version 6.36.1<br> | [CVE-2024-2224](https://nvd.nist.gov/vuln/detail/CVE-2024-2224), [CVE-2024-2223](https://nvd.nist.gov/vuln/detail/CVE-2024-2223) | **High** | 8.1  |     |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

## Additional References

- [Incorrect Regular Expression in GravityZone Update Server (VA-11465) - Bitdefender](https://www.bitdefender.com/support/security-advisories/incorrect-regular-expression-in-gravityzone-update-server-va-11465/)
- [Privilege Escalation via the GravityZone productManager UpdateServer.KitsManager API (VA-11466) - Bitdefender](https://www.bitdefender.com/support/security-advisories/privilege-escalation-via-the-gravityzone-productmanager-updateserver-kitsmanager-api-va-11466/)
