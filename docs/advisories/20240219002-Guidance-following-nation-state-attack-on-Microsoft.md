# Guidance following nation state attack on Microsoft - 20240219002

## Overview

The recent nation state [attack on Microsoft](https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/ "https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/") highlighted significant configuration vulnerabilities that may be present in Entra ID (previously known as Azure AD) tenants.

## What is vulnerable?

- If a principal holds the **AppRoleAssignment.ReadWrite.All** app role, that principal may grant any principal (including itself) any app role against any resource app, including the **RoleManagement.ReadWrite.Directory** MS Graph app role
- With the **RoleManagement.ReadWrite.Directory** MS Graph app role, a principal may assign itself or any other principal to any Entra ID role, including Global Administrator

Based on this information, we know we need to look for two primary things:

1. Foreign principals (i.r., those coming from a tenant outside of your own) with escalation privileges which create paths to highly privileged roles
1. Foreign principals that already hold highly-privileged roles

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendations

Due to the severity of a compromise of an Entra ID tenant managing privileges for an organisation, the WA SOC recommends reviewing the below guidance and ensuring that Enterprise Applications, Application Registrations and Service Principle role assignments are audited regularly as part of operational account audits and [Secure Configuration Assessments](https://soc.cyber.wa.gov.au/guidelines/secure-configuration/ "https://soc.cyber.wa.gov.au/guidelines/secure-configuration/").

## Additional References

- [**Microsoft Breach — How Can I See This In BloodHound?**](https://posts.specterops.io/microsoft-breach-how-can-i-see-this-in-bloodhound-33c92dca4c65)
- [**AzureHound Community Edition**](https://support.bloodhoundenterprise.io/hc/en-us/articles/17481394564251-AzureHound-Community-Edition)
