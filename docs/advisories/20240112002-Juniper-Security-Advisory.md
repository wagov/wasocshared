# Juniper Security Bulletin for Junos OS and Junos OS Evolved - 20240112002

## Overview

Juniper have released a security advisory for Junos OS and Junos OS Evolved. 


## What is the vulnerability?

A Missing Release of Memory after Effective Lifetime vulnerability in the Routing Protocol Daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolved allows an unauthenticated, network-based attacker to cause a Denial of Service (DoS).

In a Juniper Flow Monitoring (jflow) scenario route churn that causes BGP next hops to be updated will cause a slow memory leak and eventually a crash and restart of rpd.


## What is vulnerable?

This issue affects the following products:

Junos OS versions:

- 21.4 versions earlier than 21.4R3;
- 22.1 versions earlier than 22.1R3;
- 22.2 versions earlier than 22.2R3;

Junos OS Evolved:

- 21.4-EVO versions earlier than 21.4R3-EVO;
- 22.1-EVO versions earlier than 22.1R3-EVO;
- 22.2-EVO versions earlier than 22.2R3-EVO;


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://supportportal.juniper.net/s/article/2024-01-Security-Bulletin-Junos-OS-and-Junos-OS-Evolved-In-a-jflow-scenario-continuous-route-churn-will-cause-a-memory-leak-and-eventually-an-rpd-crash-CVE-2024-21611?language=en_US>