### T1021 - Lateral Movement - Webservers  
  

####  DESCRIPTION  
Detects lateral movement activity of webservers onto core systems.  


**example:**  
NA    


**Related** \
NA        


**Reference:**  
NA    


####  ATT&CK TACTICS    
T1003.001    

Data Source(s): [Network Traffic](https://attack.mitre.org/datasources/DS0029)  


#### SENTINEL RULE QUERY   

~~~
let webserver_ip = ()
{DeviceNetworkEvents
| where InitiatingProcessFileName has_any ('w3wp','nginx','apache') and LocalIPType == "Private"
| distinct LocalIP};
 DeviceNetworkEvents
| where InitiatingProcessFileName != 'Microsoft.Tri.Sensor.exe' // filtered out
| where (LocalIP has_any (webserver_ip()) or DeviceName contains "Web") and RemotePort in (3389,22)
~~~


#### Triage  

1. Inspect if the activity under InitiatingProcessFileName is expected.   


#### FalsePositive   
Legitimate service or Admin activity    

#### VERSION  
Version 1.0 (date: 10/07/2023)  