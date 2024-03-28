### T1059 - MicroSCADA SCILC Command Execution


####  DESCRIPTION  
Identification of Events or Host Commands that are related to the MicroSCADA SCILC programming language and specifically command execution


**Example:**  
> C:\sc\prog\exec\scilc.exe -do pack\scil\s1.txt   


**Related**  
SCADA
[Sandworm](https://attack.mitre.org/groups/G0034/)


**Reference:**  
https://www.mandiant.com/resources/blog/sandworm-disrupts-power-ukraine-operational-technology


####  ATT&CK TACTICS  
{{ mitre("T1059")}}


Data Source(s): 
[Application Log](https://attack.mitre.org/datasources/DS0015/)

#### SENTINEL RULE QUERY   
~~~
let c1 = dynamic([@"\scilc.exe", "-do"]);
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1) 
~~~


#### Triage  
1. Evaluate the commandlines
2. Analyse the sample files being executed


#### FalsePositive  
1. Red Team activity

#### VERSION  
Version 1.0 (date: 10/11/2023)  