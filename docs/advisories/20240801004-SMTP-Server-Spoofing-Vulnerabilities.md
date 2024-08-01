# Multiple SMTP Servers Vulnerable to Spoofing Attacks - 20240801004

## Overview

The WA SOC has been made aware of an article released by the Coordination Center (CERT/CC) at Carnegie Mellon University disclosing vulnerabilities in multiple hosted, outbound SMTP servers. The vulnerabilities affect the authentication and verification mechanisms provided by the Sender Policy Framework (SPF) and Domain Key Identified Mail (DKIM).

An authenticated attacker using network or SMTP authentication can spoof the identity of a shared hosting facility, circumventing any DMARC policy and sender verification provided by a domain name owner.

## What is vulnerable?

| CVE | CVSS | Severity | Description |
| --- | --- | --- | --- |
| [CVE-2024-7208](https://nvd.nist.gov/vuln/detail/CVE-2024-7208) | TBD | TBD | Hosted services do not verify the sender of an email against authenticated users, allowing an attacker to spoof the identify of another user's email address. |
| [CVE-2024-7209](https://nvd.nist.gov/vuln/detail/CVE-2024-7209) | TBD | TBD | A vulnerability exists in the use of shared SPF records in multi-tenant hosting providers, allowing attackers to use network authorization to be abused to spoof the email identify of the sender. |

## What has been observed?

The WA SOC has been made aware of exploitation in the wild for these vulnerabilities. There is no evidence exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- Carnegie Mellon University article: <https://kb.cert.org/vuls/id/244112>
