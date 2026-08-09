# Cisco Security Hardening Updates - 20260807001

## Overview

Cisco have released August security hardening updates for their Catalyst and IOS products, addressing multiple critically rated vulnerabilities.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
| ------------------- | ---------- | --- | ---- | -------- |
| Cisco Catalyst <br> Cisco IOS | [Vendor listed versions](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ)| [CVE-2026-20303](https://nvd.nist.gov/vuln/detail/CVE-2026-20303) <br> [CVE-2026-20304](https://nvd.nist.gov/vuln/detail/CVE-2026-20304) <br> [CVE-2026-20272](https://nvd.nist.gov/vuln/detail/CVE-2026-20272) <br> [CVE-2026-20310](https://nvd.nist.gov/vuln/detail/CVE-2026-20310) <br> [CVE-2026-20267](https://nvd.nist.gov/vuln/detail/CVE-2026-20267) | 9.9 <br> 9.9 <br> 9.8 <br> 9.1 <br> 9.0 | **Critical** <br> **Critical** <br> **Critical** <br> **Critical** <br> **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Cisco Catalyst: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-sdwan-faLcR3K>
- Cisco IOS: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ>
