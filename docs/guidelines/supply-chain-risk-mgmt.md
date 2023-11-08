# Supply Chain Risk Management Guideline

During all procurement and vendor management activities where digital information is handled supply chain risks should be identified and managed.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lyb5MIYLAME?si=S4fPFegah-wJk7IV&amp;start=1560" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Pre-procurement risk assessment

Consider information security risks as a part of procurement and contract risk assessment, informed by the [ACSC Procurement Guidelines](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-procurement-and-outsourcing), [ACSC Supply Chain Risk Management](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/outsourcing-and-procurement/cyber-supply-chains/cyber-supply-chain-risk-management), [ACSC Guidelines for Software Development](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-software-development).

- Perform a risk assessment taking into consideration how the procurement may impact confidentiality, integrity and availability of the entity’s operations, as well as the sensitivity of the information in the scope of the proposed procurement.
- Conduct due diligence on any suppliers’ information security maturity, including, where appropriate, whether the supplier has been independently assessed or certified against information security industry standards
    - For high-risk procurements involving managed service providers and/or cloud service providers, give preference to supplier offerings which have undergone an independent assessment by a qualified assessor under the [ACSC Infosec Registered Assessors Program (IRAP)](https://www.cyber.gov.au/resources-business-and-government/assessment-and-evaluation-programs/infosec-registered-assessors-program) or similar industry certification.
    - Recognised industry certifications: [ACSC ISM](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism) ([IRAP](https://www.cyber.gov.au/resources-business-and-government/assessment-and-evaluation-programs/infosec-registered-assessors-program)), [ISO/IEC 27001:2022](https://www.iso.org/standard/27001), [SOC 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) or [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Understand the shared responsibility model between the supplier and the entity under which services are being contracted and managed

## Template contract clauses promoting information security

Include clauses similar to below when procuring any goods or services that handle digital information.

- **Vulnerability Disclosure:** Notify the customer of confirmed security vulnerabilities in their assets within 24 hours of confirmation.
- **Cyber Incident Detection and Response:** Notify the customer of cyber security incidents within 24 hours of detection.
- **Cyber Security Performance Monitoring:** Provide visibility of [Security Operations](../baselines/security-operations.md) and [Vulnerability Management](../baselines/vulnerability-management.md) activities at least monthly.
- **Cyber Security Assessments:** Undertake an independent cyber security assurance activity across operations in scope of this contract at least every 24 months aligned to ACSC ISM (IRAP), ISO 27k, SOC 2 or NIST SP 800-53 and make available the report including noted exceptions.
- **Information Classification, Retention and Disposal:** Ensure information is secured for the duration of the contract, with secure disposal or transfer at termination of contract.

## Managing Cybersecurity Risk in Supply Chains (NIST)

Key considerations from page 16 and 17 of the [NIST CSF 2.0 Initial Public Draft](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.ipd.pdf) are below, identifying the NIST CSF subcategories relevant for **Information Secure Procurement**.

- **Identify:** Identifying, validating, and recording vulnerabilities associated with the supplier’s product or service [ID.RA-01]
- **Protect:** Authenticating users, services, and hardware [PR.AA-03]; applying appropriate configuration management practices [PR.PS-01]; generating log records and having the logs available for continuous monitoring [PR.PS-04]; and integrating secure software development practices into the supplier’s software development life cycles [PR.PS-07]
- **Detect:** Monitoring computing hardware and software for potentially adverse events [DE.CM-09]
- **Respond:** Executing incident response plans when compromised products or services are involved [RS.MA-01]
- **Recover:** Executing the recovery portion of the organization’s incident response plan when compromised products or services are involved [RC.RP-01], and restoring compromised products or services and verifying their integrity [RC.RP-05]

## ACSC ISM Controls - Contractual security requirements with service providers

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
