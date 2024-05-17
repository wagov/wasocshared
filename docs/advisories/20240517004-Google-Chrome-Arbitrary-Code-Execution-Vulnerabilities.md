# Google Chrome Arbitrary Code Execution Vulnerabilities - 20240517004

## Overview

Multiple vulnerabilities have been discovered in Google Chrome, the most severe of which could allow for arbitrary code execution. Successful exploitation of the most severe of these vulnerabilities could allow for arbitrary code execution in the context of the logged on user.

## What is vulnerable?

| CVE                                                                                                                                                                                                        | Summary                                                                        | Severity | CVSS | Product(s) Affected                                                                                     | Dated        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------- | ---- | ------------------------------------------------------------------------------------------------------- | ------------ |
| [CVE-2024-4947](https://nvd.nist.gov/vuln/detail/CVE-2024-4947)  <br/>[CVE-2024-4948](https://nvd.nist.gov/vuln/detail/CVE-2024-4948) <br/>[CVE-2024-4949](https://nvd.nist.gov/vuln/detail/CVE-2024-4949) | Type Confusion in V8.<br/> Use after free in Dawn. <br/> Use after free in V8. | **High** | 8.8  | - Chrome prior to 125.0.6422.60/.61 for Windows and Mac <br/> - Chrome prior to 125.0.6422.60 for Linux | 15 May, 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Chrome Releases](https://chromereleases.googleblog.com/2024/05/stable-channel-update-for-desktop_15.html)

## Additional References

- [Cis Security](https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-google-chrome-could-allow-for-arbitrary-code-execution_2024-058)
