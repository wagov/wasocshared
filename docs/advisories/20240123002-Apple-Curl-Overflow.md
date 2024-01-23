# Apple Curl Overflow added to CISA Known Exploited Catalog - 20240123002

## Overview

Apple have released security advisories relating to several vulnerabilities impacting macOS Monterey, macOS Ventura, iOS, and iPadOS.

## What is the vulnerability?

| CVE                                                                             | Severity     | CVSS |
| ------------------------------------------------------------------------------- | ------------ | ---- |
| [CVE-2023-38039](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38039) | **High**     | 7.5  |
| [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545) | **Critical** | 9.8  |
| [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546) | Low          | 3.7  |
| [CVE-2023-40528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40528) | TBA          | TBA  |
| [CVE-2023-42887](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42887) | TBA          | TBA  |
| [CVE-2023-42888](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42888) | TBA          | TBA  |
| [CVE-2023-42915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42915) | TBA          | TBA  |
| [CVE-2023-42935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42935) | TBA          | TBA  |
| [CVE-2023-42937](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42937) | TBA          | TBA  |
| [CVE-2024-23206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23206) | TBA          | TBA  |
| [CVE-2024-23207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23207) | TBA          | TBA  |
| [CVE-2024-23211](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23211) | TBA          | TBA  |
| [CVE-2024-23212](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23212) | TBA          | TBA  |
| [CVE-2024-23213](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23213) | TBA          | TBA  |
| [CVE-2024-23214](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23214) | TBA          | TBA  |
| [CVE-2024-23222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23222) | TBA          | TBA  |
| [CVE-2024-23224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23224) | TBA          | TBA  |

## What is vulnerable?

| Product(s) Affected                        | Vendor Advisory                                      |
| ------------------------------------------ | ---------------------------------------------------- |
| macOS Monterey before 12.7.3               | [HT214057](https://support.apple.com/en-gb/HT214057) |
| macOS Ventura before 13.6.4                | [HT214058](https://support.apple.com/en-gb/HT214058) |
| iOS before 16.7.5 and iPadOS before 16.7.5 | [HT214063](https://support.apple.com/en-gb/HT214063) |

## What has been observed?

Apple is aware of a report that this issue may have been exploited. CISA added this vulnerability in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md))
