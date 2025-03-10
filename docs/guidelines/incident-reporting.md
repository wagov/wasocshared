# WA SOC Incident Reporting Portal (IRP)

## 1. Overview

The cyber security incident reporting portal provides a secured login for each Western Australian government agency to:

- report cyber incidents
- enable coordination of incident response
- receive updates on ongoing cyber security events and topics

<img width="700" alt="Portal Overview" src="../../images/portal-overview.png">

### 1.1 Cyber Incident Response Plan

All agencies should have a **Cyber Incident Response Plan** ([ACSC Practitioner Guidance](https://www.cyber.gov.au/resources-business-and-government/governance-and-user-education/incident-response/cyber-security-incident-response-planning-practitioner-guidance) updated April 2024, [pdf](https://www.cyber.gov.au/sites/default/files/2024-04/PROTECT%20-%20Cyber%20Security%20Incident%20Response%20Planning%20-%20Practitioner%20Guidance%20%28April%202024%29.pdf) also available) defined that clearly outlines the work to ensure an effective response and prompt recovery in the event security controls don’t prevent an incident occurring. This plan should be tested and regularly reviewed.

ACSC also published an excellent [ACSC Cyber Incident Response Plan - Word Template - March 2023 (docx)](https://www.cyber.gov.au/sites/default/files/2023-03/ACSC-Cyber-Incident-Response-Plan-Template.docx) suitable for tailoring to an organisations specific context. The guidance includes some highly relevant appendices:

!!! abstract "Incident Response Appendices"

    - Appendix A - Terminology and definitions
    - Appendix B - Cyber Security Incident Response Readiness Checklist
    - Appendix C - ASD cyber security incident triage questions
    - Appendix D - Situation Report Template
    - Appendix E - Cyber Security Incident Log Template
    - Appendix F - Evidence Register Template
    - Appendix G - Remediation Action Plan Template
    - Appendix H - Post cyber security incident reviews
    - Appendix I - Action Register Template
    - Appendix J - Role cards
    - Appendix K - ASD Cyber Security Incident Categorisation Matrix

### 1.2 ACSC Incident Categorisation Matrix

<img width="700" alt="ACSC Incident Categorisation Matrix 2022" src="https://www.cyber.gov.au/sites/default/files/2024-04/Cyber%20Security%20Incident%20Response%20Planning%20Image%204.png">

## 2. Getting access

- Agencies can request access by emailing [cybersecurity@dpc.wa.gov.au](mailto:cybersecurity@dpc.wa.gov.au).
- Agencies with existing access can use the [Request access to the Incident Reporting Portal](https://wasoc.atlassian.net/servicedesk/customer/portal/2/group/1/create/103) WASOC IRP form.

### 2.1. Logging in to the WASOC IRP

The [WA Security Operations Centre - IRP](https://wasoc.atlassian.net/servicedesk/customer/portals "https://wasoc.atlassian.net/servicedesk/customer/portals") is accessible using any modern browser.

When logging in you will be prompted to use Single Sign On, please do this and **Continue with Microsoft** for your Atlassian Identity.

## 3. Creating a Cybersecurity Incident

- [Report a cyber incident](https://wasoc.atlassian.net/servicedesk/customer/portal/2/group/1/create/19) - WASOC IRP form
    - Enter the details of your incident
    - Select **Share with** your organisation
- SIEM Sentinel incidents will be automatically integrated with the IRP for monitored customers.
- To manage alerting and integrations, please use the [Request Assistance](https://wasoc.atlassian.net/servicedesk/customer/portal/2/group/1/create/1) WASOC IRP form

## 4. Managing your Cybersecurity Incidents

You can view all of your security teams incidents on the [Requests page](https://wasoc.atlassian.net/servicedesk/customer/user/requests?page=1&reporter=all) in the WASOC IRP.

The below actions can be taken on your incidents, noting that all standard activities (classification, severity, labeling, comments) should be able to be undertaken in your SIEM and automatically synced to the IRP.

- Search existing incidents by summary, description or entities
- Add comment/ updates to an Incident
    - If you add comments in your SIEM they will sync automatically
    - Attachments and Non-SIEM Incidents can be directly commented on in the portal
- Request assistance
- Create a post-incident review
    - The WA SOC can review your PIR and provide additional context as needed

### 4.1. Managing your SIEM Sentinel Analytic Rules

If your team is seeing a lot of false positive detections, please review [Handle false positives in Microsoft Sentinel
](https://docs.microsoft.com/en-us/azure/sentinel/false-positives) and reach out to the SOC using [Request Assistance](https://wasoc.atlassian.net/servicedesk/customer/portal/2/group/1/create/1) for further advice.

## 5. General security advice

For any other SIEM advice, general security problems and questions don't hesitate to reach out to the SOC using [Request Assistance](https://wasoc.atlassian.net/servicedesk/customer/portal/2/group/1/create/1). For any urgent incidents please call us on Teams or via phone.

## 6. Monthly Reporting

The below aggregate statistics are being captured by the new portal and will be available in the SOC monthly reports for your organisation. Monthly reports are under review to align them to the [WA Government Cyber Security Policy](https://www.wa.gov.au/government/publications/wa-government-cyber-security-policy) and the [NIST Cyber Security Framework](https://www.nist.gov/cyberframework).

- Incident statistics
    - Total Detections
    - Triage types (automated, manual)
    - True / False / Benign breakdown
- [MITRE Data Sources overview (SIEM event coverage)](../baselines/data-sources.md)
- [MITRE TTP Detection overview (Detection Analytics coverage)](https://attack.mitre.org/matrices/enterprise/)
