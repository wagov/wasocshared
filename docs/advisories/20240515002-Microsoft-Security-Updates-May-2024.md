# Microsoft Releases May 2024 Security Updates - 20240515002

## Overview

Microsoft has released security updates to address vulnerabilities in multiple products. A Cyber threat actor could leverage some of these vulnerabilities to exploit the affected system.

## What is vulnerable?

This release consists of the following 60 Microsoft CVEs:

- [May 2024 Security Updates](https://msrc.microsoft.com/update-guide/releaseNote/2024-May)

| Product(s) Affected  | CVE | Severity  | CVSS |Exploited| Dated|
| ----------- | --- | ------|----- | ---- |--|
| Microsoft DWM Core Library Privilege Escalation Vulnerability | [CVE-2024-30051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-30051) | **High**| 7.8 |Yes|14 May, 2024|
| Microsoft Windows MSHTML Platform Security Feature Bypass Vulnerability | [CVE-2024-30040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-30040) | **High**| 8.8 |Yes|14 May, 2024|

## What has been observed?

CISA added some of the above vulnerability in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks* (refer [Patch Management](../guidelines/patch-management.md)).

## Additional References

- [CISA - Microsoft Releases May 2024 Security Updates
    ](https://www.cisa.gov/news-events/alerts/2024/05/14/microsoft-releases-may-2024-security-updates)
- [QakBot attacks with Windows zero-day](https://securelist.com/cve-2024-30051/112618/)
