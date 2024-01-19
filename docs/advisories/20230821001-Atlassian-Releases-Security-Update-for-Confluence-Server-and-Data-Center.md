# Atlassian-Releases-Security-Update-for-Confluence-Server-and-Data-Center - 20230821001

## Overview

Atlassian has released security updates for Confluence to address a third-party dependancy vulnerability in Confluence Data Center and Server.

## What is the vulnerability?

[**CVE-2023-28709**](https://nvd.nist.gov/vuln/detail/CVE-2023-28709) - CVSS v3 Base Score: ***7.5***

This Patch Management vulnerability, with CVSS Score(s) of 7.5, allows an authenticated attacker to expose assets in your environment susceptible to exploitation which has no impact to confidentiality, no impact to integrity, high impact to availability, and requires no user interaction.

## What is vulnerable?

The vulnerability affects the following products:

- Confluence Data Center and Server Versions:
    - 7.13.15 - 7.13.18
    - 7.19.7 - 7.19.10
    - 8.1.1 - 8.4.0

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

Atlassian recommends that you upgrade your instance to **latest version**.
If you're unable to do so, upgrade to these **fixed versions: 7.13.19, 7.19.11 or 8.4.1**.

## Additional References

- [Security Bulletin - August 15 2023 | Atlassian Support | Atlassian Documentation](https://confluence.atlassian.com/security/security-bulletin-august-15-2023-1276870882.html)
- [\[CONFSERVER-90185\] Third-Party Dependency Vulnerability in Confluence - Create and track feature requests for Atlassian products.](https://jira.atlassian.com/browse/CONFSERVER-90185)
