# Network Management Guideline

This guideline is a pragmatic target for an entity's network architecture to enable effective and secure network management while minimising complexity. This guide is structured around the [use cases for a complex network](#common-network-use-cases) with a design that can be adopted in stages that is highly aligned with the [ACSC Network gateway hardening](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-hardening/gateway-security-guidance-package-executive-guidance) guidance package.

!!! note "Quick network security for Microsoft 365 customers"
    Rapidly implement **identify**, **detect** and some **protect** controls with minimal user facing / network hardware changes:

    - Implement [Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/deploy/quick-installation-guide) to **monitor identities, DNS, Kerberos and LDAP traffic**
    - [Turn on network protection](https://learn.microsoft.com/en-us/defender-endpoint/enable-network-protection) to **monitor endpoint traffic** and [enable UEBA](https://learn.microsoft.com/en-us/azure/sentinel/enable-entity-behavior-analytics?tabs=azure)
    - Implement [Per-app Access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-per-app-access) for user access to corporate resources (including [on-prem servers and DCs](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/microsoft-entra-private-access-for-on-prem-users/ba-p/3905450)) to **monitor application traffic**

    The below steps can take months to years, but won't impede the risk reduction from the above quick steps:

    - Implement [webauthn (passkeys/fido)](https://github.com/herrjemand/awesome-webauthn) with centrally logged [CIAM](https://learn.microsoft.com/en-us/entra/external-id/customers/overview-customers-ciam) for all internet exposed (i.e. citizen facing) systems
    - Deny direct network access to applications and iteratively improve network topology

![Network topology utilising recommended modern SASE solutions.](../images/Network-SASE.png)

## Contemporary Network Architecture

Organisations should strive to reduce network complexity and focus on the key outcome of connecting staff to systems securely. They should mitigate risks as much as possible by favouring managed cloud services with segregated control planes (as opposed to local direct management and the associated privileged access / shared credential complexity) and steering clear of legacy technologies such as direct Layer 3 network access.

### Remote Access for staff and vendors

It's strongly recommended to transition from traditional VPNs to modern Secure Service Edge (SSE) platforms, that can also improve the application of network policies across an organisation. SSE and SASE platforms are available from:

- Infrastructure providers ([Microsoft Security Service Edge](https://learn.microsoft.com/en-us/entra/architecture/sse-deployment-guide-intro), [VMWare SASE](https://sase.vmware.com/sd-wan/security-services))
- Network hardware vendors ([Check Point Harmony Connect](https://www.checkpoint.com/harmony/connect-sase/), [Cisco Secure Access](https://www.cisco.com/site/us/en/products/security/secure-access/index.html), [FortiSASE](https://www.fortinet.com/products/sase),  [Palo Alto Prisma SASE](https://www.paloaltonetworks.com/sase/access))
- Virtual network vendors ([Claroty SRA](https://claroty.com/industrial-cybersecurity/sra), [Teleport (open-source with self-hosted capability)](https://goteleport.com), [Netskope SASE](https://www.netskope.com/solutions/secure-access-service-edge), [Zscaler SASE](https://www.zscaler.com/capabilities/secure-access-service-edge)), [knocknoc.io (convenient for legacy systems with not many users)](https://knocknoc.io/how-it-works/)

These platforms all incorporate zero trust and policy-based access logging and management out of the box and are strongly recommended for where direct network access to legacy systems is still required. All vendors, contractors and identities external to an organisation should have access controlled via such a platform to avoid third party persistent remote access (e.g. TeamViewer, LogMeIn, AnyDesk) being utilised that may not adhere to an organisations Identity and Access Management policies and procedures.

SANS ICS has a good video on secure approaches for accessing highly privileged ICS/OT environments below:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/-XEdb-B4dCo?si=m0DvcpkJondh3rBM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Observability & Manageability

Network security and management becomes much more effective once administrators have visibility over [useful logs](https://soc.cyber.wa.gov.au/guidelines/further-five/#implementation-guidance-leveraging-network-related-logs) (baseline network activity, app & user identification, DNS, NetFlow data, firewall logs, HTTP/HTTPS sessions, etc). Having the ability to tie logs to specific apps and users both improves network segmentation capabilities and quality of log data for investigation and observation purposes. Most telco's have effective SD-WAN management capabilities ( [Aussie Broadband](https://www.aussiebroadband.com.au/enterprise/network/sd-wan/), [Optus](https://www.optus.com.au/enterprise/networking/network-connectivity/fusion-sd-wan), [Telstra](https://www.telstra.com.au/business-enterprise/products/networks/sdn/sd-wan), [TPG](https://www.tpgtelecom.com.au/business-solutions/sd-wan), [Vocus](https://www.vocus.com.au/enterprise/connectivity/managed-network-services/sd-wan) ), while still allowing an organisation read-only access for capacity and security management functions. Organisations with the requirement and capability to manage network equipment should look towards using modern hardware with a secure cloud control plane ( [Cisco DNA Center (including meraki)](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/dna-center/nb-06-dna-center-data-sheet-cte-en.html), [Forticloud](https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiCloud.pdf) ) that enable simple device management and telemetry access for all gateways, routers, switches and access points.

### Web Application Firewalls (WAFs) and Content Delivery Networks (CDNs)

In addition to standard IP session telemetry, systems and APIs exposed to the internet that aren't protected by an SSE/SASE platform as described above should have a caching CDN and fully blocking WAF deployed between them and the internet to [protect from Web Application Abuse (ACSC)](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/preventing-web-application-access-control-abuse). Deploying and implementing a cloud based CDN and WAF such as [Akamai](https://www.akamai.com/products/app-and-api-protector), [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html), [Azure Front Door](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview), [Cloudflare](https://www.cloudflare.com/en-au/application-services/products/waf/), [F5XC](https://docs.cloud.f5.com/docs/quick-start/service-chaining-cdn-waap), [Fastly](https://www.fastly.com/products/web-application-api-protection) or [Imperva](https://docs.imperva.com/bundle/cloud-application-security/page/introducing/overview.htm) in front of all internet exposed services is strongly recommended, as they avoid the significant risk of exposing any self-managed infrastructure directly to the internet. All of the products listed have significant detection capabilities that can also be integrated with an organisations SIEM for visibility by [security operations](../baselines/security-operations.md) teams.

### Route Origin Authorisations (ROA) and Resource Public Key Infrastructure (RPKI)

As per the [ACSC Gateway Security Guidance Package: Gateway Operations and Management](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-hardening/gateway-security-guidance-package-gateway-operations-management) Organisations should periodically audit their Internet number (ASN) resource assets running Border Gateway Protocol (BGP) by validating RPKI and ROA are established with Internet Service Providers (ISPs) and internet router management teams.

## Adverse Event Analysis and Asset Inventory

Maintaining an up to date asset inventory and monitoring baseline activity enable network anomaly detection. Most if not all the products mentioned in this guideline have some capability for continuous threat detection and monitoring, real-time detection and response, or at the very least log forwarding options that can allow you SIEM to ingest data and perform alerting based on SIEM rules. The below tools notably provide tunable detection analytics linked into basic case management for security operations.

| **Vendor**      | **Network Analytics**                                                                                                                 | **Detection & Response**                                                                                          | **Asset Inventory**                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Cisco**       | [Secure Network Analytics](https://www.cisco.com/site/us/en/products/security/security-analytics/secure-network-analytics/index.html) | [Cisco XDR](https://www.cisco.com/site/au/en/products/security/xdr/index.html)                                    | [Cisco Cyber Vision](https://www.cisco.com/site/us/en/products/security/industrial-security/cyber-vision/index.html)           |
| **Palo Alto**   | [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud/cloud-network-security)                                                  | [Cortex XDR](https://www.paloaltonetworks.com/engage/cortex-extended-detection-and-response/cortex-xdr-datasheet) | [IoT Security](https://docs.paloaltonetworks.com/iot/iot-security-admin/iot-security-solution/iot-security-solution-structure) |
| **Check Point** | [CloudGuard](https://www.checkpoint.com/cloudguard/)                                                                                  | [Horizon NDR](https://www.checkpoint.com/horizon/ndr/)                                                            | [Claroty xDome](https://claroty.com/industrial-cybersecurity/xdome)                                                            |
| **Fortinet**    | [FortiAnalyzer](https://www.fortinet.com/products/management/fortianalyzer)                                                           | [FortiNDR](https://www.fortinet.com/content/dam/fortinet/assets/solution-guides/sb-fortindr.pdf)                  | [Claroty xDome](https://claroty.com/industrial-cybersecurity/xdome)                                                            |

## Segmentation

Modern [network segmentation](https://soc.cyber.wa.gov.au/guidelines/further-five/#network-segmentation) helps prevent lateral movement of adversaries in an organisation and allows effective isolation/containment when responding to breaches. Through good use of network segmentation agencies can prevent certain devices or groups of devices from ever communicating with each other to adhere with principles of least privilege and protect critical infrastructure or sensitive systems. Modern SSE technologies such as those mentioned above can implement tag-based network segmentation across a broad enterprise SD-WAN including public cloud assets with appropriate egress flow monitoring. Additionally the ongoing traffic analytics from central control planes enable rapid analysis and understanding of common network flows, to simplify ongoing firewall policy management and security improvements.

Response actions may also require rapid isolation of sections of the network - a separate secure control plane (as is standard with SD-WAN and SASE architectures) with the ability to rapidly enact policy, physical and logical management boundaries between networks makes this much simpler to implement rapidly when required.

### Operational Technology

Entities with business critical OT/ICS/SCADA assets should run a distinct operational network with associated specialist resources, that ensures encryption over all backhaul links and full segmentation from "untrusted" user networks. The cost of edge routers with full encrypted transit and management capabilities has fallen significantly, see [Cisco Extended Enterprise SD-WAN with IR1101 Solution Overview](https://www.cisco.com/c/en/us/solutions/collateral/enterprise/design-zone-industry-solutions/solution-overview-c22-743249.html) for an example approach with modern cloud managed hardware.

![cisco ir1101](https://www.cisco.com/c/dam/en/us/solutions/collateral/enterprise/design-zone-industry-solutions/solution-overview-c22-743249.docx/_jcr_content/renditions/solution-overview-c22-743249_1.jpg)

## Common Network Use Cases

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
