# Supply Chain Risk Management Guideline

During all procurement and vendor management activities where digital information is handled supply chain risks should be identified and managed. This page follows the principles in the [CISA Supply Chain Risk Management Essentials (2 page PDF)](https://www.cisa.gov/sites/default/files/publications/ict_scrm_essentials_508.pdf) and is fully aligned with the [WA Gov CSP](https://www.wa.gov.au/government/publications/wa-government-cyber-security-policy) and the [ACSC ISM Controls](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism).

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/qvFfoHxfBqY?si=2VsaNSqPTnxaWqSM&amp;start=1560" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

!!! success "Federal Certified Service Providers"
    The federal government has established the [Hosting Certification Framework](https://www.hostingcertification.gov.au/framework) for sensitive government data, whole-of-government systems and systems rated at the classification level of PROTECTED (similar to state [OFFICIAL: Sensitive](https://www.wa.gov.au/government/publications/western-australian-information-classification-policy)), which includes a pre-qualified list of [Certified Service Providers](https://www.hostingcertification.gov.au/certified-service-providers).

## Pre-procurement risk assessment

Consider information security risks as a part of procurement and contract risk assessment, informed by the [ACSC Procurement Guidelines](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-procurement-and-outsourcing), [ACSC Supply Chain Risk Management](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/outsourcing-and-procurement/cyber-supply-chains/cyber-supply-chain-risk-management), [ACSC Guidelines for Software Development](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-software-development).

- Perform a risk assessment taking into consideration how the procurement may impact confidentiality, integrity and availability of the entity’s operations, as well as the sensitivity of the information in the scope of the proposed procurement.
- Conduct due diligence on any suppliers’ information security maturity, including, where appropriate, whether the supplier has been independently assessed or certified against information security industry standards
    - For high-risk procurements involving managed service providers and/or cloud service providers, give preference to supplier offerings which have undergone an independent assessment by a qualified assessor under the [ACSC Infosec Registered Assessors Program (IRAP)](https://www.cyber.gov.au/resources-business-and-government/assessment-and-evaluation-programs/infosec-registered-assessors-program) or similar industry certification.
    - Recognised industry certifications: [ACSC ISM](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism) ([IRAP](https://www.cyber.gov.au/resources-business-and-government/assessment-and-evaluation-programs/infosec-registered-assessors-program)), [ISO/IEC 27001:2022](https://www.iso.org/standard/27001), [SOC 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) or [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Understand the shared responsibility model between the supplier and the entity under which services are being contracted and managed.

!!! warning "Software Development"
    Where development is being outsourced including for managed services, the [ACSC Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Security-by-Design and Default](https://www.cyber.gov.au/about-us/view-all-content/publications/principles-and-approaches-for-security-by-design-and-default) should be followed.

!!! warning "Gateway Operators (Network and Internet managed services)"
    Where network management services are being outsourced, the [ACSC Gateway Hardening](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-hardening) security guidance should be followed. Please also refer to the [WA SOC Network Management Guideline](../guidelines/network-management.md)

## Template contract clauses promoting information security

Include clauses similar to below when procuring any goods or services that handle digital information.

- **Vulnerability Disclosure:** Notify the customer of confirmed security vulnerabilities in their assets within 24 hours of confirmation.
- **Cyber Incident Detection and Response:** Notify the customer of cyber security incidents within 24 hours of detection.
- **Cyber Security Performance Monitoring:** Provide visibility of [Security Operations](../baselines/security-operations.md) and [Vulnerability Management](../baselines/vulnerability-management.md) through an online portal (preferred) or monthly reports (fallback).
    - **Security Operations** should include performance metrics collected, [MITRE data sources](https://attack.mitre.org/datasources/) analysed for adverse events, and security incidents triaged by [MITRE ATT&CK category](https://attack.mitre.org).
    - **Vulnerability Management** should include [asset inventory](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-system-management), [secure configuration assessments](https://soc.cyber.wa.gov.au/guidelines/secure-configuration/), [vulnerability assessment scope and outstanding vulnerabilities](https://soc.cyber.wa.gov.au/baselines/vulnerability-management/).
- **Cyber Security Assessments:** Undertake an independent cyber security assurance activity across operations in scope of this contract at least every 24 months aligned to ACSC ISM (IRAP), ISO 27k, SOC 2 or NIST SP 800-53 and make available the report including noted exceptions.
- **Information Classification, Retention and Disposal:** Ensure information is secured for the duration of the contract, with secure disposal or transfer at termination of contract.

## Managing Cybersecurity Risk in Supply Chains (NIST)

Key considerations from the [NIST CSF 2.0: CYBERSECURITY SUPPLY CHAIN RISK MANAGEMENT (C-SCRM)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1305.ipd.pdf) are below, identifying the subcategories relevant for **Information Secure Procurement**.

### Govern

- **Organizational Context:** Legal, regulatory, and contractual requirements regarding cybersecurity including privacy and civil liberties obligations are understood and managed \[GV.OC-03\]
- **Roles, Responsibilities, and Authorities:** Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced \[GV.RR02\]
- **Cybersecurity Supply Chain Risk Management:** Cyber supply chain risk management processes are identified, established, managed, monitored, and improved by organizational stakeholders \[GV.SC\]

### Identify

- **Risk Assessment:** The authenticity and integrity of hardware and software are assessed prior to acquisition and use \[ID.RA-09\]; Critical suppliers are assessed prior to acquisition \[ID.RA-10\]
- **Improvement:** Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties \[ID.IM-02\]

### Protect

- **Identity Management, Authentication, and Access Control:** Identities and credentials for authorized users, services, and hardware are managed by the organization \[PR.AA-01\]
- **Awareness and Training:** Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind \[PR.AT-02\]

### Detect

- **Continuous Monitoring:** Personnel activity and technology usage are monitored to find potentially adverse events \[DE.CM-03\]

### Respond

- **Incident Management:** Incidents are escalated or elevated as needed \[RS.MA-04\]
- **Incident Response Reporting and Communication:** Internal and external stakeholders are notified of incidents \[RS.CO-02\]

### Recover

- **Incident Recovery Plan Execution:** The integrity of backups and other restoration assets is verified before using them for restoration \[RC.RP-03\]
- **Incident Recovery Communication:** Recovery activities and progress in restoring operational capabilities are communicated to designated internal and external stakeholders \[RC.CO-03\]

## Device as a Service (DaaS) options for Computing and Mobile Devices

An organisation can partially outsource asset and vulnerability management across it's end user fleet to a Device as a Service (DaaS) provider. If management is outsourced, ensure the provider is using an endpoint management platform able to meet the above [procurement clauses](#template-contract-clauses-promoting-information-security). See the below list for [Computing and Mobile Devices CUACMD2021](https://www.wa.gov.au/government/cuas/computing-and-mobile-devices-cuacmd2021) manufacturer agnostic DaaS providers.

- [CDM's Desktop as a Service](https://cdm.com.au/solutions/modern-workplace/)
- [Compnow’s Device as a Service](https://www.compnow.com.au/capabilities/lifecycle-management/)
- [Data#3’s Device as a Service](https://www.data3.com/solutions/modern-workplace/end-user-devices/device-as-a-service/)
- [JB Hi-Fi Business Device as a Service](https://www.jbhifi.business/daas)
- [stotthoare Desktop as a Service](https://stotthoare.com.au/capabilities/managed-services/device-as-a-service/)

Additionally see the [Telecommunications Solutions CUATEL2021](https://www.wa.gov.au/government/cuas/telecommunications-solutions-cuatel2021) for services that could be combined with mobile devices.

- [Optus Managed Desktop Service](http://smb.optus.com.au/opfiles/Business/PDFs/Managed_Desktop_Services_Factsheet.pdf)
- [Telstra Microsoft Surface as a Service](https://www.telstra.com.au/business-enterprise/products/mobility-solutions/plans-and-devices/surface-as-a-service)

## ACSC ISM Controls - Contractual security requirements with service providers

These are all lifted from the  [ACSC Procurement Guidelines](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-procurement-and-outsourcing).

- **Control: ISM-1793; Revision: 0; Updated: Sep-22;** Managed service providers and their managed services undergo a security assessment by an IRAP assessor at least every 24 months.
- **Control: ISM-1570; Revision: 1; Updated: Jun-22;** Outsourced cloud service providers and their cloud services undergo a security assessment by an IRAP assessor at least every 24 months.
- **Control: ISM-1395; Revision: 7; Updated: Dec-22;** Service providers, including any subcontractors, provide an appropriate level of protection for any data entrusted to them or their services.
- **Control: ISM-0072; Revision: 9; Updated: Dec-22;** Security requirements associated with the confidentiality, integrity and availability of data are documented in contractual arrangements with service providers and reviewed on a regular and ongoing basis to ensure they remain fit for purpose.
- **Control: ISM-1571; Revision: 3; Updated: Dec-22;** The right to verify compliance with security requirements is documented in contractual arrangements with service providers.
- **Control: ISM-1738; Revision: 1; Updated: Dec-22;** The right to verify compliance with security requirements documented in contractual arrangements with service providers is exercised on a regular and ongoing basis.
- **Control: ISM-1804; Revision: 0; Updated: Dec-22;** Break clauses associated with failure to meet security requirements are documented in contractual arrangements with service providers.
- **Control: ISM-0141; Revision: 7; Updated: Dec-22;** The requirement for service providers to report cyber security incidents to a designated point of contact as soon as possible after they occur or are discovered is documented in contractual arrangements with service providers.
- **Control: ISM-1794; Revision: 1; Updated: Dec-22;** A minimum notification period of one month by service providers for significant changes to their own service provider arrangements is documented in contractual arrangements with service providers.
- **Control: ISM-1451; Revision: 4; Updated: Dec-22;** Types of data and its ownership is documented in contractual arrangements with service providers.
- **Control: ISM-1572; Revision: 3; Updated: Jun-23;** The regions or availability zones where data will be processed, stored and communicated, as well as a minimum notification period for any configuration changes, is documented in contractual arrangements with service providers.
- **Control: ISM-1573; Revision: 3; Updated: Dec-22;** Access to all logs relating to an organisation's data and services is documented in contractual arrangements with service providers.
- **Control: ISM-1574; Revision: 3; Updated: Dec-22;** The storage of data in a portable manner that allows for backups, service migration and service decommissioning without any loss of data is documented in contractual arrangements with service providers.
- **Control: ISM-1575; Revision: 1; Updated: Dec-22;** A minimum notification period of one month for the cessation of any services by a service provider is documented in contractual arrangements with service providers.
- **Control: ISM-1073; Revision: 5; Updated: Jun-21;** An organisation's systems and data are not accessed or administered by a service provider unless a contractual arrangement exists between the organisation and the service provider to do so.
- **Control: ISM-1576; Revision: 2; Updated: Mar-22;** If an organisation's systems or data are accessed or administered by a service provider in an unauthorised manner, the organisation is immediately notified.
