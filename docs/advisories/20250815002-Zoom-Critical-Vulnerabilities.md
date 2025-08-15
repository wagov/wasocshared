# Zoom Critical Vulnerability - 20250815002

## Overview

Zoom has published a security advisory relating to a critical vulnerability affecting multiple products. Successful exploitation may potentially allow an unauthenticated user to conduct an escalation of privilege via network access.

## What is vulnerable?

| Product(s) Affected                                                                        | Version(s)                                                                                                         | CVE                                                               | CVSS | Severity     |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ---- | ------------ |
| Workplace for Windows <br> Workplace VDI <br> Rooms for Windows <br> Rooms Controller <br> | [Vendor Listed Affected versions](https://www.zoom.com/en/trust/security-bulletin/zsb-25030/?lang=en-US&lang=null) | [CVE-2025-49457](https://nvd.nist.gov/vuln/detail/CVE-2025-49457) | 9.6  | **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Zoom: <https://www.zoom.com/en/trust/security-bulletin/zsb-25030/?lang=en-US&lang=null>

## Additional References

- Security Affairs: <https://securityaffairs.com/181140/security/zoom-patches-critical-windows-flaw-allowing-privilege-escalation.html>
