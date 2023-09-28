# NSA, FBI, CISA, and Japanese Partners Release Advisory on PRC-Linked Cyber Actors - 20230928002

## Overview

The United States National Security Agency (NSA), the U.S. Federal Bureau of Investigation (FBI), the U.S. Cybersecurity and Infrastructure Security Agency (CISA), the Japan National Police Agency (NPA), and the Japan National Center of Incident Readiness and Strategy for Cybersecurity (NISC) are releasing this joint cybersecurity advisory (CSA) to detail activity of the People’s Republic of China (PRC)-linked cyber actors known as BlackTech.
BlackTech has demonstrated capabilities in modifying router firmware without detection and exploiting routers’ domain-trust relationships for pivoting from international subsidiaries to headquarters in Japan and the U.S..

BlackTech (a.k.a. Palmerworm, Temp.Overboard, Circuit Panda, and Radio Panda) actors have targeted government, industrial, technology, media, electronics, and telecommunication sectors, including entities that support the militaries of the U.S. and Japan. BlackTech actors use custom malware, dual-use tools, and living off the land tactics, such as disabling logging on routers, to conceal their operations. This CSA details BlackTech’s tactics, techniques, and procedures (TTPs), which highlights the need for multinational corporations to review all subsidiary connections, verify access, and consider implementing Zero Trust models to limit the extent of a potential BlackTech compromise.

## BlackTech - Observable TTPs

BlackTech actors' TTPs include developing customized malware and tailored persistence mechanisms for compromising routers. These TTPs allow the actors to disable logging [[T1562](https://attack.mitre.org/versions/v13/techniques/T1562/ "Impair Defenses")] and abuse trusted domain relationships [[T1199](https://attack.mitre.org/versions/v13/techniques/T1199/ "Trusted Relationship")] to pivot between international subsidiaries and domestic headquarters' networks.

The actors have used a range of custom malware families targeting Windows®, Linux®, and FreeBSD® operating systems. Custom malware families employed by BlackTech include:

-   BendyBear [[S0574](https://attack.mitre.org/versions/v13/software/S0574/ "BendyBear")]
-   Bifrose
-   BTSDoor
-   FakeDead (a.k.a. TSCookie) [[S0436](https://attack.mitre.org/versions/v13/software/S0436/ "TSCookie")]
-   Flagpro [[S0696](https://attack.mitre.org/versions/v13/software/S0696/ "Flagpro")]
-   FrontShell (FakeDead's downloader module)
-   IconDown
-   PLEAD [[S0435](https://attack.mitre.org/versions/v13/software/S0435/ "PLEAD")]
-   SpiderPig
-   SpiderSpring
-   SpiderStack
-   WaterBear [[S0579](https://attack.mitre.org/versions/v13/software/S0579/ "Waterbear")]

BlackTech actors continuously update these tools to evade detection [[TA0005](https://attack.mitre.org/versions/v13/tactics/TA0005/ "Defense Evasion")] by security software. The actors also use stolen code-signing certificates [[T1588.003](https://attack.mitre.org/versions/v13/techniques/T1588/003/ "Obtain Capabilities: Code Signing Certificates")] to sign the malicious payloads, which make them appear legitimate and therefore more difficult for security software to detect [[T1553.002](https://attack.mitre.org/versions/v13/techniques/T1553/002/ "Subvert Trust Controls: Code Signing")].

BlackTech actors use living off the land TTPs to blend in with normal operating system and network activities, allowing them to evade detection by endpoint detection and response (EDR) products. Common methods of persistence on a host include NetCat shells, modifying the victim registry [[T1112](https://attack.mitre.org/versions/v13/techniques/T1112/ "Modify Registry")] to enable the remote desktop protocol (RDP) [[T1021.001](https://attack.mitre.org/versions/v13/techniques/T1021/001/ "Remote Services: Remote Desktop Protocol")], and secure shell (SSH) [[T1021.004](https://attack.mitre.org/versions/v13/techniques/T1021/004/ "Remote Services: SSH")]. The actors have also used SNScan for enumeration [[TA0007](https://attack.mitre.org/versions/v13/tactics/TA0007/ "Discovery")], and a local file transfer protocol (FTP) server [[T1071.002](https://attack.mitre.org/versions/v13/techniques/T1071/002/ "Application Layer Protocol: File Transfer Protocols")] to move data through the victim network. For additional examples of malicious cyber actors living off the land, see [People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a)


### Firmware replacement process

BlackTech actors utilize the following file types to compromise the router. These files are downloaded to the router via FTP or SSH. 

| **File Type**           | **Description**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| Old Legitimate Firmware | The IOS image firmware is modified in memory to allow installation of the Modified Firmware and Modified Bootloader.|
| Modified Firmware       | The firmware has a built-in SSH backdoor, allowing operators to have unlogged interaction with the router.|
| Modified Bootloader     | The bootloader allows Modified Firmware to continue evading the router's security features for persistence across reboots. In some cases, only modified firmware is used. |

For a detailed list of processes and methods used by the BlackTech actors for compromising of routers, refer to the CISA advisory [here](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-270a).


## Detection and Mitigation Techniques

In order to detect and mitigate this BlackTech malicious activity, the authoring agencies strongly recommend the following detection and mitigation techniques. It would be trivial for the BlackTech actors to modify values in their backdoors that would render specific signatures of this router backdoor obsolete. For more robust detection, network defenders should monitor network devices for unauthorized downloads of bootloaders and firmware images and reboots. Network defenders should also monitor for unusual traffic destined to the router, including SSH.

The following are the best mitigation practices to defend against this type of malicious activity:

-   Disable outbound connections by applying the "transport output none" configuration command to the virtual teletype (VTY) lines. This command will prevent some copy commands from successfully connecting to external systems.\
    Note: An adversary with unauthorized privileged level access to a network device could revert this configuration change.[[3](https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF "Network Infrastructure Security Guide")]

-   Monitor both inbound and outbound connections from network devices to both external and internal systems. In general, network devices should only be connecting to nearby devices for exchanging routing or network topology information or with administrative systems for time synchronization, logging, authentication, monitoring, etc. If feasible, block unauthorized outbound connections from network devices by applying access lists or rule sets to other nearby network devices. Additionally, place administrative systems in separate virtual local area networks (VLANs) and block all unauthorized traffic from network devices destined for non-administrative VLANs.[[4](https://media.defense.gov/2020/Sep/17/2002499616/-1/-1/0/PERFORMING_OUT_OF_BAND_NETWORK_MANAGEMENT20200911.PDF "Performing Out-of-Band Network Management")]

-   Limit access to administration services and only permit IP addresses used by network administrators by applying access lists to the VTY lines or specific services. Monitor logs for successful and unsuccessful login attempts with the "login on-failure log" and "login on-success log" configuration commands, or by reviewing centralized Authentication, Authorization, and Accounting (AAA) events.[[3](https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF "Network Infrastructure Security Guide")]

-   Upgrade devices to ones that have secure boot capabilities with better integrity and authenticity checks for bootloaders and firmware. In particular, highly prioritize replacing all end-of-life and unsupported equipment as soon as possible.[[3](https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF "Network Infrastructure Security Guide")],[[5](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954 "Attackers Continue to Target Legacy Devices")]

-   When there is a concern that a single password has been compromised, change all passwords and keys.[[3](https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF "Network Infrastructure Security Guide")]

-   Review logs generated by network devices and monitor for unauthorized reboots, operating system version changes, changes to the configuration, or attempts to update the firmware. Compare against expected configuration changes and patching plans to verify that the changes are authorized.[[3](https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF "Network Infrastructure Security Guide")]

-   Periodically perform both file and memory verification described in the Network Device Integrity (NDI) Methodology documents to detect unauthorized changes to the software stored and running on network devices.[[3](https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF "Network Infrastructure Security Guide")]

-   Monitor for changes to firmware. Periodically take snapshots of boot records and firmware and compare against known good images.[[3](https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF "Network Infrastructure Security Guide")]

## Additional References

- [People's Republic of China-Linked Cyber Actors Hide in Router Firmware | CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-270a)
