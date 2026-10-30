# Zammad Critical Vulnerabilities - 20261005001

## Overview

The WASOC has observed updates relating to multiple critical vulnerabilities affecting Zammad. Successful exploitation could allow an attacker to hijack user sessions, achieve remote code execution as the `zammad` user, and escalate privileges locally to `root`.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
|---|---|---|---|---|
| Zammad | Zammad versions 6.3.0 to 6.5.4 (and 7.0.0 to 7.1.3, though not exploitable due to environment conditions) | [CVE-2026-102489](https://nvd.nist.gov/vuln/detail/CVE-2026-102489) | 9.4 | Critical |
| Zammad | All versions of Zammad including the latest alpha enable the local zammad user to escalate privileges to root. | [CVE-2026-102490](https://nvd.nist.gov/vuln/detail/CVE-2026-102490) | 9.4 | Critical |

## What has been observed?

These vulnerabilities have been added to the CISA Known Exploited Vulnerabilities (KEV) catalog. The WASOC has not received any reports of active exploitation on Western Australian Government networks at the time of writing.

## Recommendation
The WASOC recommends administrators apply the solutions as per vendor instructions to all affected instances within expected timeframes (refer Patch Management):

- Update affected Zammad deployments to the latest patched releases provided by the vendor.
- Restrict access to administrative and management interfaces to trusted networks.
- Monitor server logs and audit trails for unauthorized session creation or unexpected root privilege escalation attempts.

### References

- [GitHub Advisory GHSA-xmw5-m2wg-4243 (CVE-2026-102489)](https://github.com/advisories/GHSA-xmw5-m2wg-4243)
- [GitHub Advisory GHSA-hgff-g8g3-4xr8 (CVE-2026-102490)](https://github.com/advisories/GHSA-hgff-g8g3-4xr8)
- [CISA Known Exploited Vulnerabilities Catalog Alert](https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog)