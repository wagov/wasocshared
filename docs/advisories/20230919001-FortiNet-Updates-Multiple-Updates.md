# Fortinet Releases Security Updates for Multiple Products - 20230919001

## Overview

Fortinet has released security updates to address vulnerabilities affecting FortiOS, FortiProxy, and FortiWeb. A cyber threat actor can exploit one of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

- [**CVE-2023-34984**](https://nvd.nist.gov/vuln/detail/CVE-2023-34984) - CVSS v3 Base Score: ***8.8***: A protection mechanism failure [(CWE-693)](https://cwe.mitre.org/data/definitions/693.html) vulnerability in FortiWeb may allow an attacker to bypass XSS and CSRF protections.
- [**CVE-2023-29183**](https://nvd.nist.gov/vuln/detail/CVE-2023-29183) - CVSS v3 Base Score: ***5.4***: An improper neutralization of input during web page generation ('Cross-site Scripting') vulnerability [(CWE-79)](https://cwe.mitre.org/data/definitions/79.html) in FortiOS and FortiProxy GUI may allow an authenticated attacker to trigger malicious JavaScript code execution via crafted guest management setting.

## What is vulnerable?

**CVE-2023-34984**

- FortiWeb version 7.2.0 through 7.2.1
- FortiWeb version 7.0.0 through 7.0.6
- FortiWeb 6.4 **all versions**
- FortiWeb 6.3 **all versions**

**CVE-2023-29183**

- FortiProxy version 7.2.0 through 7.2.4
- FortiProxy version 7.0.0 through 7.0.10
- FortiOS version 7.2.0 through 7.2.4
- FortiOS version 7.0.0 through 7.0.11
- FortiOS version 6.4.0 through 6.4.12
- FortiOS version 6.2.0 through 6.2.14

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://www.fortiguard.com/psirt/FG-IR-23-068>
- <https://www.fortiguard.com/psirt/FG-IR-23-106>
