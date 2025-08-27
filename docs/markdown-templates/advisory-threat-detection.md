# ADVISORY TITLE - 2025MMDD001

## Overview

The WASOC has observed…

## Delivery

The primary delivery method is…
Historically, [Threat Name] has also been observed to be delivered via…

## Detection and Remediation

### Detection

1. Identify the presence of the below supplied KQL/ Kusto hunting code
1. Identify the presence of the below supplied IOCs
1. Inspect activity from the identified devices and/or users

### Recommended Remediation Steps

[Specific to type of infection] - Example from Agent Tesla:

1. Delete Registry Key entries and folder paths
1. Run a full Antivirus scan on the compromised device
1. Reset the affected user's passwords

## Reference

- URL Reference #1
- URL Reference #2

## Indicator of Compromise

### KQL Query

//KQL context and objective

```kusto
DeviceFileEvents  
| where TimeGenerated > ago(90d)
```

//KQL context and objective

```kusto
SecurityEvents  
| where TimeGenerated > ago(90d)
```

### Registry Key

```text
Key:  HKCU:\\<UserGuid>\\SOFTWARE\\MICROSOFT\\WINDOWS\\CURRENTVERSION\\RUN
Key-value:  …
```

### Folder

```text
C:\Users\<compromised user>\
C:\system\win32\
```

### File-Hash

Filename1.exe

- SHA-256:b2416875d5f34fc9ed8d20bb5eaf554a6f2e86885e30e8b904ddd66d4745d491

Filename2.exe

- SHA-1: 2e05ea754f9765993690d961a2a35181
- SHA-256: fcf53f2ec6170b2b93ac8216d3928167187931db75331a1a037720bcc79e39d5

| Artefacts / IOC Type | IOC-Value                                                                | Description        |
| -------------------- | ------------------------------------------------------------------------ | ------------------ |
| Filehash             | SHA-256:b2416875d5f34fc9ed8d20bb5eaf554a6f2e86885e30e8b904ddd66d4745d491 | Downloaded file    |
| Filehash             | SHA-256:b2416875d5f34fc9ed8d20bb5eaf554a6f2e86885e30e8b904ddd66d4745d491 | Malicious .js file |

### Signatures

Fast Corporate LTD

### IP Address

The following IPs historically were linked to that platform, any communications to them should be inspected and assessed if it’s relevant to that platform:

| Artefacts / IOC Type | IOC-Value | Description                |
| -------------------- | --------- | -------------------------- |
| IP Address           | 8.8.8.8   | Malicious sign-in attempts |
| IP Address           | 1.1.1.1   | Outbound C2 communication  |

### Domain Names

Note the below domains have not been defanged, please exercise caution when utilizing.

```text
https://www.setman.es/content.php
tavernelentrepot.be/xml.php
termowood.net/xml.php
textfabrik.de/xml.php
```
