# GitLab Critical Security Update - 20240426002


## Overview


GitLab released versions 16.11.1, 16.10.4, 16.9.6 for GitLab Community Edition (CE) and Enterprise Edition (EE) to address multiple High and Medium vulnerabilities. GitLab strongly recommends that all GitLab installations be upgraded to one of these versions. GitLab.com is already running the patched version.


## What is vulnerable?


| CVE    | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ------ | ------------ | ---- | ------------------- | ------- | ----- |
| CVE-2024-4024 | **High** | 7.3  | **versions before** 16.11.1, 16.10.4, 16.9.6 | An attacker with their Bitbucket account credentials may be able to take over a GitLab account linked to another user's Bitbucket account, if Bitbucket is used as an OAuth 2.0 provider on GitLab. | 25 April 2024 |
CVE-2024-1347 | **Medium** | 4.3 | **versions before** 16.11.1, 16.10.4, 16.9.6 | An attacker, through a crafted email address, may be able to bypass domain based restrictions on an instance or a group. | 25 April 2024 |
CVE-2024-2829 | **High** | 7.5 | **versions before** 16.11.1, 16.10.4, 16.9.6 |  A crafted wildcard filter in FileFinder may lead to a denial of service. | 25 April 2024 |


## What has been observed?


There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.


## Recommendation


The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://about.gitlab.com/releases/2024/04/24/patch-release-gitlab-16-11-1-released/


## Additional References


- [CVE-2024-4024](https://nvd.nist.gov/vuln/detail/CVE-2024-4024)
- [CVE-2024-1347](https://nvd.nist.gov/vuln/detail/CVE-2024-1347)
- [CVE-2024-2829](https://nvd.nist.gov/vuln/detail/CVE-2024-2829)
- https://securityonline.info/urgent-gitlab-update-patches-account-takeover-flaw-other-high-severity-bugs/?expand_article=1

