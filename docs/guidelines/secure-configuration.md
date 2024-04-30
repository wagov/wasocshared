# Secure Configuration Assessment Guideline

This guideline is intended to define a simple approach to ongoing monitoring and assurance of secure configuration of common tools and platforms.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/g22fKjtMS4I?si=Z7_ZxAQDV-A0K8VL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Email, File sharing and Endpoint configuration monitoring

The standard recommended actions within [Microsoft Defender](https://security.microsoft.com/securescore?viewid=actions) should be reviewed and exported each month and retained for 12 months.

### Enhanced validation of cloud service configuration

A backup of tenant configuration should be taken each month with [Microsoft365DSC - Your Cloud Configuration](https://microsoft365dsc.com) and archived to a Git repository or equivalent VCS tool that allows monitoring of configuration drift.

A tool to review tenant configuration such as the [CISA ScubaGear M365 Secure Configuration Baseline Assessment Tool](https://github.com/cisagov/ScubaGear) should be run against all tenants at least quarterly with results reviewed and retained for 12 months to guide policy remediations and improvements.

![Microsoft365DSC Export](https://microsoft365dsc.com/Images/Marketing-Export.gif)

### Enhanced validation of endpoint configuration

The [ACSC’s Cyber Toolbox](https://www.cyber.gov.au/about-us/news/essential-eight-assessment-guidance-package) is comprised of the Essential Eight Maturity Verification Tool (E8MVT) and the Application Control Verification Tool (ACVT) which should be run against a sampling of endpoints on at least a quarterly basis with results reviewed and retained for 12 months to guide policy remediations and improvements.

## Infrastructure (public cloud and on-premise compute and storage) configuration monitoring

The standard recommended actions within CSPM tools such as [Microsoft Defender for Cloud](https://portal.azure.com/#view/Microsoft_Azure_Security/SecurityMenuBlade/~/5), [AWS Security Hub](https://aws.amazon.com/security-hub/), [Oracle Cloud Guard](https://www.oracle.com/au/security/cloud-security/cloud-guard/) and [Google Cloud Security Command Centre](https://cloud.google.com/security-command-center) should be reviewed and exported each month and retained for 12 months. It is strongly recommended to ensure checks are configured against the ACSC ISM and NIST CSF (SP 800-53 R5) using compliance dashboards where possible:

- [Microsoft Defender for Cloud Compliance Dashboard](https://learn.microsoft.com/en-us/azure/defender-for-cloud/update-regulatory-compliance-packages)
- [Deploying a Conformance Pack Using the AWS Config Console](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-console.html)
- [Oracle Cloud Guard](https://www.oracle.com/au/security/cloud-security/cloud-guard/) and [Oracle Data Safe](https://www.oracle.com/au/security/database-security/data-safe/)
- [Google Cloud Security Command Centre](https://cloud.google.com/security-command-center)

## Essential Eight Implementation

The [ASD's Blueprint for Secure Cloud (process focused)](https://blueprint.asd.gov.au/) and [Microsoft Compliance - ACSC Essential Eight (technical focus)](https://learn.microsoft.com/en-us/compliance/essential-eight/e8-overview) are being regularly updated, and have in depth guidance aligned to this technical reference.

Small entities should also review the [ACSCs Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight) Microsoft 365 [Cloud Security Guides](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guides). Our below links reference security platforms and tools that have been seen to simplify establishment and monitoring of controls as per the [ACSC Essential Eight Process Guide](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-assessment-process-guide) and reduce [Supply Chain Risk](../guidelines/supply-chain-risk-mgmt.md) (where possible [Certified Service Providers](https://www.hostingcertification.gov.au/certified-service-providers) tooling has been referenced).

### Application Control

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/application-control/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-application-control)

- Start with [Essential Eight application control using AppLocker for ML1](https://learn.microsoft.com/en-us/compliance/essential-eight/e8-app-control#essential-eight-application-control-using-applocker-for-ml1) (simple 3 path block rule)
- For modern approaches to [WDAC for ML2](https://learn.microsoft.com/en-us/compliance/essential-eight/e8-app-control#essential-eight-application-control-using-wdac-for-ml2) see [Intune ACSC Windows Hardening Guidelines](https://github.com/microsoft/Intune-ACSC-Windows-Hardening-Guidelines)
- If above is still high complexity due to number of legacy or packaged applications review a third party tool like [AirLock Digital](https://www.airlockdigital.com)
- Other effective tools: [Ivanti Application Control](https://www.ivanti.com/en-au/products/application-control), [Trend Vision One Application Control](https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-application-control_001), [VMWare Carbon Black App Control](https://www.vmware.com/products/app-control.html)

### Patch Operating Systems

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/patch-os/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-operating-system)

- Manage MS endpoints OS patching with [Windows Autopatch](https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/overview/windows-autopatch-deployment-guide)
- Manage Windows and Linux server patching with [Azure Automanage](https://learn.microsoft.com/en-us/azure/automanage/automanage-arc)
- Manage MacOS endpoints as [supervised devices in Intune](https://learn.microsoft.com/en-us/mem/intune/protect/software-updates-macos)

### Patch Applications

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/patch-applications/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-applications)

- Endpoint vuln mgmt with [Microsoft Defender Vulnerability Management](https://learn.microsoft.com/en-us/microsoft-365/security/defender-vulnerability-management/defender-vulnerability-management?view=o365-worldwide)
- Cloud vuln mgmt with [Defender CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management), [Amazon Inspector](https://aws.amazon.com/inspector/)
- Server and OT vuln mgmt with [Tenable Vulnerability Management](https://www.tenable.com/products/tenable-io), [Rapid7 InsightVM](https://www.rapid7.com/products/insightvm/), [Qualys Vulnerability
    Management](https://www.qualys.com/apps/vulnerability-management-detection-response/), [Crowdstrike Falcon Spotlight](https://www.crowdstrike.com/products/exposure-management/falcon-spotlight-vulnerability-management/), [Ivanti Neurons for ASOC](https://www.ivanti.com/products/ivanti-neurons-for-asoc)
- OT and Network vuln mgmt with [Claroty xDome](https://claroty.com/industrial-cybersecurity/xdome), [Cisco Cyber Vision](https://www.cisco.com/site/us/en/products/security/industrial-security/cyber-vision/index.html) or [Palo Alto IoT Security](https://docs.paloaltonetworks.com/iot/iot-security-admin/iot-security-solution/iot-security-solution-structure)

### Restrict Microsoft Office Macros

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/restrict-microsoft-office-macros/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-configure-macro-settings)

Migrate from legacy macros to [Office Scripts and Power Automate](https://learn.microsoft.com/en-us/office/dev/scripts/develop/power-automate-integration?tabs=run-script)

### User Application Hardening

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/user-application-hardening/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-user-application-hardening)

- Block [newly registered domains (over 70% are malicious)](https://unit42.paloaltonetworks.com/newly-registered-domains-malicious-abuse-by-bad-actors/) with [Web Content Filtering](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/web-content-filtering?view=o365-worldwide)
- Migrate java applications to use [Java Web Start](https://blogs.oracle.com/ebstech/post/migrate-to-java-web-start-from-java-plug-in-now) instead of browser plugins

### Restrict Administrative Privileges

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/restrict-administrative-privileges/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-restrict-administrative-privileges)

- Implement [Windows LAPS](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview) for secure local administrator password management
- Use [Administrative Units](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units) to partition management scopes and minimise usage of global administration roles
- Use [Entra ID Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) to enable time bound tracked access to privileged resources (as opposed to persistent privileged access)
- Run shared devices in [Kiosk Mode](https://learn.microsoft.com/en-us/mem/intune/configuration/kiosk-settings) with local unprivileged users

### Multi-factor Authentication

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/multi-factor-authentication/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-multi-factor-authentication)

Once Azure AD MFA configured, below migrations will get identities and data into compliant states and locations

- Enable [DKIM/DMARC/SPF](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-about?view=o365-worldwide#how-to-avoid-email-authentication-failures-when-sending-mail-to-microsoft-36) across all registered domains belonging to the organisation
    - If legacy systems/applications dependent on SMTP exist, migrate them to separate subdomains on transactional email platforms such as [mailchimp](https://mailchimp.com/developer/transactional/docs/smtp-integration/), [postmarkapp](https://postmarkapp.com/developer/user-guide/send-email-with-smtp) or [sendgrid](https://docs.sendgrid.com/for-developers/sending-email/getting-started-smtp) to avoid reducing the security of the primary identity domains
- [Disable SMTP Auth for Exchange Online](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission#disable-smtp-auth-in-your-organization) to simplify conditional access policies and avoid reconnaisance and exploitation of primary identity domains and mailboxes
- [Migrate file shares to OneDrive, Teams, and SharePoint](https://learn.microsoft.com/en-us/sharepointmigration/fileshare-to-odsp-migration-guide) and enable [Microsoft Purview risk and compliance](https://learn.microsoft.com/en-us/purview/purview-compliance)
- [Migrate Microsoft Access data to Microsoft Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/migrate-access-to-dataverse) and [Connect to and manage Microsoft Dataverse in Microsoft Purview](https://learn.microsoft.com/en-au/purview/register-scan-dataverse)
- Implement a [Security Service Edge](https://learn.microsoft.com/en-us/entra/architecture/sse-deployment-guide-intro) or [MFA Application Proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy/application-proxy) in front of legacy systems in use by staff (internal identities)
- Implement a [cloud based CDN and WAF](https://soc.cyber.wa.gov.au/guidelines/network-management/#web-application-firewalls-wafs-and-content-delivery-networks-cdns) such as [Akamai](https://www.akamai.com/products/app-and-api-protector), [Amazon CloudFront](https://aws.amazon.com/blogs/security/protect-public-clients-for-amazon-cognito-by-using-an-amazon-cloudfront-proxy/), [Azure Front Door](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview), [Cloudflare](https://www.cloudflare.com/en-au/application-services/products/waf/), [F5XC](https://docs.cloud.f5.com/docs/quick-start/service-chaining-cdn-waap), [Fastly](https://www.fastly.com/products/web-application-api-protection) or [Imperva](https://docs.imperva.com/bundle/cloud-application-security/page/introducing/overview.htm) that interoperate with Customer IAM such as [Azure AD B2C](https://learn.microsoft.com/en-us/azure/active-directory-b2c/overview), [Amazon Cognito](https://aws.amazon.com/cognito/), [IBM Verify](https://www.ibm.com/products/verify-identity), [Okta Customer Identity Cloud](https://www.okta.com/customer-identity/), [PingOne for Customers](https://www.pingidentity.com/en/platform/solutions/pingone-for-customers.html) in front of legacy systems in use by customers (external identities)

### Regular Backups

[ASD Blueprint](https://blueprint.asd.gov.au/security-and-governance/essential-eight/regular-backups/), [ACSC Technical Example](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-regular-backups)

- Mirror onprem fileshares with [Azure File Sync (Disaster Recovery for local file shares)](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/hybrid/hybrid-file-share-dr-remote-local-branch-workers)
- Back up simple servers with [Back up on-premises applications and data to the cloud (Azure Backup)](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/backup-archive-on-premises-applications)
- Back up complex environments with backup platforms like [Druva Phoenix](https://www.druva.com/products/data-center)
