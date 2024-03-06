## Recent Advisories

{{ date_index("docs/advisories", prefix="advisories/", expand=1, include=2) }}

## WA SOC - Recent Threat Activity (Feburary 2024)

Based on recent high impact incidents seen by the WA SOC, security teams should be focusing on the below areas of improvement:

!!! warning "WASOC Guidance targeted on recent threat activity"
    - AD configuration and deployments continue to cause significant exposure to organisations, please ensure there is appropriate separation of concerns to avoid exploits such as [spoofing DNS by abusing DHCP](https://www.akamai.com/blog/security-research/spoofing-dns-by-abusing-dhcp)
    - Any attacker that obtains the private key of an externally generated certificate can forge any SAML response that can then access the application as any user - see [Silver SAML: Golden SAML in the Cloud](https://www.semperis.com/blog/meet-silver-saml/) (high risk for any SCIM / Identity federation SAML integrations that may have applications authorised to impersonate and/or manage identities in Entra ID).

Recent WA SOC advisories this month worth staying across include:

- [Ivanti Services](https://soc.cyber.wa.gov.au/advisories/20240122002-Ivanti-CISA-Guidance/)
- [Fortinet VPN SSL](https://soc.cyber.wa.gov.au/advisories/20240209002-Fortinet-Multiple-RCE-Vulnerabilities-Exploited/)
- [ConnectWise](https://soc.cyber.wa.gov.au/advisories/20240221004-ConnectWise-Patches-Critical-ScreenConnect-Vulnerability/)

Agencies should review the latest [NIST CSF 2.0](https://www.nist.gov/quick-start-guides).

**Security Hardening** remains a focus for all organisations. Please refer to the below guides to ensure all external and internal sign-ins are appropriately monitored.

- [ASD Blueprint for Secure Cloud (E8)](https://blueprint.asd.gov.au/security-and-governance/essential-eight/)
