# Detection Guidance for Volt Typhoon - 20230525001

## Overview
The United States and international cybersecurity authorities issued a [joint
Cybersecurity Advisory (CSA)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a) on 24 May 2023 to highlight a recently discovered cluster of activity of interest associated with a state-sponsored cyber actor also known as [Volt Typhoon](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)

The authoring agencies assess there is significant risk these **Tactics, Techniques and Procedures (TTPs)** could be employed by the actor against **Critical Infrastructure (CI)** and other sectors worldwide.

## Detection Guidance
The WA SOC recommends informing all cyber security personnel of the advisory. Additionally WA public sector agencies are requested to investigate utilising their security event databases and report any suspicious or unexpected events to the WA SOC following the below guidance.

### Kusto Query Language detections
These can be run in [Microsoft Defender Advanced Hunting](https://learn.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-modes?view=o365-worldwide#get-started-with-advanced-hunting-mode), [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/kusto-overview) and [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/queries).

```kusto
TODO:
```

### SIGMA detection logic
These can be converted to multiple target platforms using [uncoder.io](https://uncoder.io)

```sigma
TODO:
```

Additional behaviours and indicators can be found in the [CSA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a), however due to the nature of the tactics, techniques and procedures (TTPs) in use, there is a high chance of detecting non-malicious events as well. Please review any detections with expected activities within your organisation, and contact the WA SOC if there is any uncertainty as to whether a detected event is suspicious.

## Additional References:

For further information, please see:

- [PRC State-Sponsored Cyber Actor Living off the Land to Evade Detection](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [ACSC - People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection](https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection)
- [Microsoft - Volt Typhoon targets US critical infrastructure with living-off-the-land techniques](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
