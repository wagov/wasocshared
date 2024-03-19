# Directory Traversal PoC in FileCatalyst Workflow - 20240319001

## Overview

A proof of concept (PoC) has been released for a vulnerability where the 'ftpservlet' of the FileCatalyst Workflow Web Portal may allow files to be uploaded outside of the intended 'uploadtemp' directory with a POST request. In situations where a file is successfully uploaded to a web portal's DocumentRoot, specially crafted JSP files could be used to execute code, including web shells.

## What is vulnerable?

| CVE                                                               | Severity | CVSS    | Product(s) Affected                                     | Summary      |
| ----------------------------------------------------------------- | -------- | ------- | ------------------------------------------------------- | ------------ |
| [CVE-2024-25153](https://nvd.nist.gov/vuln/detail/CVE-2024-25153) | Critical | **9.8** | Fortra FileCatalyst Workflow 5.x before 5.1.6 Build 114 | **Critical** |

## What has been observed?

The vulnerability was reported on August 9, 2023, and addressed two days later in FileCatalyst Workflow version 5.1.6 Build 114 without a CVE identifier however Fortra published the CVE on 03/13/2024. There has since been a proof of concept released by security researchers.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- [Fortra - FI-2024-002 - Directory Traversal in FileCatalyst Workflow](https://www.fortra.com/security/advisory/FI-2024-002)

## Additional References

- [PoC - CVE-2024-25153: Remote Code Execution in Fortra FileCatalyst](https://labs.nettitude.com/blog/cve-2024-25153-remote-code-execution-in-fortra-filecatalyst/)
