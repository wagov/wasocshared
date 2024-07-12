# GitLab Critical Advisory - 20240712002

## Overview

The WA SOC has been made aware of a several critical vulnerabilities affecting GitLab, a popular web-based DevOps platform. 

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE  | CVSS          | Severity   |
| ------------------- | ---------- | ---- | ------------- | ---------- |
| GitLab      | 17.1 before 17.1.2 <br> 17.0 before 17.0.4 <br> 15.8 before 16.11.6 | [CVE-2024-6385](https://nvd.nist.gov/vuln/detail/CVE-2024-6385) <br> [CVE-2024-5257](https://nvd.nist.gov/vuln/detail/CVE-2024-5257) <br> [CVE-2024-5470](https://nvd.nist.gov/vuln/detail/CVE-2024-5470) <br> [CVE-2024-6595](https://nvd.nist.gov/vuln/detail/CVE-2024-6595) <br> [CVE-2024-2880](https://nvd.nist.gov/vuln/detail/CVE-2024-2880) <br> [CVE-2024-5528](https://nvd.nist.gov/vuln/detail/CVE-2024-5528)  | 9.6 <br> 4.9 <br> 3.7 <br> 6.5 <br> 2.7 <br> 6.5 | **Critical** <br> Medium <br> Low <br> Medium <br> Low <br> Medium |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://about.gitlab.com/releases/2024/07/10/patch-release-gitlab-17-1-2-released/#an-attacker-can-run-pipeline-jobs-as-an-arbitrary-user>

## Additional References

- SecurityOnline: <https://securityonline.info/gitlab-patches-critical-security-vulnerability-cve-2024-6385-urges-immediate-upgrade/>
