### S0650 - Qakbot: Process executions

####  DESCRIPTION  
Detects potential QBot activity by looking for process executions used previously by QBot  

**Example:**  
> "C:\Windows\System32\cmd.exe" /c ping.exe -n 6 127.0.0.1 & type "C:\Windows\System32\calc.exe" > "C:\Users\admin\AppData\Local\Temp\aNkxbUo.exe"  

**Related**  
Malware  

**Reference**  
https://github.com/SigmaHQ/sigma/blob/4de6102dc7d94c9ee70995aeea27b77184d62c35/rules-emerging-threats/2019/Malware/QBot/proc_creation_win_malware_qbot.yml#L4    
https://www.trendmicro.com/en_au/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html   


####  ATT&CK TACTICS
{{mitre("S0650")}}

Data source - Command  

####  SENTINEL RULE QUERY  

~~~  
let c1 = dynamic([@'/c ping.exe -n 6 127.0.0.1 & type']);
let c2 = dynamic(['regsvr32.exe','.tmp',@'C:\ProgramData']);
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1) or
InitiatingProcessCommandLine has_all (c2) or ProcessCommandLine has_all (c2) or CommandLine has_all (c2) 
~~~  


####  Triage  
1. Inspect commands to identify Qbot activity    
 


####  Version  
Version 1.0 (date 5/7/2023)  
