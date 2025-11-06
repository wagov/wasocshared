# Critical Cisco Vulnerabilities - 20251106001

## Overview

WASOC has become aware of multiple vulnerabilities in the Java Remote Method Invocation (RMI) process of Cisco Unified Contact Center Express (Unified CCX) could allow an unauthenticated, remote attacker to upload arbitrary files, bypass authentication, execute arbitrary commands, and elevate privileges to root.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE    | CVSS     | Severity    |
| ------------------- | ---------- |------- | -------- | ----------- |
| Packaged Contact Center Enterprise (Packaged CCE) <br> Unified Contact Center Enterprise (Unified CCE) | Version    | [CVE-2025-20354](https://nvd.nist.gov/vuln/detail/CVE-2025-20354) <br> [CVE-2025-20358](https://nvd.nist.gov/vuln/detail/CVE-2025-20358) | 9.8 <br> 9.4 | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- CISCO: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cc-unauth-rce-QeN8h7mQ#fs>

