# WA Cyber Security Unit (Office of Digital Government)

This site contains technical information to support WA Government Cyber Security activities. Please email cybersecurity@dpc.wa.gov.au with any feedback on this content.

## WA Security Operations Centre (WA SOC)

- [Connecting to the WA SOC](onboarding.md)    
- [Advisories (TLP:CLEAR)](advisories.md)
- [Incident Reporting User Guide (Jira)](docs/incident-reporting.md)

### Baselines

The WA SOC has developed a [Baseline for Event Ingestion](onboarding/baseline-event-ingestion.md). It's currently under review to align with [MITRE ATT&CK®](https://attack.mitre.org) and develop detection coverage/quality into a standalone baseline. See [MITRE Data Sources](https://attack.mitre.org/datasources/) for SIEM (sensors/events) coverage and [MITRE Tactics](https://attack.mitre.org/tactics/enterprise/) for SIEM automated detection coverage.


!!! danger "Critical Infrastructure Entities"

    The [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) detail very effective network and server hardening controls that are a highly valuable addition to the ACSC Essential 8, especially for entities in scope of [SOCI regulatory obligations](https://www.cisc.gov.au/legislative-information-and-reforms/critical-infrastructure/regulatory-obligations).


### Guidelines

- [Guide to Securing Remote Access Software (CISA)](https://www.cisa.gov/resources-tools/resources/guide-securing-remote-access-software) - remote access software overview, including the malicious use of remote access software, detection methods, and recommendations for all organizations.
- [#StopRansomware Guide (CISA)](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) - one-stop resource to help organizations reduce the risk of ransomware incidents through best practices to detect, prevent, respond, and recover, including step-by-step approaches to address potential attacks.
- [Microsoft Sentinel Connector Guidance](onboarding/sentinel-guidance.md) - Sentinel deployment guide including prioritisation of connector configuration based on cost and complexity.


## Technical Documentation

- [SOC Analyst Induction](docs/analyst-induction.md)
  - [Azure VM (Virtual Machines) Basic Training](docs/azure-basics.md)
  - [Security Operations Workstation Self-Build (Linux, macOS, Windows)](docs/workstations.md)
- [Collecting Digital Forensic Evidence](docs/collecting-evidence.md)
- [Cyber Security Playbooks](docs/playbooks.md)





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
