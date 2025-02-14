# Palo Alto Monthly Security Update and Active Exploitation - 20250214002

## Overview

Palo Alto has released security updates to address numerous vulnerabilities in multiple products, one of which has been noted as having current active exploitation.

## What is vulnerable?

### Monthly Updates of note

| Product(s) Affected      | Version(s)                                                                           | CVE                                                             | CVSS     | Severity |
| ------------------------ | ------------------------------------------------------------------------------------ | --------------------------------------------------------------- | -------- | -------- |
| Prisma Access Browser    | < 132.111.3017.2                                                                     | <https://security.paloaltonetworks.com/PAN-SA-2025-0004>        | Multiple | Multiple |
| PAN-OS                   | 11.2: < 11.2.4-h4 <br> 11.1: < 11.1.6-h1<br>10.2: < 10.2.13-h3<br>10.1: < 10.1.14-h9 | [CVE-2025-0111](https://nvd.nist.gov/vuln/detail/CVE-2025-0111) | 6.6      | Medium   |
| PAN-OS OpenConfig Plugin | < 2.1.2                                                                              | [CVE-2025-0110](https://nvd.nist.gov/vuln/detail/CVE-2025-0110) | 6.6      | Medium   |

### Known exploited

| Product(s) Affected | Version(s)                                                                           | CVE                                                             | CVSS | Severity |
| ------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ---- | -------- |
| PAN-OS              | 11.2: < 11.2.4-h4 <br> 11.1: < 11.1.6-h1<br>10.2: < 10.2.13-h3<br>10.1: < 10.1.14-h9 | [CVE-2025-0108](https://nvd.nist.gov/vuln/detail/CVE-2025-0108) | 5.1  | Medium   |

## What has been observed?

There is evidence of active exploitation of CVE-2025-0108 affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Palo Alto:
    - <https://security.paloaltonetworks.com/PAN-SA-2025-0004>
    - <https://security.paloaltonetworks.com/CVE-2025-0111>
    - <https://security.paloaltonetworks.com/CVE-2025-0110>
    - <https://security.paloaltonetworks.com/CVE-2025-0108>

## Additional References

- Tenable:
    - <https://www.tenable.com/cve/CVE-2025-0111>
    - <https://www.tenable.com/cve/CVE-2025-0110>
    - <https://www.tenable.com/cve/CVE-2025-0108>
