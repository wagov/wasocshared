## Recent Advisories

{{ include_file('docs/advisories.md', 0, 10)  }}

## WA SOC - Recent Threat Activity (June 2023)

Based on recent high impact incidents seen by the WA SOC, security teams should be focusing on the below areas of improvement:

!!! warning "ACSC Mitigating Controls targeted on recent threat activity"

    - [Implementing Network Segmentation and Segregation](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/network-hardening/implementing-network-segmentation-and-segregation)
    - [Guidelines for Procurement and Outsourcing](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-procurement-and-outsourcing)
    - [How to Combat Fake Emails](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/email-hardening/how-combat-fake-emails)

Recently key high profile vulnerabilities this month worth staying across include:

- [MOVEit Transfer Critical Vulnerability - 20230602001](advisories/20230602001-MOVEit-File-Transfer-Vulnerability.md)
- [Barracuda Security Gateway appliance vulnerability -  20230529001](/advisories/20230529001-Barracuda-Security-Gateway-Appliance-Vulnerability.md)
- [State-Sponsored Cyber Actor Living off the Land to Evade Detection - 20230525001](advisories/20230525001-State-Sponsored-Cyber-Actor-Living-off-the-Land-to-Evade-Detection.md)

Agencies should review their software asset register(s) and vulnerability remediation (patching) processes to mitigate against the above vulnerabilities. Any exposed **email** services should be worth prioritising due to ongoing threat activity.

**Phishing activity remains high** across all organisations with multiple incidents detected weekly. Please refer to the below guides to ensure all external and internal signins are appropriately monitored.

- [Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue, PRT, OAuth)](https://jeffreyappel.nl/tips-for-preventing-against-new-modern-identity-attacks-aitm-mfa-fatigue-prt-oauth/)
  - [Enabling MFA number matching to mitigate MFA fatigue attacks (AAD)](https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match#enable-number-matching-in-the-portal)
- [How to implement Defender for Identity and configure all prerequisites](https://jeffreyappel.nl/how-to-implement-defender-for-identity-and-configure-all-prerequisites/)
