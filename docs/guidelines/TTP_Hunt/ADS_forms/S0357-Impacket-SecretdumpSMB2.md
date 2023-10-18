###  S0357 - Impacket Secretdump with SMB2  

####  DESCRIPTION  
Actor may use Impacket’s wmiexec, which redirects output to a file within the victim host’s ADMIN$ share (C:\Windows\) containing an epoch timestamp in its name.  


**example:**  
cmd.exe /Q /c dir 1> \\127.0.0.1\ADMIN$\__1684944005.9400265 2>&1  

**Related**  
Volt Typhoon activity  

**Reference:**  
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection  
https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/  
https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-277a  
https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Attacker%20Tools%20Threat%20Protection%20Essentials/Hunting%20Queries/PotentialImpacketExecution.yaml  

####  ATT&CK TACTICS<br>
S0357 

Data Source(s): [Process](https://attack.mitre.org/datasources/DS0009/), [Command](https://attack.mitre.org/datasources/DS0017/)

#### SENTINEL RULE QUERY  

~~~
let c1 = dynamic(["SYSTEM32", ".tmp"]);
find where (EventID == 5145 and RelativeTargetName has 'SYSTEM32' and RelativeTargetName endswith @".tmp") or 
(EventID == 5145 and EventData has_all (c1)) 
~~~

#### Triage  


1. Identify user/service triggering the activity
2. Check time of activity if within business hours  
3. Investigate further if the activity is expected and approved   


#### VERSION
Version 1.0 (date: 10/07/2023)  
