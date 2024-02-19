### S0650 - Qakbot: Post compromise commands

#### DESCRIPTION

Detect when multiple Qakbot post compromise commands have been executed

**example:**\
Automated reconnaissance commands:
nslookup -querytype=ALL -timeout=12 \_ldap.\_tcp.dc.\_msdcs.\<domain_fqdn>

**Related**\
Malware

**Reference**\
https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules/blob/22cf7b2e0ef909e3f8ba1b39e2a8e897b6f49fb5/Defender%20For%20Endpoint/QakbotPostCompromiseCommandsExecuted.md?plain=1\
https://github.com/Azure/Azure-Sentinel/blob/2030f55a46b18e9d9723b06557d0653f38e21724/Hunting%20Queries/Microsoft%20365%20Defender/Campaigns/Qakbot/Qakbot%20reconnaissance%20activities.yaml#L2\
https://www.trendmicro.com/en_au/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html

#### ATT&CK TACTICS <br />

{{mitre("S0650")}}

Data Source(s): [Command](https://attack.mitre.org/datasources/DS0017), [Process](https://attack.mitre.org/datasources/DS0009/)

#### SENTINEL RULE QUERY <br />

```
let QakBotCommands = dynamic(['net view', 'cmd /c set', 'arp -a', 'ipconfig /all', 'nslookup-querytype=ALL -timeout=12', '_ldap._tcp.dc._msdcs.WORKGROUP', 'net share', 'net1 share', 'route print', 'net localgroup', 'whoami /all']); // source: https://twitter.com/1ZRR4H/status/1568395544359309312
DeviceProcessEvents
| where TimeGenerated between (startofmonth(ago(15d)) .. endofmonth(ago(15d))) //workaround for datetime filtering to run previous month data
| where ProcessCommandLine in (QakBotCommands)
| summarize TotalCommandsFound = count(), CommandLineList = make_set(ProcessCommandLine), TimeGenerated = min(TimeGenerated) by DeviceName, AccountName, TenantId //dummy TimeGenerated
| extend TotalUniqueCommandsFound = array_length(CommandLineList)
| where TotalUniqueCommandsFound > 3 // Adjust to reduce false positives
| sort by TotalUniqueCommandsFound, TotalCommandsFound
```

#### Triage  <br />

1. This is high-fidelity detections, collect information on the device(s) and understand the context of activities occurred using timeline analysis

#### FalsePositive<br />

1. Threat Hunt rules tuned, this is a high-fidelity detections

#### Version  <br />

Version 2.0 (date 09/02/2024)
