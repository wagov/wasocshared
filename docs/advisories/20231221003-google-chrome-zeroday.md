# Google Chrome Critical Security Updates - 20231221003

## Overview

Google has released an update for the Chrome web browser to address multiple serious security vulnerabilities.

Google is aware that an exploit for CVE-2023-7024 exists in the wild.

## What is the vulnerability?

| CVE ID | CVSS Score | Description |
| --- | --- | --- |
| [CVE-2023-7024](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7024) | TBD | Heap buffer overflow in WebRTC.  |

## What is vulnerable?

The vulnerability affects the following Google products:

- Google Chrome stable channel below 120.0.6099.129 for Mac,Linux and 120.0.6099.129/130 for Windows
- Extended Stable channel versions below 120.0.6099.129 for Mac and 120.0.6099.130 for Windows

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing. Google is aware that an exploit for CVE-2023-7024 exists in the wild. 

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- [Google - Stable Channel Update for Chrome Desktop](https://chromereleases.googleblog.com/2023/12/stable-channel-update-for-desktop_20.html)

## Updated advisories

A new advisory has been released for the above vulnerability with updates and can be found [here](https://soc.cyber.wa.gov.au/advisories/20240105001-CISA-adds-two-known-exploited-vulnerabilities-to-catalogue/).