## T1016-Potential Discovery Activity Via Dnscmd.exe
  
###  DESCRIPTION

Detects an attempt to leverage dnscmd.exe to enumerate the DNS zones of a domain. DNS zones used to host the DNS records for a particular domain    

#### Example:
> dnscmd . /enumrecords /zone {REDACTED}

> dnscmd . /enumzones

> dnscmd /enumrecords {REDACTED} . /additional


#### Related
LOLBins
Discovery
#### Reference:
- https://github.com/SigmaHQ/sigma/blob/583f08ecaca532c7bff6e56e73c2e25c5b184796/rules/windows/process_creation/proc_creation_win_dnscmd_discovery.yml#L13
- https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/dnscmd
- https://lolbas-project.github.io/lolbas/Binaries/Dnscmd/
- https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection

####  ATT&CK TACTICS

{{ mitre("T1016")}}

Data Source(s): [Command](https://attack.mitre.org/datasources/DS0017), [Process](https://attack.mitre.org/datasources/DS0009/)

#### SENTINEL RULE QUERY

~~~
let selection_cli = dynamic(['/enumrecords','/enumzones','/ZonePrint','/info']);
DeviceProcessEvents
| where FolderPath endswith @"dnscmd.exe" and ProcessCommandLine has_any (selection_cli)
//| summarize count(), num_distinctDevices = dcount(DeviceName), set_ProcessCMD=make_set(ProcessCommandLine), set_InitiatingProcessCMD=make_set(InitiatingProcessCommandLine), first_ = min(TimeGenerated), last_ = max(TimeGenerated) by InitiatingProcessFolderPath, InitiatingProcessFileName, FolderPath, FileName, AccountName, TenantId 
~~~

#### Triage

1. Remove the comment "//" in 'summarize' statement in above KQL to assist in analysis and removing data duplicates.
2. Examine the FolderPath and the command-line whether the activity is suspicious
3. Inspect if the activity was expected and approved

#### FalsePositive

Legitimate administration use 

#### VERSION

Version 1.0 (date: 20/03/2024)
