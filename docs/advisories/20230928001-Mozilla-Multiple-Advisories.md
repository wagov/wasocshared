# Mozilla Releases Advisories for Multiple Products - 20230928001

## Overview

Mozilla have released 3 advisories regarding high vulnerabilities across multiple products. These vulnerabilities can be used to gather sensitive data from sites in other windows or inject data or code into those sites, requiring no more than normal browsing actions.

## What is the vulnerability?

- [**CVE-2023-5168**](https://nvd.nist.gov/vuln/detail/CVE-2023-5168) - CVSS v3 Base Score: ***TBA***: A compromised content process could have provided malicious data to `FilterNodeD2D1` resulting in an out-of-bounds write, leading to a potentially exploitable crash in a privileged process. This vulnerability affects Firefox < 118, Firefox ESR < 115.3, and Thunderbird < 115.3.
- [**CVE-2023-5169**](https://nvd.nist.gov/vuln/detail/CVE-2023-5169) - CVSS v3 Base Score: ***TBA***: A compromised content process could have provided malicious data in a `PathRecording` resulting in an out-of-bounds write, leading to a potentially exploitable crash in a privileged process. This vulnerability affects Firefox < 118, Firefox ESR < 115.3, and Thunderbird < 115.3.
- [**CVE-2023-5170**](https://nvd.nist.gov/vuln/detail/CVE-2023-5170) - CVSS v3 Base Score: ***TBA***: In canvas rendering, a compromised content process could have caused a surface to change unexpectedly, leading to a memory leak of a privileged process. This memory leak could be used to effect a sandbox escape if the correct data was leaked. This vulnerability affects Firefox < 118.
- [**CVE-2023-5171**](https://nvd.nist.gov/vuln/detail/CVE-2023-5171) - CVSS v3 Base Score: ***TBA***: During Ion compilation, a Garbage Collection could have resulted in a use-after-free condition, allowing an attacker to write two NUL bytes, and cause a potentially exploitable crash. This vulnerability affects Firefox < 118, Firefox ESR < 115.3, and Thunderbird < 115.3.
- [**CVE-2023-5172**](https://nvd.nist.gov/vuln/detail/CVE-2023-5172) - CVSS v3 Base Score: ***TBA***: A hashtable in the Ion Engine could have been mutated while there was a live interior reference, leading to a potential use-after-free and exploitable crash. This vulnerability affects Firefox < 118.
- [**CVE-2023-5173**](https://nvd.nist.gov/vuln/detail/CVE-2023-5173) - CVSS v3 Base Score: ***TBA***: In a non-standard configuration of Firefox, an integer overflow could have occurred based on network traffic (possibly under influence of a local unprivileged webpage), leading to an out-of-bounds write to privileged process memory. *This bug only affects Firefox if a non-standard preference allowing non-HTTPS Alternate Services (`network.http.altsvc.oe`) is enabled.* This vulnerability affects Firefox < 118.
- [**CVE-2023-5174**](https://nvd.nist.gov/vuln/detail/CVE-2023-5174) - CVSS v3 Base Score: ***TBA***: If Windows failed to duplicate a handle during process creation, the sandbox code may have inadvertently freed a pointer twice, resulting in a use-after-free and a potentially exploitable crash. *This bug only affects Firefox on Windows when run in non-standard configurations (such as using `runas`). Other operating systems are unaffected.* This vulnerability affects Firefox < 118, Firefox ESR < 115.3, and Thunderbird < 115.3.
- [**CVE-2023-5175**](https://nvd.nist.gov/vuln/detail/CVE-2023-5175) - CVSS v3 Base Score: ***TBA***: During process shutdown, it was possible that an `ImageBitmap` was created that would later be used after being freed from a different codepath, leading to a potentially exploitable crash. This vulnerability affects Firefox < 118.
- [**CVE-2023-5176**](https://nvd.nist.gov/vuln/detail/CVE-2023-5176) - CVSS v3 Base Score: ***TBA***s: Memory safety bugs present in Firefox 117, Firefox ESR 115.2, and Thunderbird 115.2. Some of these bugs showed evidence of memory corruption and we presume that with enough effort some of these could have been exploited to run arbitrary code. This vulnerability affects Firefox < 118, Firefox ESR < 115.3, and Thunderbird < 115.3.


## What is vulnerable?

The vulnerability affects the following products:

- Firefox ***versions before 118***
- Firefox ESR ***versions before 115.3***
- Thunderbird ***versions before 115.3***

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Firefox 118](https://www.mozilla.org/en-US/security/advisories/mfsa2023-41/)
- [Firefox ESR 115.3](https://www.mozilla.org/en-US/security/advisories/mfsa2023-42/)
- [Thunderbird 115.3](https://www.mozilla.org/en-US/security/advisories/mfsa2023-43/)
