# WA Cyber Security Unit (Office of Digital Government)

[![OpenSSF Scorecard](https://img.shields.io/ossf-scorecard/github.com/wagov/wasocshared.svg?label=openssf%20scorecard)](https://securityscorecards.dev/viewer/?uri=github.com/wagov/wasocshared)

This site contains technical information to support WA Government Cyber Security activities. Please propose updates directly via the edit link on each page or email [cybersecurity@dpc.wa.gov.au](mailto:cybersecurity@dpc.wa.gov.au) with any feedback. The site is built with [Material for MkDocs (reference)](https://squidfunk.github.io/mkdocs-material/reference/) which includes several [extensions to markdown](https://squidfunk.github.io/mkdocs-material/setup/extensions/) for enhanced technical writing.

!!! tip "RSS Feeds"

    If you would like to subscribe to updates for this site please use the [RSS](/rss.xml) or [ATOM](/atom.xml) feeds.

## WA Security Operations Centre (WASOC)

- [Connecting to the WASOC](onboarding.md) ([Sentinel Guidance](onboarding/sentinel-guidance.md))
- [Advisories (TLP:CLEAR)](advisories.md)
- [Incident Reporting User Guide (Jira)](guidelines/incident-reporting.md)
- [Threat Hunting (MITRE ATT&CK Tactics and Techniques)](guidelines/TTP_Hunt/ttp-detection-guidelines.md)
- [ACSC Essential Eight Assessment Process Guide](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-assessment-process-guide)

## Baselines & Guidelines

Baselines are for use as self-assessment checklists, and guidelines are for general implementation guidance.

!!! abstract "Baselines"

    - [Security Operations Baseline](baselines/security-operations.md) - aligned with [MITRE 11 Strategies of a World-Class Cybersecurity Operations Center](pdfs/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf) and [ACSC's Cyber Incident Response Plan Resource](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/publications/cyber-incident-response-plan).
    - [Detection Coverage Baseline](baselines/data-sources.md) - *[telemetry collection](https://attack.mitre.org/datasources/)* and *[detection analytics](https://attack.mitre.org)* aligned to the [MITRE ATT&CK Framework](https://attack.mitre.org).
    - [Vulnerability Management Baseline](baselines/vulnerability-management.md) - focused on undertaking operational **Identify** and **Protect** capabilities.

!!! danger "Critical Infrastructure Entities and Operational Technology"

    The [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) are clear targeted recommendations focusing on most common and impactful threats, including cost, complexity and impact ratings against each recommendation. These are highly relevant targets for entities in scope of [SOCI regulatory obligations](https://www.cisc.gov.au/legislative-information-and-reforms/critical-infrastructure/regulatory-obligations).

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/podtgMpjVp4?si=rmJ_tqjca9iQX_in" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

!!! tip "Guidelines"

    - Supply Chain Risk Management Guideline - Implementation guidance for [ACSC Cyber Supply Chain Risk Management](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/outsourcing-and-procurement/cyber-supply-chains/cyber-supply-chain-risk-management).
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
