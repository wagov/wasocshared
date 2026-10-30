# Linux Kernel Vulnerability - ipv4 malformed checksum - 20261019001

## Overview

The WASOC has observed newly published updates from Red Hat addressing a critical vulnerability affecting their products. Successful exploitation could allow an unauthorized attacker to send malformed packets leading to arbitary code execution on the host, a system crash resulting in Denial of Service (DoS), or information disclosure of sensitive memory.

## What is vulnerable?

| Product(s) and Versions Affected                                                        | CVE                                                               | CVSS | Severity |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| [Vendor listed affected products and versions](https://access.redhat.com/security/cve/cve-2026-99999) | [CVE-2026-99999](https://nvd.nist.gov/vuln/detail/cve-2026-99999) | 9.3 | Critical |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Red Hat: <https://access.redhat.com/security/cve/cve-2026-99999>
