### T1016 - Info stealer Grixba

#### DESCRIPTION

Detects custom info stealer tool Grixba used by Play ransomware
It was developed by Play ransomware actors using Costura, a popular.NET development tool for embedding an application's dependencies into a single executable file

**example:**\
Imageload log containing file name costura.commandline.dll which is used by Grixba

**Related**\
Play ransomware

**Reference:**\
https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a\
https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/play-ransomware-volume-shadow-copy\
https://www.bleepingcomputer.com/news/security/play-ransomware-gang-uses-custom-shadow-volume-copy-data-theft-tool/

#### ATT&CK TACTICS <br />

{{mitre("T1016")}}

Data Source(s): [Module](https://attack.mitre.org/datasources/DS0011/)

#### SENTINEL RULE QUERY <br />

```
let filter_signOriginalFileName = dynamic(['MacDrive.exe', 'MacDrive Service.exe', 'MacDrive Helper.exe', 'SoftRAID.exe', 'SoftRAID Service.exe', 'SoftRAID Helper.exe']);
let filter_signCompanyName = dynamic(['Other World Computing, Inc.', 'OWC']);
DeviceImageLoadEvents
| where FileName contains "costura"
| where InitiatingProcessVersionInfoOriginalFileName !in (filter_signOriginalFileName) and InitiatingProcessVersionInfoCompanyName !in (filter_signCompanyName)
```

#### Triage <br />

1. Inspect if DLL image loaded's FileName is 'costura.commandline.dll', which is used by Grixba to parse command lines
1. Inspect InitiatingProcessFolderPath for any anomalies/ suspicious process

#### False Positive  <br />

Known good used by legitimate companies

#### VERSION <br />

Version 1.0 (date: 06/02/2024)
