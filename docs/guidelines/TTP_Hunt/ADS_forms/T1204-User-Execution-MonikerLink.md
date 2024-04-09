### T1204 - MonikerLink - User Execution

#### DESCRIPTION

Detects potential MonikerLink exploit CVE-2024-21413 activity by looking for certain strings in URLs

**Example:**

```
"href="file[:][/][/][/]\\10[.]10[.]111[.]111\test\test[.]rtf[!]something">CLICK ME<[/]a>*"
```

**Related**

Microsoft Outlook CVE-2024-21413

**Reference**

https://research.checkpoint.com/2024/the-risks-of-the-monikerlink-bug-in-microsoft-outlook-and-the-big-picture <br>
https://github.com/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability?tab=readme-ov-file <br>

#### ATT&CK TACTICS

{{mitre("T1204")}}

Data Source(s): [Network Traffic](https://attack.mitre.org/datasources/DS0029/)

#### SENTINEL RULE QUERY

```
union isfuzzy=true 
(EmailUrlInfo
| where Url matches regex @".*file:.*!"),
(union  DeviceNetworkEvents, DeviceEvents
| where RemoteUrl matches regex @".*file:.*!")
```

#### Triage

1. Inspect URL links to identify malicious activity

#### Version

Version 1.0 (date 19/2/2024)
