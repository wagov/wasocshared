# Chromium V8 Type Confusion - 20260907001

## Overview

Google have published security updates addressing critical vulnerabilities affecting Chromium-based products. Successful exploitation could allow a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page.

## What is vulnerable?

| Products Affected | Version(s) | CVE | CVSS | Severity |
| --- | --- | --- | --- | --- |
| **Chromium-based Browsers** <br> - Google Chrome <br> - Microsoft Edge <br> - Brave <br> - Vivaldi | - Prior to 152.0.7977.82/.83 for Windows and Mac <br> - Prior to 152.0.7977.82 for Linux  | [CVE-2026-85046](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) | 8.8 | High |

## What has been observed?

Google is aware that an exploit for one of more of the mentioned items exists in the wild.
CISA has added one of more of the mentioned items to their [Known Exploited Vulnerability](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalogue.
The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Google: <https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html>
