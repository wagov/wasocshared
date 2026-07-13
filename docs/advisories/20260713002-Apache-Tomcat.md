# Apache Tomcat - 20260713002

## Overview

WASOC has become aware of a vulnerability in Apache Tomcat which when exploited could lead to a Remote Code Execution and/or Information Disclosure and/or malicious content added to uploaded files via write enabled Default Servlet.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                      | CVSS         | Severity             |
| ------------------- | ---------- | ---------------------------------------- | ------------ | -------------------- |
| Apache Tomcat      | from 11.0.0-M1 through 11.0.2, <br> from 10.1.0-M1 through 10.1.34, <br> from 9.0.0.M1 through 9.0.98 <br> EOL versions: <br> from 8.5.0 through 8.5.100     | [CVE-2025-24813](https://nvd.nist.gov/vuln/detail/CVE-2025-24813)  | 9.8  | **Critical**  |


## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Apache: <https://lists.apache.org/thread/j5fkjv2k477os90nczf2v9l61fb0kkgq>


