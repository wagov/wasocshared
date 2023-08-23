###  S0154 - Cobalt Strike NamedPipe

####  DESCRIPTION  
Cobalt Strike is a famous Pen Test tool that is used by pen testers as well as attackers alike to compromise an environment. 
CobaltStrike uses named pipes for communication between processes. Default beacon configs use pipes in the format "MSSE-x-server", where "x" is a number from 1 to 4 characters. 
  
**example:**  
"MSSE-x-server", where "x" is a number from 1 to 4 characters  

**Related**  
CobaltStrike

**Reference:**  
https://github.com/SigmaHQ/sigma/blob/dcfb4c5c28431dcdc1d26ed4e008945965afd8ed/rules/windows/pipe_created/pipe_created_mal_cobaltstrike.yml#L4  
https://twitter.com/d4rksystem/status/1357010969264873472  
https://labs.f-secure.com/blog/detecting-cobalt-strike-default-modules-via-named-pipe-analysis/  
https://github.com/SigmaHQ/sigma/issues/253  
https://blog.cobaltstrike.com/2021/02/09/learn-pipe-fitting-for-all-of-your-offense-projects/  
https://redcanary.com/threat-detection-report/threats/cobalt-strike/  

####  ATT&CK TACTICS<br>
[S0154](https://attack.mitre.org/software/S0154/)  

Data Source(s): [Named Pipe](https://attack.mitre.org/datasources/DS0023)  

#### SENTINEL RULE QUERY<br>

~~~
DeviceEvents
| where ActionType == "NamedPipeEvent"
| where AdditionalFields.PipeName has_any ('MSSE-','msagent_','status_','postex_ssh_','postex_')
~~~

#### Triage

1. Inspect named pipe pattern if matching "MSSE-x-server"  



#### VERSION
Version 0.1 (date: 10/07/2023)
