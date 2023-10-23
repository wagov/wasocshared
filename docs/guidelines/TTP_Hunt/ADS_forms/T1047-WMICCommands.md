### T1047 - WMIC Commands

####  DESCRIPTION  
The actor has executed WMIC commands to create a copy of the ntds.dit file and SYSTEM registry.   

**example:**  
wmic process call create "ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\pro  
wmic process call create "cmd.exe /c ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\Pro"  
wmic process call create "cmd.exe /c mkdir C:\Windows\Temp\tmp & ntdsutil \"ac i ntds\" ifm   

**Related**  
Volt Typhoon activity

**Reference**  
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection
https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/

####  ATT&CK TACTICS
{{ mitre("T1047") }}  

Data source - [Command](https://attack.mitre.org/datasources/DS0017)

####  SENTINEL RULE QUERY  ###  
~~~
let c1 = dynamic(["wmic", "process", "create"]);  
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1)   
~~~  

#### Triage

1. Inspect which account and at what time the activity was performed  
2. Question the user if the activity was expected and approved  

#### Version
Version 1.0 (date 5/7/2023)
