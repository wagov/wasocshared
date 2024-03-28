### TA0005 - Potentially Suspicious Windows App Activity

#### DESCRIPTION

Detects potentially suspicious child process of applications launched from inside the WindowsApps directory. This could be a sign of a rogue ".appx" package installation/execution

**example:**

```
"c:\Program Files\WindowsApps\<randomGUID>\UpdateFix\SecurityFix.exe" spawning "c:\Windows\System32\cmd.exe" /C regsvr32 /s "C:\Users\XXX\AppData\Local\Temp\4h23123qwe.dll"
```

**Related**\
BazarBackdoor
BazarLoader

**Reference**\
https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/identifying-and-mitigating-living-off-the-land-techniques
https://github.com/SigmaHQ/sigma/blob/6b8cd1f0f1d222dcffa95394b4cbcec2a05137a0/rules/windows/process_creation/proc_creation_win_susp_appx_execution.yml#L6

#### ATT&CK TACTICS

{{ mitre("T1059")}}
{{ mitre("T1218.005")}}
{{ mitre("T1047")}}

Data Source(s): [Command](https://attack.mitre.org/datasources/DS0017/), [Process](https://attack.mitre.org/datasources/DS0009/)

#### SENTINEL RULE QUERY

```
let selection_parent = @"C:\Program Files\WindowsApps\";
let selection_susp_img = @".*(/cmd.exe|/cscript.exe|/mshta.exe|/powershell.exe|/pwsh.exe|/regsvr32.exe|/rundll32.exe|/wscript.exe)$"; 
let selection_susp_cli = dynamic (['cmd /c','Invoke-','Base64']);
let filter_optional_terminal = @".*(/WindowsTerminal.exe|/powershell.exe|/cmd.exe|/pwsh.exe)$"; 
DeviceProcessEvents
| where ActionType == "ProcessCreated"
| where InitiatingProcessFolderPath contains selection_parent and (FolderPath matches regex selection_susp_img or ProcessCommandLine has_any (selection_susp_cli))
| where not(InitiatingProcessFolderPath contains @":\Program Files\WindowsApps\Microsoft.WindowsTerminal" or InitiatingProcessFolderPath endswith @"\WindowsTerminal.exe" or FolderPath matches regex filter_optional_terminal)
```

#### Triage

1. Verify ProcessCommandLine field for any suspicious activities spawned by WindowsApps.
1. Determine whether the Windows Apps was known to the environment and approved.

### False Positive

```
- Legitimate Windows App running
```

#### Version

Version 1.0 (date 19/3/2024)
