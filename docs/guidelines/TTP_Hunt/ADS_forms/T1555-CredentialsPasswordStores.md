### T1555 - Credentials from Password Stores

#### DESCRIPTION

Detects suspicious credential access commands. Alone they may be normal but in concert, they may be worth looking into

**Example:**

> dir C:\\Users{REDACTED}.ssh\\known_hosts
> dir C:\\users{REDACTED}\\appdata\\roaming\\Mozilla\\firefox\\profiles
> reg query hklm\\software\\OpenSSH
> reg query hklm\\software\\OpenSSH\\Agent
> reg query hklm\\software\\realvnc
> reg query hklm\\software\\realvnc\\vncserver
> reg query hklm\\software\\realvnc\\Allusers
> reg query hklm\\software\\realvnc\\Allusers\\vncserver
> reg query hkcu\\software{REDACTED}\\putty\\session
> reg save hklm\\sam ss.dat
> reg save hklm\\system sy.dat

!!! tip "Related"
    Volt Typhoon

**Reference:**\
https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

#### ATT&CK TACTICS

{{ mitre("T1555")}}

Data Source(s): [Command](https://attack.mitre.org/datasources/DS001/)

#### SENTINEL RULE QUERY

```
let c1 = dynamic(["dir", ".ssh","known_hosts"]); 
let c2 = dynamic(["dir", @"firefox\profiles"]); 
let c3 = dynamic(["reg", " query", "OpenSSH"]); 
let c4 = dynamic(["reg", " query", "realvnc"]); 
let c5 = dynamic(["reg", " query", @"putty\session"]); 
let c6 = dynamic(["reg", " save", @" hklm\sam", " ss.dat"]); 
let c7 = dynamic(["reg", " save", @" hklm\system", " sy.dat"]); 
find where (InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1)) or
(InitiatingProcessCommandLine has_all (c2) or ProcessCommandLine has_all (c2) or CommandLine has_all (c2)) or
(InitiatingProcessCommandLine has_all (c3) or ProcessCommandLine has_all (c3) or CommandLine has_all (c3)) or 
(InitiatingProcessCommandLine has_all (c4) or ProcessCommandLine has_all (c4) or CommandLine has_all (c4)) or
(InitiatingProcessCommandLine has_all (c5) or ProcessCommandLine has_all (c5) or CommandLine has_all (c5)) or
(InitiatingProcessCommandLine has_all (c6) or ProcessCommandLine has_all (c6) or CommandLine has_all (c6)) or
(InitiatingProcessCommandLine has_all (c7) or ProcessCommandLine has_all (c7) or CommandLine has_all (c7))  
```

#### Triage

1. Inspect if the activity is expected and approved. It may be performed by an admin or a service
1. Pivot on the account, the host or the parent process and investigate additional activities

#### VERSION

Version 1.0 (date: 10/07/2023)
