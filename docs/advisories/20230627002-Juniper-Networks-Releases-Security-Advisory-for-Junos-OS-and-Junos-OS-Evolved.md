# Juniper Networks Releases Security Advisory for Junos OS and Junos OS Evolved - 20230627002

## Overview

The WA SOC has observed An Improper Input Validation vulnerability in the Routing Protocol Daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolved allows an unauthenticated, network-based attacker to cause a Denial of Service (DoS).

When a Border Gateway Protocol (BGP) update message is received over an established BGP session, and that message contains a specific, optional transitive attribute, this session will be torn down with an update message error. This issue cannot propagate beyond an affected system as the processing error occurs as soon as the update is received. This issue is exploitable remotely as the respective attribute can propagate through unaffected systems and intermediate AS (if any).

Some customers have experienced these BGP session flaps which prompted Juniper Networks Security Incident Response Team (Juniper SIRT) to release this advisory out of cycle before fixed releases are widely available as there is an effective workaround.

## What is the vulnerability?

[**CVE-2023-0026**](https://nvd.nist.gov/vuln/detail/CVE-2023-0026) - CVSS v3 Base Score: ***7.5***

## What is vulnerable?

The vulnerability affects:

Juniper Networks Junos OS:

- 15.1R1 and later versions prior to 20.4R3-S8;
- 21.1 version 21.1R1 and later versions prior to 21.2R3-S6;
- 21.3 versions prior to 21.3R3-S5;
- 21.4 versions prior to 21.4R3-S4;
- 22.1 versions prior to 22.1R3-S4;
- 22.2 versions prior to 22.2R3-S2;
- 22.3 versions prior to 22.2R3-S2;
- 22.4 versions prior to 22.4R2-S1, 22.4R3;
- 23.1 versions prior to 23.1R1-S1, 23.1R2.

Juniper Networks Junos OS Evolved:

- All versions prior to 20.4R3-S8-EVO;
- 21.1 version 21.1R1-EVO and later versions prior to 21.2R3-S6-EVO;
- 21.3 versions prior to 21.3R3-S5-EVO;
- 21.4 versions prior to 21.4R3-S4-EVO;
- 22.1 versions prior to 22.1R3-S4-EVO;
- 22.2 versions prior to 22.2R3-S2-EVO;
- 22.3 versions prior to 22.3R2-S2-EVO, 22.3R3-S1-EVO;
- 22.4 versions prior to 22.4R2-S1-EVO, 22.4R3-EVO;
- 23.1 versions prior to 23.1R1-S1-EVO, 23.1R2-EVO.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within one month (refer [Patch Management](../guidelines/patch-management.md)):

- [https://kb.juniper.net/JSA71542](https://supportportal.juniper.net/s/article/2023-06-Out-of-Cycle-Security-Bulletin-Junos-OS-and-Junos-OS-Evolved-A-BGP-session-will-flap-upon-receipt-of-a-specific-optional-transitive-attribute-CVE-2023-0026?language=en_US)
- [https://www.juniper.net/documentation/us/en/software/junos/bgp/topics/topic-map/bgp-error-messages.html](https://www.juniper.net/documentation/us/en/software/junos/bgp/topics/topic-map/bgp-error-messages.html)
