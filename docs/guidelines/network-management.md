# Network Management Guideline (DRAFT)

This guideline is intended to define a pragmatic target for an entities network architecture to enable effective network management with modern tooling. This guide is structured around the [use cases for a complex network](#network-use-cases) with a design that can be adopted incrementally based on an agencies requirements.

Organisations should strive to reduce network complexity to facilitate its adoption, training, and management. They should mitigate risks as much as possible by favouring managed cloud services and steering clear of legacy VPNs like IPSEC or SSL. Instead, they should adopt contemporary VPN solutions like [WireGuard](https://www.wireguard.com/) or [MASQUE-based](https://blog.cloudflare.com/masque-building-a-new-protocol-into-cloudflare-warp/) VPNs

## Modern Network Design

TODO: diagram

- [ ] Implement a cloud based secure web gateway for end users ( [Microsoft Entra Internet Access](https://learn.microsoft.com/en-gb/azure/global-secure-access/overview-what-is-global-secure-access), [Cisco Umbrella SIG](https://umbrella.cisco.com/products/sig-product) )
    - [ ] Utilise endpoint management to filter outbound endpoint traffic, block all inbound endpoint traffic
    - [ ] Configure endpoint management to utilise authoritative name servers that integrate with [Australian Protective Domain Name Service (AUPDNS)](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-security-guidance/gateway-technology-guides#authoritative-name-servers)
- [ ] Migrate inter-office connectivity to an SD-WAN with local direct internet access for performance
    - [ ] Review commercial managed SD-WAN services as an all-inclusive option for small to medium complexity networks:
        - [Telstra](https://www.telstra.com.au/business-enterprise/products/networks/sdn/sd-wan), [Optus](https://www.optus.com.au/enterprise/networking/network-connectivity/fusion-sd-wan), [Vocus](https://www.vocus.com.au/enterprise/connectivity/managed-network-services/sd-wan), [Aussie Broadband](https://www.aussiebroadband.com.au/enterprise/network/sd-wan/), [TPG Telecom](https://www.tpgtelecom.com.au/business-solutions/sd-wan)
        - Ensure services include managed detection and response capabilities for adverse network activity.
        - Prefer wireless access over ethernet ports and source network switches and wireless access points as part of the commercial SD-WAN service where possible.
        - Integrate SD-WAN with public cloud services as needed to securely access business applications. Note that cloud resources should be segmented per system by default, with access between systems only implemented as required (i.e. don't treat cloud resources as one flat network).
- [ ] Limit remote access to on-premise systems using internet based Zero Trust Network Access solutions ( [Microsoft Entra Private Access](https://learn.microsoft.com/en-gb/azure/global-secure-access/overview-what-is-global-secure-access), [Cisco Umbrella SASE](https://www.cisco.com/c/en/us/products/collateral/security/at-a-glance-c45-2391315.html), [Palo PRISMA Access](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access) )
- [ ] Eliminate any legacy remote access VPNs / access gateways for remote staff.

### Additional considerations for Operational Technology and on-premise servers and/or entities with > 500 staff

- [ ] Ensure network incidents are captured appropriately in a central SIEM ( [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview), [Cisco SecureX](https://www.cisco.com/c/en/us/products/collateral/security/securex/at-a-glance-c45-744497.html?CCID=cc001528&DTID=olgmcdc001463&OID=trlsc021059), [Palo XSOAR](https://xsoar.pan.dev/docs/concepts/getting-started-guide) )
- [ ] Segment all fully managed endpoints (desktops, laptops, desk phones, mobiles) from critical infrastructure or sensitive information systems
    - [ ] Define and segment on-premise servers into management groups
        - [ ] Ensure individual servers can be isolated if needed for [incident response](../guidelines/playbooks.md) and [vulnerability management](../baselines/vulnerability-management.md)
    - [ ] Define and segment Operational Technology (OT) devices into management groups ()
        - [ ] Constrain traffic for each management group to its minimum requirements for management and serviceability
        - [ ] Ensure all devices are tagged at the point of access
        - [ ] Ensure all inter-site traffic between OT devices is encrypted

#### Observability & Manageability

Network security and management becomes much more effective once administrators have visibility over [useful logs](https://soc.cyber.wa.gov.au/guidelines/further-five/#implementation-guidance-leveraging-computer-related-logs) (baseline network activity, app & user identification, DNS, NetFlow data, firewall logs, HTTP/HTTPS sessions, etc). Having the ability to tie logs to specific apps and users both improves network segmentation capabilities and quality of log data for investigation and observation purposes. Products such as:

- [Cisco DNA Cloud](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/dna-center/nb-06-dna-center-data-sheet-cte-en.html)

- Palo Alto Panorama

- Fortigate Cloud

- VMware [SD-WAN and SASE](https://sase.vmware.com/sd-wan/security-services) with VMware Secure Access

- [Check Point Quantum](https://www.checkpoint.com/quantum/next-generation-firewall/)

Will give visibility over many of these areas to improve observability and manageability of networks. Next-Gen firewalls are an effective way to implement this when leveraging the above cloud services.

#### Adverse Event Analysis

Detailed logging mentioned in *Observability & Manageability* allows agencies to perform event analysis both automated and manual. Understanding inventory and baseline activity allows anomaly detection. Most if not all of the products mentioned in this guidance have some capability for continuous threat detection and monitoring, real-time detection and response, or at the very least log forwarding options that can allow your SIEM to ingest data and perform alerting based on SIEM rules.

- Cisco [Security Network Analytics](https://www.cisco.com/c/en/us/products/collateral/security/stealthwatch/datasheet-c78-739398.html) -- Provides baseline network monitoring and anomaly detection.

- Palo Alto [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud/cloud-network-security) - Anomaly policies use audit logs and network flow logs to help you identify unusual network and user activity for all users.

    - [Cortex XDR](https://www.paloaltonetworks.com/engage/cortex-extended-detection-and-response/cortex-xdr-datasheet) - Real-time response and monitoring

- Check Point [CloudGuard](https://www.checkpoint.com/cloudguard/) - Cloud workload centric solution for threat detection including [anomaly detection](https://blog.checkpoint.com/securing-the-cloud/cloudguard-intelligence-threat-hunting/) for abnormal network behaviour.

    - [Horizon NDR](https://www.checkpoint.com/horizon/ndr/) - Network Detection and Response

- Fortinet - [FortiNDR](https://www.fortinet.com/content/dam/fortinet/assets/solution-guides/sb-fortindr.pdf)

#### Segmentation

Modern [network segmentation](https://soc.cyber.wa.gov.au/guidelines/further-five/#network-segmentation) helps prevent lateral movement of adversaries in an organisation and allows effective isolation/containment ([RESPOND](https://www.nist.gov/cyberframework/online-learning/five-functions#respond)) when responding to breaches. Through good use of network segmentation agencies can prevent certain devices or groups of devices from ever communicating with each other to adhere with principles of least privilege ([PROTECT](https://www.nist.gov/cyberframework/online-learning/five-functions#protect)) and protect critical infrastructure or sensitive systems. By ensuring all devices on the network can be segmented into appropriate groups, organisations can greatly improve cyber security and modernise their networks for the future. Keeping in the ecosystem of current equipment will reduce complexity for easier adoption:

- Cisco Networks: [Cisco TrustSec](https://www.cisco.com/c/en/us/solutions/enterprise-networks/trustsec/index.html) integrated with Cisco DNA

- Palo Alto: Cloud Managed [Prisma Access](https://www.paloaltonetworks.com/sase/access) (Additional [Documentation](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/guides/sase-segmentation-solution-guide))

- VMware [SD-WAN and SASE](https://sase.vmware.com/sd-wan/security-services)

An agency may start this process by brainstorming appropriate groups to segment devices into and begin to find solutions for incremental changes using products appropriate to their current infrastructure.

## Network Use Cases

- [ ] End Users working flexibly (baseline) - includes users at home/work/offsite accessing resources over the internet
- [ ] Collaborative technologies (Email, Telephony, Video Conferencing, Filesharing)
- [ ] Local access to office resources
- [ ] Remote access to business systems that don't support modern access protocols
- [ ] Remote access to servers (compute & storage) resources
- [ ] Operational Technology (OT) networks - all network connected devices without endpoint agents
    - Industrial Control Systems
    - Building Management Systems
    - Sector specific technology (Critical Infrastructure & Health)
    - Physical security systems (CCTV, Access Systems)
- [ ] Remote access to Operational Technology devices

## Security Goals

With a modern architecture, the goals below can all be delivered using cloud or on-premise network orchestration tools, and in common use cases can largely be outsourced to enterprise telecommunication providers.

- [ ] IDENTIFY - Device inventories and tagging / grouping
- [ ] DETECT - Traffic Analytics
- [ ] PROTECT - Network infrastructure maintenance
- [ ] PROTECT - Protective DNS & outbound traffic filtering
- [ ] PROTECT - Network segmentation (principle of least privilege)
- [ ] RESPOND - Network segmentation (isolation / containment)
