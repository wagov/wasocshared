# Baseline for Vulnerability Management

This document and associated checklist is intended to be used as a high-level self assessment to determine the capability and maturity of a vulnerability management (including patching) function for organisations connected to the WA SOC. Note this excludes the Governance, Risk and Compliance (GRC) roles and is focused primarily on undertaking operational **Identify** and **Protect** capabilities under the [WA Cyber Security Policy](https://www.wa.gov.au/government/publications/wa-government-cyber-security-policy) (and takes into consideration the oversight capabilities available entities in scope of the WA SOC).

The links embedded in the checklist below are to recommended approaches that can be used for implementation, however any equivalent capability is suitable as long as the organisation is able to maintain an up to date asset database with a full inventory of **devices, resources (compute, storage, network), software and code repositories** in use.

## Checklist

- [ ] Automate asset discovery
    - [ ] Validate internet-facing asset ownership and daily discovery with the WA SOC.
    - [ ] Implement fortnightly [asset fingerprinting and discovery](https://www.runzero.com/docs/discovering-assets/) across all network connected devices.
- [ ] Implement daily active [Web](https://www.tenable.com/products/tenable-io/web-application-scanning) & [Basic Network Scans](https://docs.tenable.com/nessus/Content/ScanAndPolicyTemplates.htm#Scanner_Templates) across internet-facing assets 
- [ ] Implement Cloud Security Posture Management (CSPM) across all public cloud assets aligned with [Microsoft cloud security benchmark (v1)](https://learn.microsoft.com/en-us/security/benchmark/azure/overview)
- [ ] Implement weekly active [Basic Network Scans](https://docs.tenable.com/nessus/Content/ScanAndPolicyTemplates.htm#Scanner_Templates) and [Basic Agent Scans](https://docs.tenable.com/nessus/Content/ScanAndPolicyTemplates.htm#Scanner_Templates) towards all assets on the corporate network (as separate from Operational Technology / vendor managed device networks)
- [ ] Assign all discovered assets to Maintenance Groups as outlined in [NIST Special Publication 800-40r4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf) (Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology)
- [ ] Implement [Patch Management](../guidelines/patch-management.md) following [Assessing Security Vulnerabilities and Applying Patches](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-administration/assessing-security-vulnerabilities-and-applying-patches)
    - [ ] **internet-facing services**: within two weeks, or within 48 hours if an exploit exists
    - [ ] **workstations, servers, network devices and other network-connected devices:** within one month
