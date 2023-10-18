### S0521 - Bloodhound/Sharphound Execution Commandlets 


####  DESCRIPTION  
Detects BloodHound activity in commandlines. Bloodhound is and Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment    

**example:**  
 


**Related**  
Bloodhound/Sharphound       


**Reference:**  
https://github.com/SigmaHQ/sigma/blob/cf29e28a54daa9d52f7d1a5996f023e2d08cde84/rules/windows/process_creation/proc_creation_win_hktl_bloodhound_sharphound.yml#L40     


####  ATT&CK TACTICS  
{{ mitre("S0521")}}    

Data Source(s): [Command](https://attack.mitre.org/datasources/DS001/)


#### SENTINEL RULE QUERY   

~~~
	let c1 = dynamic([' -CollectionMethod All ', ' --CollectionMethods Session ', ' --Loop --Loopduration ', ' --PortScanTimeout ', '.exe -c All -d', 'Invoke-Bloodhound', 'Get-BloodHoundData']);
    let c2 = dynamic([' -JsonFolder ', ' -ZipFileName ']);
    let c3 = dynamic([' DCOnly ', ' --NoSaveCache ']);
    find where (InitiatingProcessCommandLine has_any (c1) or ProcessCommandLine has_any (c1) or CommandLine has_any (c1)) or 
    InitiatingProcessCommandLine has_all (c2) or ProcessCommandLine has_all (c2) or CommandLine has_all (c2) or 
    InitiatingProcessCommandLine has_all (c3) or ProcessCommandLine has_any (c3) or CommandLine has_all (c3)   
~~~


#### Triage  

1. Inspect if the activity is expected and performed by an admin or a pen-test  
2. Check if other programs that use these command line option and accepts an 'All' parameter 


#### VERSION  
Version 1.0 (date: 10/07/2023)  
