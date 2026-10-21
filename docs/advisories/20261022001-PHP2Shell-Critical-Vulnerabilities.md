# PHP Critical Vulnerabilities named PHP2Shell  - 20261022001

## Overview

The WASOC has observed new updates published by PHP addressing critical vulnerabilities affecting the core PHP language runtime, collectively known as "PHP2Shell". Successful exploitation can expose applications to unauthenticated remote code execution and memory disclosure.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
| ------------------- | ---------- | --- | ---- | -------- |
| PHP | - All versions prior to 8.2.35 <br> - 8.3.x	prior to 8.3.36 <br> - 8.4.x prior to 8.4.27 <br> - 8.5.x	prior to 8.5.12 | [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) </br> [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) | 9.8 </br> 9.8 | **Critical** </br> **Critical** |

## What has been observed?

PHP is aware of active exploitation in the wild for one or more of the mentioned items.
The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- PHP Github article: <https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w>

### Additional Resources

- Wiz article: <https://www.wiz.io/blog/php2shell-php-rce>