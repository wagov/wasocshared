# FortiSIEM Proof Of Concept Published - 20240530001

## Overview

Since the publication of [Advisory 20240207003](https://soc.cyber.wa.gov.au//advisories/20240207003-FortiSIEM-Critical-Command-Injection-Vulnerabilities), a proof-of-concept exploit (PoC) for Fortinet's FortiSIEM product has been published.

## What is vulnerable?

| CVE                                                                             | Severity.    | CVSS |
| ------------------------------------------------------------------------------- | ------------ | ---- |
| [CVE-2023-34992](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34992) | **Critical** | 9.8  |
| [CVE-2024-23108](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23108) | **Critical** | 9.8  |
| [CVE-2024-23109](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23109) | **Critical** | 9.8  |

The following products and versions are affected:

- FortiSIEM
  - 7.1.0 through 7.1.1 (inclusive)
  - 7.0.0 through 7.0.2 (inclusive)
  - 6.7.0 through 6.7.8 (inclusive)
  - 6.6.0 through 6.6.3 (inclusive)
  - 6.5.0 through 6.5.2 (inclusive)
  - 6.4.0 through 6.4.2 (inclusive)


## Recommendation

A Proof of Concept (POC) exploit has been published. The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://fortiguard.fortinet.com/psirt/FG-IR-23-130>

### Additional Resources

- Horizon3.ai deep-dive article: <https://www.horizon3.ai/attack-research/cve-2024-23108-fortinet-fortisiem-2nd-order-command-injection-deep-dive/>
- Dark Reading blog article: <https://www.darkreading.com/vulnerabilities-threats/exploit-fortinet-critical-rce-bug-siem-root-access>