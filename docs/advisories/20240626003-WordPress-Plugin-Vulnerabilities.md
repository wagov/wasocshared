# WordPress Plugin Vulnerabilities - 20240626003

## Overview

Several plugins for WordPress hosted on WordPress.org have been compromised and injected with malicious PHP scripts. A malicious threat actor compromised the source code of various plugins and injected code that exfiltrates database credentials and is used to create new, malicious, administrator users and send that data back to a server.

## What is vulnerable?

| Products Affected | CVE | CVSS | Severity |
| --- | --- | ---- | ------------ |
| **[List of Affected Products](https://www.cve.org/CVERecord?id=CVE-2024-6297)** | [CVE-2024-6297](https://www.cve.org/CVERecord?id=CVE-2024-6297) | 10   | **Critical** |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- https://www.wordfence.com/threat-intel/vulnerabilities/detail/several-wordpressorg-plugins-various-versions-injected-backdoor
