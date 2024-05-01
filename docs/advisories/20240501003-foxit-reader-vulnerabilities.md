# Foxit PDF Reader Vulnerabilities - 20240501003

## Overview

The Foxit PDF Reader has three High vulnerabilities that can lead to memory corruption and result in arbitrary code execution if triggered by a malicious file or website for which the browser plugin is enabled.

## What is vulnerable?

| CVE            | Severity | CVSS | Product(s) Affected        | Summary                                                                                                           | Dated         |
| -------------- | -------- | ---- | -------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------- |
| CVE-2024-25575 | **High** | 8.8  | **versions before** 2024.2 | A type confusion vulnerability vulnerability exists in the way Foxit Reader 2024.1.0.23997 handles a Lock object. | 30 April 2024 |
| CVE-2024-25648 | **High** | 8.8  | **versions before** 2024.2 | A use-after-free vulnerability exists in the way Foxit Reader 2024.1.0.23997 handles a ComboBox widget.           | 30 April 2024 |
| CVE-2024-25938 | **High** | 8.8  | **versions before** 2024.2 | A use-after-free vulnerability exists in the way Foxit Reader 2024.1.0.23997 handles a Barcode widget.            | 30 April 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://www.foxit.com/support/security-bulletins.html

## Additional References

- [CVE-2024-25575](https://nvd.nist.gov/vuln/detail/CVE-2024-25575)
- [CVE-2024-25648](https://nvd.nist.gov/vuln/detail/CVE-2024-25648)
- [CVE-2024-25938](https://nvd.nist.gov/vuln/detail/CVE-2024-25938)
