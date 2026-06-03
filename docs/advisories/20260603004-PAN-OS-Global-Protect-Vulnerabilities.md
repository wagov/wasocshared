# PAN-OS: GlobalProtect Authentication Bypass Vulnerabilities - 20260603004

## Overview

Palo Alto Networks has released information regarding a critical authentication bypass vulnerability affecting PAN-OS GlobalProtect portal and gateway components. This vulnerability allows unauthenticated attackers to bypass authentication mechanisms and establish unauthorized VPN connections to affected systems.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
|--------------------|-----------|-----|------|----------|
| GlobalProtect Portal & Gateway) | PAN-OS < 12.1.4-h6 and < 12.1.7<br> | [CVE-2026-0257](https://nvd.nist.gov/vuln/detail/CVE-2026-0257) | 9.1 | **Critical**
| Prisma Access | Prisma Access 11.2 < 11.2.7-h13<br> and < 10.2.10-h36 | [CVE-2026-0257](https://nvd.nist.gov/vuln/detail/CVE-2026-0257) | 9.1 | **Critical** |




## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing. However, Palo Alto Networks has confirmed limited exploitation attempts targeting unpatched PAN‑OS devices without mitigations applied

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Palo Alto Networks: <https://security.paloaltonetworks.com/CVE-2026-0257>



