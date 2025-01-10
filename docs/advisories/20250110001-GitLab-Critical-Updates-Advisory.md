# GitLab Releases Critical Updates Advisory - 20250110001

## Overview

GitLab has released patches for crtical vulnerabilities discovered in GitLab CE/EE, which allows an attacker trigger a pipeline as another user under certain circumstances.

## What is the vulnerability?

| CVE                                                             | Severity     | CVSS |
| --------------------------------------------------------------- | ------------ | ---- |
| [CVE-2024-5655](https://nvd.nist.gov/vuln/detail/CVE-2024-5655) | **Critical** | 9.6  |
| [CVE-2024-6385](https://nvd.nist.gov/vuln/detail/CVE-2024-6385) | **Critical** | 9.6  |
| [CVE-2024-6678](https://nvd.nist.gov/vuln/detail/CVE-2024-6678) | **Critical** | 9.9  |
| [CVE-2024-8970](https://nvd.nist.gov/vuln/detail/CVE-2024-8970) | **High**     | 8.2  |

## What is vulnerable?

| Product(s) Affected |                                   |
| ------------------- | --------------------------------- |
| GitLab CE/EE        | **versions from** 8.14 to 17.1.7  |
| GitLab CE/EE        | **versions from** 17.2 to 17.2.9  |
| GitLab CE/EE        | **versions from** 17.3 to 17.3.5  |
| GitLab CE/EE        | **versions from** 17.4 to 17.4.2  |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- GitLab Security Release: <https://about.gitlab.com/releases/2025/01/08/patch-release-gitlab-17-7-1-released/>

## Additional References

- SecurityOnline: <https://securityonline.info/gitlab-tackles-critical-security-flaws-in-latest-patch-release/>
