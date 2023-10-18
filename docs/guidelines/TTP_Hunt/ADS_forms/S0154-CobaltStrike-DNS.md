###  S0154 - Cobalt Strike: DNS Beaconing

####  DESCRIPTION  
Cobalt Strike is a famous Pen Test tool that is used by pen testers as well as attackers alike to compromise an environment. 
The query tries to detect suspicious DNS queries known from Cobalt Strike beacons. 
  
**example:**  
aaa.stage.[encryptedstage].MaliciousDomain.com, 
baa.stage.[encryptedstage].MaliciousDomain.com, 
caa.stage.[encryptedstage].MaliciousDomain.com
post.[EncryptedData].[RandomValue].MaliciousDomain.com


**Related**  
CobaltStrike

**Reference:**  
https://github.com/SigmaHQ/sigma/blob/dcfb4c5c28431dcdc1d26ed4e008945965afd8ed/rules/network/dns/net_dns_mal_cobaltstrike.yml#L4  
https://blog.sekoia.io/hunting-and-detecting-cobalt-strike/  
https://blog.gigamon.com/2017/07/26/footprints-of-fin7-tracking-actor-patterns-part-1/  


####  ATT&CK TACTICS<br>
{{mitre("S0154")}}

Data Source(s): [Network Traffic](https://attack.mitre.org/datasources/DS0029)

#### SENTINEL RULE QUERY<br>

~~~
let badNames = dynamic(["aaa.stage","baa.stage","caa.stage", "post.1"]);
(union isfuzzy=true
(DnsEvents 
| where Name has_any (badNames)
| extend Domain = Name, SourceIp = ClientIP, RemoteIP = todynamic(IPAddresses)
| mvexpand RemoteIP
| extend RemoteIP = tostring(RemoteIP)),
(VMConnection
| where isnotempty(RemoteDnsCanonicalNames) 
| parse RemoteDnsCanonicalNames with * '["' DNSName '"]' *
| where DNSName has_any (badNames)
| extend Domain = DNSName, RemoteIP = RemoteIp
))
| summarize StartTimeUtc = min(TimeGenerated), EndTimeUtc = max(TimeGenerated) by Domain, SourceIp, RemoteIP, Computer
| extend timestamp = StartTimeUtc, HostCustomEntity = Computer, IPCustomEntity = RemoteIP
~~~

#### Triage

1. Inspect DNS queries and destination IP
2. Note source of endpoint beaconing  


#### VERSION
Version 1.0 (date: 10/07/2023)



