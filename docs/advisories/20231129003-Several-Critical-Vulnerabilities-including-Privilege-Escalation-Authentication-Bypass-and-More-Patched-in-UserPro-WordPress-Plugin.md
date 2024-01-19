# Several Critical Vulnerabilities including Privilege Escalation, Authentication Bypass, and More Patched in UserPro WordPress Plugin - 20231129003

## Overview

The WA SOC has observed a vulnerability in UserPro plugin for WordPress. When exploited, it would allow a threat actor unauthorised access.

## What is the vulnerability?

[**CVE-2023-2448**](https://nvd.nist.gov/vuln/detail/CVE-2023-2448) - CVSS v3 Base Score: ***6.5***

The UserPro plugin for WordPress is vulnerable to unauthorized access of data due to a missing capability check on the 'userpro_shortcode_template' function in versions up to, and including, 5.1.4. This makes it possible for unauthenticated attackers to arbitrary shortcode execution. An attacker can leverage CVE-2023-2446 to get sensitive information via shortcode.

[**CVE-2023-2446**](https://nvd.nist.gov/vuln/detail/CVE-2023-2446) - CVSS v3 Base Score: ***6.5***

The UserPro plugin for WordPress is vulnerable to sensitive information disclosure via the 'userpro' shortcode in versions up to, and including 5.1.1. This is due to insufficient restriction on sensitive user meta values that can be called via that shortcode. This makes it possible for authenticated attackers, with subscriber-level permissions, and above to retrieve sensitive user meta that can be used to gain access to a high privileged user account.

## What is vulnerable?

The vulnerability affects the following products:

- The 'userpro' shortcode in versions up to, and including 5.1.1
- the 'userpro_shortcode_template' function in versions up to, and including, 5.1.4

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- Update to version 5.1.5 (or the latest) of the plugin.

## Additional References

- [Several Critical Vulnerabilities including Privilege Escalation, Authentication Bypass, and More Patched in UserPro WordPress Plugin (wordfence.com)](https://www.wordfence.com/blog/2023/11/several-critical-vulnerabilities-including-privilege-escalation-authentication-bypass-and-more-patched-in-userpro-wordpress-plugin/)
