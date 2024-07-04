# Juniper Security Advisory - 20240704001

## Overview

An Improper Check for Unusual or Exceptional Conditions vulnerability in the Packet Forwarding Engine (PFE) of Juniper Networks Junos OS on SRX Series allows an unauthenticated, network-based attacker to cause a Denial-of-Service (DoS).
The PFE will crash and restart if an SRX Series device receives specific valid traffic destined to the device. Continued traffic receipt and processing will create a sustained DoS condition.

## What is vulnerable?

| Product(s) Affected                                                      | Version(s)     |  CVE                                                               | Severity | CVSS |
| ------------------------------------------------------------------------ | -------------- |----------------------------------------------------------------- | -------- | ---- |
| Junos OS on SRX Series                                                   | 21.4 versions before 21.4R3-S7.9, 22.1 versions before 22.1R3-S5.3, 22.2 versions before 22.2R3-S4.11, 22.3 versions before 22.3R3, 22.4 versions before 22.4R3 | [CVE-2024-21586](https://nvd.nist.gov/vuln/detail/CVE-2024-21586) | **High** | 8.7  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing and Junos OS versions prior to 21.4R1 are not affected by this issue.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 48 hours (refer [Patch Management](../guidelines/patch-management.md)):

- <https://supportportal.juniper.net/s/article/2024-07-Out-of-Cycle-Security-Bulletin-Junos-OS-SRX-Series-Specific-valid-traffic-leads-to-a-PFE-crash-CVE-2024-21586?language=en_US>


## Additional References

- Tenable: <https://www.tenable.com/cve/CVE-2024-21586>
