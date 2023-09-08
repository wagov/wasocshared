## Recent Advisories

{{ date_index("docs/advisories/*.md", prefix="advisories/", expand=1, include=2) }}

## WA SOC - Recent Threat Activity (Aug 2023)

Based on recent high impact incidents seen by the WA SOC, security teams should be focusing on the below areas of improvement:

!!! warning "ACSC Guidance targeted on recent threat activity"

    - [2022 Top Routinely Exploited Vulnerabilities](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/2022-top-routinely-exploited-vulnerabilities)
    - [Preventing Web Application Access Control Abuse](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/preventing-web-application-access-control-abuse)
    - [How to Combat Fake Emails](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/email-hardening/how-combat-fake-emails)

Recent WA SOC advisories this month worth staying across include:

- [Downfall and Zenbleed - Modern Processor Attacks](https://soc.cyber.wa.gov.au/advisories/20230810001-Downfall-and-Zenbleed-Processor-Attacks/)
- [Secure Cloud Business Applications (SCuBA) Project](https://soc.cyber.wa.gov.au/advisories/20230809004-SCuBA-Recommendations/)
- [Sophisticated network attacks and guidance for agencies](https://soc.cyber.wa.gov.au/advisories/20230816001-Sophisticated-Network-Attacks-and-Guidance/)
- [Results of Major Technical Investigations for Storm-0558 Key Acquisition ](https://msrc.microsoft.com/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition/)

Agencies should review [ACSC's Questions to Ask Managed Service Providers](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/outsourcing-and-procurement/managed-services/questions-ask-managed-service-providers), especially service providers managing their **network**, **compute** and **file/email (Microsoft 365)** resources. A supporting extract from page 16 and 17 of the [NIST CSF 2.0 Initial Public Draft](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.ipd.pdf) is below, identifying what should be addressed as part of procurement and contract management.

!!! note "Managing Cybersecurity Risk in Supply Chains (NIST)"

    - **Identify:** Identifying, validating, and recording vulnerabilities associated with the supplier’s product or service [ID.RA-01]
    - **Protect:** Authenticating users, services, and hardware [PR.AA-03]; applying appropriate configuration management practices [PR.PS-01]; generating log records and having the logs available for continuous monitoring [PR.PS-04]; and integrating secure software development practices into the supplier’s software development life cycles [PR.PS-07]
    - **Detect:** Monitoring computing hardware and software for potentially adverse events [DE.CM-09]
    - **Respond:** Executing incident response plans when compromised products or services are involved [RS.MA-01]
    - **Recover:** Executing the recovery portion of the organization’s incident response plan when compromised products or services are involved [RC.RP-01], and restoring compromised products or services and verifying their integrity [RC.RP-05]

Additionally agencies should prioritise remediating vulnerabilities in any internet-facing **remote access** services due to ongoing threat activity. If you were affected by the [LastPass breach](https://soc.cyber.wa.gov.au/advisories/20221223001-Lastpass-breach-update/) last year, please also review [Experts Fear Crooks are Cracking Keys Stolen in LastPass Breach](https://krebsonsecurity.com/2023/09/experts-fear-crooks-are-cracking-keys-stolen-in-lastpass-breach/).

**Phishing activity remains high** across all organisations with multiple incidents detected weekly. Please refer to the below guides to ensure all external and internal sign-ins are appropriately monitored.

- [AiTM/ MFA phishing attacks in combination with “new” Microsoft protections (2023 edition)](https://jeffreyappel.nl/aitm-mfa-phishing-attacks-in-combination-with-new-microsoft-protections-2023-edt/)
- [How to use Automatic Attack Disruption in Microsoft 365 Defender (BEC, AiTM & HumOR)](https://jeffreyappel.nl/how-to-use-automatic-attack-disruption-in-microsoft-365-defender-bec-aitm-humor/)
- [How to implement Defender for Identity and configure all prerequisites](https://jeffreyappel.nl/how-to-implement-defender-for-identity-and-configure-all-prerequisites/)
