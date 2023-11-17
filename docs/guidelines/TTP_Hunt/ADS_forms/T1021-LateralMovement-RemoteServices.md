### T1021 - Lateral Movement - Remote Services   
  

####  DESCRIPTION  
Detects lateral movement activity of webservers onto core systems.  

**example:**  
N/A    

**Related**  
N/A        

**Reference:**  
https://attack.mitre.org/techniques/T1021/    


####  ATT&CK TACTICS    
{{ mitre("T1003.001")}}    

Data Source(s): [Network Traffic](https://attack.mitre.org/datasources/DS0029)  


#### SENTINEL RULE QUERY   

~~~
let webserver_ip = ()
{DeviceNetworkEvents
| where InitiatingProcessFileName has_any ('w3wp','nginx','apache') and LocalIPType == "Private"
| distinct LocalIP};
DeviceNetworkEvents
| where (LocalIP has_any (webserver_ip()) or DeviceName contains "Web") and RemotePort in (3389,22)
| distinct RemoteIP, DeviceName,RemotePort, InitiatingProcessCommandLine
~~~


#### Triage  

1. Inspect command lines for suspicious activity   
2. Inspect if the activity is expected and approved. It may be performed by an admin or a service  


#### VERSION  
Version 1.0 (date: 10/07/2023)  
