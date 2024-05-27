# Google Patches Chrome Zero Day Vulnerability - 20240527001

## Overview

Google have released a critical security advisory relating to a vulnerability impacting Chrome on Windows, Mac, and Linux.

## What is vulnerable?

| Product(s) Affected | CVE | Severity | CVSS |
| --- | --- | --- | --- |
| Windows and Mac versions **before** 125.0.6422.112/.113 | [CVE-2024-5274](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5274) | **High** | 7.5 |
| Linux versions **before** 125.0.6422.112 | [CVE-2024-5274](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5274) | **High** | 7.5 |


## What has been observed?

Google is aware that an exploit for CVE-2024-5274 exists in the wild.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://chromereleases.googleblog.com/2024/05/stable-channel-update-for-desktop_23.html>

## Additional References

- Tenable CVE article: <https://www.tenable.com/cve/CVE-2024-5274>