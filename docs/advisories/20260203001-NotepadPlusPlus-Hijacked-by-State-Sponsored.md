# NotepadPlusPlus Hijacked by State-Sponsored Hackers - 20260203001

## Overview

Since the publication of [Advisory 20251215002](https://soc.cyber.wa.gov.au/advisories/20251215002-NotepadPlusPlus-Traffic-Hijacking-Vulnerability/), the WASOC has observed a recently published article detailing how a nation-state sophisticated campaign attributed to the Chinese APT group Lotus Blossom exploited hosting infrastructure to hijack Notepad++ updates.

The report states that traffic from some targeted users were selectively routed to attacker-controlled servers serving malware update manifests.

To address this, the vendor has migrated to a new hosting provider with significantly stronger security practices, and released a new product version to include all relevant security enhancements.

## What has been observed?

The newly observed article reports that state‑sponsored threat actors compromised the infrastructure of Notepad++’s hosting provider and hijacked its update system. They then redirected some users to malicious servers serving altered installers, taking advantage of weaker verification checks in older versions.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices.
At the time of writing, the vendor instructions are to **newly download and install v8.9.1**, which includes all relevant security enhancements.

- Notepad++: <https://notepad-plus-plus.org/news/hijacked-incident-info-update>

## Additional references

- Rapid7: <https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit>
