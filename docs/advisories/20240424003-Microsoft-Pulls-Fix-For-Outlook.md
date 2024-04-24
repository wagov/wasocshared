# Microsoft pulls fix for Outlook bug behind ICS security alerts - 20240424003

## Overview

Microsoft has rolled back a fix for a known Outlook issue that was causing incorrect security alerts when opening ICS calendar files after installing the December Outlook Desktop security updates. Affected Microsoft 365 users are seeing unexpected warnings that "Microsoft Office has identified a potential security concern" and that "This location may be unsafe" when double-clicking ICS files saved on their devices.

## What is vulnerable?

| CVE                                                               | Severity   | CVSS |
| ----------------------------------------------------------------- | ---------- | ---- |
| [CVE-2023-35636](https://nvd.nist.gov/vuln/detail/CVE-2023-35636) | **Medium** | 6.5  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Microsoft](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-35636)

## Additional References

- [Bleeping Computer: Microsoft pulls fix for Outlook bug behind ICS security alerts](https://www.bleepingcomputer.com/news/microsoft/microsoft-pulls-fix-for-outlook-bug-unexpected-ICS-warnings-after-December-security-updates/)
