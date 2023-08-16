# Sophisticated network attacks and guidance for agencies - 20230816001

## Overview

Several recent reports from major companies in the network security space including Cisco and Mandiant have highlighted the focus from sophisticated threat actors on targeting network infrastructure. WA SOC has recently published some high-level guidance for agencies that can prevent or provide improved visibility over many of these attacks.

## What has been observed?

### Cisco Talos 

Cisco Talos and many intelligence agencies have [reported attacks](https://blog.talosintelligence.com/state-sponsored-campaigns-target-global-network-infrastructure/) against firewalls and routers globally, these attacks leverage gateway vulnerabilities from unpatched network hardware, leaked credentials, legacy infrastructure, flawed configurations and persist by further exploiting these vulnerabilities to introduce even more network weaknesses. [Network Resilience: Defending against sophisticated attacks targeting network infrastructure](https://blogs.cisco.com/security/network-resilience-defending-against-sophisticated-attacks-targeting-network-infrastructure) outlines in further detail some of the protections against attacks they have seen. 

### Mandiant

Google's Mandiant has also released a [blog post](https://www.mandiant.com/resources/blog/chinese-espionage-tactics) about the tactics used by state-sponsored threat actors to avoid detection and that 'cyber espionage zero-day exploitation in 2021 and 2022 has focused on security, networking, and virtualization technologies'. Mandiant continues to list seven more cases of similar threat actors launching network attacks targeting firewalls, routers, VPNs, and email gateways.

Agencies vulnerable to these threats may be [unaware of active exploits](https://www.mandiant.com/resources/blog/barracuda-esg-exploited-globally) due to the sophisticated persistence techniques used.

## How are these risks addressed?

As many of the risks outlined in the reports are directly on gateway devices and associated internet exposed appliances, ACSC's [Gateway Security Guidance](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-hardening/gateway-security-guidance-package-executive-guidance) offers helpful executive guidance, principles and frameworks to address many of the concerns. Listed within that guidance is an essential list of governance-related security principles that organisations need to be aware of as part of using gateways. These are:

-   risk cannot be outsourced
-   security management is continuous
-   risk is continuously managed
-   the invisible cannot be protected
-   gateways protect organisations and staff
-   Commonwealth entities have specific obligations
-   plan for security flaws
-   balance business and security.

A definition of gateways can be described as anything facilitating data flow between an organisation’s internal network and the internet.

## Recommendation

In addition to recommending ACSC's [Gateway Security Guidance](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-hardening/gateway-security-guidance-package-executive-guidance), the WA SOC has recently published some high-level [Network Management Guidelines](https://soc.cyber.wa.gov.au//guidelines/network-management/) that agencies can use to help transform and modernise their networks to address many of the shortcomings of existing out-of-date network architecture. 

- [Contemporary Network Architecture](https://soc.cyber.wa.gov.au//guidelines/network-management/#contemporary-network-architecture)
- [Observability & Manageability](https://soc.cyber.wa.gov.au//guidelines/network-management/#observability-manageability)
- [Adverse Event Analysis](https://soc.cyber.wa.gov.au//guidelines/network-management/#adverse-event-analysis)
- [Segmentation](https://soc.cyber.wa.gov.au//guidelines/network-management/#segmentation)
- [Common Network Use Cases](https://soc.cyber.wa.gov.au//guidelines/network-management/#common-network-use-cases)

## Additional References

- [WA SOC Network Management Guideline](https://soc.cyber.wa.gov.au//guidelines/network-management/)
- [Cisco - Threat Actors Exploiting SNMP Vulnerabilities in Cisco Routers](https://blogs.cisco.com/security/threat-actors-exploiting-snmp-vulnerabilities-in-cisco-routers)
- [ACSC - Gateway Hardening](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-hardening)
