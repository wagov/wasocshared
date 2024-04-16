# Node.js Security Patch for Critical Vulnerability - 20240416001

## Overview

Node.js have released security updates for the 18.x, 20.x, 21.x Node.js release lines that addresses a critical vulnerability on Windows.

Due to the improper handling of batch files in child_process.spawn / child_process.spawnSync, a malicious command line argument can inject arbitrary commands and achieve code execution even if the shell option is not enabled.

## What is vulnerable?

| CVE                                                               | Severity     | CVSS | Product(s) Affected                                                            | Summary                                                                                                | Dated                            |
| ----------------------------------------------------------------- | ------------ | ---- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------- |
| [CVE-2024-27980](https://nvd.nist.gov/vuln/detail/CVE-2024-27980) | **Critical** | 9.8  | This vulnerability affects all users in active release lines: 18.x, 20.x, 21.x | A malicious command line argument can inject arbitrary commands and achieve code execution on Windows. | Not yet published as of writing. |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of two weeks (refer [Patch Management](../guidelines/patch-management.md)):

- [Node.js - Wednesday, April 10, 2024 Security Releases](https://nodejs.org/en/blog/vulnerability/april-2024-security-releases-2)

## Additional References

- [Tenable - CVE-2024-27980](https://www.tenable.com/cve/CVE-2024-27980)
