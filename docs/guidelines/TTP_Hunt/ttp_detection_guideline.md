# TTP Detection Guideline

This page serves as a high-level guideline specifically for WA SOC threat hunting activities, showcasing prominent tactics, techniques, and procedures (TTPs). The ADS provides a tailored Kusto Query Language (KQL) queries to assist in threat hunting inside Microsoft Sentinel environment.

The [MITRE ATT&CK](https://attack.mitre.org/) framework is a knowledge base of adversary tactics and techniques based on real-world observations. Relevant KQL queries are mapped to each of the techniques used by threat actor tactics in line with the MITRE ATT&CK framework.

This section highlights queries that can be mapped in the MITRE ATT&CK Framework. Reconnaissance and Resource Development are out of the hunting services initial scope. The [Top 10 MITRE ATT&CK Techniques for Ransomware](https://top-attack-techniques.mitre-engenuity.org) is another sensible resource with a broader scope that can also be used to prioritise detection logic.

## Guidelines/Instructions:
* Review the TTP Hunt results shared with you via email/JIRA ticket.
* Identify the detected TTP MITRE ATT&CK code, and refer to ADS document
* Understand the detection objectives and perform triage investigation against detected logs
* Upon true-positive investigation results, raise an incident ticket with WA SOC. Reference: [WA SOC - Incident Reporting](https://soc.cyber.wa.gov.au/guidelines/incident-reporting/)
* Upon false-positive/benign true-positive investigation results, OR if you would like to request specific threat hunt TTPs, please contact cybersecurity@dpc.wa.gov.au 

## Initial Access
| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1190 | Web shells | [Network Traffic](https://attack.mitre.org/datasources/DS0029/)  | [T1190 - Webshells Suspicious URI](./ADS_forms/T1190-WebshellsSuspiciousURI.md) |
| TA0001 | PcAppStore | [Network Traffic](https://attack.mitre.org/datasources/DS0029/)  | [TA0001 - PcAppStore - Potential Malware Installed](./ADS_forms/TA0001-PcAppStore-PotentialMalwareInstalled.md) |
| T1566 | Phishing | [Application Log](https://attack.mitre.org/datasources/DS0015/)  | [T1566.001 - QR Code Phishing Attachment (Quishing)](./ADS_forms/T1566.001-QR-CodePhishingAttachment(Quishing).md) |


## Execution

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1047 | WMI | [Command](https://attack.mitre.org/datasources/DS0017/) | [WMIC commands](./ADS_forms/T1047-WMICCommands.md) |
| T1059.007 | GootLoader | [Command](https://attack.mitre.org/datasources/DS0017/) | [GootLoader Execution](./ADS_forms/T1059.007-GootLoaderJavaScriptExecution.md)
| S0552 | AdFind Execution| [Command](https://attack.mitre.org/datasources/DS0017/) | [AdFind Execution](./ADS_forms/S0552-AdFindExecution.md) |
  

## Persistence

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1547.001 | Persistence Via Run Keys | [Command](https://attack.mitre.org/datasources/DS0017/) | [T1547.001 - Persistence Via Run Keys](./ADS_forms/T1547.001-PersistenceViaRunKeys.md) |
| T1505.003 | Web shells | [Process](https://attack.mitre.org/datasources/DS0009/) | [T1505.003 - IIS Webshell File Writes](./ADS_forms/T1505.003-IISWebshellFileWrites.md) |


## Defense Evasion

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1562.001  | PowerShell Downgrade attack|  [Command](https://attack.mitre.org/datasources/DS0017/)  | [T1562.001-ImpairDefenses-PowershellDowngrade](./ADS_forms/T1562.001-ImpairDefenses-PowershellDowngrade.md)| 
| T1562.001  | AMSI Bypass attack |  [Command](https://attack.mitre.org/datasources/DS0017/)  | [T1562.001-ImpairDefenses-AMSIBypassAttack](./ADS_forms/T1562.001-ImpairDefenses-AMSIBypass.md)| 
| T1562.001  | PowerShell Defender Disabling Or Exclusions|  [Command](https://attack.mitre.org/datasources/DS0017/)  | [T1562.001-ImpairDefenses-DefenderDisablingOrExclusions](./ADS_forms/T1562.001-ImpairDefenses-DefenderDisablingOrExclusions.md)| 
| T1562.001  | Disable Defender via RegistryKey |  [Windows Registry](https://attack.mitre.org/datasources/DS0024)  | [T1562.001-ImpairDefenses-DisableDefenderRegistryKey](./ADS_forms/T1562.001-ImpairDefenses-DisableDefenderRegistryKey.md)| 
| T1562.002 | Disable Windows Logging MiniNT |  [Windows Registry](https://attack.mitre.org/datasources/DS0024)   | [T1562.002-DisableWindowsLoggingMiniNT](./ADS_forms/T1562.002-DisableWindowsLoggingMiniNT.md)| 
| T1562.002 | Disable Windows Logging EventID |  [Active Directory](https://attack.mitre.org/datasources/DS0026)  | [T1562.002-DisableWindowsLoggingEventID](./ADS_forms/T1562.002-DisableWindowsLoggingEventID.md)| 
| T1562.002 | Disable Windows Logging Multi |  [Command](https://attack.mitre.org/datasources/DS0017)  | [ T1562.002 - Disable Windows Logging Multi](./ADS_forms/T1562.002-DisableWindowsLoggingMulti.md)| 

## Credential Access

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1003.001  | OS Credential Dumping | [Command](https://attack.mitre.org/datasources/DS0017/) | [T1003.001 - OS Credential Dumping: LSASS Memory](./ADS_forms/T1003.001-OSCredentialDumpingLSASSMemory.md) |
| T1003.003  | OS Credential Dumping | [Command](https://attack.mitre.org/datasources/DS0017/) | [T1003.003 - OS Credential Dumping: exfiltrate ntds.dit](./ADS_forms/T1003.003-OSCredentialDumpingExfiltratentds.dit.md) |
| T1003.003  | OS Credential Dumping | [Command](https://attack.mitre.org/datasources/DS0017/) | [T1003.003 - OS Credential Dumping: NTDS using tools](./ADS_forms/T1003.003-OSCredentialDumpingNTDSusingTools.md) |
| T1003.006  | Credential Dumping: DCSync | [Command](https://attack.mitre.org/datasources/DS0017/) | [DCSync](./ADS_forms/T1003.006-DCSyncAD.md) |
| T1552.002  | Unsecured Credentials | [Command](https://attack.mitre.org/datasources/DS001/), [Windows Registry](https://attack.mitre.org/datasources/DS0024) | [T1552.002 - REGISTRY Password Dumping](./ADS_forms/T1552.002-REGISTRYPasswordDumping.md)
| T1555  | Credentials from Password Stores | [Command](https://attack.mitre.org/datasources/DS001/) | [T1555 - Credentials from Password Stores](./ADS_forms/T1555-CredentialsPasswordStores.md)
| T1558.003 | Steal or Forge Kerberos Tickets | [Security Events](https://attack.mitre.org/datasources/DS0026/) | [T1558.003 - Kerberoasting](./ADS_forms/T1558.003-Kerberoasting.md)



## Discovery

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1016  | System Network Configuration Discovery | [Command](https://attack.mitre.org/datasources/DS0017/)  | [T1016-EnumerateNetworkTopology](./ADS_forms/T1016-EnumerateNetworkTopology.md)| 
| T1033 | System Owner/User Discovery |[Command](https://attack.mitre.org/datasources/DS0017/)  | [T1033-Identify successful logons to the host](./ADS_forms/T1033-IdentifySuccessfulLogons.md)| 
| T1082  | System Information Discovery | [Command](https://attack.mitre.org/datasources/DS0017/)  | [T1082_SystemInformationDiscovery](./ADS_forms/T1082-SystemInformationDiscovery.md)| 


## Lateral Movement

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1021 | Lateral Movement - Remote Services | [Network Traffic](https://attack.mitre.org/datasources/DS0029) | [T1021 - Lateral Movement Webservers](./ADS_forms/T1021-LateralMovementWebservers.md) |


## Command and Control

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| T1090 | C2 Proxy|[Command](https://attack.mitre.org/datasources/DS0017/) | [T1090 - Proxy](./ADS_forms/T1090-Proxy.md) |


## Malware / Tools

| Technique ID | Title  | Data Source  | ADS |
| ---  | --- | --- |--- |
| S0357 | Impacket | [Command](https://attack.mitre.org/datasources/DS0017/) | [S0357-ImpacketDirCommand](./ADS_forms/S0357-ImpacketDirCommand.md)
| S0357 | Impacket | [Command](https://attack.mitre.org/datasources/DS0017/) | [S0357-ImpacketSecretDumpSMB2](./ADS_forms/S0357-ImpacketSecretdumpSMB2.md)
| S0154 | Cobalt Strike |  [Network Traffic](https://attack.mitre.org/datasources/DS0029) | [S0154-CobaltStrike_DNS](./ADS_forms/S0154-CobaltStrike_DNS.md) |
| S0154 | Cobalt Strike |  [Named Pipe](https://attack.mitre.org/datasources/DS0023) | [S0154-CobaltStrike_NamedPipe](./ADS_forms/S0154-CobaltStrike_NamedPipe.md) |
| S0650 | QakBot | [Command](https://attack.mitre.org/datasources/DS0017/) | [Qakbot Post Compromise](./ADS_forms/S0650-QakbotPostCompromise.md) |
| S0650 | QakBot | [Command](https://attack.mitre.org/datasources/DS0017/) | [Qakbot Process Execution](./ADS_forms/S0650-QakbotProcessExecution.md) |
| S0650 | QakBot | [Command](https://attack.mitre.org/datasources/DS0017/) | [Qakbot Defender Exclusions](./ADS_forms/S0650-Qakbot-DefenderExclusions.md) |
| S0521 | Bloodhound/Sharphound | [Command](https://attack.mitre.org/datasources/DS0017/) | [S0521 - Bloodhound/Sharphound Execution Commandlets](./ADS_forms/S0521-BloodHoundCommandlets.md) |






