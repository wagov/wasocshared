# Mozilla Patches 2 Firefox Zero-Day Vulnerabilities - 20250520001

## Overview

Mozilla has released security updates to address two critical security flaws in its Firefox browser that could potentially be exploited to access sensitive data or achieve code execution. The vulnerabilities affect standard and Extended Support Release (ESR) versions.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Firefox, Firefox ESR   | All versions < 138.0.4, All ESR versions < 115.23.1, 128.10.1    | [CVE-2025-4918](https://nvd.nist.gov/vuln/detail/CVE-2025-4918) <br> [CVE-2025-4919](https://nvd.nist.gov/vuln/detail/CVE-2025-4919)                                                                    | 7.5  <br> 8.8        | High <br> High                               |


## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla Firefox ESR 128.10.1: <https://www.mozilla.org/en-US/security/advisories/mfsa2025-37/>
- Mozilla Firefox ESR 115.23.1: <https://www.mozilla.org/en-US/security/advisories/mfsa2025-38/>
- Mozilla Firefox 138.0.4: <https://www.mozilla.org/en-US/security/advisories/mfsa2025-36/>

## Additional References

- Firefox Patches 2 Zero-Days Exploited at Pwn2Own Berlin with $100K in Rewards: <https://thehackernews.com/2025/05/firefox-patches-2-zero-days-exploited.html>
