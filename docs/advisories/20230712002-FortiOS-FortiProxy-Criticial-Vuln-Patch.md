# FortiOS and FortiProxy Critical Vulnerability Patch Released - 20230712002

## Overview

Fortinet has released security updates for FortiOS and FortiProxy to address a critical vulnerability that a remote attacker could exploit to take control of an affected system.

A stack-based overflow vulnerability [CWE-124] in FortiOS & FortiProxy may allow a remote attacker to execute arbitrary code or commands via crafted packets reaching proxy policies or firewall policies with proxy mode alongside SSL deep packet inspection.

## What is the vulnerability?

[**CVE-2023-33308**](https://www.fortiguard.com/psirt/FG-IR-23-183) - CVSS v3 Base Score: ***9.8***

- As of writing, NIST does not have the [CVE](https://nvd.nist.gov/vuln/detail/CVE-2023-33308) listed. However, details may be added in the future.

## What is vulnerable?

The vulnerability affects the following products:

- FortiOS
    - version 7.2.0 through 7.2.3
    - version 7.0.0 through 7.0.10
- FortiProxy
    - version 7.2.0 through 7.2.2
    - version 7.0.0 through 7.0.9

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within the expected time frame of 2 weeks (refer [Patch Management](../guidelines/patch-management.md)):

- [FortiGuard - CVE-2023-33308](https://www.fortiguard.com/psirt/FG-IR-23-183)