### T1557 - AiTM - Phishing logging

#### DESCRIPTION

Detects potential successful AITM-Phishing-Login based on risk sign in level and application used.  

**Example:**   
Successful Sign-in logs with ResultType == "0" from a malicious (unexpected) IP Address  

**Related**  

https://www.microsoft.com/en-us/security/blog/2023/06/08/detecting-and-mitigating-a-multi-stage-aitm-phishing-and-bec-campaign/

**Reference:**  

https://github.com/GossiTheDog/ThreatHunting/blob/867aaa3e1ea996c5f19f5262f2f4b70e08c9ac37/AzureSentinel/Successful-AITM-Phishing-Login 

####  ATT&CK TACTICS  
{{ mitre("T1557")}}   
{{ mitre("T1111")}}

Data Source(s): [Logon Session](https://attack.mitre.org/datasources/DS0028/)

#### SENTINEL RULE QUERY  

~~~
SigninLogs  
| where parse_json(RiskEventTypes_V2) has_any ("unfamiliarFeatures","Travel") and RiskLevelDuringSignIn == "high"
| extend authenticationStepResultDetail_ = tostring(parse_json(AuthenticationDetails)[0].authenticationStepResultDetail) //Capture first sucessful password auth
| where ResultType == "0" or authenticationStepResultDetail_ == "Correct password"
| where AppDisplayName == "OfficeHome"
| project-reorder TimeGenerated,IPAddress, Location, UserPrincipalName, AppDisplayName, Category, authenticationStepResultDetail_, ResultType, ResultDescription, RiskLevelDuringSignIn, RiskEventTypes_V2, RiskDetail, AutonomousSystemNumber,  AuthenticationDetails
~~~  

####  Triage  

1. Check IP Address origin and reputation  
2. Check historical User’s Sign-in activity  
3. Pivot on user’s device inspecting device logs for suspicious phishing urls 5-15min before the sign-in  
4. If a VPN related activity, confirm if it is expected and approved  
5. Reset user’s passwords and revoke session tokens if proven to be malicious   

####  FalsePositive  
1. Risky sign ins from AU locations  
2. Expected VPN usage  

####  VERSION  
Version 2.0 (date: 25/10/2023)  