# Detection Guidance for Volt Typhoon - 20230525001

## Overview
The United States and international cybersecurity authorities issued a [joint
Cybersecurity Advisory (CSA)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a) on 24 May 2023 to highlight a recently discovered cluster of activity of interest associated with a state-sponsored cyber actor also known as [Volt Typhoon](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)

The authoring agencies assess there is significant risk these **Tactics, Techniques and Procedures (TTPs)** could be employed by the actor against **Critical Infrastructure (CI)** and other sectors worldwide.

## Detection Guidance
The WA SOC recommends informing all cyber security personnel of the advisory. Additionally WA public sector agencies are requested to investigate utilising their security event databases and report any suspicious or unexpected events to the WA SOC following the below guidance.

### Kusto Query Language detections
These can be run in [Microsoft Defender Advanced Hunting](https://learn.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-modes?view=o365-worldwide#get-started-with-advanced-hunting-mode), [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/kusto-overview) and [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/queries).

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

**Hashes (please report any actual hits)**
```kusto
let hashes = dynamic(['f4dd44bc19c19056794d29151a5b1bb76afd502388622e24c863a8494af147dd',
    'ef09b8ff86c276e9b475a6ae6b54f08ed77e09e169f7fc0872eb1d427ee27d31',
    'd6ebde42457fe4b2a927ce53fc36f465f0000da931cfab9b79a36083e914ceca',
    '472ccfb865c81704562ea95870f60c08ef00bcd2ca1d7f09352398c05be5d05d',
    '66a19f7d2547a8a85cee7a62d0b6114fd31afdee090bd43f36b89470238393d7',
    '3c2fe308c0a563e06263bbacf793bbe9b2259d795fcc36b953793a7e499e7f71',
    '41e5181b9553bbe33d91ee204fe1d2ca321ac123f9147bb475c0ed32f9488597',
    'c7fee7a3ffaf0732f42d89c4399cbff219459ae04a81fc6eff7050d53bd69b99',
    '3a9d8bb85fbcfe92bae79d5ab18e4bca9eaf36cea70086e8d1ab85336c83945f',
    'fe95a382b4f879830e2666473d662a24b34fccf34b6b3505ee1b62b32adafa15',
    'ee8df354503a56c62719656fae71b3502acf9f87951c55ffd955feec90a11484']);
find where SHA256 has_any (hashes) or InitiatingProcessSHA256 has_any (hashes) or FileHash has_any (hashes) or FileHashSha256 has_any (hashes) or FileHashValue has_any (hashes)
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
            - 'f4dd44bc19c19056794d29151a5b1bb76afd502388622e24c863a8494af147dd'
            - 'ef09b8ff86c276e9b475a6ae6b54f08ed77e09e169f7fc0872eb1d427ee27d31'
            - 'd6ebde42457fe4b2a927ce53fc36f465f0000da931cfab9b79a36083e914ceca'
            - '472ccfb865c81704562ea95870f60c08ef00bcd2ca1d7f09352398c05be5d05d'
            - '66a19f7d2547a8a85cee7a62d0b6114fd31afdee090bd43f36b89470238393d7'
            - '3c2fe308c0a563e06263bbacf793bbe9b2259d795fcc36b953793a7e499e7f71'
            - '41e5181b9553bbe33d91ee204fe1d2ca321ac123f9147bb475c0ed32f9488597'
            - 'c7fee7a3ffaf0732f42d89c4399cbff219459ae04a81fc6eff7050d53bd69b99'
            - '3a9d8bb85fbcfe92bae79d5ab18e4bca9eaf36cea70086e8d1ab85336c83945f'
            - 'fe95a382b4f879830e2666473d662a24b34fccf34b6b3505ee1b62b32adafa15'
            - 'ee8df354503a56c62719656fae71b3502acf9f87951c55ffd955feec90a11484'
    selection_cmd:
        - CommandLine|contains|all:
            - 'cmd'
            - 'wmic'
            - 'caption'
            - 'filesystem'
        - CommandLine|contains|all:
            - 'ntds.dit'
        - CommandLine|contains|all:
            - 'Secretsdump.py'
        - CommandLine|contains|all:
            - 'Invoke-NinjaCopy'
        - CommandLine|contains|all:
            - 'DSInternals'
        - CommandLine|contains|all:
            - 'portproxy'
            - 'netsh'
            - 'add'
        - CommandLine|contains|all:
            - 'Get-EventLog'
            - '4624'
        - CommandLine|contains|all:
            - 'curl'
            - 'www.ip-api.com'
        - CommandLine|contains|all:
            - 'ldifde.exe'
            - 'subtree'
        - CommandLine|contains|all:
            - 'mimikatz.exe'
        - CommandLine|contains|all:
            - 'reg'
            - 'ss.dat'
        - CommandLine|contains|all:
            - 'reg'
            - 'sy.dat'
    condition: 1 of selection*
```

Additional behaviours and indicators can be found in the [CSA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a), however due to the nature of the tactics, techniques and procedures (TTPs) in use, there is a high chance of detecting non-malicious events as well. Please review any detections with expected activities within your organisation, and contact the WA SOC if there is any uncertainty as to whether a detected event is suspicious.

## Additional References:

For further information, please see:

- [PRC State-Sponsored Cyber Actor Living off the Land to Evade Detection](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [ACSC - People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection](https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection)
- [Microsoft - Volt Typhoon targets US critical infrastructure with living-off-the-land techniques](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
