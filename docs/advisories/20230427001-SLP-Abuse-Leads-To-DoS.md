# Service Location Protocol (SLP) Abuse May Lead to DoS Attack - 20230427001

## Overview

The WA SOC has observed a vulnerability reported by researchers from [Bitsight and Curesec](https://www.bitsight.com/blog/new-high-severity-vulnerability-cve-2023-29552-discovered-service-location-protocol-slp) where attackers may abuse SLP to conduct high amplification factor DoS attacks using spoofed source addresses.

## What is the vulnerability?

[**CVE-2023-29552**](https://nvd.nist.gov/vuln/detail/CVE-2023-29552) - CVSS v3 Base Score: ***8.6***

## What is vulnerable?

The vulnerability affects SLP services that are visible to the internet.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing

## Recommendation

The WA SOC recommends administrators should consider disabling or restricting network access to SLP servers and apply the solutions as per vendor instructions to all affected devices.

## Additional References

- [**CISA - Advisory**](https://www.cisa.gov/news-events/alerts/2023/04/25/abuse-service-location-protocol-may-lead-dos-attacks)
- [**CISA - Understanding and Responding to DDoS Attacks**](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-ddos-attacks_508c.pdf)
- [**VMware Response to CVE-2023-29552**](https://blogs.vmware.com/security/2023/04/vmware-response-to-cve-2023-29552-reflective-denial-of-service-dos-amplification-vulnerability-in-slp.html)
