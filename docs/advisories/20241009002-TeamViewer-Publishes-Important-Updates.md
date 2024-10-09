# TeamViewer Publishes Important Updates - 20241009002

## Overview

A vulnerability has been discovered in the TeamViewer Remote clients for Windows which allows local privilege escalation on a Windows system.

## What is vulnerable?

| Product(s) Affected                                             | Version(s)                                                                            | CVE #                                                                                                                                  | CVSS v4/v3  | Severity   |
| ----------------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------|------------|
| TeamViewer Full Client (Windows) <br> TeamViewer Host (Windows) | < 15.58.4 <br> < 14.7.48796 <br> < 13.2.36225 <br> < 12.0.259312 <br> < 11.0.259311   | [CVE-2024-7479](https://nvd.nist.gov/vuln/detail/CVE-2024-7479) <br> [CVE-2024-7481](https://nvd.nist.gov/vuln/detail/CVE-2024-7481)   | 8.8         | High       |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- TeamViewer: <https://www.teamviewer.com/en-au/resources/trust-center/security-bulletins/tv-2024-1006/?>

## Additional References

- Cybersecurity News: <https://securityonline.info/exploit-releases-for-teamviewer-flaws-cve-2024-7479-cve-2024-7481-let-unprivileged-users-load-arbitrary-kernel-drivers/>
