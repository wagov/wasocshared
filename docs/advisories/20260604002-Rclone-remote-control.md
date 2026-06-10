# Rclone Remote Control - 20260604002

## Overview

The WASOC has been made aware of a remote control vulnerability exists in Rclone when exposed Remote Control (RC) endpoint is exploited to disable the authorisation mechanism and other RC methods. 

This will allow an attacker to gain access to sensitive data and execute arbitary local commands to gain control of the Rclone server.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Rclone     |  from 1.4.9 before 1.73.5   | [CVE-2026-41176](https://nvd.nist.gov/vuln/detail/CVE-2026-41176) <br> [CVE-2026-41179](https://nvd.nist.gov/vuln/detail/CVE-2026-41179) | 9.8 <br> 9.8 | **Critical** <br> **Critical** |

## What has been observed?

The WASOC has observed public reports of proof of concept exploit code.
The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Redhat: <https://access.redhat.com/security/cve/cve-2026-41176>
- Redhat: <https://access.redhat.com/security/cve/cve-2026-41179>

## Additional References

- Redhat BugZilla: <https://bugzilla.redhat.com/show_bug.cgi?id=2460989>
