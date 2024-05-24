# GitLab Account Takeover Vulnerability - 20240524002

## Overview

GitLab, the web-based DevOps platform has released security patches to address a vulnerability where a XSS condition exists within versions 15.11 before 16.10.6, 16.11 before 16.11.3, and 17.0 before 17.0.1. By leveraging this condition, an attacker can craft a malicious page to exfiltrate sensitive user information.

## What is the Vulnerability?

| CVE                                                             | Severity     | CVSS Score | Summary                                                                                                                                     | Dated       |
| --------------------------------------------------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [CVE-2024-4835](https://nvd.nist.gov/vuln/detail/CVE-2024-4835) | **High** | 8         | A XSS condition exists within GitLab in versions 15.11 before 16.10.6, 16.11 before 16.11.3, and 17.0 before 17.0.1. By leveraging this condition, an attacker can craft a malicious page to exfiltrate sensitive user information. | 23 May, 2024 |

## What is vulnerable?

The most severe vulnerability, CVE-2024-4835 (CVSS 8.0), involves a cross-site scripting (XSS) flaw in the code editor on gitlab.com. Attackers could exploit this flaw to steal sensitive user information, potentially leading to a full account takeover. GitLab strongly urges all users to update their installations immediately to mitigate this risk.

The vulnerability affects the following products:

GitLab - All deployment types:

- 15.11 before 16.10.6
- 16.11 before 16.11.3
- 17.0 before 17.0.1.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- <https://about.gitlab.com/releases/2024/05/22/patch-release-gitlab-17-0-1-released/>

## Additional References

- [CVE-2024-4835: GitLab Fixes Account Takeover Vulnerability](https://securityonline.info/cve-2024-4835-gitlab-fixes-account-takeover-vulnerability/)
