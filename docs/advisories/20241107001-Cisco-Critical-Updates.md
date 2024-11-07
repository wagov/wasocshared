# Cisco Releases Critical Updates - 20241107001

## Overview

Cisco has released multiple updates for products to address a vulnerability in the web-based management interface of Cisco Unified Industrial Wireless Software for Cisco Ultra-Reliable Wireless Backhaul (URWB) Access Points could allow an unauthenticated, remote attacker to perform command injection attacks with root privileges on the underlying operating system.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS         | Severity                                                        |
| ------------------- | ---------- | --- | ------------ | --- |
| Cisco Catalyst IW9165D / IW9165E / IW9167E Access Points | All versions below 17.15.1 | [CVE-2024-20418](https://nvd.nist.gov/vuln/detail/CVE-2024-20418) | 10 | **Critical**  |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Cisco: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-backhaul-ap-cmdinj-R7E28Ecs#vp>

## Additional References

- CISecurity: <https://www.cisecurity.org/advisory/a-vulnerability-in-cisco-unified-industrial-wireless-software-for-ultra-reliable-wireless-backhaul-access-point-could-allow-for-remote-code-execution_2024-123>
