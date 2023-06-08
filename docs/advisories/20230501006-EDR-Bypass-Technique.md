# EDR Bypass Technique 'Aukill' - 20230501006

## Overview

A recent report by Sophos details new techniques to disable EDR controls, the tool dubbed **Aukill** currently abuses an outdated version of the driver used by version 16.32 of the Microsoft utility, Process Explorer, to disable EDR processes before deploying either a backdoor or ransomware on the target system.

## What is vulnerable?

Vulnerabilities stem from out-dated or custom drivers loaded onto Windows devices.

## What has been observed?

Sophos reports the *Aukill* tool has been observed in at least three ransomware incidents in the past 5 months.

## Recommendation

- It is highly suggested to check if your endpoint security product implements and enables tamper protection. This feature provides a strong layer against such type of attacks.
- Practice strong Windows security roles hygiene. This attack is only possible if the attacker escalates privileges they control, or can obtain administrator rights. Separation between user and admin privileges can help prevent attackers from easily loading drivers.
- Keep your system updated. Windows maintains a list of drivers for which Microsoft has revoked certificates, or deprecated drivers that have been historically abused, and updates that list through the Windows Update mechanism.
- In addition to your operating system, it's also important to check, periodically, whether there are updates for applications and other tools on your computer, and to remove older tools if they are no longer required or used.
- Legitimate driver abuse can also happen if a vulnerable driver already exists on the system. Having a strong vulnerability management program can aid in closing such protection gaps.
- Research and maintain strong detection rules in your EDR and SIEM products to allow detection of suspicious drivers, processes and activity on endpoints.

## Additional References

- [**Sophos Report**](https://news.sophos.com/en-us/2023/04/19/aukill-edr-killer-malware-abuses-process-explorer-driver/)
- [**The Hacker News Article**](https://thehackernews.com/2023/04/ransomware-hackers-using-aukill-tool-to.html)
