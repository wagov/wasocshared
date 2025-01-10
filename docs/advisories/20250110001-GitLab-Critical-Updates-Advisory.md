# GitLab Releases Critical Updates - 20250110001

## Overview

GitLab has released critical updates for their GitLab Community Edition(CE) and GitLab Enterprise Edition (EE) products. Successful exploitation could allow an attacker trigger a pipeline as another user under certain circumstances.

## What is vulnerable?

| Product(s) Affected | Versions(s)                                                | CVE                                                             | Severity | CVSS         |
| ------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- | -------- | ------------ |
| GitLab CE/EE        | - 15.8 < 16.11.5 <br> - 17.6 < 17.6.3 <br> - 17.7 < 17.7.1 | [CVE-2024-5655](https://nvd.nist.gov/vuln/detail/CVE-2024-5655) | 9.6      | **Critical** |
| GitLab CE/EE        | - 15.8 < 16.11.6 <br> - 17.0 < 17.0.4 <br> - 17.1 < 17.1.2 | [CVE-2024-6385](https://nvd.nist.gov/vuln/detail/CVE-2024-6385) | 9.6      | **Critical** |
| GitLab CE/EE        | - 8.14 < 17.1.7 <br> - 17.2 < 17.2.5 <br> - 17.3 < 17.3.2  | [CVE-2024-6678](https://nvd.nist.gov/vuln/detail/CVE-2024-6678) | 9.9      | **Critical** |
| GitLab CE/EE        | - 11.6 < 17.2.9 <br> - 17.3 < 17.3.5 <br> - 17.4 < 17.4.2  | [CVE-2024-8970](https://nvd.nist.gov/vuln/detail/CVE-2024-8970) | 8.2      | High         |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- GitLab Security Release: <https://about.gitlab.com/releases/2025/01/08/patch-release-gitlab-17-7-1-released/>

## Additional References

- SecurityOnline: <https://securityonline.info/gitlab-tackles-critical-security-flaws-in-latest-patch-release/>
