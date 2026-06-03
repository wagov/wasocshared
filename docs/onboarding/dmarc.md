# WASOC DMARC

## Overview

!!! note

    This DMARC pilot program is now an established service catalogue item from the WASOC, as such, access to this service is now available to WA Government Entities upon request.
    If interested in the services, please raise a request via the [WASOC IRP](https://irp.dpc.wa.gov.au/).

The WASOC is looking to enhance the email security posture of Western Australian Government entities by improving visibility and detection of email-based threats targeting domain-based communications. The WASOC will assist entities with the implementation and monitoring of DMARC, DKIM, and SPF controls to protect against domain spoofing, phishing, and business email compromise. This initiative will strengthen the identification of unauthorised email activity and improve the overall resilience of government communication channels.

DMARC provides a mechanism to enhance the detection of unauthorised and malicious email activity by monitoring how domains are used in email communications. Through the implementation of DMARC, organisations can establish policies and reporting capabilities that reflect legitimate email behaviour across their environment.

When threat actors attempt to exploit or spoof organisational domains, DMARC reporting and monitoring can identify these unauthorised activities. This enables security teams to detect suspicious behaviour, gain visibility into email-based threats, and respond to potential risks affecting an entity's communication channels.

??? note "Participants Prerequisite"

    The service has prerequisites that must be met to have the minimum technical & commitment requirements to onboard to the DMARC Pilot Program as to take advantage of the full service offering.

    The prerequisites as follows.

    - Must have signed an exisiting MOU (T0,T1,T2) with the WASOC
    - Must have a Microsoft Sentinel workspace located in region **Australia EAST**
    - Must have been already onboarded to the WASOC via [Azure Lighthouse](https://soc.cyber.wa.gov.au/onboarding/#23-azure-subscription-access-delegation)
    - Must have access to the [WASOC IRP](https://irp.dpc.wa.gov.au/) to raise DMARC request tickets.
    - Must be able nominate a individual from your organisation to work closely with the WASOC Engineering Team during the pilot.

    The onboarding to the DMARC Platform is handled entirely by the WASOC and can be facilitated upon request via the [WASOC IRP](https://irp.dpc.wa.gov.au/).

    The WASOC is willing to work with entities to adapt the platform as fit for purpose for their environment but may not be able to take full advantage of the service offering.

## Onboarding Process

The WASOC has developed guidance to assist Western Australian Government entities in integrating DMARC monitoring and reporting capabilities into their existing Microsoft Sentinel workspaces.This can be found at the [Github pages](https://wagov.github.io/wasoc-dmarc/) or at our [Github repository](https://github.com/wagov/wasoc-dmarc/) for DMA.

## DMARC Guidance

DMARC is an email authentication protocol that builds on SPF and DKIM to help organisations protect their domains from spoofing, phishing, and unauthorised use.

Key Components of DMARC Deployment:

-   Sender Policy Framework (SPF) :\
    Defines which mail servers are authorised to send emails on behalf of the domain.
-   DomainKeys Identified Mail (DKIM):\
    Provides cryptographic validation that email content has not been altered and confirms the sender's domain identity.
-   DMARC Policy:\
    Specifies how receiving systems should handle messages that fail SPF/DKIM checks:

    - none: monitoring only
    - quarantine: mark as suspicious    
    - reject: block the message

-   Reporting (RUA/RUF):\
    Enables aggregate and forensic feedback from receiving systems to provide insight into email authentication performance and potential abuse.

### DMARC Deployment Approach

-   Begin with a monitoring policy (p=none) to baseline legitimate email sources.
-   Analyse DMARC reports to identify authorised and unauthorised senders.
-   Gradually transition to enforcement policies (quarantine → reject) once confidence in legitimate sources is established.
-   Continuously review and update SPF/DKIM configurations to reflect new services or changes.

### Ideal Scope for DMARC Implementation:

DMARC should be applied across all domains that are capable of sending or could be abused for sending emails, including:

-   Primary organisational domains
-   Secondary and legacy domains
-   Domains used by third-party services
-   Internet-facing email systems