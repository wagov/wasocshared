# Apache Struts 2 Critical RCE Vulnerability - 20231213001

## Overview

A critical vulnerability in Apache Struts 2 can be exploited by an attacker to manipulate file upload parameters to enable path traversal and may lead to uploading a malicious file which can be used to perform Remote Code Execution.

Apache is urging Struts 2 developers and users to immediately upgrade to version 2.5.33, or Struts 6.3.0.2 or greater.

## What is the vulnerability?

[**CVE-2023-50164**](https://nvd.nist.gov/vuln/detail/CVE-2023-50164) - CVSS v3 Base Score: ***9.8***

## What is vulnerable?

The vulnerability affects the following products:

- Apache Struts 2 versions:
    - Struts 2.0.0 - 2.3.37
    - Struts 2.5.0 - 2.5.32
    - Struts 6.0.0 - 6.3.0

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- [Apache Struts 2 Security Bulletin](https://cwiki.apache.org/confluence/display/WW/S2-066)
- [Apache Warns of Critical Vulnerability in Struts 2](https://www.infosecurity-magazine.com/news/apache-warns-critical/)
