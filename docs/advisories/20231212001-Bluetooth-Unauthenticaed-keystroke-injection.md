# Mobile Device Unauthenticated Bluetooth Keystroke-Injection - 20231212001

## Overview

The WA SOC has observed a blog post relating to the disclosure of **CVE-2023-45866**, an unauthenticated bluetooth keystroke-injection affecting Android, Linux, macOS and iOS mobile devices.

The attack does not require specialized hardware, and can be performed from a Linux computer using a normal Bluetooth adapter.

## What is the vulnerability?

| CVE ID                                                            | CVSS Score | Overview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CVE-2023-45866](https://nvd.nist.gov/vuln/detail/CVE-2023-45866) | 9.8        | Bluetooth HID Hosts in BlueZ may permit an unauthenticated Peripheral role HID Device to initiate and establish an encrypted connection, and accept HID keyboard reports, potentially permitting injection of HID messages when no user interaction has occurred in the Central role to authorize such access. An example affected package is bluez 5.64-0ubuntu1 in Ubuntu 22.04LTS. NOTE: in some cases, a CVE-2020-0556 mitigation would have already addressed this Bluetooth HID Hosts issue. |

## What is vulnerable?

According to the findings of the blog post author, the vulnerability affects the following products:

| Platform    | Device / version                           |
| ----------- | ------------------------------------------ |
| Android     | Pixel 7 running Android 14                 |
|             | Pixel 6 running Android 13                 |
|             | Pixel 4a (5G) running Android 13           |
|             | Pixel 2 running Android 11                 |
|             | Pixel 2 running Android 10                 |
|             | Nexus 5 running Android 6.0.1              |
|             | BLU DASH 3.5 running Android 4.2.2         |
| Linux/BlueZ | Ubuntu 18.04, 20.04, 22.04, 23.10          |
| MacOS       | 2022 MacBook Pro with MacOS 13.3.3 (M2)    |
|             | 2017 MacBook Air with macOS 12.6.7 (Intel) |
| iOS         | iPhone SE running iOS 16.6                 |

## Recommendation

The WA SOC recommends administrators apply the latest patches as per vendor instructions to all affected devices where possible.

## Additional References

- Original blog post "Hi, My Name Is Keyboard": <https://github.com/skysafe/reblog/tree/main/cve-2023-45866>
- NIST CVE Drtails: <https://nvd.nist.gov/vuln/detail/CVE-2023-45866>
- Tenable CVE Details: <https://www.tenable.com/cve/CVE-2023-45866>
