# Mozilla Critical Vulnerabilities - 20250714001

## Overview

Multiple vulnerabilities have been discovered in Mozilla, the most severe of which could allow for arbitrary code execution. 

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Firefox     | Version < 140    | [CVE-2025-6427](https://nvd.nist.gov/vuln/detail/CVE-2025-6427)                                                                        | 9.1          | **Critical**                                   |
| Firefox     | Version < 140    | [CVE-2025-6433](https://nvd.nist.gov/vuln/detail/CVE-2025-6433)                                                                        | 9.8          | **Critical**                                   |
| Multiple Mozilla Products     | Firefox < 140 <br> Firefox ESR < 115.25 <br> Firefox ESR < 128.12 <br> Thunderbird < 140 <br> Thunderbird < 128.12    | [CVE-2025-6424](https://nvd.nist.gov/vuln/detail/CVE-2025-6424)                                                                        | 9.8         | **Critical**                                   |


## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla: <https://www.mozilla.org/en-US/security/advisories/mfsa2025-54/>

## Additional References

- Tenable: <https://www.tenable.com/cve/CVE-2025-6427>
- Tenable: <https://www.tenable.com/cve/CVE-2025-6433>
- Tenable: <https://www.tenable.com/cve/CVE-2025-6424>
- CIS Advisories: <https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-mozilla-thunderbird-could-allow-for-arbitrary-code-execution_2025-064>

