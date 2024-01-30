### S0650 - Qakbot: Post compromise commands

#### DESCRIPTION

Detect when multiple Qakbot post compromise commands have been executed

**example:**

> Automated reconnaissance commands:\
> nslookup -querytype=ALL -timeout=12 \_ldap.\_tcp.dc.\_msdcs.\<domain_fqdn>

**Related**\
Malware

**Reference**\
https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules/blob/22cf7b2e0ef909e3f8ba1b39e2a8e897b6f49fb5/Defender%20For%20Endpoint/QakbotPostCompromiseCommandsExecuted.md?plain=1%5C
https://github.com/Azure/Azure-Sentinel/blob/2030f55a46b18e9d9723b06557d0653f38e21724/Hunting%20Queries/Microsoft%20365%20Defender/Campaigns/Qakbot/Qakbot%20reconnaissance%20activities.yaml#L2%5C
https://www.trendmicro.com/en_au/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html

#### ATT&CK TACTICS

{{mitre("S0650")}}

Data source - Command

#### SENTINEL RULE QUERY

```
let c1 = dynamic(['net view', 'cmd /c set', 'nslookup-querytype=ALL -timeout=12', '_ldap._tcp.dc._msdcs.WORKGROUP', 'net share', 'net1 share', 'route print', 'net localgroup', 'whoami /all']);
find where InitiatingProcessCommandLine in (c1) or ProcessCommandLine in (c1) or CommandLine in (c1)  
```

#### Triage

1. Inspect other commands to confirm reconnaissance and beaconing activities

#### Version

Version 1.0 (date 5/7/2023)
