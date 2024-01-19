# Atlassian releases fixes for RCE vulnerabilities in multiple products - 20231207001

## Overview

Atlassian has released security fixes for RCE (Remote Code Execution) vulnerabilities in multiple products and relevant mitigations as part of their [**December 2023 Security Advisories**](https://confluence.atlassian.com/security/december-2023-security-advisories-overview-1318892103.html).

## What is vulnerable?

***CVE-2022-1471*** *-* [*SnakeYAML library RCE Vulnerability impacts Multiple Products*](https://confluence.atlassian.com/x/AQBCTQ)

- *Bitbucket Data Center and Server*
- *Confluence Data Center and Server*
- *Confluence Cloud Migration App (CCMA)*
- *Jira Core Data Center and Server*
- *Jira Service Management Data Center and Server*
- *Jira Software Data Center and Server*
- *Automation for Jira (A4J) app (including Server Lite edition)*

***CVE-2023-22522*** *-* [*RCE Vulnerability in Confluence Data Center and Server*](https://confluence.atlassian.com/x/ugunTg)

- *Confluence Data Center and Server*

***CVE-2023-22524*** *-*[*RCE Vulnerability in Atlassian Companion App for MacOS*](https://confluence.atlassian.com/security/cve-2023-22524-rce-vulnerability-in-atlassian-companion-app-for-macos-1319249492.html)

- *Confluence Data Center and Server (former and present customers)*

***CVE-2023-22523*** *-* [*RCE Vulnerability in Assets Discovery*](https://confluence.atlassian.com/x/EiSiTg) *(stand-alone app)*

- *Jira Service Management Data Center and Server*

## What has been observed?

The Australian Signal Directorate’s Australian Cyber Security Centre (ASD’s ACSC) notes that previous critical vulnerabilities in Confluence and Jira have had significant exploitation by malicious cyber actors.

## Recommendation

See [ACSC Serious vulnerabilities in Atlassian products including Confluence, Jira and Bitbucket](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/serious-vulnerabilities-in-atlassian-products-including-confluence-jira-and-bitbucket) for more detail.

- If you operate Confluence, Jira or Bitbucket, particularly in internet facing configurations, review the vendor advisories to determine if you are affected
- If you are affected carefully apply all vendor recommended mitigations within expected timeframe of *48 hours* for internet facing instances (refer [Patch Management](../guidelines/patch-management.md)):
- Reassess whether your system needs to be internet facing and filter from the internet if possible.
