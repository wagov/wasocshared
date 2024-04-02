# GitLab Stored XSS Vulnerability - 20240402003

## Overview

The WA SOC has been made aware of a vulnerability in GitLab CE/EE where a wiki page with a crafted payload may lead to a Stored XSS, allowing attackers to perform arbitrary actions on behalf of victims.

GitLab strongly recommends that all affected instances are upgraded to the latest version as soon as possible.

## What is vulnerable?

| CVE                                                             | Severity | CVSS | Product(s) Affected                                                                                                                                            | Summary                                                                                                                            | Dated      |
| --------------------------------------------------------------- | -------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [CVE-2023-6371](https://nvd.nist.gov/vuln/detail/CVE-2023-6371) | **High** | 8.7  | GitLab CE/EE affecting all versions **before 16.8.5**, all versions starting **from 16.9 before 16.9.3**, all versions starting **from 16.10 before 16.10.1**. | A wiki page with a crafted payload may lead to a Stored XSS, allowing attackers to perform arbitrary actions on behalf of victims. | 28/03/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- [GitLab Security Release: 16.10.1, 16.9.3, 16.8.5](https://about.gitlab.com/releases/2024/03/27/security-release-gitlab-16-10-1-released/)

## Additional References

- [Stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored)
