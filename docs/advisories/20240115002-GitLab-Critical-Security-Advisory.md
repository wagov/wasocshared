# GitLab Critical Security Advisory - 20240115002

## Overview

GitLab has released a critical security advisory announcing the release of versions 16.7.2, 16.6.4, 16.5.6 for GitLab Community Edition (CE) and Enterprise Edition (EE).

Additionally, GitLab has noted "*These versions contain important security fixes, and we strongly recommend that all GitLab installations be upgraded to one of these versions immediately. GitLab.com is already running the patched version.*"

## What is the Vulnerability?

| CVE| Severity| CVSS Score | Summary |Exploied|Dated|
|------ | ------ | ----- |------|---- |--|
| [CVE-2023-7028](https://nvd.nist.gov/vuln/detail/CVE-2023-7028) | **Critical** | 10         | An issue has been discovered in GitLab CE/EE in which user account password reset emails could be delivered to an unverified email address. |Yes| 1 May, 2024|

## What is vulnerable?

CISA added this vulnerability in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

The vulnerability affects the following products:

GitLab - All deployment types:

- 16.1 prior to 16.1.5
- 16.2 prior to 16.2.8
- 16.3 prior to 16.3.6
- 16.4 prior to 16.4.4
- 16.5 prior to 16.5.6
- 16.6 prior to 16.6.4
- 16.7 prior to 16.7.2

## What has been observed?

GitLab says it has not detected any cases of active exploitation, however  Self-managed customers can review their logs to check for possible attempts to exploit this vulnerability:

- `Check gitlab-rails/production_json.log for HTTP requests to the /users/password path with params.value.email consisting of a JSON array with multiple email addresses.`
- `Check gitlab-rails/audit_json.log for entries with meta.caller.id of PasswordsController#create and target_details consisting of a JSON array with multiple email addresses.`

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://about.gitlab.com/releases/2024/01/11/critical-security-release-gitlab-16-7-2-released/>

## Additional References

- BleepingComputer article "*GitLab warns of critical zero-click account hijacking vulnerability*": <https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-zero-click-account-hijacking-vulnerability/>
