# BD Alaris System with Guardrails Suite MX - 20230714002

## Overview

The WA SOC has observed eight vulnerabilities in medical technology products by Becton, Dickinson and Company (BD) Alaris infusion System with Guardrails Suite MX. As such, successful exploitation of these vulnerabilities could allow an attacker to compromise sensitive data, hijack a session, modify firmware, make changes to system configurations, among other system impacts.

## What is the vulnerability?

- [IMPROPER INPUT VALIDATION CWE-20](https://cwe.mitre.org/data/definitions/20.html)  
[**CVE-2023-30559**](https://nvd.nist.gov/vuln/detail/CVE-2023-30559) - CVSS v3 Base Score: ***6.8***

- [IMPROPER AUTHENTICATION CWE-287](https://cwe.mitre.org/data/definitions/287.html)  
[**CVE-2023-30560**](https://nvd.nist.gov/vuln/detail/CVE-2023-30560) - CVSS v3 Base Score: ***6.8***

- [MISSING ENCRYPTION OF SENSITIVE DATA CWE-311](https://cwe.mitre.org/data/definitions/311.html)  
[**CVE-2023-30561**](https://nvd.nist.gov/vuln/detail/CVE-2023-30561) - CVSS v3 Base Score: ***6.1***

- [INSUFFICIENT VERIFICATION OF DATA AUTHENTICITY CWE-345](https://cwe.mitre.org/data/definitions/345.html)  
[**CVE-2023-30562**](https://nvd.nist.gov/vuln/detail/CVE-2023-30562) - CVSS v3 Base Score: ***6.7***

- [IMPROPER NEUTRALIZATION OF INPUT DURING WEB PAGE GENERATION ('CROSS-SITE SCRIPTING') CWE-79](https://cwe.mitre.org/data/definitions/79.html)  
[**CVE-2023-30563**](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2023-30563) - CVSS v3 Base Score: ***8.2***

- [IMPROPER NEUTRALIZATION OF INPUT DURING WEB PAGE GENERATION ('CROSS-SITE SCRIPTING') CWE-79](https://cwe.mitre.org/data/definitions/79.html)  
[**CVE-2023-30564**](https://nvd.nist.gov/vuln/detail/CVE-2023-30564) - CVSS v3 Base Score: ***6.9***

- [CLEARTEXT TRANSMISSION OF SENSITIVE INFORMATION CWE-319](https://cwe.mitre.org/data/definitions/319.html)  
[**CVE-2023-30565**](https://nvd.nist.gov/vuln/detail/CVE-2023-30565) - CVSS v3 Base Score: ***3.5***

- [IMPROPER RESTRICTION OF XML EXTERNAL ENTITY REFERENCE CWE-611](https://cwe.mitre.org/data/definitions/611.html)  
[**CVE-2018-1285**](https://nvd.nist.gov/vuln/detail/CVE-2018-1285) - CVSS v3 Base Score: ***9.8***


## What is vulnerable?

The vulnerability affects the following products:

-   BD Alaris Point-of-Care Unit (PCU) Model 8015: Versions 12.1.3 and prior
-   BD Alaris Guardrails Editor: Versions 12.1.2 and prior
-   BD Alaris Systems Manager: Versions 12.3 and prior
-   CQI Reporter: v10.17 and prior
-   Calculation Services: Versions 1.0 and prior

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [BD security bulletin/patches](https://www.bd.com/en-us/about-bd/cybersecurity/bulletin/bd-alaris-system-with-guardrails-suite-mx)

## Additional References

- [CISA](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-23-194-010)
- [BD cybersecurity Trust Center](https://www.bd.com/en-us/about-bd/cybersecurity?activetab=2)
