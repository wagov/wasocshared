### S0357 - Impacket Secretdump with SMB2

#### DESCRIPTION

Actor may use Impacket’s wmiexec, which redirects output to a file within the victim host’s ADMIN$ share (C:\\Windows) containing an epoch timestamp in its name.

**Example:**

> cmd.exe /Q /c dir 1> \\127.0.0.1\\ADMIN$\_\_1684944005.9400265 2>&1

**Related**\
Volt Typhoon activity

**Reference:**\
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection%5C
https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/%5C
https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-277a%5C
https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Attacker%20Tools%20Threat%20Protection%20Essentials/Hunting%20Queries/PotentialImpacketExecution.yaml

#### ATT&CK TACTICS<br>

{{mitre("S0357")}}

Data Source(s): [Process](https://attack.mitre.org/datasources/DS0009/), [Command](https://attack.mitre.org/datasources/DS0017/)

#### SENTINEL RULE QUERY

```
(union isfuzzy=true
  (SecurityEvent
  | where EventID == '5145'
  | where RelativeTargetName has 'SYSTEM32' and RelativeTargetName endswith @".tmp"
  | where ShareName has "\\\\*\\ADMIN$"
  ),
  (WindowsEvent
  | where EventID == '5145' 
  | extend RelativeTargetName= tostring(EventData.RelativeTargetName)
  | extend ShareName= tostring(EventData.ShareName)
  | where RelativeTargetName has 'SYSTEM32' and RelativeTargetName endswith @".tmp"
  | where ShareName has "\\\\*\\ADMIN$"
  | extend Account =  strcat(tostring(EventData.SubjectDomainName),"\\", tostring(EventData.SubjectUserName))
  )
  )
  | extend timestamp = TimeGenerated 
  | extend NTDomain = split(Account, '\\', 0)[0], UserName = split(Account, '\\', 1)[0]
  | extend HostName = split(Computer, '.', 0)[0], DnsDomain = strcat_array(array_slice(split(Computer, '.'), 1, -1), '.')
  | extend Account_0_Name = UserName
  | extend Account_0_NTDomain = NTDomain
  | extend Host_0_HostName = HostName
  | extend Host_0_DnsDomain = DnsDomain
```

#### Triage

1. Identify user/service triggering the activity
1. Validate .tmp file names and location
1. Investigate further if the activity is expected and approved

#### VERSION

Version 1.1 (date: 26/10/2023)
