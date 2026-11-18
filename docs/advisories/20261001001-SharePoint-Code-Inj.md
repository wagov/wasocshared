# SharePoint Code Injection Exploited Vulnerability - 20261001001 

## Overview

Microsoft has released a security advisory relating to a high-severity vulnerability in SharePoint Server where an authenticated attacker with low-level access to an affected server could send a specially crafted request to execute code on the server via a code injection exploit. User interaction is not required.

Patches addressing the vulnerability have been released and Microsoft is encouraging all affected users to apply the patches.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                       | CVSS          | Severity                                                        |
| ------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------- |
| Microsoft SharePoint Enterprise Server 2016</br>Microsoft SharePoint Server 2019</br>Microsoft SharePoint Server Subscription Edition      | from 16.0.0 before 16.0.5565.1001</br>from 16.0.0 before 16.0.10417.20198</br>from 16.0.0 before 16.0.19725.20522   | [CVE-2026-65660](https://nvd.nist.gov/vuln/detail/CVE-2026-65660)                                                                         | 8.8           | High                              |

## What has been observed?

CISA has added one or more of the mentioned items to their [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft: <https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-65660>