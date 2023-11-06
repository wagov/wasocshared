### T1047 - WMIC Commands

####  DESCRIPTION  
The actor has executed WMIC commands to create a copy of the ntds.dit file and SYSTEM registry.   

**Example:**  
> wmic process call create "ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\pro  
> wmic process call create "cmd.exe /c ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\Pro"  
> wmic process call create "cmd.exe /c mkdir C:\Windows\Temp\tmp & ntdsutil \"ac i ntds\" ifm   

**Related**  
Volt Typhoon activity

**Reference**  
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection
https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/

####  ATT&CK TACTICS
{{ mitre("T1047") }}  

Data Source(s): [Command](https://attack.mitre.org/datasources/DS0017), [Process Creation](https://attack.mitre.org/datasources/DS0009/#Process%20Creation)

####  SENTINEL RULE QUERY  ###  

~~~
let selection_main = dynamic(['wmic.exe','powershell.exe','cmd.exe','ntdsutil.exe']);
let selection_wmic = dynamic(["wmic", "process", "create"]); //not used
let selection_command = dynamic(['ntdsutil','ntds','ac','i','ifm']);
union isfuzzy=true
(DeviceProcessEvents
| where FolderPath has_any(selection_main)
| where ProcessCommandLine has_all (selection_command) or InitiatingProcessCommandLine has_all (selection_command)
),
(SecurityEvent
| where EventID == 4688
| where CommandLine has_all (selection_command)
)
~~~  

#### Triage

1. Verify the command line that ntds.dit is copied by user, and check folder location where ntds.dit was copied
2. Confirm with user if the activity was expected and approved

#### Version
Version 1.1 (date 26/10/2023)
