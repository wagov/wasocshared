# FreeRDP Vulnerabilities - 20260603003

## Overview

The WASOC has been made aware of vulnerabilities in FreeRDP, a free implementation of the Remote Desktop Protocol (RDP). A remote attacker can exploit these vulnerabilities, which can result in arbitrary code execution and a denial of service for the FreeRDP client.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Red Hat Enterprise Linux |[all previous versions of packages listed here](https://access.redhat.com/security/cve/cve-2026-31806)  | [CVE-2026-31806](https://nvd.nist.gov/vuln/detail/CVE-2026-31806)                                                                        | 9.8       |**Critical**                                   |
| Red Hat Enterprise Linux     | [all previous versions of packages listed here](https://access.redhat.com/security/cve/cve-2026-31883)   |  [CVE-2026-31883](https://nvd.nist.gov/vuln/detail/CVE-2026-31883) | 6.5       |**Medium**                                   |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- FreeRDP: <br><https://github.com/FreeRDP/FreeRDP/commit/16df2300e1e3f5a51f68fb1626429e58b531b7c8><br> <https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-85x9-4xxp-xhm5><br><https://github.com/FreeRDP/FreeRDP/commit/83d9aedea278a74af3e490ff5eeb889c016dbb2b><br><https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-rrqm-46rj-cmx2>

## Additional References

- RedHatsecurity:<br> <https://access.redhat.com/security/cve/cve-2026-31806><br><https://access.redhat.com/security/cve/cve-2026-31883>
