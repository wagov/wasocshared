###  T1082 - SystemInformationDiscovery

####  DESCRIPTION  
The actor has executed commands to gather information about the storage devices on the local host

**Example:**  
> "cmd.exe /C "wmic path win32_logicaldisk get caption,filesystem,freespace,size,volumename" 

**Related**  
Volt Typhoon activity

**Reference**  
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection
https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/

####  ATT&CK TACTICS <br />
{{ mitre("T1082")}} 

Data source - [Command](https://attack.mitre.org/datasources/DS0017)

####  SENTINEL RULE QUERY <br />  
~~~
let selection_cmd = dynamic(["cmd", "wmic", "caption", "filesystem"]); 
DeviceProcessEvents
| where ActionType == "ProcessCreated"
| where FileName == "cmd.exe"
| where ProcessCommandLine has_all (selection_cmd)
//| summarize count(), first_seen = min(TimeGenerated), last_seen = max(TimeGenerated) by TenantId, DeviceName, AccountName, InitiatingProcessFolderPath, FolderPath, ProcessCommandLine
~~~

#### Triage <br />

1. Inspect which account and at what time the activity was performed  
2. Question the user if the activity was expected and approved  

#### Version <br />
Version 1.1 (date 07/02/2024)