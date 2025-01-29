# SonicWall Critical Advisory - 20250129001

## Overview

The WA SOC has been made aware a critical authentication vulnerability in SonicOS products.

Successful exploitation of this vulnerability allows a remote unauthenticated attacker to hijack existing authenticated client SSLVPN sessions. Multi-factor authentication is bypassed during exploitation, facilitating initial access even via accounts with MFA enabled. Exploitation does not require the knowledge of an existing username or password.

## What is vulnerable?

| Product(s) Affected      | Version(s)                           | CVE                                                               | CVSS | Severity     |
| ------------------------ | ------------------------------------ | ----------------------------------------------------------------- | ---- | ------------ |
| Gen7 Firewalls, Gen7 NSv | 7.1.1-7058 and older <br> 7.1.2-7019 | [CVE-2024-53704](https://nvd.nist.gov/vuln/detail/CVE-2024-53704) | 9.8  | **Critical** |
| TZ80                     | Version 8.0.0-8035                   | [CVE-2024-53704](https://nvd.nist.gov/vuln/detail/CVE-2024-53704) | 9.8  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 48 hours:

- SonicWall: <https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0003>

## Additional References

- AttackerKB: <https://attackerkb.com/topics/UB3P3xHVAo/cve-2024-53704/rapid7-analysis>
