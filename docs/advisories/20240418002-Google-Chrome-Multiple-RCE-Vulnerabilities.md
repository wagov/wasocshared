# Google Chrome Multiple RCE Vulnerabilities - 20240418002

## Overview

Multiple vulnerabilities have been discovered in Google Chrome, which could allow for remote code execution. Successful exploitation of these vulnerabilities could allow for remote code execution in the context of the logged on user.

## What is vulnerable?

| CVE                                                             | Severity     | CVSS | Product(s) Affected                                                                       | 
| --------------------------------------------------------------- | ------------ | ---- | ----------------------------------------------------------------------------------------- | 
| [CVE-2024-1673](https://nvd.nist.gov/vuln/detail/CVE-2024-1673) | **Critical** | 9.8  | **Chrome versions prior to 124.0.6367.60/.61 for Wins & Mac and 124.0.6367.60 for Linux** |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe  (refer [Patch Management](../guidelines/patch-management.md)):

- [Chrome Releases](https://chromereleases.googleblog.com/2024/04/stable-channel-update-for-desktop_16.html)

## Additional References

- [Multiple Vulnerabilities in Google Chrome Could Allow for Remote Code Execution](https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-google-chrome-could-allow-for-remote-code-execution_2024-040)
