# Notepad++ Hijacked by State-Sponsored Hackers - 20260203001

## Overview

Since the publication of Advisory 20251215002, the WASOC has observed a recently published article detailing how a nation-state sophisticated campaign attributed to the Chinese APT group Lotus Blossom exploited hosting infrastructure to hijack Notepad++ updates.

The report states that traffic from some targeted users were selectively routed to attacker-controlled servers serving malware update manifests.

## What has been observed?

The newly observed article reports that state‑sponsored threat actors compromised the infrastructure of Notepad++’s hosting provider and hijacked its update system. They then redirected some users to malicious servers serving altered installers, taking advantage of weaker verification checks in older versions.

## Recommendation

The WASOC recommends that administrators review and remove affected versions of Notepad++ packages from their environments:

- Notepad article: <https://notepad-plus-plus.org/news/hijacked-incident-info-update>
- Rapid7 article: <https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit>
