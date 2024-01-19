## Recent Advisories

{{ date_index("docs/advisories", prefix="advisories/", expand=1, include=2) }}

## WA SOC - Recent Threat Activity (December 2023)

Based on recent high impact incidents seen by the WA SOC, security teams should be focusing on the below areas of improvement:

!!! warning "ACSC & CISA Guidance targeted on recent threat activity"
    - [Russian FSB - Star Blizzard](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/russian-fsb-cyber-actor-star-blizzard-continues-worldwide-spear-phishing-campaigns)
    - [Insights from the CISA Healthcare and Public Health Sector Risk and Vulnerability Assessment](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-349a)

Recent WA SOC advisories this month worth staying across include:

- [Apache Strut 2 RCE vulnerability](https://soc.cyber.wa.gov.au/advisories/20231213001-Apache-Struts-2-crit-vuln/)
- [MongoDB Compromise](https://soc.cyber.wa.gov.au/advisories/20231218004-MongoDB-Compromise/)
- [#StopRansomware: Play ransomware](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/stopransomware-play-ransomware)

Agencies should ensure their procurement and vendor management processes are aligned to the [Supply Chain Risk Management Guideline](guidelines/supply-chain-risk-mgmt.md). Additionally agencies should prioritise remediating vulnerabilities in any internet-facing **remote access** services due to ongoing threat activity.

Microsoft recommends deploying new devices as cloud-native using Microsoft Entra join. Deploying new devices as Microsoft Entra hybrid join devices isn't recommended, including through Autopilot. For more information: [Microsoft Entra joined vs. Microsoft Entra hybrid joined in cloud-native endpoints: Which option is right for your organization](https://learn.microsoft.com/en-us/mem/solutions/cloud-native-endpoints/azure-ad-joined-hybrid-azure-ad-joined#which-option-is-right-for-your-organization).

**Security Hardening** remains a focus for all organisations. Please refer to the below guides to ensure all external and internal sign-ins are appropriately monitored.

- [ASD Blueprint for Secure Cloud (E8)](https://blueprint.asd.gov.au/security-and-governance/essential-eight/)
