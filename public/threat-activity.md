# WA SOC - Recent Threat Activity (December 2022)

**Phishing activity remains high** across all organisations with multiple incidents detected weekly. Please refer to the below guides are effective controls to ensure all external and internal signins are appropriately monitored.

- [Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue, PRT, OAuth)](https://jeffreyappel.nl/tips-for-preventing-against-new-modern-identity-attacks-aitm-mfa-fatigue-prt-oauth/)
- [How to implement Defender for Identity and configure all prerequisites](https://jeffreyappel.nl/how-to-implement-defender-for-identity-and-configure-all-prerequisites/)

**Agent Tesla (spyware Trojan)** has been detected across several organisations. It is used to steal sensitive information from a victim's device such as user credentials, keystrokes, clipboard data, sessions and credentials from browsers, and other information. The malware was deployed from various websites and blocked by EDR across the incidents the SOC was aware of.

[Mitre ATT&CK](https://attack.mitre.org/) reference for [Agent Tesla](https://attack.mitre.org/software/S0331/) techniques and tactics to aid detections.

**QakBot** is a modular banking trojan that has been used primarily by financially-motivated actors since at least 2007. Qakbot is continuously maintained and developed and has evolved from an information stealer into delivery agent for ransomware, most notably [ProLock](https://attack.mitre.org/software/S0654/) and [Egregor](https://attack.mitre.org/software/S0554/).  After initial compromise of an organization, it is common to see lateral movement, command-and-control (C2) communications, and ransomware payloads installed on multiple devices. Early indicators of compromise associated with this activity are typically followed by a ransomware attack. This has been detected and remediated at some agencies.

[Mitre ATT&CK](https://attack.mitre.org/) reference for [QakBot](https://attack.mitre.org/software/S0650/) techniques and tactics to aid detections.
