# Microsoft Server Privilege Escalation CertiGhost - 20261112001

## Overview

The WASOC has observed newly published updates from Microsoft addressing one or more critical vulnerabilities affecting their products. Successful exploitation could allow an authorized attacker to elevate privileges over a network.

Articles have dubbed this vulnerbility "CertiGhost".

## What is vulnerable?

| Product(s) and Versions Affected | CVE | CVSS | Severity |
| --- | --- | --- | --- |
| [Vendor listed products and versions](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54121) | [CVE-2026-54121](https://nvd.nist.gov/vuln/detail/CVE-2026-54121) | 8.8 | HIGH |

## What has been observed?

The WASOC have observed mentions of proof-of-concept (POC) exploitation code for one or more of the mentioned items.<br>
The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft: <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54121>

### Additional Resources

- Github POC: <https://github.com/KrakenEU/CVE-2026-54121-CertiGhost>
