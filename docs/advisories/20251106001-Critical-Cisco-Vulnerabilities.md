# Critical Cisco Vulnerabilities - 20251106001

## Overview

Cisco have released an advisory addressing multiple vulnerabilities in the Java Remote Method Invocation (RMI) process of Cisco Unified Contact Center Express (Unified CCX). Successful exploitation could allow an unauthenticated, remote attacker to upload arbitrary files, bypass authentication, execute arbitrary commands, and elevate privileges to root.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE    | CVSS     | Severity    |
| ------------------- | ---------- |------- | -------- | ----------- |
| Cisco Unified CCX | All versions prior to	12.5 SU3 ES07 <br> 15.0 prior to 15.0 ES01 | [CVE-2025-20354](https://nvd.nist.gov/vuln/detail/CVE-2025-20354) <br> [CVE-2025-20358](https://nvd.nist.gov/vuln/detail/CVE-2025-20358) | 9.8 <br> 9.4 | **Critical** |

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- CISCO: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cc-unauth-rce-QeN8h7mQ#fs>

