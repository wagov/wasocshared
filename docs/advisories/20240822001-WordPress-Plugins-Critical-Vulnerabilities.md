# WordPress Plugins Critical Vulnerabilities- 20240822001

## Overview

The WA SOC has been made aware of vulnerabilities present within versions of the GiveWP – Donation Plugin and Fundraising Platform plugin for WordPress. This allows unauthenticated attackers to inject a PHP Object. The additional presence of a POP chain allows attackers to execute code remotely, and to delete arbitrary files. 

## What is vulnerable?

| Product(s) Affected | Version(s)      | CVE                                                                                                                                  | CVSS         | Severity               |
| ------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ---------------------- |
|  Plugin “GiveWP – Donation Plugin and Fundraising Platform”  | < 3.14.2 | [CVE-2024-5932](https://nvd.nist.gov/vuln/detail/cve-2024-5932)                                    | 10           | Critical               |
| Plugin “LiteSpeed Cache” | < 6.4 | [CVE-2024-28000](https://nvd.nist.gov/vuln/detail/CVE-2024-28000)                                                                         | 9.8          | Critical               |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- Wordfence Intelligence article: <https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/give/givewp-donation-plugin-and-fundraising-platform-3141-unauthenticated-php-object-injection-to-remote-code-execution>

## Additional References

- CyberSecurity News: <https://securityonline.info/cve-2024-5932-cvss-10-critical-rce-vulnerability-impacts-100k-wordpress-sites/>
- PatchStack: <https://patchstack.com/database/vulnerability/litespeed-cache/wordpress-litespeed-cache-plugin-6-3-0-1-unauthenticated-privilege-escalation-vulnerability?_s_id=cve>
