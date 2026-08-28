# Flaw in OpenEXR image library - 20260629003

## Overview

The WASOC has been made aware of OpenEXR HTJ2K decoder vulnerable to heap buffer over-read in ht_undo_impl() (DoS). OpenEXR is the reference implementation and specification for the EXR image format, widely used in the motion picture industry. If exploited the vulnerability would result into a deterministic crash (DoS) and potential adjacent-heap leak.

## What is vulnerable?

| Product(s) Affected                 | Version(s)                          | CVE                                                               | CVSS | Severity |
| ----------------------------------- | ----------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| AcademySoftwareFoundation - openexr | affected at >= 3.4.0 through 3.4.11 | [CVE-2026-45696](https://nvd.nist.gov/vuln/detail/CVE-2026-45696) | 8.3  | High     |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- RedHatBugzilla: <https://access.redhat.com/security/cve/cve-2026-45696#cve-affected-packages>

## Additional References

- CVE.ORG: <https://www.cve.org/CVERecord?id=CVE-2026-45696>
