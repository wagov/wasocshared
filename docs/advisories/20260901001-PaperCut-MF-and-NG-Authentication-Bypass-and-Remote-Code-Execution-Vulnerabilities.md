# PaperCut MF and NG Authentication Bypass and Remote Code Execution Vulnerabilities - 20260901001

## Overview

Critical vulnerabilities affecting PaperCut NG/MF are being actively exploited. Successful exploitation may allow unauthenticated attackers to modify system configurations and achieve remote code execution. Organisations using PaperCut NG/MF should apply the latest security patches immediately and restrict access to PaperCut management interfaces to trusted networks only.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| PaperCut NG and PaperCut MF     | All versions    | [CVE-2026-81578](https://nvd.nist.gov/vuln/detail/CVE-2026-81578)   <br> [CVE-2026-82078](https://nvd.nist.gov/vuln/detail/CVE-2026-82078)                                                                    | 8.8   <br> 9.4      | High <br> **Critical**|


## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- PaperCut: <https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/>

## Additional References

- GitHub: <https:​/​/​github.​com/​advisories/​GHSA-​mjg5-​wj9r-​9mfx> <br>
- GitHub: <https:​/​/​github.​com/​advisories/​GHSA-​44wc-​j6f2-​7fjr> 
