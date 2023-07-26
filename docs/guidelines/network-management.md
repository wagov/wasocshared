# Network Management Guideline (DRAFT)

This guideline is intended to define a pragmatic target for an entities network architecture to enable effective network management with modern tooling. This guide is structured around the [use cases for a complex network](#network-use-cases) with a design that can be adopted incrementally based on an agencies requirements.

add some content regarding complexity reduction, and exposure minimisation (e.g. all internet facing services should be fully managed public/network cloud, avoid legacy VPN's (IPSEC/SSL) over modern ones (MASQUE/wireguard))

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

### Additional considerations for Operational Technology and on-premise servers and/or entities with > 500 staff

- [ ] Ensure network incidents are captured appropriately in a central SIEM ( [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview), [Cisco SecureX](https://www.cisco.com/c/en/us/products/collateral/security/securex/at-a-glance-c45-744497.html?CCID=cc001528&DTID=olgmcdc001463&OID=trlsc021059), [Palo XSOAR](https://xsoar.pan.dev/docs/concepts/getting-started-guide) )
- [ ] Segment all fully managed endpoints (desktops, laptops, desk phones, mobiles) from critical infrastructure or sensitive information systems
    - [ ] Define and segment on-premise servers into management groups
        - [ ] Ensure individual servers can be isolated if needed for [incident response](../guidelines/playbooks.md) and [vulnerability management](../baselines/vulnerability-management.md)
    - [ ] Define and segment Operational Technology (OT) devices into management groups ()
        - [ ] Constrain traffic for each management group to its minimum requirements for management and serviceability
        - [ ] Ensure all devices are tagged at the point of access
        - [ ] Ensure all inter-site traffic between OT devices is encrypted
        - [ ] Limit remote access to OT devices using internet based Zero Trust Network Access solutions ( [Microsoft Entra Private Access](https://learn.microsoft.com/en-gb/azure/global-secure-access/overview-what-is-global-secure-access), [Cisco Umbrella SASE](https://www.cisco.com/c/en/us/products/collateral/security/at-a-glance-c45-2391315.html), [Palo PRISMA Access](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access) )

#### Observability & Manageability

reference device / asset visibility and access logs (IDENTIFY)

note Cisco DNA cloud / Panorama / Fortigate Cloud

#### Adverse Event Analysis

reference continuous detection and response (NDR - DETECT)

#### Segmentation

reference network segmentation (PROTECT / RESPOND)

- [Cisco TrustSec](https://www.cisco.com/c/en/us/solutions/enterprise-networks/trustsec/index.html)

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