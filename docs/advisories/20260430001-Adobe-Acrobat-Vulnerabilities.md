# Adobe Acrobat Vulnerabilities - 20260430001

## Overview

Adobe has released a security update for Adobe Acrobat and Reader for Windows and macOS. This update addresses critical and important vulnerabilities affected by an Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution') vulnerability that could result in arbitrary code execution in the context of the current user. Exploitation of this issue requires user interaction in that a victim must open a malicious file.

## What is vulnerable?

| Product(s) Affected                                 | Version(s)                                                                                                                   | CVE                                                               | CVSS | Severity |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| Acrobat DC <br> Acrobat Reader DC <br> Acrobat 2024 | 26.001.21411 and earlier <br> 26.001.21411 and earlier <br/> Windows 24.001.30362 and earlier , Mac 24.001.30360 and earlier | [CVE-2026-34622](https://nvd.nist.gov/vuln/detail/CVE-2026-34622) | 8.6  | High     |

## What has been observed?

The WASOC has observed claims of exploitation in the wild.
The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Adobe Security Bulletin: <https://helpx.adobe.com/security/products/acrobat/apsb26-44.html>

## Additional References

- Starlabs Article: <https://starlabs.sg/blog/2026/04-three-bugs-walk-into-a-pdf-prototype-pollution-served-cold/>
