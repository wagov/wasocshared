# GitLab Vulnerabilities June 2024 - 20240628001

## Overview

GitLab, the web-based DevOps platform has released security patches to address several a vulnerabilities including a critical 9.6 CVSS that allows an attacker to run pipelines as any user.

## What is the Vulnerability?

| CVE                                                                           | Severity     | CVSS Score | Summary                                                                                                                                                                                                                                                                                                         | Dated         |
| ----------------------------------------------------------------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [CVE-2024-5655](https://nvd.nist.gov/vuln/detail/CVE-2024-5655)               | **Critical** | 9.6        | An issue was discovered in GitLab CE/EE affecting all versions starting from 15.8 prior to 16.11.5, starting from 17.0 prior to 17.0.3, and starting from 17.1 prior to 17.1.1, which allows an attacker to trigger a pipeline as another user under certain circumstances.                                     | 26 June, 2024 |
| [CVE-2024-4901](https://nvd.nist.gov/vuln/detail/CVE-2024-4901)               | **High**     | 8.7        | An issue was discovered in GitLab CE/EE affecting all versions starting from 16.9 prior to 16.11.5, starting from 17.0 prior to 17.0.3, and starting from 17.1 prior to 17.1.1, where a stored XSS vulnerability could be imported from a project with malicious commit notes.                                  | 26 June, 2024 |
| [CVE-2024-4994](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4994) | **High**     | 8.1        | An issue has been discovered in GitLab CE/EE affecting all versions from 16.1.0 before 16.11.5, all versions starting from 17.0 before 17.0.3, all versions starting from 17.1.0 before 17.1.1 which allowed for a CSRF attack on GitLab's GraphQL API leading to the execution of arbitrary GraphQL mutations. | 26 June, 2024 |
| [CVE-2024-6323](https://nvd.nist.gov/vuln/detail/CVE-2024-6323)               | **High**     | 7.7        | Improper authorization in global search in GitLab EE affecting all versions from 16.11 prior to 16.11.5 and 17.0 prior to 17.0.3 and 17.1 prior to 17.1.1 allows an attacker leak content of a private repository in a public project.                                                                          | 26 June, 2024 |

## What is vulnerable?

The most severe vulnerability, CVE-2024-5655 (CVSS 9.6), involves use of the GitLab piplines which are a feature of the CI/CD system that enables users to autmatically run processes and tasks. The vulnerability gives an attacker the opportunity to run these pipelines as any user.

For this most critical vulnerability, it affects the following products:

GitLab - All deployment types:

- 15.8 before 16.11.5
- 17.0 before 17.03
- 17.1 before 17.1.1

Each vulnerability affects different versions listed in above table.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- <https://about.gitlab.com/releases/2024/06/26/patch-release-gitlab-17-1-1-released/>

## Additional References

- [Critical GitLab bug lets attackers run pipelines as any user](https://www.bleepingcomputer.com/news/security/critical-gitlab-bug-lets-attackers-run-pipelines-as-any-user/)
