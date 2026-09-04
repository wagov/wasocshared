# PaperCut MF and NG Remote Code Execution - 20260901001

## Overview

Papercut have published a security advisory relating to critical vulnerabilities affecting their NG and MF products. Successful exploitation may allow unauthenticated attackers to modify system configurations and achieve remote code execution. Organisations using PaperCut NG/MF should apply the latest security patches immediately and restrict access to PaperCut management interfaces to trusted networks only.

At the time of writing, PaperCut have released emergency patches and has advised that it is continuing to work towards an official release addressing these vulnerabilities.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
| ------------------- | ---------- | --- | ---- | -------- |
| PaperCut NG and PaperCut MF | All versions | [CVE-2026-82078](https://nvd.nist.gov/vuln/detail/CVE-2026-82078) <br> [CVE-2026-81578](https://nvd.nist.gov/vuln/detail/CVE-2026-81578) | 9.4 <br> 8.8 | **Critical** <br> High |


## What has been observed?

CISA has added these vulnerabilities into their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalogue.
The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

Administrators are encouraged to regularly review the vendor's security advisory page for the latest updates, patches and remediation guidance as PaperCut continues to investigate and respond to these vulnerabilities.
The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- PaperCut: <https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/>

## Additional References

- GitHub: <https:​/​/​github.​com/​advisories/​GHSA-​mjg5-​wj9r-​9mfx>
- GitHub: <https:​/​/​github.​com/​advisories/​GHSA-​44wc-​j6f2-​7fjr>
