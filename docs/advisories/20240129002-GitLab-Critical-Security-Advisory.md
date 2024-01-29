## GitLab Critical Security Advisory - 20240129002

## Overview

GitLab has released patches for crtical vulnerability discovered in GitLab CE/EE, which allows an authenticated user to write files to arbitrary locations on the GitLab server while creating a workspace.

## What is the vulnerability?

| CVE                                                               | Severity     | CVSS |
| ----------------------------------------------------------------- | ------------ | ---- |
| [CVE-2024-0402](https://nvd.nist.gov/vuln/detail/CVE-2024-0402) | **Critical** | 9.9  |

## What is vulnerable?

| Product(s) Affected                                                   | |
| ------ | ------------ | 
|GitLab CE/EE | **versions before** 16.0 to 16.6.6|
|GitLab CE/EE|**versions before** 16.7 to 16.7.4|
|GitLab CE/EE|**versions before** 16.8 to 16.8.1|  

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks* (refer [Patch Management](../guidelines/patch-management.md)):

- [Gotlab security release](https://about.gitlab.com/releases/2024/01/25/critical-security-release-gitlab-16-8-1-released/#arbitrary-file-write-while-creating-workspace)


