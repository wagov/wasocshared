# ACSC releases Cisco SD-WAN Threat Hunt Guide - 20260226001

## Overview

The ACSC has published 'Cisco SD-WAN Threat Hunt Guide'. ACSC has observed malicious cyber activities targeting **Cisco Software-Defined Wide Area Network (SD-WAN)** environments. At least one malicious actor exploited a **previously unknown (zero-day) vulnerability** to compromise Cisco SD-WAN deployments. This vulnerability has since been **patched by the vendor**.

The vulnerability enabled the creation of a **rogue SD-WAN peer** within the **management and control plane**, appearing as a legitimate but temporary component under the actor’s control. This rogue device was able to perform **trusted actions** within the SD-WAN environment.

This guide is intended to support **cybersecurity professionals and network administrators** in identifying **indicators of compromise** within Cisco SD-WAN deployments and assessing potential exposure.

## What is vulnerable?

| Product(s) Affected     | Version(s) | CVE                                                               | CVSS | Severity     |
| ----------------------- | ---------- | ----------------------------------------------------------------- | ---- | ------------ |
| Cisco SD-WAN Appliances | -          | [CVE-2026-20127](https://nvd.nist.gov/vuln/detail/CVE-2026-20127) | 10   | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes, as well as review the ACSC Threat Hunt Guide to detect for signs of compromise within their environments:

- Cisco Advisory: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-sd-wan-priv-E6e8tEdF.html>
- ACSC Guide: <https://www.cyber.gov.au/sites/default/files/2026-02/ACSC-led%20Cisco%20SD-WAN%20Hunt%20Guide.pdf>
