# Cisco Patches Vulnerabilities in Integrated Management Controller - 20240419001

## Overview

A vulnerability in the CLI of the Cisco Integrated Management Controller (IMC) could allow an authenticated, local attacker to perform command injection attacks on the underlying operating system and elevate privileges to root. To exploit this vulnerability, the attacker must have read-only or higher privileges on an affected device.

## What is vulnerable?

| CVE                                                               | Severity | CVSS | Product(s) Affected               |
| ----------------------------------------------------------------- | -------- | ---- | --------------------------------- |
| [CVE-2024-20295](https://nvd.nist.gov/vuln/detail/CVE-2024-20295) | **High** | 8.8  | See vendor link in Recommendation |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices (refer [Patch Management](../guidelines/patch-management.md)):

- [CISCO Security Advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-cmd-inj-mUx4c5AJ)

## Additional References

- [Tenable-CVE-2024-20295](https://www.tenable.com/cve/CVE-2024-20295)
- [Bleeping Computer - Cisco discloses root escalation flaw with public exploit code](https://www.bleepingcomputer.com/news/security/cisco-discloses-root-escalation-flaw-with-public-exploit-code/)
