# Baseline for Security Operations

This document and associated checklist is intended to be used as a high-level self assessment to determine the capability and maturity of a security operations function for various organisations. Note this excludes the Governance, Risk and Compliance (GRC) roles and is focused primarily on how many Security Analysts are required to undertake operational **Identify**, **Detect** and **Respond** capabilities under the [WA Cyber Security Policy](https://www.wa.gov.au/government/publications/wa-government-cyber-security-policy) (and takes into consideration the oversight capabilities available entities in scope of the WA SOC). The WA SOC and this document both are aligned with [MITRE 11 Strategies of a World-Class Cybersecurity Operations Center](../pdfs/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf).

- [ ] Define security operations scope (sensor availability, common/high impact events to focus on, business continuity objectives)
- [ ] Ensure SIEM visibility across all endpoints used, applications / services delivered, and network traffic flows
    - [ ] Make available relevant [MITRE Data Sources](https://attack.mitre.org/datasources/) to the security operations team
    - [ ] Ensure the platform can be configured with automated detection capabilities for [MITRE Tactics](https://attack.mitre.org/tactics/enterprise/)
- [ ] Review and update the below security artefacts quarterly
    - [ ] **IDENTIFY** Perceived risk from common and high impact events (this can also feed into **PROTECT** control implementation)
    - [ ] **DETECT** Configure automated detection logic in SIEM platform for [MITRE Techniques](https://attack.mitre.org) likely to be used by threat actors based on perceived risk.
- [ ] **RESPOND** Ensure Operational risks have [cyber security response playbooks](../guidelines/playbooks.md) defined and exercised for common and high impact events at least annually.
    - [ ] Document how to protect, respond and recover from cyber security events
    - [ ] Document all shared responsibilities for critical business systems
    - [ ] Exercise real-world detection and response with high coverage, low risk assumed breach offensive testing (typically [Persistence](https://attack.mitre.org/tactics/TA0003), [Collection](https://attack.mitre.org/tactics/TA0009) and [Exfiltration](https://attack.mitre.org/tactics/TA0010))

Regarding sizing, dedicated operational security analyst roles should start at 2 FTE equivalents (scaling an additional 1 FTE for every 1-2k staff) of dedicated security roles managing:

- Endpoint Devices (EDR - e.g Microsoft Defender)
- Servers & Applications (WAF, EASM, Platforms & Infrastructure)
- Network Traffic Analytics (Flow baselining and alerting on deviations)
- Operations, Training & Awareness (developing and understanding of how technology is used and how to improve it's use securely)

If the above resourcing is difficult to retain due to a small organisational size, internal leadership roles to coordinate an external Managed Service Provider (MSP) to include a Security Service typically starts at $40k AUD annual to cover 200hrs/year of effort (approx $200/hr for basic analysts):

- 50-200 staff with 2-3 incidents needing investigation each day
- 10hrs / month triaging incidents (40-60 incidents at approx 15 mins an incident)
- 20hrs / quarter detection engineering = 200hrs per year

Consolidating MSP and MSSP services to deliverboth IT management (endpoints, identities, infrastructure and platforms) and security operations functions from a single provider greatly reduces the complexity of vendor management and is a sensible goal. For business applications that aren't aligned with an organisations core enterprise architecture, they should be procured as fully managed services (i.e. SaaS) to minimise the complexity of shared responsibilities and associated risk which that incurs.
