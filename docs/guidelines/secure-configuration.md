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

## Addressing Microsoft 365 cloud service risks

Organisations with Microsoft 365 premium or enterprise licencing should at a minimum undertake the following basics:

- Enable security defaults in Azure Active Directory. Microsoft has published [guidance on enabling Security defaults](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/concept-fundamentals-security-defaults#enabling-security-defaults). 
- Enrol your compatible devices in Intune. Microsoft has published guidance on [enrolling Windows devices in Intune](https://docs.microsoft.com/en-us/mem/intune/enrollment/windows-enrollment-methods).

![Security defaults](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/media/security-defaults/security-defaults-entra-admin-center.png)
![Intune enrollment](https://learn.microsoft.com/en-us/mem/intune/fundamentals/media/deployment-guide-enroll/deployment-plan-enroll.png)

### Essential Eight Implementation

This subsequently enables straightforward implementation of the [ACSCs Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight) Microsoft 365 [Cloud Security Guides](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guides) listed below for reference. The indented links reference security platforms and tools that have been seen to simplify establishment and monitoring of controls as per the [ACSC Essential Eight Process Guide](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-assessment-process-guide) and introduce low [Supply Chain Risk](../guidelines/supply-chain-risk-mgmt.md).

- [Application control (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-application-control)
    - [AirLock Digital](https://www.airlockdigital.com), [Ivanti Application Control](https://www.ivanti.com/en-au/products/application-control), [Trend Vision One Application Control](https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-application-control_001) or [VMWare Carbon Black App Control](https://www.vmware.com/products/app-control.html)
- [Patch operating systems (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-operating-system), [Patch applications (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-applications)
    - [Microsoft Defender Vulnerability Management](https://learn.microsoft.com/en-us/microsoft-365/security/defender-vulnerability-management/defender-vulnerability-management?view=o365-worldwide), [Tenable Vulnerability Management](https://www.tenable.com/products/tenable-io), [Rapid7 InsightVM](https://www.rapid7.com/products/insightvm/), [Qualys Vulnerability
Management](https://www.qualys.com/apps/vulnerability-management-detection-response/), [Crowdstrike Falcon Spotlight](https://www.crowdstrike.com/products/exposure-management/falcon-spotlight-vulnerability-management/), [Ivanti Neurons for ASOC](https://www.ivanti.com/products/ivanti-neurons-for-asoc)
- [Configure macro settings (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-configure-macro-settings)
    - Migrate from legacy macros to [Office Scripts and Power Automate](https://learn.microsoft.com/en-us/office/dev/scripts/develop/power-automate-integration?tabs=run-script)
- [User application hardening (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-user-application-hardening)
    - Block [newly registered domains (over 70% are malicious)](https://unit42.paloaltonetworks.com/newly-registered-domains-malicious-abuse-by-bad-actors/) with [Web Content Filtering](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/web-content-filtering?view=o365-worldwide)
    - Migrate java applications to use [Java Web Start](https://blogs.oracle.com/ebstech/post/migrate-to-java-web-start-from-java-plug-in-now) instead of browser plugins
- [Restrict administrative privileges (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-restrict-administrative-privileges)
    - Use [Administrative Units](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units) to partition management scopes
    - Run shared devices in [Kiosk Mode](https://learn.microsoft.com/en-us/mem/intune/configuration/kiosk-settings) with local unprivileged users
- [Multi-factor authentication (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-multi-factor-authentication) - Once Azure AD MFA configured, below migrations will get data into compliant locations
    - [Migrate file shares to OneDrive, Teams, and SharePoint](https://learn.microsoft.com/en-us/sharepointmigration/fileshare-to-odsp-migration-guide) and enable [Microsoft Purview risk and compliance](https://learn.microsoft.com/en-us/purview/purview-compliance)
    - [Migrate Microsoft Access data to Microsoft Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/migrate-access-to-dataverse) and [Connect to and manage Microsoft Dataverse in Microsoft Purview](https://learn.microsoft.com/en-au/purview/register-scan-dataverse)
    - Implement a [Security Service Edge](https://learn.microsoft.com/en-us/entra/architecture/sse-deployment-guide-intro) or [MFA Application Proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy/application-proxy) in front of legacy systems in use by staff (internal identities)
    - Implement a [cloud based CDN and WAF](https://soc.cyber.wa.gov.au/guidelines/network-management/#web-application-firewalls-wafs-and-content-delivery-networks-cdns) such as [Akamai](https://www.akamai.com/products/app-and-api-protector), [Amazon CloudFront](https://aws.amazon.com/blogs/security/protect-public-clients-for-amazon-cognito-by-using-an-amazon-cloudfront-proxy/), [Azure Front Door](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview), [Cloudflare](https://www.cloudflare.com/en-au/application-services/products/waf/), [F5XC](https://docs.cloud.f5.com/docs/quick-start/service-chaining-cdn-waap), [Fastly](https://www.fastly.com/products/web-application-api-protection) or [Imperva](https://docs.imperva.com/bundle/cloud-application-security/page/introducing/overview.htm) that interoperate with Customer IAM such as [Azure AD B2C](https://learn.microsoft.com/en-us/azure/active-directory-b2c/overview), [Amazon Cognito](https://aws.amazon.com/cognito/), [IBM Verify](https://www.ibm.com/products/verify-identity), [Okta Customer Identity Cloud](https://www.okta.com/customer-identity/), [PingOne for Customers](https://www.pingidentity.com/en/platform/solutions/pingone-for-customers.html) in front of legacy systems in use by customers (external identities)
- [Regular backups (ACSC Example)](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-regular-backups)
    - [Azure File Sync (Disaster Recovery for local file shares)](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/hybrid/hybrid-file-share-dr-remote-local-branch-workers), [Back up on-premises applications and data to the cloud (Azure Backup)](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/backup-archive-on-premises-applications), [Druva Phoenix](https://www.druva.com/products/data-center)


