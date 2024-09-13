# GitLab Critical Update - 20240913003

## Overview

GitLab has released critical updates to address multiple vulnerabilities, the most severe of them allowing an attacker to trigger pipelines as arbitrary users under certain conditions.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                               | CVE                                                             | CVSS    | Severity     |
| ------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ------------ |
| GitLab CE/EE        | 8.14 prior to 17.1.7 <br> 17.2 prior to 17.2.5 <br> 17.3 prior to 17.3.2 | [CVE-2024-6678](https://nvd.nist.gov/vuln/detail/CVE-2024-6678) | **9.9** | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- GitLab Critical Patch Release Notes: <https://about.gitlab.com/releases/2024/09/11/patch-release-gitlab-17-3-2-released/>

## Additional References

- BleepingComputer article: <https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-pipeline-execution-vulnerability/>
