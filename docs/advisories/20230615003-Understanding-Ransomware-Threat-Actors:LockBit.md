  
# Understanding Ransomware Threat Actors: LockBit - 20230615003

## Overview

This advisory uses the MITRE ATT&CK for Enterprise framework, version 13.1. See the MITRE ATT&CK Tactics and Techniques section for tables of LockBit’s activity mapped to MITRE ATT&CK® tactics and techniques.

The LockBit RaaS and its affiliates have negatively impacted organizations, both large and small, across the world. In 2022, LockBit was the most active global ransomware group and RaaS provider in terms of the number of victims claimed on their data leak site.

## Delivery

LockBit affiliates have been observed using various freeware and open-source tools that are intended for legal use. When repurposed by LockBit, these tools are then used for a range of malicious cyber activity, such as network reconnaissance, remote access and tunneling, credential dumping, and file exfiltration. Use of PowerShell and batch scripts are observed across most intrusions, which focus on system discovery, reconnaissance, password/credential hunting, and privilege escalation. Artifacts of professional penetration-testing tools such as Metasploit and Cobalt Strike have also been observed.

Table 4 of the [CISA advisory found here](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a), shows a list of tools that are used by LockBit Affiliates.

## What is the vulnerability?

Based on secondary sources, it was noted that affiliates exploit older vulnerabilities like [CVE-2021-22986](https://nvd.nist.gov/vuln/detail/CVE-2021-22986), F5 iControl REST unauthenticated Remote Code Execution Vulnerability, as well as newer vulnerabilities such as:

-   [CVE-2023-0669](https://nvd.nist.gov/vuln/detail/CVE-2023-0669): Fortra GoAnyhwere Managed File Transfer (MFT) Remote Code Execution Vulnerability
-   [CVE-2023-27350](https://nvd.nist.gov/vuln/detail/CVE-2023-27350): PaperCut MF/NG Improper Access Control Vulnerability

LockBit affiliates have been documented exploiting numerous CVEs, including:

-   [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228): Apache Log4j2 Remote Code Execution Vulnerability,
-   [CVE-2021-22986](https://nvd.nist.gov/vuln/detail/CVE-2021-22986): F5 BIG-IP and BIG-IQ Centralized Management iControl REST Remote Code Execution Vulnerability,
-   [CVE-2020-1472: NetLogon Privilege Escalation Vulnerability,](https://nvd.nist.gov/vuln/detail/CVE-2020-1472)
-   [CVE-2019-0708](https://nvd.nist.gov/vuln/detail/CVE-2019-0708): Microsoft Remote Desktop Services Remote Code Execution Vulnerability, and
-   [CVE-2018-13379](https://nvd.nist.gov/vuln/detail/CVE-2018-13379): Fortinet FortiOS Secure Sockets Layer (SSL) Virtual Private Network (VPN) Path Traversal Vulnerability.

## Detection and Remediation

The listed mitigations are ordered by MITRE ATT&CK tactic. Mitigations that apply to multiple MITRE ATT&CK tactics are listed under the tactic that occurs earliest in an incident’s lifecycle. 

### Detection

 1. Identify the presence of the below supplied KQL/ Kusto hunting code
 2. Identify the presence of the below supplied IOCs
 3. Inspect activity from the identified devices and/or users

### Recommended Remediation Steps

[Specific to type of infection] - Example from Agent Tesla:

1. Delete Registry Key entries and folder paths
2. Run a full Antivirus scan on the compromised device
3. Reset the affected user's passwords

## Reference

* URL Reference #1
* URL Reference #2

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

* SHA-256:b2416875d5f34fc9ed8d20bb5eaf554a6f2e86885e30e8b904ddd66d4745d491

Filename2.exe

* SHA-1: 2e05ea754f9765993690d961a2a35181
* SHA-256: fcf53f2ec6170b2b93ac8216d3928167187931db75331a1a037720bcc79e39d5

| Artefacts / IOC Type | IOC-Value | Description |
| - | --- | - |
|Filehash|SHA-256:b2416875d5f34fc9ed8d20bb5eaf554a6f2e86885e30e8b904ddd66d4745d491|Downloaded file|
|Filehash|SHA-256:b2416875d5f34fc9ed8d20bb5eaf554a6f2e86885e30e8b904ddd66d4745d491|Malicious .js file|

### Signatures

Fast Corporate LTD

### IP Address

The following IPs historically were linked to that platform, any communications to them should be inspected and assessed if it’s relevant to that platform:

| Artefacts / IOC Type | IOC-Value | Description |
| - | - | --- |
|IP Address|8.8.8.8|Malicious sign-in attempts|
|IP Address|1.1.1.1|Outbound C2 communication|

### Domain Names

Note the below domains have not been defanged, please exercise caution when utilizing.

```text
https://www.setman.es/content.php
tavernelentrepot.be/xml.php
termowood.net/xml.php
textfabrik.de/xml.php
```
