## Recent Advisories

{{ date_index("docs/advisories/*.md", prefix="advisories/", expand=1, include=2) }}

## WA SOC - Recent Threat Activity (November 2023)

Based on recent high impact incidents seen by the WA SOC, security teams should be focusing on the below areas of improvement:

!!! warning "ACSC Guidance targeted on recent threat activity"

    - [Preventing Web Application Access Control Abuse](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/preventing-web-application-access-control-abuse)
    - [How to Combat Fake Emails](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/email-hardening/how-combat-fake-emails)
    - [What is QRCode Phishing - "Quishing"](https://www.cyber.gov.au/learn-basics/explore-basics/watch-out-threats/quishing)

Recent WA SOC advisories this month worth staying across include:

- [Citrix Vulnerabilities "Bleed"](https://soc.cyber.wa.gov.au/advisories/20231123001-CISA-StopRansomware-LockBit-Citrix-Bleed/)
- [Increased BEC activity](https://soc.cyber.wa.gov.au/advisories/20231012002-Awareness-BEC-Increased-Activity/)
- [QRCode Phishing](https://soc.cyber.wa.gov.au/advisories/20230922003-Increase-in-QR-Code-Phishing-Technique/)
    - The WASOC has developed out a new Sentinel Analytic rule to assist agencies with the detection of "quishing" (QRCode Phishing) attacks. [Analtyic/Threat Hunt Rule](https://soc.cyber.wa.gov.au/guidelines/TTP_Hunt/ADS_forms/T1566.001-QR-CodePhishingAttachment%28Quishing%29/)

Agencies should ensure their procurement and vendor management processes are aligned to the [Supply Chain Risk Management Guideline](guidelines/supply-chain-risk-mgmt.md). Additionally agencies should prioritise remediating vulnerabilities in any internet-facing **remote access** services due to ongoing threat activity.

**Phishing activity remains high** across all organisations with multiple incidents detected weekly. Please refer to the below guides to ensure all external and internal sign-ins are appropriately monitored.

- [AiTM/ MFA phishing attacks in combination with “new” Microsoft protections (2023 edition)](https://jeffreyappel.nl/aitm-mfa-phishing-attacks-in-combination-with-new-microsoft-protections-2023-edt/)
- [How to use Automatic Attack Disruption in Microsoft 365 Defender (BEC, AiTM & HumOR)](https://jeffreyappel.nl/how-to-use-automatic-attack-disruption-in-microsoft-365-defender-bec-aitm-humor/)
- [How to implement Defender for Identity and configure all prerequisites](https://jeffreyappel.nl/how-to-implement-defender-for-identity-and-configure-all-prerequisites/)