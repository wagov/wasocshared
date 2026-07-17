# ANGLE in Google Chrome - 20260708001

## Overview

Insufficient validation of untrusted input in ANGLE in Google Chrome prior to 150.0.7871.46 allowed a remote attacker to potentially perform a sandbox escape via a crafted HTML page.

## What is vulnerable?

| Product(s) Affected    | Version(s)             | CVE                                                               | CVSS | Severity     |
| ---------------------- | ---------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| ANGLE in Google Chrome | prior to 150.0.7871.46 | [CVE-2026-14382](https://nvd.nist.gov/vuln/detail/CVE-2026-14382) | 9.6  | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Google: <https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop_0175352312.html>
