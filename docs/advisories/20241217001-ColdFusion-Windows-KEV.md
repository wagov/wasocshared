# Microsoft and Adobe Known Exploited Vulnerabilities - 20241217001

## Overview

Microsoft and Adobe have released critical security advisories relating to vulnerabilities impacting Windows and ColdFusion.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                       | CVSS          | Severity                                                        |
| ------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------- |
| Windows      | [Vendor Supplied Version List](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-35250)    | [CVE-2024-35250](https://nvd.nist.gov/vuln/detail/CVE-2024-35250)                                                                         | 7.8           | High                                  |
| ColdFusion      | ColdFusion 2023 <= Update 6 </br> ColdFusion <= Update 12 | [CVE-2024-20767](https://nvd.nist.gov/vuln/detail/CVE-2024-20767) | 7.4 | High|

## What has been observed?

CISA added this vulnerability in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe recommended in [Patch Management](../guidelines/patch-management.md):

- Microsoft: <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-35250>
- Adobe: <https://helpx.adobe.com/security/products/coldfusion/apsb24-14.html>
