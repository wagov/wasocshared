### S0552 - AdFind Execution

####  DESCRIPTION  
Detects the use of Adfind. AdFind continues to be seen across majority of breaches. It is used to domain trust discovery to plan out subsequent steps in the attack chain.   

**example:**  
adfind.exe -f "(objectcategory=person)" > ad_users.txt      


objectcategory=person – Finds all person objects  
objectcategory=computer – Finds all computers in domain  
trustdmp – Dumps trust objects.  
objectcategory=subnet – Finds all subnets  
domainlist – Dumps all Domain NCs in forest in sorted DNS list format  
dcmodes – Shows modes of all DCs in forest from config  
adinfo – Shows Active Directory Info with whoami info.  
dclist – Dumps Domain Controllers FQDNs.  
computers_pwdnotreqd – Dumps users set with password not required.   


**Related**  
common tool           


**Reference:**  
https://github.com/SigmaHQ/sigma/blob/cac07b8ecd07ffe729ed82dfa2082fdb6a1ceabc/rules/windows/process_creation/proc_creation_win_pua_adfind_susp_usage.yml  
https://thedfirreport.com/2020/05/08/adfind-recon/   
https://thedfirreport.com/2021/01/11/trickbot-still-alive-and-well/   


####  ATT&CK TACTICS  
{{mitre("S0552")}}  

	- attack.discovery
    - attack.t1018
    - attack.t1087.002
    - attack.t1482
    - attack.t1069.002    

Data Source(s): [Command](https://attack.mitre.org/datasources/DS0017/)   


#### SENTINEL RULE QUERY   

~~~
let c1 = dynamic(['domainlist', 'trustdmp', 'dcmodes', 'adinfo', ' dclist ', 'computer_pwdnotreqd', 'objectcategory=', '-subnets -f', 'name="Domain Admins"', '-sc u:', 'domainncs', 'dompol', ' oudmp ', 'subnetdmp', 'gpodmp', 'fspdmp', 'users_noexpire', 'computers_active', 'computers_pwdnotreqd']);
find where 
FileName =~ "AdFind.exe" or ProcessVersionInfoOriginalFileName =~ "AdFind.exe" or 
InitiatingProcessFileName =~ "AdFind.exe" or InitiatingProcessVersionInfoOriginalFileName =~ "AdFind.exe" or Process =~ "AdFind.exe" or
ProcessCommandLine has_any (c1)    
~~~


#### Triage  

1. Check if AdFind is renamed and if any of the C1 commandlets are used in the command line   
2. Inspect if the activity is expected and approved.   


#### FalsePositive  

Legitimate administrative activity    


#### VERSION  
Version 1.0 (date: 10/07/2023)