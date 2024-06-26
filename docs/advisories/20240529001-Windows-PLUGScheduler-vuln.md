# Windows 10 PLUGScheduler Elevation of Privilege Vulnerability - 20240529001

## Overview

By manipulating the PLUGScheduler process on vulnerbale Windows 10 versions, attackers can achieve arbitrary file write permissions as SYSTEM, effectively granting them complete control over the operating system. Microsoft is encouraging all customers to apply the patch as soon as possible.

## What is vulnerable?

| CVE                                                               | Severity | CVSS | Product(s) Affected                  | Summary                                                                     | Dated      |
| ----------------------------------------------------------------- | -------- | ---- | ------------------------------------ | --------------------------------------------------------------------------- | ---------- |
| [CVE-2024-26238](https://nvd.nist.gov/vuln/detail/CVE-2024-26238) | **High** | 7.8  | Windows 10 version 2004 through 20H2 | Microsoft PLUGScheduler Scheduled Task Elevation of Privilege Vulnerability | 14/05/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of one month (refer [Patch Management](../guidelines/patch-management.md)):

- [Microsoft PLUGScheduler Scheduled Task Elevation of Privilege Vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-26238)

## Additional References

- [SYNACTIV - WINDOWS 10 PLUGSCHEDULER ELEVATION OF PRIVILEGE](https://www.synacktiv.com/advisories/windows-10-plugscheduler-elevation-of-privilege)
