# Chromium Critical Vulnerabilities - 20260610002

## Overview

The WASOC has been made aware of a use after free vulnerability in Google Chrome Navigation and an insufficient validation of untrusted input vulnerability in Google Chrome UI that allowed a remote attacker to potentially perform a sandbox escape via a crafted HTML page.

## What is vulnerable?

| Products Affected | CVE | CVSS | Severity |
| --- | --- | --- | --- |
| **Chromium-based Browsers** <br> - Google Chrome <br> - Microsoft Edge <br> - Brave <br> - Vivaldi | [CVE-2026-11671](https://nvd.nist.gov/vuln/detail/CVE-2026-11671) <br> [CVE-2026-11697](https://nvd.nist.gov/vuln/detail/CVE-2026-11697) | 9.6 | **Critical** |


## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Google: <https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop.html>

## Additional References

- <https://github.com/advisories/GHSA-93cq-cwfp-9r89>
- <https://github.com/advisories/GHSA-rxx6-vjpq-6755>