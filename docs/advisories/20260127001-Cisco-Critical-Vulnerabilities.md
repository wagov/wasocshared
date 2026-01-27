# Cisco Critical Vulnerabilities - 20260127001

## Overview

Cisco has released an advisory addressing multiple vulnerabilities across its Unified Communications products.
A remote code execution vulnerability allows an unauthenticated attacker to send crafted HTTP requests to the management interface, enabling user‑level access and potential escalation to root.

## What is vulnerable?

| Product(s) Affected                                                                                           | Version(s)                                         | CVE                                                                    | CVSS | Severity |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------- | ---- | -------- |
| Cisco UCM <br> Cisco UCM Session Manager <br> Cisco UCM IM Prescence Service <br> Cisco Unity Connection <br> | All versions prior to 14su5 <br> 15 prior to 15su4 | [CVE-2026-20045](https://nvd.nist.gov/vuln/detail/CVE-2026-20045) <br> | 9.8  | Critical |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- CISCO: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-rce-mORhqY4b>
