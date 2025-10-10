# WA SOC Microsoft Sentinel Guidance

The below guide has been developed by the WASOC to expedite a SIEM implementation with Microsoft Sentinel focused on improving operational efficiency and [better threat detection](https://soc.cyber.wa.gov.au//baselines/data-sources/#4-detection-checklist).

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xu7UIRJ7tBw?si=HupWLNVC5TSjebn1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 1. Sentinel Deployment Notes

It is recommended to deploy Microsoft Sentinel in the **Australia East** region following the [Deployment guide for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/deploy-overview)

!!! note "Transition your Microsoft Sentinel experience from the Azure portal to the Defender portal"

    Important Update: Microsoft is transitioning the Microsoft Sentinel experience from the Azure portal to the Microsoft Defender portal and by July 1, 2026 the Azure portal experience for Microsoft Sentinel will be retired. For customers with an existing workspace enabled for Microsoft Sentinel in order to transition to Microsoft Defender follow the [Transition Microsoft Sentinel environment to the Defender portal Guide](https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender)


## 2. Telemetry to collect (prioritised)

Below is a rapid approach to get Microsoft workloads covered rapidly using Sentinel.

1. [Turn on auditing and health monitoring](https://learn.microsoft.com/en-us/azure/sentinel/enable-monitoring)
1. [Enable User and Entity Behavior Analytics (UEBA)](https://learn.microsoft.com/en-us/azure/sentinel/enable-entity-behavior-analytics)
1. [Microsoft 365 Defender XDR connector](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/microsoft-365-defender)
    1. [Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/step-by-step-guides/step-by-step-guide-overview?view=o365-worldwide)
    1. [Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/quick-installation-guide)
    1. [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mde-planning-guide?view=o365-worldwide) (including [Attack Surface Reduction](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/overview-attack-surface-reduction?view=o365-worldwide))
    1. [Connect Microsoft Defender for Cloud (servers)](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud)
1. [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/microsoft-entra-id) which includes [Entra External ID (CIAM & B2B)](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview)

Steps 1-3 should be straightforward to complete under E5/A5 licencing. Once telemetry is being collected, the [Maturity Model For Event Log Management](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/MaturityModelForEventLogManagementM2131#onboarding-prerequisites) solution adds the capability to detect changes in telemetry quality over time (which supports [Secure Configuration Assessment](../guidelines/secure-configuration.md) of the SIEM environment itself).

### 2.1. SIEM Retention for threat hunting and investigations

[Configuring retention for 12 months](https://learn.microsoft.com/en-us/azure/sentinel/configure-data-retention) is recommended to ensure logs are available for investigations and threat hunting. For high volume telemetry sources, [streaming events to object storage](https://learn.microsoft.com/en-us/defender-xdr/streaming-api-storage) and using [lifecycle management to retain for 365 days](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure?tabs=azure-portal#create-or-manage-a-policy) is a validated alternative that can be queried in place with tools like [DuckDB to Azure Blob storage](https://duckdb.org/docs/extensions/azure.html) (also supports [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) via [S3 API](https://duckdb.org/docs/extensions/httpfs/s3api)), [Azure Data Explorer](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/schema-entities/external-tables) and [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html).

!!! note "Simplify telemetry collection"

    Moving [Configuration Manager to Intune](https://learn.microsoft.com/en-us/mem/intune/fundamentals/deployment-guide-intune-setup), [Fileshares to SharePoint](https://learn.microsoft.com/en-us/sharepointmigration/fileshare-to-odsp-migration-guide) and [Identities from Active Directory to Entra](https://learn.microsoft.com/en-us/entra/architecture/road-to-the-cloud-migrate) are highly effective ways to improve security visibility while also reducing telemetry volume from self-managed platforms and servers.

!!! note "Data Retention and Cost Optimization"

    Microsoft Sentinel uses two primary storage tiers to balance performance, cost, and retention needs:
    [Analytics Tier](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview#data-tiers): High-performance storage for real-time threat detection, hunting, and alerting. Store Microsoft tables (e.g. Defender XDR, Entra ID, Azure activity logs) for up to 90 days at no additional ingestion cost before transitioning to the Data Lake Tier to optimize expenses.
    [Data Lake Tier](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview): Low-cost "cold" storage offering up to 85% cost savings compared to the Analytics Tier. Use this tier to:
    - Ingest third-party logs (e.g., network logs from firewalls, proxies, or AWS CloudTrail) directly to reduce expenses without sacrificing storage capacity.
    - Transfer Microsoft tables from the Analytics Tier after the 90-day free retention period to maintain long-term retention requirements (up to 12 years) for investigations, compliance, and historical analysis.


[Fileshares to SharePoint](https://learn.microsoft.com/en-us/sharepointmigration/fileshare-to-odsp-migration-guide) and [Identities from Active Directory to Entra](https://learn.microsoft.com/en-us/entra/architecture/road-to-the-cloud-migrate) are highly effective ways to improve security visibility while also reducing telemetry volume from self-managed platforms and servers.

## 3. Third party solutions (Telemetry re-ingestion)

!!! note "Log Analytics Auxilary plan (preview)"

    The low cost [Auxiliary plan](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/create-custom-table-auxiliary) is now available in public preview on data collection rule-based custom tables you create using the [Tables - Create Or Update API](https://learn.microsoft.com/en-us/rest/api/loganalytics/tables/create-or-update), which is suitable for retention of third party log sources.

[Deploy domain solutions with ASIM analytic rules](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-catalog#domain-solutions) and connect associated telemetry for relevant products. Note for large environments this can be costly, so moving to incident synchronisation only may be more effective (see next section). Deploying the [ASIM Parsers](https://github.com/Azure/Azure-Sentinel/tree/master/ASIM) directly also makes developing and managing telemetry agnostic detection rules much easier.

- [Endpoint Threat Protection Essentials](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-endpointthreat?tab=Overview)
- [Security Threat Essentials](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-securitythreatessentialsol?tab=Overview)
- [DNS Essentials Solution](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-dns-domain?tab=Overview)
- [Web Session Essentials](https://azuremarketplace.microsoft.com/en-gb/marketplace/apps/azuresentinel.azure-sentinel-solution-websession-domain?tab=Overview)
- [Network Session Essentials](https://azuremarketplace.microsoft.com/en-GB/marketplace/apps/azuresentinel.azure-sentinel-solution-networksession?tab=Overview)

## 4. Third party integrations (Incident synchronisation only)

[Create incidents based on events from systems whose logs are not ingested into Microsoft Sentinel.](https://learn.microsoft.com/en-us/azure/sentinel/create-incident-manually)

The above guide supports the below incident creation flows from third party systems:

- [Create an incident using Azure Logic Apps](https://learn.microsoft.com/en-us/azure/sentinel/create-incident-manually#create-an-incident-using-azure-logic-apps)
    - [Create Incidents with Email](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks/Create%20Incidents%20with%20Email)
    - [Create Incidents from Webhook (HTTP)](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks/Create%20Incidents%20From%20Http)
- [Create an incident using the Microsoft Sentinel API](https://learn.microsoft.com/en-us/azure/sentinel/create-incident-manually#create-an-incident-using-the-microsoft-sentinel-api)

Ensuring that integrations include **severity**, **classification** and **mitre tactic / technique** attributes helps the WASOC triage and prioritise incidents. Additionally incidents with similar subjects or identifiers should be grouped if possible (a good rule of thumb is if something is triggering more than 4 times a day it should be grouped into hourly or larger aggregated incidents).

## 5. Optimise security operations

The [Microsoft SOC Optimisations page](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access?tabs=azure-portal#access-the-soc-optimization-page) aims to empower security teams by providing invaluable insights into your Microsoft Sentinel environment and offering recommendations to enhance cost efficiency, operational effectiveness, and overall management overview. The WASOC also offers an addtional cost reduction service through the [dedicated cluster initative](https://soc.cyber.wa.gov.au//onboarding/#24-dedicated-cluster).
