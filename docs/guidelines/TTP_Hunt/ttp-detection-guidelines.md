# Threat Hunting Guideline

This page serves as a high-level guideline specifically for WA SOC threat hunting activities, showcasing prominent tactics, techniques, and procedures (TTPs). The ADS provides a tailored Kusto Query Language (KQL) queries to assist in threat hunting inside Microsoft Sentinel environment. An overview of why threat hunting is valuable is below:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/VNp35Uw_bSM?si=N2709vnW2VqRQFB7&amp;start=1560" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The [MITRE ATT&CK](https://attack.mitre.org/) framework is a knowledge base of adversary tactics and techniques based on real-world observations. Relevant KQL queries are mapped to each of the techniques used by threat actor tactics in line with the MITRE ATT&CK framework.

This section highlights queries that can be mapped in the MITRE ATT&CK Framework. Reconnaissance and Resource Development are out of the hunting services initial scope. The [Top 10 MITRE ATT&CK Techniques for Ransomware](https://top-attack-techniques.mitre-engenuity.org) is another sensible resource with a broader scope that can also be used to prioritise detection logic.

## Guidelines/Instructions:

- Review the TTP Hunt results shared with you via email/JIRA ticket.
- Identify the detected TTP MITRE ATT&CK code, and refer to ADS document
- Understand the detection objectives and perform triage investigation against detected logs
- Upon true-positive investigation results, raise an incident ticket with WA SOC. Reference: [WA SOC - Incident Reporting](https://soc.cyber.wa.gov.au/guidelines/incident-reporting/)
- Upon false-positive/benign true-positive investigation results, OR if you would like to request specific threat hunt TTPs, please contact cybersecurity@dpc.wa.gov.au

## Initial Access

| Technique ID | Title               | Data Source                                                     | ADS                                                                                                      |
| ------------ | ------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| T1190        | Web shells          | [Network Traffic](https://attack.mitre.org/datasources/DS0029/) | [Webshells Suspicious URI](./ADS_forms/T1190-WebshellsSuspiciousURI.md)                                  |
| T1566        | Phishing            | [Application Log](https://attack.mitre.org/datasources/DS0015/) | [QR Code Phishing Attachment (Quishing)](<./ADS_forms/T1566.001-QR-CodePhishingAttachment(Quishing).md>) |
| T1189        | Drive-by Compromise | [File](https://attack.mitre.org/datasources/DS0022/)            | [Drive-by Compromise - FakeUpdate](./ADS_forms/T1189-Drive-byCompromise-FakeUpdate.md)                   |

## Execution

| Technique ID | Title            | Data Source                                                                                                                                  | ADS                                                                                             |
| ------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| T1047        | WMI              | [Command](https://attack.mitre.org/datasources/DS0017/), [Process Creation](https://attack.mitre.org/datasources/DS0009/#Process%20Creation) | [WMIC commands](./ADS_forms/T1047-WMICCommands.md)                                              |
| T1059        | MicroSCADA SCILC | [Application Log](https://attack.mitre.org/datasources/DS0015/)                                                                              | [MicroSCADA SCILC - Command Execution](./ADS_forms/T1059-MicroSCADA-SCILC-Command-Execution.md) |

## Persistence

| Technique ID | Title                                                                  | Data Source                                                                                                                                                                                                                                     | ADS                                                                                                                                                                                           |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T1505.003    | Web shells                                                             | [Process](https://attack.mitre.org/datasources/DS0009/)                                                                                                                                                                                         | [IIS Webshell File Writes](./ADS_forms/T1505.003-IISWebshellFileWrites.md)                                                                                                                    |
| T1505.003    | Suspicious Windows Strings In URI                                      | [NA](<>)                                                                                                                                                                                                                                        | [Suspicious Windows Strings In URI](./ADS_forms/T1505.003-SuspiciousWindowsStringsInURI.md)                                                                                                   |
| T1505.003    | Windows Webshell Creation                                              | [File](https://attack.mitre.org/datasources/DS0022/)                                                                                                                                                                                            | [Windows Webshell Creation](./ADS_forms/T1505.003-WindowsWebshellCreation.md)                                                                                                                 |
| T1505.003    | Suspicious Child Process Of SQL Server                                 | [Process Creation](https://attack.mitre.org/datasources/DS0009/#Process%20Creation)                                                                                                                                                             | [Suspicious Child Process Of SQL Server](./ADS_forms/T1505.003-SuspiciousChildProcessOfSQLServer.md)                                                                                          |
| T1505.004    | Suspicious IIS Module Registration                                     | [NA](<>)                                                                                                                                                                                                                                        | [Suspicious IIS Module Registration](./ADS_forms/T1505.004-Suspicious-IIS-Module-Registration.md)                                                                                             |
| T1543.003    | Service Installations in Registry                                      | [registry_set](https://attack.mitre.org/datasources/DS0024/)                                                                                                                                                                                    | [CobaltStrike: Service Installations in Registry](./ADS_forms/T1543.003-CobaltStrike-ServiceInstallationsInRegistry.md)                                                                       |
| T1543.003    | Create or Modify System Process                                        | [File](https://attack.mitre.org/datasources/DS0022/), [Windows Registry](https://attack.mitre.org/datasources/DS0024), [Process](https://attack.mitre.org/datasources/DS0009/), [Application Log](https://attack.mitre.org/datasources/DS0015/) | [Create or Modify System Process - Remote Access Tool Services Have Been Installed](./ADS_forms/T1543.003-Create-or-Modify-System-Process-Remote-Access-Tool-Services-Have-Been-Installed.md) |
| T1543.003    | Potential Persistence Attempt Via Existing Service Tampering (reg.exe) | [Process](https://attack.mitre.org/datasources/DS0009/)                                                                                                                                                                                         | [Potential Persistence Attempt Via Existing Service Tampering (reg.exe)](<./ADS_forms/T1543.003-Potential-Persistence-Attempt-Via-Existing-Service-Tampering-(reg.exe).md>)                   |
| T1543.003    | Potential Persistence Attempt Via Existing Service Tampering (sc.exe)  | [Process](https://attack.mitre.org/datasources/DS0009/)                                                                                                                                                                                         | [Potential Persistence Attempt Via Existing Service Tampering (sc.exe)](<./ADS_forms/T1543.003-Potential-Persistence-Attempt-Via-Existing-Service-Tampering(sc.exe).md>)                      |
| T1053.005    | Diamond Sleet APT Scheduled Task Creation - Registry  | [Windows Registry](https://attack.mitre.org/datasources/DS0024/)  | [Diamond Sleet APT Scheduled Task Creation - Registry](<./ADS_forms/T1053.005-Diamond-Sleet-APT-Scheduled-Task-Creation-Registry.md>)                      |

## Defense Evasion

| Technique ID | Title                                                   | Data Source                                                     | ADS                                                                                                                                       |
| ------------ | ------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| T1562.001    | AMSI Bypass attack                                      | [Command](https://attack.mitre.org/datasources/DS0017/)         | [ImpairDefenses - AMSIBypass Attack](./ADS_forms/T1562.001-ImpairDefenses-AMSIBypass.md)                                                  |
| T1562.001    | Impair Defenses: Removal Of AMSI Provider Registry Keys | [Windows Registry](https://attack.mitre.org/datasources/DS0024) | [Impair Defenses: Removal Of AMSI Provider Registry Keys](./ADS_forms/T1562.001-ImpairDefenses-Removal-Of-AMSI-Provider-Registry-Keys.md) |
| T1562.002    | Disable Windows Logging MiniNT                          | [Windows Registry](https://attack.mitre.org/datasources/DS0024) | [ImpairDefenses - Disable Windows Logging Mini NT](./ADS_forms/T1562.002-ImpairDefenses-DisableWindowsLoggingMiniNT.md)                   |
| T1562.002    | Impair Defenses: Disable Windows Logging on EventID     | [Active Directory](https://attack.mitre.org/datasources/DS0026) | [ImpairDefenses - Disable Windows Logging on EventID](./ADS_forms/T1562.002-ImpairDefenses-DisableWindowsLoggingonEventID.md)             |
| T1562.002    | Impair Defenses: Disable Windows Logging using wevtutil | [Process](https://attack.mitre.org/datasources/DS0009/)         | [Impair Defenses: Disable Windows Logging using wevtutil](./ADS_forms/T1562.002-ImpairDefenses-DisableWindowsLoggingWevtutil.md)          |
| T1027.006 | HTML Smuggling |  [NA](<>)  | [HTML Smuggling](./ADS_forms/T1027.006-HTMLSmuggling.md)|

<!-- | T1562.002 | Disable Windows Logging Multi |  [Command](https://attack.mitre.org/datasources/DS0017)  | [ImpairDefenses - Disable Windows Logging Multi](./ADS_forms/T1562.002-ImpairDefenses-DisableWindowsLoggingMulti.md)| Removed -->



## Credential Access

| Technique ID | Title                            | Data Source                                                                                                             | ADS                                                                                                           |
| ------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| T1003.001    | OS Credential Dumping            | [Command](https://attack.mitre.org/datasources/DS0017/)                                                                 | [OS Credential Dumping: LSASS Memory](./ADS_forms/T1003.001-OSCredentialDumping-LSASSMemory.md)               |
| T1003.003    | OS Credential Dumping            | [Process](https://attack.mitre.org/datasources/DS0009/), [Command](https://attack.mitre.org/datasources/DS0017/)        | [OS Credential Dumping: Exfiltrate ntds.dit](./ADS_forms/T1003.003-OSCredentialDumping-Exfiltratentds.dit.md) |
| T1003.003    | OS Credential Dumping            | [Command](https://attack.mitre.org/datasources/DS0017/)                                                                 | [OS Credential Dumping: NTDS using tools](./ADS_forms/T1003.003-OSCredentialDumping-NTDSusingTools.md)        |
| T1003.006    | OS Credential Dumping            | [Command](https://attack.mitre.org/datasources/DS0017/)                                                                 | [OS Credential Dumping: DCSync](./ADS_forms/T1003.006-OSCredentialDumping-DCSyncAD.md)                        |
| T1552.002    | Unsecured Credentials            | [Command](https://attack.mitre.org/datasources/DS001/), [Windows Registry](https://attack.mitre.org/datasources/DS0024) | [REGISTRY Password Dumping](./ADS_forms/T1552.002-REGISTRYPasswordDumping.md)                                 |
| T1555        | Credentials from Password Stores | [Command](https://attack.mitre.org/datasources/DS001/)                                                                  | [Credentials from Password Stores](./ADS_forms/T1555-CredentialsPasswordStores.md)                            |
| T1557        | AiTM - Phishing logging          | [Security Events](https://attack.mitre.org/datasources/DS0026/)                                                         | [AiTM - Phishing logging](./ADS_forms/T1557-AiTM-PhishingLogging.md)                                          |

## Discovery

| Technique ID | Title                                  | Data Source                                             | ADS                                                                                     |
| ------------ | -------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| T1016        | System Network Configuration Discovery | [Command](https://attack.mitre.org/datasources/DS0017/) | [EnumerateNetworkTopology](./ADS_forms/T1016-EnumerateNetworkTopology.md)               |
| T1033        | System Owner/User Discovery            | [Command](https://attack.mitre.org/datasources/DS0017/) | [Identify successful logons to the host](./ADS_forms/T1033-IdentifySuccessfulLogons.md) |
| T1082        | System Information Discovery           | [NA](<>)                                                | [System Information Discovery](./ADS_forms/T1082-SystemInformationDiscovery.md)         |

## Lateral Movement

| Technique ID | Title                              | Data Source                                                    | ADS                                                                                       |
| ------------ | ---------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| T1021        | Lateral Movement - Remote Services | [Network Traffic](https://attack.mitre.org/datasources/DS0029) | [Lateral Movement - Remote Services](./ADS_forms/T1021-LateralMovement-RemoteServices.md) |

<!-- | T1021 | Lateral Movement - Webservers | [Network Traffic](https://attack.mitre.org/datasources/DS0029) | [Lateral Movement - Webservers](./ADS_forms/T1021-LateralMovement-Webservers.md) | -->

## Command and Control

| Technique ID | Title    | Data Source                                             | ADS                                 |
| ------------ | -------- | ------------------------------------------------------- | ----------------------------------- |
| T1090        | C2 Proxy | [Command](https://attack.mitre.org/datasources/DS0017/) | [Proxy](./ADS_forms/T1090-Proxy.md) |

## Malware / Tools

| Technique ID | Title                 | Data Source                                                    | ADS                                                                                          |
| ------------ | --------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| S0357        | Impacket              | [Command](https://attack.mitre.org/datasources/DS0017/)        | [Impacket - DirCommand](./ADS_forms/S0357-Impacket-DirCommand.md)                            |
| S0357        | Impacket              | [Command](https://attack.mitre.org/datasources/DS0017/)        | [Impacket - SecretDumpSMB2](./ADS_forms/S0357-Impacket-SecretdumpSMB2.md)                    |
| S0154        | Cobalt Strike         | [Network Traffic](https://attack.mitre.org/datasources/DS0029) | [CobaltStrike - DNS](./ADS_forms/S0154-CobaltStrike-DNS.md)                                  |
| S0154        | Cobalt Strike         | [Named Pipe](https://attack.mitre.org/datasources/DS0023)      | [CobaltStrike - NamedPipe](./ADS_forms/S0154-CobaltStrike-NamedPipe.md)                      |
| S0650        | QakBot                | [Command](https://attack.mitre.org/datasources/DS0017/)        | [Qakbot - Process Execution](./ADS_forms/S0650-Qakbot-ProcessExecution.md)                   |
| S0650        | QakBot                | [Command](https://attack.mitre.org/datasources/DS0017/)        | [Qakbot - Defender Exclusions](./ADS_forms/S0650-Qakbot-DefenderExclusions.md)               |
| S0521        | Bloodhound/Sharphound | [Command](https://attack.mitre.org/datasources/DS0017/)        | [Bloodhound/Sharphound - Execution Commandlets](./ADS_forms/S0521-BloodHound-Commandlets.md) |

