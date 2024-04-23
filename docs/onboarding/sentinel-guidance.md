# WA SOC Microsoft Sentinel Guidance

The below guide has been developed by the WASOC to expedite a SIEM implementation with Microsoft Sentinel to align to best align to the [better threat detection](https://soc.cyber.wa.gov.au//baselines/data-sources/#4-detection-checklist).

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xu7UIRJ7tBw?si=HupWLNVC5TSjebn1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 1. Sentinel Deployment Notes

It is recommended to deploy Microsoft Sentinel in the **Australia East** region following the [Deployment guide for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/deploy-overview)

## 2. Telemetry to collect (prioritised)

Below is a rapid approach to get Microsoft workloads covered rapidly using Sentinel.

1. [Turn on auditing and health monitoring](https://learn.microsoft.com/en-us/azure/sentinel/enable-monitoring)
1. [Enable User and Entity Behavior Analytics (UEBA)](https://learn.microsoft.com/en-us/azure/sentinel/enable-entity-behavior-analytics)
1. [Microsoft 365 Defender XDR connector](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/microsoft-365-defender)
    1. [Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/step-by-step-guides/step-by-step-guide-overview?view=o365-worldwide)
    1. [Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/quick-installation-guide)
    1. [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mde-planning-guide?view=o365-worldwide) (including [Attack Surface Reduction](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/overview-attack-surface-reduction?view=o365-worldwide))
    1. [Connect Microsoft Defender for Cloud (servers)](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud)
1. [Microsoft Entra ID (formerley AAD)](https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory)

Steps 1-3 should be straightforward to complete under E5/A5 licencing. Once telemetry is being collected, the [Maturity Model For Event Log Management](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/MaturityModelForEventLogManagementM2131#onboarding-prerequisites) solution adds the capability to detect changes in telemetry quality over time (which supports [Secure Configuration Assessment](../guidelines/secure-configuration.md) of the SIEM environment itself).

## 3. Third party solutions (Telemetry re-ingestion)

[Deploy domain solutions with ASIM analytic rules](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-catalog#domain-solutions) and connect associated telemetry for relevant products. Note for large environments this can be costly, so moving to incident synchronisation only may be more effective (see next section). Deploying the [ASIM Parsers](https://github.com/Azure/Azure-Sentinel/tree/master/ASIM) directly also makes developing and managing telemetry agnostic detection rules much easier.

- [Endpoint Threat Protection Essentials](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-endpointthreat?tab=Overview)
- [Security Threat Essentials](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-securitythreatessentialsol?tab=Overview)
- [DNS Essentials Solution](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-dns-domain?tab=Overview)
- [Web Session Essentials](https://azuremarketplace.microsoft.com/en-gb/marketplace/apps/azuresentinel.azure-sentinel-solution-websession-domain?tab=Overview)
- [Network Session Essentials](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-networksession?tab=Overview)

## 4. Third party integrations (Incident synchronisation only)

[Create incidents based on events from systems whose logs are not ingested into Microsoft Sentinel.](https://learn.microsoft.com/en-us/azure/sentinel/create-incident-manually)

The above guide supports the below incident creation flows from third party systems (ideally for these integrations aim to ensure that **classification**, **severity** are set and related incidents are grouped):

- [Create an incident using Azure Logic Apps](https://learn.microsoft.com/en-us/azure/sentinel/create-incident-manually#create-an-incident-using-azure-logic-apps)
    - [Create Incidents with Email](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks/Create%20Incidents%20with%20Email)
    - [Create Incidents from Webhook (HTTP)](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks/Create%20Incidents%20From%20Http)
- [Create an incident using the Microsoft Sentinel API](https://learn.microsoft.com/en-us/azure/sentinel/create-incident-manually#create-an-incident-using-the-microsoft-sentinel-api)

Including **severity**, **classification** and **mitre tactic / technique** attributes helps the WASOC triage and prioritise incidents.

## 5. Performance and cost optimisation

The [Microsoft Sentinel Optimization Workbook](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/introducing-microsoft-sentinel-optimization-workbook/ba-p/3901489) aims to empower security teams by providing invaluable insights into your Microsoft Sentinel environment and offering recommendations to enhance cost efficiency, operational effectiveness, and overall management overview. The WASOC also offers an addtional cost reduction service through the [dedicated cluster initative](https://soc.cyber.wa.gov.au//onboarding/#24-dedicated-cluster).
