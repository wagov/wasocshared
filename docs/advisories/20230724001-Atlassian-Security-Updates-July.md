# On-prem Atlassian Stacks are vulnerable - 20230724001

## Overview

The WA SOC has observed a critical and high severity RCE (Remote Code Execution) vulnerability, which allows an authenticated attacker to execute arbitrary code which has high impact to confidentiality, integrity, availability, and no user interaction.

## What is the vulnerability?

[**CVE-2023-22505**](https://nvd.nist.gov/vuln/detail/CVE-2023-22505) - CVSS v3 Base Score: ***8.0***

[**CVE-2023-22506**](https://nvd.nist.gov/vuln/detail/CVE-2023-22506) - CVSS v3 Base Score: ***7.5***

[**CVE-2023-22508**](https://nvd.nist.gov/vuln/detail/CVE-2023-22508) - CVSS v3 Base Score: ***8.5***

## What is vulnerable?

The vulnerability affects the following products:

- Confluence Data Center (8.0.0, 7.4.0)
- Confluence Server (8.0.0, 7.4.0)
- Bamboo Data Center and Server 8.0.0

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Atlassian Security Bulletin July](https://confluence.atlassian.com/security/security-bulletin-july-18-2023-1251417643.html)
- [Confluence Release Notes](https://confluence.atlassian.com/doc/confluence-release-notes-327.html)

## Additional References

- [Confluence Download Archives](https://www.atlassian.com/software/confluence/download-archives)
- [CISA](https://www.cisa.gov/news-events/alerts/2023/07/21/atlassian-releases-security-updates)
