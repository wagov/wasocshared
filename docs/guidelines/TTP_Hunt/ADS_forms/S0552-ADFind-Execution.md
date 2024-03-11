### S0552 - AdFind Execution

#### DESCRIPTION <br />

Detects the use of Adfind. AdFind continues to be seen across majority of breaches. It is used to domain trust discovery to plan out subsequent steps in the attack chain.

**Example:**

> adfind.exe -f "(objectcategory=person)" > ad_users.txt
>
> objectcategory=person – Finds all person objects\
> objectcategory=computer – Finds all computers in domain\
> trustdmp – Dumps trust objects.\
> objectcategory=subnet – Finds all subnets\
> domainlist – Dumps all Domain NCs in forest in sorted DNS list format\
> dcmodes – Shows modes of all DCs in forest from config\
> adinfo – Shows Active Directory Info with whoami info.\
> dclist – Dumps Domain Controllers FQDNs.\
> computers_pwdnotreqd – Dumps users set with password not required.

**Related**\
Common tool

**Reference:**\
https://github.com/SigmaHQ/sigma/blob/cac07b8ecd07ffe729ed82dfa2082fdb6a1ceabc/rules/windows/process_creation/proc_creation_win_pua_adfind_susp_usage.yml%5C
https://github.com/SigmaHQ/sigma/blob/b9c0dd661eac6b6efdb47f7cfcbb20b5a5c169da/rules/windows/process_creation/proc_creation_win_renamed_adfind.yml
https://thedfirreport.com/2020/05/08/adfind-recon/%5C
https://thedfirreport.com/2021/01/11/trickbot-still-alive-and-well/

#### ATT&CK TACTICS  <br />

{{mitre("S0552")}}

```
- attack.discovery
- attack.t1018
- attack.t1087.002
- attack.t1482
- attack.t1069.002    
```

Data Source(s): [Command](https://attack.mitre.org/datasources/DS0017/)

#### SENTINEL RULE QUERY   <br />

```
let selection_1 = dynamic(['domainlist', 'trustdmp', 'dcmodes', 'adinfo', ' dclist ', 'computer_pwdnotreqd', 'objectcategory=', '-subnets -f', 'name="Domain Admins"', '-sc u:', 'domainncs', 'dompol', ' oudmp ', 'subnetdmp', 'gpodmp', 'fspdmp', 'users_noexpire', 'computers_active', 'computers_pwdnotreqd']); 
DeviceProcessEvents
| where ActionType == "ProcessCreated"
| where FileName == "AdFind.exe" or FolderPath endswith @"\AdFind.exe"
| where ProcessCommandLine has_any (selection_1)
```

#### Triage  <br />

1. This is a high-fidelity threat hunt rules, check the user that performed this action.
1. Inspect if the activity is expected and approved.
1. If this process is unexpected, build further context upon user and device's activities using timeline analysis

#### FalsePositive  <br />

1. Legitimate administrative activity.
1. Tuned, high-fidelity threat hunt rules

#### VERSION   <br />

Version 2.0 (date: 10/02/2024)
