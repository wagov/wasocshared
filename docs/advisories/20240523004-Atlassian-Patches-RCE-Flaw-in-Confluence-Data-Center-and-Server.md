# Atlassian Patches RCE Flaw in Confluence Data Center and Server - 20240523004

## Overview

Atlassian has released a security announcement for a Remote Code Execution (RCE) vulnerability in Confluence Data Center and Server. This vulnerability allows authenicated attackers to perform RCE by sending malicious requests.

## What is vulnerable?

| CVE                                                               | Severity | CVSS | Product(s) Affected                                                                                     | Summary                                                                                                                                                                                                                                                                 | Dated      |
| ----------------------------------------------------------------- | -------- | ---- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [CVE-2024-21683](https://nvd.nist.gov/vuln/detail/CVE-2024-21683) | **High** | N.A  | **Versions: 5.2, 7.19.0, 7.20.0, 8.0.0, 8.1.0, 8.2.0, 8.3.0, 8.4.0, 8.5.0, 8.6.0, 8.8.0, 8.7.1, 8.9.0** | This RCE (Remote Code Execution) vulnerability, with a CVSS Score of 8.3, allows an authenticated attacker to execute arbitrary code which has high impact to confidentiality, high impact to integrity, high impact to availability, and requires no user interaction. | 21-05-2024 |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *2 weeks...* (refer [Patch Management](../guidelines/patch-management.md)):

- **Confluence Data Center**

Atlassian recommends that Confluence Data Center customers upgrade to the latest version. If you are unable to do so, upgrade your instance to one of the specified supported fixed versions:

|   **Affected versions**    |              **Fixed versions**               |
| :------------------------: | :-------------------------------------------: |
|           8.9.0            |                     8.9.1                     |
|    from 8.8.0 to 8.8.1     |                     8.9.1                     |
|    from 8.7.0 to 8.7.2     |                     8.9.1                     |
|    from 8.6.0 to 8.6.2     |                     8.9.1                     |
|  from 8.5.0 to 8.5.8 LTS   |        8.9.1 or 8.5.9 LTS recommended         |
|    from 8.4.0 to 8.4.5     |        8.9.1 or 8.5.9 LTS recommended         |
|    from 8.3.0 to 8.3.4     |        8.9.1 or 8.5.9 LTS recommended         |
|    from 8.2.0 to 8.2.3     |        8.9.1 or 8.5.9 LTS recommended         |
|    from 8.1.0 to 8.1.4     |        8.9.1 or 8.5.9 LTS recommended         |
|    from 8.0.0 to 8.0.4     |        8.9.1 or 8.5.9 LTS recommended         |
|   from 7.20.0 to 7.20.3    |        8.9.1 or 8.5.9 LTS recommended         |
| from 7.19.0 to 7.19.21 LTS | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |
|   from 7.18.0 to 7.18.3    | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |
|   from 7.17.0 to 7.17.5    | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |
|    Any earlier versions    | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |

- **Confluence Server**

Atlassian recommends that Confluence Server customers upgrade to the latest version. If you are unable to do so, upgrade your instance to one of the specified supported fixed versions:

|   **Affected versions**    |              **Fixed versions**               |
| :------------------------: | :-------------------------------------------: |
|  from 8.5.0 to 8.5.8 LTS   |             8.5.9 LTS recommended             |
|    from 8.4.0 to 8.4.5     |             8.5.9 LTS recommended             |
|    from 8.3.0 to 8.3.4     |             8.5.9 LTS recommended             |
|    from 8.2.0 to 8.2.3     |             8.5.9 LTS recommended             |
|    from 8.1.0 to 8.1.4     |             8.5.9 LTS recommended             |
|    from 8.0.0 to 8.0.4     |             8.5.9 LTS recommended             |
|   from 7.20.0 to 7.20.3    |             8.5.9 LTS recommended             |
| from 7.19.0 to 7.19.21 LTS |     8.5.9 LTS recommended or 7.19.22 LTS      |
|   from 7.18.0 to 7.18.3    |     8.5.9 LTS recommended or 7.19.22 LTS      |
|   from 7.17.0 to 7.17.5    |     8.5.9 LTS recommended or 7.19.22 LTS      |
|    Any earlier versions    |     8.5.9 LTS recommended or 7.19.22 LTS      |
| from 7.19.0 to 7.19.21 LTS | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |
|   from 7.18.0 to 7.18.3    | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |
|   from 7.17.0 to 7.17.5    | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |
|    Any earlier versions    | 8.9.1 or 8.5.9 LTS recommended or 7.19.22 LTS |

## Additional References

- [CVE-2024-21683: Atlassian Patches RCE Flaw in Confluence Data Center and Server (securityonline.info)](https://securityonline.info/cve-2024-21683-atlassian-patches-rce-flaw-in-confluence-data-center-and-server/)
- [Confluence Remote Code Execution Vulnerability (CVE-2024-21683) Notification - NSFOCUS, Inc., a global network and cyber security leader, protects enterprises and carriers from advanced cyber attacks. (nsfocusglobal.com)](https://nsfocusglobal.com/confluence-remote-code-execution-vulnerability-cve-2024-21683-notification/)
- [\[CONFSERVER-95832\] RCE (Remote Code Execution) in Confluence Data Center and Server - Create and track feature requests for Atlassian products.](https://jira.atlassian.com/browse/CONFSERVER-95832)
