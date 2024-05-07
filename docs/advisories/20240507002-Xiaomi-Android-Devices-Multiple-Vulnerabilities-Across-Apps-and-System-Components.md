# Xiaomi Android Devices Multiple Vulnerabilities Across Apps and System Components - 20240507002

## Overview

Multiple security vulnerabilities have been disclosed in various applications and system components within Xiaomi devices running Android. These vulnerabilities could lead to accessing arbitrary activities, receivers and services with system privileges; theft of arbitrary files with system privileges, disclosure of phone settings and Xiaomi account data.

## What is vulnerable?

The below listed apps and components have been identified as impacted by these vulnerabilities:

- Gallery (com.miui.gallery)
- GetApps (com.xiaomi.mipicks)
- Mi Video (com.miui.videoplayer)
- MIUI Bluetooth (com.xiaomi.bluetooth)
- Phone Services (com.android.phone)
- Print Spooler (com.android.printspooler)
- Security (com.miui.securitycenter)
- Security Core Component (com.miui.securitycore)
- Settings (com.android.settings)
- ShareMe (com.xiaomi.midrop)
- System Tracing (com.android.traceur), and
- Xiaomi Cloud (com.miui.cloudservice)

Some of the notable flaws include a shell command injection bug impacting the System Tracing app and flaws in the Settings app that could enable theft of arbitrary files as well as leak information about Bluetooth devices, connected Wi-Fi networks, and emergency contacts.

The Mi Video app has been found to use implicit intents to send Xiaomi account information, such as username and email address via broadcasts, which could be intercepted by any third-party app installed on the devices using its own broadcast receivers.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- Users are advised to apply the latest updates to mitigate against potential threats.

## Additional References

- [Xiaomi Android Devices Hit by Multiple Flaws Across Apps and System Components (thehackernews.com)](https://thehackernews.com/2024/05/xiaomi-android-devices-hit-by-multiple.html)
