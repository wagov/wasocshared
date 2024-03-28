### S0154 - Cobalt Strike: DNS Beaconing

#### DESCRIPTION

Cobalt Strike is a famous Pen Test tool that is used by pen testers as well as attackers alike to compromise an environment.
The query tries to detect suspicious DNS queries known from Cobalt Strike beacons.

**Example:**

> aaa.stage.\[encryptedstage\].MaliciousDomain.com <br>
> baa.stage.\[encryptedstage\].MaliciousDomain.com <br>
> caa.stage.\[encryptedstage\].MaliciousDomain.com <br>
> post.\[EncryptedData\].\[RandomValue\].MaliciousDomain.com <br>

**Related**

CobaltStrike

**Reference:**

https://github.com/SigmaHQ/sigma/blob/dcfb4c5c28431dcdc1d26ed4e008945965afd8ed/rules/network/dns/net_dns_mal_cobaltstrike.yml#L4 <br>
https://blog.sekoia.io/hunting-and-detecting-cobalt-strike <br>
https://blog.gigamon.com/2017/07/26/footprints-of-fin7-tracking-actor-patterns-part-1 <br>

#### ATT&CK TACTICS

{{mitre("S0154")}}

Data Source(s): [Network Traffic](https://attack.mitre.org/datasources/DS0029)

#### SENTINEL RULE QUERY

```
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
```

#### Triage

1. Inspect DNS queries and destination IP
1. Note source of endpoint beaconing

#### VERSION

Version 2.0 (date: 19/12/2023)
