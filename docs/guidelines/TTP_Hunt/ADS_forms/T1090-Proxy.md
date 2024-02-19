### T1090 - Proxy

#### DESCRIPTION

Adversary may use connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure.

**Example:**

> "cmd.exe /c "netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=9999 connectaddress=<internal ip address> connectport=8443 protocol=tcp""
> "cmd.exe /c netsh interface portproxy add v4tov4 listenport=50100 listenaddress=0.0.0.0 connectport=1433 connectaddress=<internal ip address>"

**Related**\
Volt Typhoon activity

**Reference:**\
https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection

#### ATT&CK TACTICS<br>

{{ mitre("T1090")}}

Data Source(s): [Process](https://attack.mitre.org/datasources/DS0009/), [Command](https://attack.mitre.org/datasources/DS0017/)

#### SENTINEL RULE QUERY<br>

```
let c1 = dynamic(["portproxy", "netsh", "add"]);
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1)
```

#### Triage

1. Inspect if the activity is expected and performed by an admin or a service

#### VERSION

Version 1.0 (date: 10/07/2023)
