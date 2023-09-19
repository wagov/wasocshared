# Secure Configuration Assessment Guideline

This guideline is intended to define a simple approach to ongoing monitoring and assurance of secure configuration of common tools and platforms.

## Email, File sharing and Endpoint configuration monitoring

The standard recommended actions within [Microsoft Defender](https://security.microsoft.com/securescore?viewid=actions) should be reviewed and exported each month and retained for 12 months.

### Enhanced validation of cloud service configuration

A tool to review tenant configuration such as the [CISA ScubaGear M365 Secure Configuration Baseline Assessment Tool](https://github.com/cisagov/ScubaGear) should be run against all tenants at least quarterly with results reviewed and retained for 12 months to guide policy remediations and improvements.

### Enhanced validation of endpoint configuration

The [ACSC’s Cyber Toolbox](https://www.cyber.gov.au/about-us/news/essential-eight-assessment-guidance-package) is comprised of the Essential Eight Maturity Verification Tool (E8MVT) and the Application Control Verification Tool (ACVT) which should be run against a sampling of endpoints on at least a quarterly basis with results reviewed and retained for 12 months to guide policy remediations and improvements.

## Infrastructure (public cloud and on-premise compute and storage) configuration monitoring

The standard recommended actions within [Microsoft Defender for Cloud](https://portal.azure.com/#view/Microsoft_Azure_Security/SecurityMenuBlade/~/5) should be reviewed and exported each month and retained for 12 months.

## Addressing Microsoft 365 cloud service risks

Organisations with Microsoft 365 premium or enterprise licencing should at a minimum undertake the following basics:

- Enable security defaults in Azure Active Directory. Microsoft has published [guidance on enabling Security defaults](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/concept-fundamentals-security-defaults#enabling-security-defaults). 
- Enrol your compatible devices in Intune. Microsoft has published guidance on [enrolling Windows devices in Intune](https://docs.microsoft.com/en-us/mem/intune/enrollment/windows-enrollment-methods).

This subsequently enables straightforward implementation of the [ACSCs Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight) Microsoft 365 [Cloud Security Guides](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guides) listed below for reference:

- [Application control](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-application-control)
- [Patch applications](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-applications)
- [Configure macro settings](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-configure-macro-settings)
- [User application hardening](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-user-application-hardening)
- [Restrict administrative privileges](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-restrict-administrative-privileges)
- [Patch operating systems](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-operating-system)
- [Multi-factor authentication](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-multi-factor-authentication)
- [Regular backups](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-regular-backups)
