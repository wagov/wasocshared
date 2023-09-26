# Atlassian Addresses Vulnerabilities for Multiple Products - 20230926002

## Overview

Atlassian has released its security bulletin for September 2023 to address vulnerabilities in multiple products. A malicious actor could exploit some of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

- [**CVE-2022-25647**](https://www.cve.org/CVERecord?id=CVE-2022-25647) - CVSS v3 Base Score: ***7.5***: The package com.google.code.gson:gson before 2.8.9 are vulnerable to Deserialization of Untrusted Data via the writeReplace() method in internal classes, which may lead to DoS attacks.

- [**CVE-2023-22512**](https://nvd.nist.gov/vuln/detail/CVE-2023-22512) - CVSS v3 Base Score: ***TBA***: This vulnerability allows an unauthenticated attacker to cause a resource to be unavailable for its intended users by temporarily or indefinitely disrupting services of a vulnerable host (Confluence instance) connected to a network, which has no impact on confidentiality, no impact to integrity, high impact to availability, and requires no user interaction.

- [**CVE-2023-22513**](https://nvd.nist.gov/vuln/detail/CVE-2023-22513) - CVSS v3 Base Score: ***8.8***: This vulnerability allows an authenticated attacker to execute arbitrary code which has high impact to confidentiality, high impact to integrity, high impact to availability, and requires no user interaction.

- [**CVE-2023-28709**](https://nvd.nist.gov/vuln/detail/CVE-2023-28709) - CVSS v3 Base Score: ***7.5***: If non-default HTTP connector settings were used such that the maxParameterCount could be reached using query string parameters and a request was submitted that supplied exactly maxParameterCount parameters in the query string, the limit for uploaded request parts could be bypassed with the potential for a denial of service to occur.

## What is vulnerable?

The vulnerability affects the following products:

- Jira Service Management Server and Data Center
- Confluence Server and Data Center
- Bitbucket Server and Data Center
- Bamboo Server and Data Center

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://confluence.atlassian.com/security/security-bulletin-september-19-2023-1283691616.html>
