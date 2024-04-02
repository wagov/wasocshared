## T1090 - Proxy - netsh abuse

### DESCRIPTION

Detects usage of [netsh](https://attack.mitre.org/software/S0108) in the commands that configure a new port forwarding (PortProxy) rule

#### Example:

> netsh I p a v l=8001 listena=127.0.0.1 connectp=80 c=192.168.1.1.
> netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=9999"

#### Related

LOLBINs

#### Reference:

https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/identifying-and-mitigating-living-off-the-land-techniques
https://github.com/SigmaHQ/sigma/blob/49adcf9a00247ed6c3daacba03b589470f6716d0/rules/windows/process_creation/proc_creation_win_netsh_port_forwarding.yml#L7

#### ATT&CK TACTICS

{{ mitre("T1090")}}

Data Source(s): [Command](https://attack.mitre.org/datasources/DS0017), [Process](https://attack.mitre.org/datasources/DS0009/)

#### SENTINEL RULE QUERY

```
let selection_cli_1 = dynamic(['interface','portproxy','add','v4tov4']);
let selection_cli_2 = dynamic(['i' ,'p ','a ','v ']);
let selection_cli_3 = dynamic(['connectp', 'listena', 'c=']);
union isfuzzy=true 
(DeviceProcessEvents
| where ActionType == "ProcessCreated"
| where FolderPath endswith @"\netsh.exe" or ProcessVersionInfoOriginalFileName == "netsh.exe"
| where 
ProcessCommandLine has_all (selection_cli_1) or ProcessCommandLine has_all (selection_cli_2) or ProcessCommandLine has_all (selection_cli_3) ),
(SecurityEvent
| where EventID == 4688
| where NewProcessName endswith @"\netsh.exe" //or ProcessVersionInfoOriginalFileName == "netsh.exe"
| where CommandLine has_all (selection_cli_1) or CommandLine has_all (selection_cli_2) or CommandLine has_all (selection_cli_3))
```

#### Triage

1. Inspect if the activity was expected and approved

#### FalsePositive

- Legitimate administration activity

#### VERSION

Version 1.0 (date: 20/03/2024)

---
