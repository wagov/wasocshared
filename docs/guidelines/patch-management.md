# Patch Management Guideline

This guideline is intended to define a pragmatic target for effective patch management and associated tools for most use cases. This guide is primarily focused on routine patching as defined within [NIST Special Publication 800-40r4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf) (Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology).

## Small / hybrid scenarios

In some situations, a central management tool is already being used by a third party, or a deployment is small enough (e.g. dev/test environments) that incorporating into an enterprise wide management tool is not very effective. For these the below small scale operations tools that can be run locally are quite effective:

- [Windows Admin Center](https://learn.microsoft.com/en-gb/windows-server/manage/windows-admin-center/overview) - simple/predefined
- [Red Hat Satellite](https://www.redhat.com/en/technologies/management/satellite) - simple/predefined
- [Ansible (IT automation tool)](https://docs.ansible.com/ansible/latest/getting_started/index.html) - complex/manual

## Large / enterprise scenarios

For larger deployments across an enterprise using [Azure server management services](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/azure-server-management/ "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/azure-server-management/") for all on premise and cloud workloads can simplify backups/patching significantly:

- [Configure the service for a subscription - Cloud Adoption Framework | Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/azure-server-management/onboard-at-scale)
- [About Azure Automanage Machine Best Practices | Microsoft Learn](https://learn.microsoft.com/en-us/azure/automanage/overview-about)

!!! note "Vulnerability Management Business Context"

    Ensuring that [vulnerability management](../baselines/vulnerability-management.md) activities also ensure the appropriate business context is applied (e.g. using [Tags (Tenable Vulnerability Management)](https://docs.tenable.com/vulnerability-management/Content/Settings/Tagging/Tags.htm)) should effectively prioritise patch activities.

### Example patching approach

A checklist based on ACSC's [Assessing Security Vulnerabilities and Applying Patches](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-administration/assessing-security-vulnerabilities-and-applying-patches) resource is below:

- [ ] Configure and implement a fully automated patching process
    - [ ] [Azure Automanage for Windows Server | Microsoft Learn](https://learn.microsoft.com/en-us/azure/automanage/automanage-windows-server)
    - [ ] [Azure Automanage for Linux | Microsoft Learn](https://learn.microsoft.com/en-us/azure/automanage/automanage-linux)
    - [ ] [Windows Autopatch (for endpoints)](https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/overview/windows-autopatch-overview)
- [ ] Ensure backups are in place before patch window to enable rollbacks
- [ ] Ensure availability monitoring is in place to enable rapid addressing of patching issues before end of patch window
- [ ] Share the maintenance window (automated patching schedule) widely with the business
    - [ ] Default to weekly - e.g. 2am-5am a standard day each week (ideally before least busy day for operational team)
    - [ ] Potentially extend to fortnightly if teams can't be available weekly for patch issue remediation
- [ ] Exclude systems with major constraints making them not able to be patched in standard maintenance window
    - [ ] Isolate these systems individually in their own [network segments](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/network-hardening/implementing-network-segmentation-and-segregation)
    - [ ] Limit access to them from [monitored jump box / bastion](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-administration/secure-administration) type services
    - [ ] Schedule manual reviews of 'excluded' systems quarterly
- [ ] Critical external posture alerts and [advisories (from DGov and others)](../advisories.md) should trigger urgent / unplanned patching
    - [ ] **internet-facing services:** within two weeks, or within 48 hours if an exploit exists
    - [ ] **workstations, servers, network devices and other network-connected devices:** within one month
