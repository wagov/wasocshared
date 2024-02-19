### T1016 - Enumerate Network Topology

#### DESCRIPTION

Detects commands that are used to enumerate the network topology.

**Example:**

> curl www\<.>ip-api\<.>com\
> ldifde.exe -f c:\\windows\\temp\\cisco_up.txt -p subtree

**Related**\
Volt Typhoon activity

**Reference**\
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection
https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/

#### ATT&CK TACTICS

{{ mitre("T1016")}}

Data source - [Command](https://attack.mitre.org/datasources/DS0017)

#### SENTINEL RULE QUERY

```
let c1 = dynamic(["curl", "www.ip-api.com"]);
let c2 = dynamic(["ldifde.exe", "subtree"]);
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1) or
InitiatingProcessCommandLine has_all (c2) or ProcessCommandLine has_all (c2) or CommandLine has_all (c2)  
```

#### Triage

1. Inspect which account and at what time the activity was performed
1. Question the user if the activity was expected and approved

#### Version

Version 1.0 (date 5/7/2023)
