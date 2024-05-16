# Cacti Command Injection and XSS Vulnerabilities - 20240516004

## Overview

Cacti, an operational monitoring and fault management framework, has recently released a crucial security update to address two significant vulnerabilities that could leave systems exposed to malicious attacks.

## What is vulnerable?

| CVE                                                               | Severity     | CVSS | Product(s) Affected           | Summary | Dated |
| ----------------------------------------------------------------- | ------------ | ---- | ----------------------------- | ------- | ----- |
| [CVE-2024-29895](https://nvd.nist.gov/vuln/detail/CVE-2024-29895) | **Critical** | 10   | **versions before 1.3.x DEV** |         |       |
| [CVE-2024-30268](https://nvd.nist.gov/vuln/detail/CVE-2024-30268) | **Medium**   | 6.1  | **versions before 1.3.x DEV** |         |       |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- https://github.com/Cacti/cacti/security/advisories/GHSA-cr28-x256-xf5m
- https://github.com/Cacti/cacti/commit/99633903cad0de5ace636249de16f77e57a3c8fc
- https://github.com/Cacti/cacti/commit/53e8014d1f082034e0646edc6286cde3800c683d
- https://github.com/Cacti/cacti/blob/501712998589763d411a68d35e3cda98fd9cfd18/cmd_realtime.php#L119
- https://github.com/Cacti/cacti/security/advisories/GHSA-9m3v-whmr-pc2q
- https://github.com/Cacti/cacti/commit/a38b9046e9772612fda847b46308f9391a49891e
- https://github.com/Cacti/cacti/blob/08497b8bcc6a6037f7b1aae303ad8f7dfaf7364e/settings.php#L66
