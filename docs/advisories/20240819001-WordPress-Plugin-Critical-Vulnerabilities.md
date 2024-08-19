# WordPress Plugin Critical Vulnerabilities - 20240819001

## Overview

The WA SOC has been made aware of critical unauthorized access and deletion of data vulnerability affecting WordPress InPost Plugins.

Wordfence Intelligence have posted an advisory relating to a vulnerability caused by plugins `InPost for WooCommerce` and `InPost PL` for WordPress allowing unauthorized access and deletion of data due to a missing capability check on the 'parse_request' function. This makes it possible for unauthenticated attackers to read and delete arbitrary files on Windows servers. On Linux servers, only files within the WordPress install will be deleted, but all files can be read.

## What is vulnerable?

| Product(s) Affected |  CVE   | CVSS          | Severity          |
| ------------------- |  ----------------- | ------------- | -------------------- |
| - Plugin “InPost PL” versions < 1.4.5 </br> - Plugin “InPost for WooCommerce” versions <= 1.4.0 (unpatched at time of writing)  | [CVE-2024-6500](https://nvd.nist.gov/vuln/detail/CVE-2024-6500) | 10 | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Wordfence Intelligence: <https://www.wordfence.com/threat-intel/vulnerabilities/detail/inpost-for-woocommerce-140-and-inpost-pl-144-missing-authorization-to-unauthenticated-arbitrary-file-read-and-delete>

## Additional References

- CyberSecurity News: <https://securityonline.info/10000-wordpress-sites-at-risk-critical-file-deletion-flaw-found-in-inpost-plugins/>
