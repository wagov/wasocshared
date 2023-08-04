## Recent Advisories

{{ date_index("docs/advisories/*.md", prefix="advisories/", expand=1, include=2) }}

## WA SOC - Recent Threat Activity (Aug 2023)

Based on recent high impact incidents seen by the WA SOC, security teams should be focusing on the below areas of improvement:

!!! warning "ACSC Guidance targeted on recent threat activity"

- [2022 Top Routinely Exploited Vulnerabilities](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/2022-top-routinely-exploited-vulnerabilities)
- [Preventing Web Application Access Control Abuse](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/preventing-web-application-access-control-abuse)
- [How to Combat Fake Emails](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/email-hardening/how-combat-fake-emails)

Recently key high profile vulnerabilities this month worth staying across include:

- [Threat Actors Exploiting Citrix CVE-2023-3519 to Implant Webshells - 20230721002](https://soc.cyber.wa.gov.au//advisories/20230721002-Threat-Actors-Exploiting-Webshells-Citrix/)
- [FortiOS and FortiProxy Critical Vulnerability Patch Released - 20230712002](https://soc.cyber.wa.gov.au//advisories/20230712002-FortiOS-FortiProxy-Criticial-Vuln-Patch/) 
- [Increase in QR Code Phishing Technique - 20230710003](https://soc.cyber.wa.gov.au//advisories/20230710003-QR-Code-Phishing-Increase/)

Agencies should review their software asset register(s) and vulnerability remediation (patching) processes to mitigate against the above vulnerabilities. Any exposed **email** services should be worth prioritising due to ongoing threat activity.

**Phishing activity remains high** across all organisations with multiple incidents detected weekly. Please refer to the below guides to ensure all external and internal sign-ins are appropriately monitored.

- [Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue, PRT, OAuth)](https://jeffreyappel.nl/tips-for-preventing-against-new-modern-identity-attacks-aitm-mfa-fatigue-prt-oauth/)
    - [Enabling MFA number matching to mitigate MFA fatigue attacks (AAD)](https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match#enable-number-matching-in-the-portal)
- [How to implement Defender for Identity and configure all prerequisites](https://jeffreyappel.nl/how-to-implement-defender-for-identity-and-configure-all-prerequisites/)
