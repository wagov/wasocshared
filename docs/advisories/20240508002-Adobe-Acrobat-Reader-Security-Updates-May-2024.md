# Adobe Acrobat Updates May 2024 For Windows And MacOS - 20240508002

## Overview

Adobe has released security update for Adobe Acrobat and Reader for Windows and macOS. This update addresses critical and important vulnerabilities. Successful exploitation could lead to arbitrary code execution, application denial-of-service, and memory leak.

## What is vulnerable?

| CVE                                                               | Severity   | CVSS | Product(s) Affected                                           | Summary                                                                                                                                                                                                                                                                           | Dated       |
| ----------------------------------------------------------------- | ---------- | ---- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [CVE-2024-30304](https://nvd.nist.gov/vuln/detail/CVE-2024-30304) | **High**   | 7.8  | **versions before 20.005.30539, 23.008.20470**                | Affected by a Use After Free vulnerability that could result in arbitrary code execution in the context of the current user. Exploitation of this issue requires user interaction in that a victim must open a malicious file.                                                    | 7 May, 2024 |
| [CVE-2024-30302](https://nvd.nist.gov/vuln/detail/CVE-2024-30302) | **Medium** | 5.5  | Acrobat Reader **versions before 20.005.30539, 23.008.20470** | Affected by a Use After Free vulnerability that could lead to disclosure of sensitive memory. An attacker could leverage this vulnerability to bypass mitigations such as ASLR. Exploitation of this issue requires user interaction in that a victim must open a malicious file. | 7 May, 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Adobe Security Bulletin](https://helpx.adobe.com/au/security/products/acrobat/apsb24-07.html)

## Additional References

- [Zero Day Initiative ZDI-24-426](https://www.zerodayinitiative.com/advisories/ZDI-24-426/)
- [Zero Day Initiaive ZDI-24-422](https://www.zerodayinitiative.com/advisories/ZDI-24-422/)
