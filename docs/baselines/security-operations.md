# Baseline for Security Operations (DRAFT)

This document and associated checklist is intended to be used as a high-level self assessment to determine the capability and maturity of a security operations function for various organisations. Note this excludes the Governance, Risk and Compliance (GRC) roles and is focused primarily on how many Security Analysts are required to undertake operational **Identify**, **Detect** and **Respond** capabilities under the [WA Cyber Security Policy](https://www.wa.gov.au/government/publications/wa-government-cyber-security-policy) (and takes into consideration the oversight capabilities available entities in scope of the WA SOC). The WA SOC and this document both are aligned with [MITRE 11 Strategies of a World-Class Cybersecurity Operations Center](../pdfs/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf).

- [ ] Define security operations scope (sensors and events import to the organisation)
    - [ ] Focus on covering all endpoints used, applications / services delivered, and network traffic flows
- [ ] Ingest from above data sources into a tool with automated detections
- [ ] Align detections to MITRE TTPs affecting your org (review [playbooks](../guidelines/playbooks.md))
- [ ] Regularly update detections, priority TTPs and incident playbooks (at least quarterly)
- [ ] Regularly exercise playbooks (at least annually)

Regarding sizing, dedicated operational security analyst roles should start at 2 FTE equivalents (scaling an additional 1 FTE for every 1-2k staff) of dedicated security roles managing:

- Endpoint Devices (EDR - e.g Microsoft Defender)
- Servers & Applications (WAF, EASM, Platforms & Infrastructure)
- Network Traffic Analytics
- Operations, Training & Awareness (how staff use technology securely)

If the above resourcing is difficult to retain due to a small organisational size, internal leadership roles to coordinate an external Managed Service Provider (MSP) to include a Security Service typically starts at $40k AUD annual to cover 200hrs/year of effort (approx $200/hr for basic analysts):

- 50-200 staff with 2-3 incidents needing investigation each day
- 10hrs / month triaging incidents (40-60 incidents at approx 15 mins an incident)
- 20hrs / quarter detection engineering = 200hrs per year

Try to ensure a single entity is providing both IT management (endpoints, identities, infrastructure and platforms) and security greatly reduces the complexity of vendor management and is a sensible goal.
