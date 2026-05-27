# Multiple VLC Vulnerabilities - 20260527001

## Overview

The WASOC has been made aware of multiple vulnerabilities affecting VLC Media Player (VLC). Older versions of VLC have been in embedded into ICS devices, which could lead to exploitation.

Successful exploitation may allow attackers to cause denial of service, memory corruption, or arbitrary code execution via specially crafted media files or streams.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
| ------------------- | ---------- | ---- | ----- | -------- |
| ABB Ability Camera Connect | 1.5.0.14 and earlier | [CVE-2023-47359](https://nvd.nist.gov/vuln/detail/CVE-2023-47359) | 9.8 | **Critical** |
| ABB Ability Camera Connect | 1.5.0.14 and earlier | [CVE-2019-13962](https://nvd.nist.gov/vuln/detail/CVE-2019-13962) | 9.8 | **Critical** |
| ABB Ability Camera Connect | 1.5.0.14 and earlier | [CVE-2017-10699](https://nvd.nist.gov/vuln/detail/CVE-2017-10699) | 9.8 | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- CISA: <https://www.cisa.gov/news-events/ics-advisories/icsa-26-146-05>

## Additional References

- NIST: <https://nvd.nist.gov/vuln/detail/CVE-2023-47359>
- NIST : <https://nvd.nist.gov/vuln/detail/CVE-2019-13962>
- NIST : <https://nvd.nist.gov/vuln/detail/CVE-2017-10699L>
