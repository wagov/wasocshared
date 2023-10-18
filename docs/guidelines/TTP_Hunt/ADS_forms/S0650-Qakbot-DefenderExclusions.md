### S0650 - Qakbot: Defender Exclusions  


####  DESCRIPTION  
Qbot used reg.exe to add Defender folder exceptions for folders within AppData and ProgramData.  

**example:**  
C:\Windows\system32\reg.exe ADD \"HKLM\SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths\" /f /t REG_DWORD /v \"C:\ProgramData\Microsoft\Oweboiqnb\" /d \"0\"
C:\Windows\system32\reg.exe ADD \"HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths\" /f /t REG_DWORD /v \"C:\ProgramData\Microsoft\Oweboiqnb\" /d \"0\"    

**Related**  
Malware  

**Reference**  
https://github.com/SigmaHQ/sigma/blob/4de6102dc7d94c9ee70995aeea27b77184d62c35/rules/windows/process_creation/proc_creation_win_reg_defender_exclusion.yml#L4        
https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/     

####  ATT&CK TACTICS  
{{ mitre("T1562.001")}}  

Data source - Command  

####  SENTINEL RULE QUERY   

~~~
let c1 = dynamic([@'SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths', @'SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths']);  
find where InitiatingProcessCommandLine has_any (c1) or ProcessCommandLine has_any (c1) or CommandLine has_any (c1)   
~~~

####  Triage   
1. Inspect commands to identify Qbot activity     

####  Version   
Version 1.0 (date 5/7/2023)   
