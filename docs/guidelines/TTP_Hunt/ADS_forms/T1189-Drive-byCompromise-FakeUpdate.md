### T1189 - Drive-by Compromise - FakeUpdate  

#### DESCRIPTION  

Detects the existence of FakeUpdate .zip file, commonly associated with SocGholish malware family. Javascript file (.js) is usually hidden inside the .zip file  

**Example:**  
Edge.6ebddd.zip
Edge.7a859a.zip

**Related**  
https://www.secureworks.com/research/threat-profiles/gold-prelude   



**Reference:**  
https://redcanary.com/threat-detection-report/threats/socgholish/ 
https://www.cybereason.com/blog/threat-analysis-report-socgholish-and-zloader-from-fake-updates-and-installers-to-owning-your-systems 

#### ATT&CK TACTICS  

{{ mitre("T1189") }}   

Data Source(s): [File](https://attack.mitre.org/datasources/DS0022/)  

#### SENTINEL RULE QUERY  

~~~
DeviceFileEvents
| where FileName matches regex @"Edge\\.[a-z0-9]{6}\\.zip" or FileName matches regex @"Chrome\\.Update\\.[a-z0-9]{6}\\.zip" or FileName matches regex @"FireFox\\.Update\\.[a-z0-9]{6}\\.zip" or FileName matches regex @"download\\.[a-z0-9]{6}\\.zip"
| where InitiatingProcessFileName <> "MsSense.exe" //Exclude files detected by Defender for Endpoint
~~~

#### Triage  

1. Examine the FileOriginUrl field and determine whether it's suspicious/ malicious
2. Delete the malicious file
3. Determine whether user have clicked the file/ not

#### FalsePositive  

Unknown

#### VERSION  

Version 1.0 (date: 22/08/2023)  