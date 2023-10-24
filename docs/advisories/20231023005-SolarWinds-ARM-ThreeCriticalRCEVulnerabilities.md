# Three critical remote code execution vulnerabilities in the SolarWinds Access Rights Manager (ARM) product - 20231023005

## Overview

SolarWinds has released an advisory for eight vulnerabilities, including three critical remote code execution vulnerabilities in the SolarWinds Access Rights Manager (ARM) product that remote attackers could use to run code with SYSTEM privileges.

## What is the vulnerability?

**Three Critical Vulnerabilities:**  

[**CVE-2023-35182**](https://nvd.nist.gov/vuln/detail/CVE-2023-35182) - CVSS v3 Base Score: ***8.8***
 - Remote unauthenticated attackers can execute arbitrary code in the context of SYSTEM due to the deserialization of untrusted data in the ‘createGlobalServerChannelInternal’ method


[**CVE-2023-35185**](https://nvd.nist.gov/vuln/detail/CVE-2023-35185) - CVSS v3 Base Score: ***8.8***
- Remote unauthenticated attackers can execute arbitrary code in the context of SYSTEM due to a lack of validation of user-supplied paths in the ‘OpenFile’ method


[**CVE-2023-35187**](https://nvd.nist.gov/vuln/detail/CVE-2023-35187) - CVSS v3 Base Score: ***8.8***
- Remote unauthenticated attackers can execute arbitrary code in the context of SYSTEM without authentication due to lack of validation of user-supplied paths in the ‘OpenClientUpdateFile’ method


**Other Vulnerabilities:**  

[**CVE-2023-35180**](https://nvd.nist.gov/vuln/detail/CVE-2023-35180) - CVSS v3 Base Score: ***8.0***

- The SolarWinds Access Rights Manager was susceptible to Remote Code Execution Vulnerability. This vulnerability allows authenticated users to abuse SolarWinds ARM API.

[**CVE-2023-35181**](https://nvd.nist.gov/vuln/detail/CVE-2023-35181) - CVSS v3 Base Score: ***7.8***

- The SolarWinds Access Rights Manager was susceptible to Privilege Escalation Vulnerability. This vulnerability allows users to abuse incorrect folder permission resulting in Privilege Escalation.

[**CVE-2023-35183**](https://nvd.nist.gov/vuln/detail/CVE-2023-35183) - CVSS v3 Base Score: ***7.8***

- The SolarWinds Access Rights Manager was susceptible to Privilege Escalation Vulnerability. This vulnerability allows authenticated users to abuse local resources to Privilege Escalation.


[**CVE-2023-35184**](https://nvd.nist.gov/vuln/detail/CVE-2023-35184) - CVSS v3 Base Score: ***8.8***

- The SolarWinds Access Rights Manager was susceptible to Remote Code Execution Vulnerability. This vulnerability allows an unauthenticated user to abuse a SolarWinds service resulting in a remote code execution.

[**CVE-2023-35186**](https://nvd.nist.gov/vuln/detail/CVE-2023-35186) - CVSS v3 Base Score: ***8.0***

- The SolarWinds Access Rights Manager was susceptible to Remote Code Execution Vulnerability. This vulnerability allows an authenticated user to abuse SolarWinds service resulting in remote code execution.


## What is vulnerable?

The vulnerability affects the following products:

- Access Rights Manager 2023.2

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [ARM 2023.2.1 Release Notes (solarwinds.com)](https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2023-2-1_release_notes.htm)

## Additional References

- [Critical RCE flaws found in SolarWinds access audit solution (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/critical-rce-flaws-found-in-solarwinds-access-audit-solution/)
- [ARM 2023.2.1 Release Notes (solarwinds.com)](https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2023-2-1_release_notes.htm)
