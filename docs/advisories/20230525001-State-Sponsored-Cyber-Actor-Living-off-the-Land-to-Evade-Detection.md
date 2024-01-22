# Detection Guidance for Volt Typhoon - 20230525001

## Overview

The United States and international cybersecurity authorities issued a [joint
Cybersecurity Advisory (CSA)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a) on 24 May 2023 to highlight a recently discovered cluster of activity of interest associated with a state-sponsored cyber actor also known as [Volt Typhoon](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)

The authoring agencies assess there is significant risk these **Tactics, Techniques and Procedures (TTPs)** could be employed by the actor against **Critical Infrastructure (CI)** and other sectors worldwide.

## Detection Guidance

The WA SOC recommends informing all cyber security personnel of the advisory. Additionally WA public sector agencies are requested to investigate utilising their security event databases and report any suspicious or unexpected events to the WA SOC following the below guidance.

### Kusto Query Language detections

These can be run in [Microsoft Defender Advanced Hunting](https://learn.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-modes?view=o365-worldwide#get-started-with-advanced-hunting-mode), [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/kusto-overview) and [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/queries).

**Hashes (please report any actual hits)**

```kusto
let hashes = dynamic(['baeffeb5fdef2f42a752c65c2d2a52e84fb57efc906d981f89dd518c314e231c', 
'b4f7c5e3f14fb57be8b5f020377b993618b6e3532a4e1eb1eae9976d4130cc74', 
'4b0c4170601d6e922cf23b1caf096bba2fade3dfcf92f0ab895a5f0b9a310349', 
'c0fc29a52ec3202f71f6378d9f7f9a8a3a10eb19acb8765152d758aded98c76d', 
'd6ab36cb58c6c8c3527e788fc9239d8dcc97468b6999cf9ccd8a815c8b4a80af', 
'9dd101caee49c692e5df193b236f8d52a07a2030eed9bd858ed3aaccb406401a', 
'450437d49a7e5530c6fb04df2e56c3ab1553ada3712fab02bd1eeb1f1adbc267', 
'93ce3b6d2a18829c0212542751b309dacbdc8c1d950611efe2319aa715f3a066', 
'7939f67375e6b14dfa45ec70356e91823d12f28bbd84278992b99e0d2c12ace5', 
'389a497f27e1dd7484325e8e02bbdf656d53d5cf2601514e9b8d8974befddf61', 
'c4b185dbca490a7f93bc96eefb9a597684fdf532d5a04aa4d9b4d4b1552c283b', 
'e453e6efc5a002709057d8648dbe9998a49b9a12291dee390bb61c98a58b6e95', 
'6036390a2c81301a23c9452288e39cb34e577483d121711b6ba6230b29a3c9ff', 
'cd69e8a25a07318b153e01bba74a1ae60f8fc28eb3d56078f448461400baa984', 
'17506c2246551d401c43726bdaec800f8d41595d01311cf38a19140ad32da2f4', 
'8fa3e8fdbaa6ab5a9c44720de4514f19182adc0c9c6001c19cf159b79c0ae9c2', 
'd17317e1d5716b09cee904b8463a203dc6900d78ee2053276cc948e4f41c8295', 
'472ccfb865c81704562ea95870f60c08ef00bcd2ca1d7f09352398c05be5d05d', 
'3e9fc13fab3f8d8120bd01604ee50ff65a40121955a4150a6d2c007d34807642']);
find where SHA256 has_any (hashes)
or InitiatingProcessSHA256 has_any (hashes)
or FileHash has_any (hashes)
or FileHashSha256 has_any (hashes)
or FileHashValue has_any (hashes)
```

**CommandLines to review**

```kusto
let c1 = dynamic(["cmd", "wmic", "caption", "filesystem"]);
let c2 = dynamic(["ntds.dit"]);
let c3 = dynamic(["Secretsdump.py"]);
let c4 = dynamic(["Invoke-NinjaCopy"]);
let c5 = dynamic(["DSInternals"]);
let c6 = dynamic(["portproxy", "netsh", "add"]);
let c7 = dynamic(["Get-EventLog", "4624"]);
let c8 = dynamic(["curl", "www.ip-api.com"]);
let c9 = dynamic(["wmic", "process", "create", "stop"]);
let c10 = dynamic(["ldifde.exe", "subtree"]);
let c11 = dynamic(["mimikatz.exe"]);
let c12 = dynamic(["reg", "ss.dat"]);
let c13 = dynamic(["reg", "sy.dat"]);
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1) or InitiatingProcessCommandLine has_all (c2) or ProcessCommandLine has_all (c2) or CommandLine has_all (c2) or InitiatingProcessCommandLine has_all (c3) or ProcessCommandLine has_all (c3) or CommandLine has_all (c3) or InitiatingProcessCommandLine has_all (c4) or ProcessCommandLine has_all (c4) or CommandLine has_all (c4) or InitiatingProcessCommandLine has_all (c5) or ProcessCommandLine has_all (c5) or CommandLine has_all (c5) or InitiatingProcessCommandLine has_all (c6) or ProcessCommandLine has_all (c6) or CommandLine has_all (c6) or InitiatingProcessCommandLine has_all (c7) or ProcessCommandLine has_all (c7) or CommandLine has_all (c7) or InitiatingProcessCommandLine has_all (c8) or ProcessCommandLine has_all (c8) or CommandLine has_all (c8) or InitiatingProcessCommandLine has_all (c9) or ProcessCommandLine has_all (c9) or CommandLine has_all (c9) or InitiatingProcessCommandLine has_all (c10) or ProcessCommandLine has_all (c10) or CommandLine has_all (c10) or InitiatingProcessCommandLine has_all (c11) or ProcessCommandLine has_all (c11) or CommandLine has_all (c11) or InitiatingProcessCommandLine has_all (c12) or ProcessCommandLine has_all (c12) or CommandLine has_all (c12) or InitiatingProcessCommandLine has_all (c13) or ProcessCommandLine has_all (c13) or CommandLine has_all (c13)
```

### SIGMA detection logic

These can be converted to several target platforms using [uncoder.io](https://uncoder.io) or [pySigma](https://github.com/SigmaHQ/pySigma).

```yaml
title: Volt Typhoon Hunt
logsource:
#service:
category:
product: windows
detection:
selection_hash:
Hashes|contains:
  - baeffeb5fdef2f42a752c65c2d2a52e84fb57efc906d981f89dd518c314e231c
  - b4f7c5e3f14fb57be8b5f020377b993618b6e3532a4e1eb1eae9976d4130cc74
  - 4b0c4170601d6e922cf23b1caf096bba2fade3dfcf92f0ab895a5f0b9a310349
  - c0fc29a52ec3202f71f6378d9f7f9a8a3a10eb19acb8765152d758aded98c76d
  - d6ab36cb58c6c8c3527e788fc9239d8dcc97468b6999cf9ccd8a815c8b4a80af
  - 9dd101caee49c692e5df193b236f8d52a07a2030eed9bd858ed3aaccb406401a
  - 450437d49a7e5530c6fb04df2e56c3ab1553ada3712fab02bd1eeb1f1adbc267
  - 93ce3b6d2a18829c0212542751b309dacbdc8c1d950611efe2319aa715f3a066
  - 7939f67375e6b14dfa45ec70356e91823d12f28bbd84278992b99e0d2c12ace5
  - 389a497f27e1dd7484325e8e02bbdf656d53d5cf2601514e9b8d8974befddf61
  - c4b185dbca490a7f93bc96eefb9a597684fdf532d5a04aa4d9b4d4b1552c283b
  - e453e6efc5a002709057d8648dbe9998a49b9a12291dee390bb61c98a58b6e95
  - 6036390a2c81301a23c9452288e39cb34e577483d121711b6ba6230b29a3c9ff
  - cd69e8a25a07318b153e01bba74a1ae60f8fc28eb3d56078f448461400baa984
  - 17506c2246551d401c43726bdaec800f8d41595d01311cf38a19140ad32da2f4
  - 8fa3e8fdbaa6ab5a9c44720de4514f19182adc0c9c6001c19cf159b79c0ae9c2
  - d17317e1d5716b09cee904b8463a203dc6900d78ee2053276cc948e4f41c8295
  - 472ccfb865c81704562ea95870f60c08ef00bcd2ca1d7f09352398c05be5d05d
  - 3e9fc13fab3f8d8120bd01604ee50ff65a40121955a4150a6d2c007d34807642
selection_cmd:
  - CommandLine|contains|all:
  - cmd
  - wmic
  - caption
  - filesystem
  - CommandLine|contains|all:
  - ntds.dit
  - CommandLine|contains|all:
  - Secretsdump.py
  - CommandLine|contains|all:
  - Invoke-NinjaCopy
  - CommandLine|contains|all:
  - DSInternals
  - CommandLine|contains|all:
  - portproxy
  - netsh
  - add
  - CommandLine|contains|all:
  - Get-EventLog
  - '4624'
  - CommandLine|contains|all:
  - curl
  - www.ip-api.com
  - CommandLine|contains|all:
  - ldifde.exe
  - subtree
  - CommandLine|contains|all:
  - mimikatz.exe
  - CommandLine|contains|all:
  - reg
  - ss.dat
  - CommandLine|contains|all:
  - reg
  - sy.dat
condition: 1 of selection*
```

Additional behaviours and indicators can be found in the [CSA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a), however due to the nature of the tactics, techniques and procedures (TTPs) in use, there is a high chance of detecting non-malicious events as well. Please review any detections with expected activities within your organisation, and contact the WA SOC if there is any uncertainty as to whether a detected event is suspicious.

## Additional References

For further information, please see:

- [PRC State-Sponsored Cyber Actor Living off the Land to Evade Detection](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [ACSC - People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection](https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection)
- [Microsoft - Volt Typhoon targets US critical infrastructure with living-off-the-land techniques](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
