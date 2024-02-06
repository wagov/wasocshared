### T1190 - Webshell by suspicious URI requests

#### DESCRIPTION

This will look for connections to files on the server that are requested by only a single client.
This analytic will be effective where an actor is utilising relatively static operational IP addresses. The threshold can be modified.
The larger the execution window for this query the more reliable the results returned.

**example:**\
NA

!!! tip "Related"
    common persistance

**Reference:**\
https://attack.mitre.org/techniques/T1505/003/%5C
https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/W3CIISLog/RareClientFileAccess.yaml

#### ATT&CK TACTICS

{{ mitre("T1190")}}

Data Source(s): [Network Traffic](https://attack.mitre.org/datasources/DS0029/)

#### SENTINEL RULE QUERY

```
let clientThreshold = 1;
  let scriptExtensions = dynamic([".php", ".aspx", ".asp", ".cfml"]);
  let data = W3CIISLog
  | where csUriStem has_any(scriptExtensions)
  |where scStatus == 200
  |where ipv4_is_private(cIP) == false and  cIP !startswith "fe80" and cIP !startswith "::" and cIP !startswith "127."
  |where ipv4_is_private(sIP) == false   
  | summarize StartTime = min(TimeGenerated), EndTime = max(TimeGenerated), makelist(cIP), dcount(TimeGenerated) by csUriStem, sSiteName, csUserAgent;
  data
  | mvexpand list_cIP
  | distinct StartTime, EndTime, tostring(list_cIP), csUriStem, sSiteName, csUserAgent
  | summarize StartTime = min(StartTime), EndTime = max(StartTime), dcount(list_cIP), makelist(list_cIP), makelist(sSiteName) by csUriStem, csUserAgent
  | where dcount_list_cIP == clientThreshold 
  | where csUserAgent startswith "Mozilla"
  | extend timestamp = StartTime, UserAgentCustomEntity = csUserAgent    
```

#### Triage

1. Inspect network traffic to potential web shells. Most webshells take commands via POSTs. Successfull commands are met with a "200"

#### FalsePositive

unknown

#### VERSION

Version 1.0 (date: 10/07/2023)
