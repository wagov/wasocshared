# Broadcast - Mozilla Firefox Critical Vulnerabilities - 20250724001

## Overview

Multiple vulnerabilities have been discovered in Mozilla. These vulnerabilities could allow attackers to execute arbitrary code, manipulate URL display, bypass navigation security checks, bypass cookie security mechanisms, intercept and obtain sensitive authentication credentials and manipulate WebAssembly execution.

## What is vulnerable?

| Product(s) Affected       | Version(s)                                                                                                                                                           | CVE                                                             | CVSS | Severity     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---- | ------------ |
| Firefox and Thunderbird   | Firefox < 141 <br> Thunderbird < 141                                                                                                                                 | [CVE-2025-8044](https://nvd.nist.gov/vuln/detail/CVE-2025-8044) | 9.8  | **Critical** |
| Firefox and Thunderbird   | Firefox < 141 <br> Thunderbird < 141                                                                                                                                 | [CVE-2025-8043](https://nvd.nist.gov/vuln/detail/CVE-2025-8043) | 9.8  | **Critical** |
| Multiple Mozilla Products | Firefox < 141 <br> Firefox ESR < 140.1 <br> Thunderbird < 141 <br> Thunderbird < 140.1                                                                               | [CVE-2025-8038](https://nvd.nist.gov/vuln/detail/CVE-2025-8038) | 9.8  | **Critical** |
| Multiple Mozilla Products | Firefox < 141 <br> Firefox ESR < 140.1 <br> Thunderbird < 141 <br> Thunderbird < 140.1                                                                               | [CVE-2025-8037](https://nvd.nist.gov/vuln/detail/CVE-2025-8037) | 9.1  | **Critical** |
| Multiple Mozilla Products | Firefox < 141 <br> Firefox ESR < 128.13 <br> Firefox ESR < 140.1 <br> Thunderbird < 141 <br> Thunderbird < 128.13 <br> Thunderbird < 140.1                           | [CVE-2025-8031](https://nvd.nist.gov/vuln/detail/CVE-2025-8031) | 9.8  | **Critical** |
| Multiple Mozilla Products | Firefox < 141 <br> Firefox ESR < 115.26 <br> Firefox ESR < 128.13 <br> Firefox ESR < 140.1 <br> Thunderbird < 141 <br> Thunderbird < 128.13 <br> Thunderbird < 140.1 | [CVE-2025-8028](https://nvd.nist.gov/vuln/detail/CVE-2025-8028) | 9.8  | **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected products within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Mozilla: <https://www.mozilla.org/en-US/security/advisories/mfsa2025-56/>
