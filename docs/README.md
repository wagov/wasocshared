# WA Cyber Security Unit (Office of Digital Government)

This site contains technical information to support WA Government Cyber Security activities. Please propose updates directly via the edit link on each page or email [cybersecurity@dpc.wa.gov.au](mailto:cybersecurity@dpc.wa.gov.au) with any feedback. The site is built with [Material for MkDocs (reference)](https://squidfunk.github.io/mkdocs-material/reference/) which includes several [extensions to markdown](https://squidfunk.github.io/mkdocs-material/setup/extensions/) for enhanced technical writing.

## WA Security Operations Centre (WA SOC)

- [Connecting to the WA SOC](onboarding.md)
- [Advisories (TLP:CLEAR)](advisories.md)
- [Incident Reporting User Guide (Jira)](guidelines/incident-reporting.md)
- [ACSC Essential Eight Assessment Process Guide](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-assessment-process-guide)

## Baselines & Guidelines

Baselines are for use as self-assessment checklists, and guidelines are for general implementation guidance.

!!! abstract "Baselines"

    The WA SOC has developed a [Baseline for Event Ingestion](baselines/data-sources.md). It's currently under review to align with [MITRE ATT&CK®](https://attack.mitre.org) and develop detection coverage/quality into a standalone baseline. See [MITRE Data Sources](https://attack.mitre.org/datasources/) for SIEM (sensors/events) coverage and [MITRE Tactics](https://attack.mitre.org/tactics/enterprise/) for SIEM automated detection coverage.

!!! danger "Critical Infrastructure Entities"

    The [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) detail very effective network and server hardening controls that are a highly valuable addition to the ACSC Essential 8, especially for entities in scope of [SOCI regulatory obligations](https://www.cisc.gov.au/legislative-information-and-reforms/critical-infrastructure/regulatory-obligations).

!!! tip "Guidelines"

    - [Guide to Securing Remote Access Software (CISA)](https://www.cisa.gov/resources-tools/resources/guide-securing-remote-access-software) - remote access software overview, including the malicious use of remote access software, detection methods, and recommendations for all organizations.
    - [#StopRansomware Guide (CISA)](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) - one-stop resource to help organizations reduce the risk of ransomware incidents through best practices to detect, prevent, respond, and recover, including step-by-step approaches to address potential attacks.
    - [Microsoft Sentinel Guidance](onboarding/sentinel-guidance.md) - Implementation guidance for using Sentinel for [ACSC Guidelines for System Monitoring](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-system-monitoring)
    - [Network Management Guideline](guidelines/network-management.md) - Implementation guidance for [ACSC Network gateway hardening](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/gateway-hardening/gateway-security-guidance-package-executive-guidance).
    - [Patch Management Guideline](guidelines/patch-management.md) - Implementation guidance for [ACSC Assessing Security Vulnerabilities and Applying Patches](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-administration/assessing-security-vulnerabilities-and-applying-patches).

## Additional documentation

The below documents are for general use.

!!! note "Technical Documentation"

    - [SOC Analyst Induction](training/analyst-induction.md)
    - [Collecting Digital Forensic Evidence](guidelines/collecting-evidence.md)
    - [Cyber Security Playbooks](guidelines/playbooks.md)

{% include 'threat-activity.md' %}

<script>
    if (window.location.hash && window.location.hash[1] === "/") {
        var location_parts = window.location.hash.slice(1).split("?id=");
        window.location.hash = '';
        if (location_parts[1]) {
            window.location.hash = location_parts[1];
        }
        window.location.pathname = window.location.pathname + location_parts[0].replace(".md", "");
    }
</script>
