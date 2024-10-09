# Siemens Publishes ICS Advisory - 20241009004

## Overview

The WA SOC has been made aware of a vulnerability identified in Siemens SINEC Security Monitor. The affected application does not properly validate user input for the `ssmctl-client` command. This could allow an authenticated, lowly privileged remote attacker to execute arbitrary code with root privileges on the underlying operating system.

## What is vulnerable?

| Vendor | Advisory Link(s) |
| --- | --- |
| Siemens SINEC Security Monitor | [SSA-430425](https://cert-portal.siemens.com/productcert/html/ssa-430425.html) |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Siemens Security Advisory: <https://cert-portal.siemens.com/productcert/html/ssa-430425.html>

## Additional References

- Tenable: <https://www.tenable.com/cve/CVE-2024-47553>
