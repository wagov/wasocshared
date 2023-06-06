# WA Cyber Security Unit (Office of Digital Government)

This site contains technical information to support WA Government Cyber Security activities. Please email cybersecurity@dpc.wa.gov.au with any feedback on this content.

## WA Security Operations Centre (WA SOC)

- [Connecting to the WA SOC](onboarding.md)    
- [Advisories (TLP:CLEAR)](advisories.md)
- [Incident Reporting User Guide (Jira)](docs/incident-reporting.md)

### Baselines

- [Baseline for Event Ingestion](onboarding/baseline-event-ingestion.md)

### Guidelines

- [Microsoft Sentinel Connector Guidance](onboarding/sentinel-guidance.md)

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