### S0650 - Qakbot: Defender Exclusions

#### DESCRIPTION

Qbot used reg.exe to add Defender folder exceptions for folders within AppData and ProgramData.

**Example:**

> C:\\Windows\\system32\\reg.exe ADD "HKLM\\SOFTWARE\\Microsoft\\Microsoft Antimalware\\Exclusions\\Paths" /f /t REG_DWORD /v "C:\\ProgramData\\Microsoft\\Oweboiqnb" /d "0"
> C:\\Windows\\system32\\reg.exe ADD "HKLM\\SOFTWARE\\Microsoft\\Windows Defender\\Exclusions\\Paths" /f /t REG_DWORD /v "C:\\ProgramData\\Microsoft\\Oweboiqnb" /d "0"

**Related**\
Malware

**Reference**\
https://github.com/SigmaHQ/sigma/blob/4de6102dc7d94c9ee70995aeea27b77184d62c35/rules/windows/process_creation/proc_creation_win_reg_defender_exclusion.yml#L4%5C
https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/

#### ATT&CK TACTICS

{{ mitre("T1562.001")}}

Data Source(s): [Process Creation](https://attack.mitre.org/datasources/DS0009/#Process%20Creation)

#### SENTINEL RULE QUERY

```
let selection_1 = dynamic([@'SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths', @'SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths']); 
let selection_2 = dynamic(['ADD ', @'/t ','REG_DWORD ',@'/v ',@'/d ', '0']); 
DeviceProcessEvents
| where ActionType == "ProcessCreated"
| where FolderPath endswith @'\\reg.exe'
| where ProcessCommandLine has_any (selection_1) and ProcessCommandLine has_all (selection_2)
```

#### Triage

1. Inspect commands and check whether it's expected
1. Verify on folders path and name being added into Defender exclusion

#### Version

Version 1.0 (date 26/10/2023)
