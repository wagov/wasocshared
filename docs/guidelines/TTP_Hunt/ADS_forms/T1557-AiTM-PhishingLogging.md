### T1557 - AiTM - Phishing logging

#### DESCRIPTION

Detects potential successful AITM-Phishing-Login based on risk sign in level and application used.  

**example:**   
Successful Sign-in logs with ResultType == "0" from a malicious (unexpected) IP Address  

**Related**  

https://www.microsoft.com/en-us/security/blog/2023/06/08/detecting-and-mitigating-a-multi-stage-aitm-phishing-and-bec-campaign/

**Reference:**  

https://github.com/GossiTheDog/ThreatHunting/blob/867aaa3e1ea996c5f19f5262f2f4b70e08c9ac37/AzureSentinel/Successful-AITM-Phishing-Login 

####  ATT&CK TACTICS  
{{ mitre("T1557")}}   
{{ mitre("T1111")}}

Data Source(s): TBA

#### SENTINEL RULE QUERY  

~~~
SigninLogs  
| where parse_json(RiskEventTypes_V2) has "unfamiliarFeatures" and RiskLevelDuringSignIn == "high"
| where ResultType == "0"
| where AppDisplayName == "OfficeHome"
| project-reorder TimeGenerated,IPAddress, Location, UserPrincipalName, AppDisplayName, Category, ResultType, ResultDescription, RiskLevelDuringSignIn, RiskEventTypes_V2, RiskDetail, AutonomousSystemNumber,  AuthenticationDetails
~~~  

####  Triage  

1. Check IP Address origin and reputation  
2. Check historical User’s Sign-in activity  
3. Pivot on user’s device inspecting device logs for suspicious phishing urls 5-15min before the sign-in  
4. If a VPN related activity, confirm if it is expected and approved  
5. Reset user’s passwords and revoke session tokens if proven to be malicious   

####  FalsePositive  
Risky sign ins from AU locations  
Expected VPN usage  

####  VERSION  
Version 1.0 (date: 22/08/2023)  