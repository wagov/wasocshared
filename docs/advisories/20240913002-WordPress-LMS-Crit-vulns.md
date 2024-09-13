# WordPress Plugin Critical Update - 20240913002

## Overview

The WA SOC has been made aware of 2 CVSS 10 critical vulnerablities in the "LearnPress – WordPress LMS Plugin".

The vulnerabilities allow an unauthenticated attacker to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database. The plugin author has released an update that patches the vulnerabilties.

## What is vulnerable?

| Product(s) Affected               | Version(s) | CVE                                                             | CVSS | Severity     |
| --------------------------------- | ---------- | --------------------------------------------------------------- | ---- | ------------ |
| LearnPress – WordPress LMS Plugin | \<= 4.2.7  | [CVE-2024-8529](https://nvd.nist.gov/vuln/detail/CVE-2024-8529) | 10.0 | **Critical** |
| LearnPress – WordPress LMS Plugin | \<= 4.2.7  | [CVE-2024-8522](https://nvd.nist.gov/vuln/detail/CVE-2024-8522) | 10.0 | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- https://wordpress.org/plugins/learnpress/

## Additional References

- Wordfence: [LearnPress – WordPress LMS Plugin \<= 4.2.7 - Unauthenticated SQL Injection via 'c_only_fields'](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/learnpress/learnpress-wordpress-lms-plugin-427-unauthenticated-sql-injection-via-c-only-fields)
- Wordfence: [LearnPress – WordPress LMS Plugin \<= 4.2.7 - Unauthenticated SQL Injection via 'c_fields'](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/learnpress/learnpress-wordpress-lms-plugin-427-unauthenticated-sql-injection-via-c-fields)
