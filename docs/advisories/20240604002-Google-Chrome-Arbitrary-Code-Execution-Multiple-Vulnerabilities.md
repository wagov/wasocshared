# Google Chrome Arbitrary Code Execution Multiple Vulnerabilities - 20240604002

## Overview

Multiple vulnerabilities have been discovered in Google Chrome, the most severe of which could allow for arbitrary code execution. Successful exploitation of the most severe of these vulnerabilities could allow for arbitrary code execution in the context of the logged on user. Depending on the privileges associated with the user an attacker could then install programs; view, change, or delete data; or create new accounts with full user rights. Users whose accounts are configured to have fewer user rights on the system could be less impacted than those who operate with administrative user rights.

## What is vulnerable?

| CVE                                                             | Severity | CVSS | Product(s) Affected                  |
| --------------------------------------------------------------- | -------- | ---- | ------------------------------------ |
| [CVE-2024-5493](https://nvd.nist.gov/vuln/detail/CVE-2024-5493) <br> [CVE-2024-5494](https://nvd.nist.gov/vuln/detail/CVE-2024-5494)<br> [CVE-2024-5495](https://nvd.nist.gov/vuln/detail/CVE-2024-5495)<br> [CVE-2024-5496](https://nvd.nist.gov/vuln/detail/CVE-2024-5496)<br> [CVE-2024-5497](https://nvd.nist.gov/vuln/detail/CVE-2024-5497)<br> [CVE-2024-5498](https://nvd.nist.gov/vuln/detail/CVE-2024-5498)<br> [CVE-2024-5499](https://nvd.nist.gov/vuln/detail/CVE-2024-5499)| **High** | N/A | versions prior to **125.0.6422.141/.142 for Windows and Mac** <br> versions prior to **125.0.6422.141 for Linux**  |


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-google-chrome-could-allow-for-arbitrary-code-execution_2024-064
- https://chromereleases.googleblog.com/2024/05/stable-channel-update-for-desktop_30.html
