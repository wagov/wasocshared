# Zoom Rooms Local Privilege Escalation Vulnerability - 20230117004

## Overview
Zoom Rooms contains a local privilege escalation vulnerability which a local low-privileged user could exploit in an attack chain to escalate their privileges to the SYSTEM user.

## What is vulnerable? 
The vulnerability affects the following products:
- Zoom Rooms for macOS clients **before** version 5.11.3
   - [**CVE-2022-36926**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36926): CVSS Score 8.8
   - [**CVE-2022-36927**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36927): CVSS Score 8.8
- Zoom Rooms for Windows clients **before** version 5.12.7
   - [**CVE-2022-36929**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36929): CVSS Score 7.8
- Zoom Rooms for Windows installers **before** version 5.13.0
   - [**CVE-2022-36930**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-36930): CVSS Score 8.2

## Recommendation
The WA SOC recommends administrators apply the latest updates as per vendor instructions to all affected devices: [https://zoom.us/download](https://zoom.us/download)

## Additional References:
* Zoom Security Bulletin: [https://explore.zoom.us/en/trust/security/security-bulletin/](https://explore.zoom.us/en/trust/security/security-bulletin/)