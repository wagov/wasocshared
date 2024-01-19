# CISA Releases Oracle E-Business Suite & SugarCRM Known Vulnerabilities Updates - 20230203003

## Overview

CISA has added two new vulnerabilities to its [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), based on evidence of active exploitation. These types of vulnerabilities are frequent attack vectors for malicious cyber actors and pose significant risks to federal enterprises.

## What is vulnerable?

| CVE                                                               | Vendor/Project | Product           | Vulnerability Name                                             | Date Added to Catalog | Short Description                                                                                                                                                                              | Action                                                                                                          | Due Date   |
| ----------------------------------------------------------------- | -------------- | ----------------- | -------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------- |
| [CVE-2022-21587](https://nvd.nist.gov/vuln/detail/CVE-2022-21587) | Oracle         | E-Business Suite  | Oracle E-Business Suite Unspecified Vulnerability              | 2023-02-02            | Oracle E-Business Suite contains an unspecified vulnerability that allows an unauthenticated attacker with network access via HTTP to compromise Oracle Web Applications Desktop Integrator.   | Apply updates per [vendor instructions](https://www.oracle.com/security-alerts/cpuoct2022.html).                | 2023-02-23 |
| [CVE-2023-22952](https://nvd.nist.gov/vuln/detail/CVE-2023-22952) | SugarCRM       | Multiple Products | Multiple SugarCRM Products Remote Code Execution Vulnerability | 2023-02-02            | Multiple SugarCRM products contain a remote code execution vulnerability in the EmailTemplates. Using a specially crafted request, custom PHP code can be injected through the EmailTemplates. | Apply updates per [vendor instructions](https://support.sugarcrm.com/Resources/Security/sugarcrm-sa-2023-001/). | 2023-02-23 |
|                                                                   |                |                   |                                                                |                       |                                                                                                                                                                                                |                                                                                                                 |            |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices.

## Additional References

- <https://www.cisa.gov/uscert/ncas/current-activity/2023/02/02/cisa-adds-two-known-exploited-vulnerabilities-catalog>
- <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>
- <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21587>
- <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22952>
