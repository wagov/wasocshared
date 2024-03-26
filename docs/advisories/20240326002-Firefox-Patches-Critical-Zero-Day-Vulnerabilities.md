# Firefox Patches Critical Zero-Day Vulnerabilities - 20240326002

## Overview

Mozilla has released security updates for Firefox and Firefox ESR in response to 2 critical zero-day vulnerabilities. The vulnerabilities were exploited during the Pwn2Own Vancouver 2024 hacking competition and can lead to remote code execution. This could in turn compromise the sensitive data and systems.

## What is vulnerable?

| CVE || | Product(s) Affected                 | Dated          |
| --------------------------------------------------------------- | ---------- | ---- | ----------------------------------- | -------------- |
| [CVE-2024-29943](https://cve.org/CVERecord?id=CVE-2024-29943), [CVE-2024-29944](https://www.cve.org/CVERecord?id=CVE-2024-29944) |  |  | **Firefox 124.0.1** | March 22, 2024 |
| [CVE-2024-29944](https://www.cve.org/CVERecord?id=CVE-2024-29944) |  |  | **Firefox ESR 115.9.1** | March 22, 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla’s advisory [mozilla.org](https://www.mozilla.org/security/advisories/mfsa2024-15/)
