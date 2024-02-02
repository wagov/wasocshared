###  T1082 - System Information Discovery

####  DESCRIPTION  
The actor has executed commands to gather information about the storage devices on the local host

**Example:**  
> "cmd.exe /C "wmic path win32_logicaldisk get caption,filesystem,freespace,size,volumename" 

**Related**  
Volt Typhoon activity

**Reference**  
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection
https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/

####  ATT&CK TACTICS
{{ mitre("T1082")}}  

Data source - [Command](https://attack.mitre.org/datasources/DS0017)

####  SENTINEL RULE QUERY  ###  
~~~
let c1 = dynamic(["cmd", "wmic", "caption", "filesystem"]); 
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1) 
~~~

#### Triage

1. Inspect which account and at what time the activity was performed  
2. Question the user if the activity was expected and approved  

#### Version
Version 1.0 (date 5/7/2023)
