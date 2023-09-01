#  CISA and FBI Publish JointAdvisoryonQakBotInfrastructure - 20230901001

## Overview

CISA has released a joint advisory with FBI to disseminate QakBot infrastructure indicators of compromise (IOCs) identified through FBI investigations as of August 2023. This advisory aims to help organisations detect and protect against newly identified QakBot-related activity and malware.


## Delivery

The delivery method for QakBot has been carried out mainly via phishing campaigns containing malicious attachments or links to download the malware, which would reside in memory once on the victim network.


## Indicator of Compromise

The following list of IOC's can be used for detecting and identifying of any activity related to QakBot.

### Registry Key(s) and Folder(s)

FBI has observed the following threat actor tactics, techniques, and procedures (TTPs) in association with QakBot infections:

1. QakBot sets up persistence via the Registry Run Key as needed. It will delete this key when running and set it back up before computer restart:
    ```text
    HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\<random_string>
    ```

2. QakBot will also write its binary back to disk to maintain persistence in the following folder:
    ```text
    C:\Users\<user>\AppData\Roaming\Microsoft\<random_string>\
    ```

3. QakBot will write an encrypted registry configuration detailing information about the bot to the following registry key:
    ```text
    HKEY_CURRENT_USER\Software\Microsoft\<random_string>
    ```

### IP Address

The following IPs have been assessed to be linked to that platform, any communications to them should be inspected and assessed if it’s relevant to QakBot/malware activity:


| **IP Address**    | **First Seen** |
|-------------------|----------------|
| 85.14.243[.]111   | April 2020     |
| 51.38.62[.]181    | April 2021     |
| 51.38.62[.]182    | December 2021  |
| 185.4.67[.]6      | April 2022     |
| 62.141.42[.]36    | April 2022     |
| 87.117.247[.]41   | May 2022       |
| 89.163.212[.]111  | May 2022       |
| 193.29.187[.]57   | May 2022       |
| 193.201.9[.]93    | June 2022      |
| 94.198.50[.]147   | August 2022    |
| 94.198.50[.]210   | August 2022    |
| 188.127.243[.]130 | September 2022 |
| 188.127.243[.]133 | September 2022 |
| 94.198.51[.]202   | October 2022   |
| 188.127.242[.]119 | November 2022  |
| 188.127.242[.]178 | November 2022  |
| 87.117.247[.]41   | December 2022  |
| 190.2.143[.]38    | December 2022  |
| 51.161.202[.]232  | January 2023   |
| 51.195.49[.]228   | January 2023   |
| 188.127.243[.]148 | January 2023   |
| 23.236.181[.]102  | Unknown        |
| 45.84.224[.]23    | Unknown        |
| 46.151.30[.]109   | Unknown        |
| 94.103.85[.]86    | Unknown        |
| 94.198.53[.]17    | Unknown        |
| 95.211.95[.]14    | Unknown        |
| 95.211.172[.]6    | Unknown        |
| 95.211.172[.]7    | Unknown        |
| 95.211.172[.]86   | Unknown        |
| 95.211.172[.]108  | Unknown        |
| 95.211.172[.]109  | Unknown        |
| 95.211.198[.]177  | Unknown        |
| 95.211.250[.]97   | Unknown        |
| 95.211.250[.]98   | Unknown        |
| 95.211.250[.]117  | Unknown        |
| 185.81.114[.]188  | Unknown        |
| 188.127.243[.]145 | Unknown        |
| 188.127.243[.]147 | Unknown        |
| 188.127.243[.]193 | Unknown        |
| 188.241.58[.]140  | Unknown        |
| 193.29.187[.]41   | Unknown        |


## Recommended Remediation Steps

CISA and FBI recommend network defenders apply the following mitigations to reduce the likelihood of QakBot-related activity and promote identification of QakBot-induced ransomware and malware infections. Disruption of the QakBot botnet does not mitigate other already-installed malware or ransomware on victim computers.

**Best Practice Mitigation Recommendations** :

1. Implement a recovery plan to maintain and retain multiple copies of sensitive or proprietary data and servers in a physically separate, segmented, and secure location

2. Require all accounts with password logins (e.g., service accounts, admin accounts, and domain admin accounts) to comply with [NIST's standards](https://pages.nist.gov/800-63-3/sp800-63b.html "NIST Special Publication 800-63B") when developing and managing password policies

3. Use phishing-resistant multi-factor authentication (MFA).

4. Keep all operating systems, software, and firmware up to date.

5. Segment networks to prevent the spread of ransomware.

6. Identify, detect, and investigate abnormal activity and potential traversal of the indicated malware with a networking monitoring tool.

7. Install, regularly update, and enable real time detection for antivirus software on all hosts.

8. Review domain controllers, servers, workstations, and active directories for new and/or unrecognized accounts.

9. Audit user accounts with administrative privileges and configure access controls.

10. Disable any unused network ports.

11. Consider adding an email banner to emails received from outside your organization.

12. Disable hyperlinks in received emails.

13. Implement time-based access for accounts set at the admin level and higher.

14. Disable command-line and scripting activities and permissions.

15. Perform regular secure system backups and create known good copies of all device configurations for repairs and/or restoration.

16. Ensure all backup data is encrypted, immutable (i.e., cannot be altered or deleted), and covers the entire organization’s data infrastructure.


For more information on mitigations, please refer to CISA's [Identification and Disruption of QakBot Infrastructure](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-242a) advisory.

***Note***: *For situational awareness, the following SHA-256 hash is associated with FBI’s QakBot uninstaller*: 
```
7cdee5a583eacf24b1f142413aabb4e556ccf4ef3a4764ad084c1526cc90e117
```

#### Resources:

-   [HHS: Qbot/QakBot Malware](https://www.cisa.gov/stopransomware/qbotqakbot-malware-report "Qbot/Qakbot Malware Report")
-   [CISA: CPGs](https://www.cisa.gov/cpg "Cross-Sector Cybersecurity Performance Goals")
-   [NIST: 800-63B Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html "NIST Special Publication 800-63B")
-   [CISA: MFA](https://www.cisa.gov/MFA "More than a Password")
-   [CISA: Implementing Phishing-Resistant MFA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf "Implementing Phishing-Resistant MFA")
-   [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog "Known Exploited Vulnerabilities Catalog")
-   [CISA: Cyber Hygiene](https://www.cisa.gov/cyber-hygiene-services "Services")
-   [CISA: Zero Trust](https://www.cisa.gov/zero-trust-maturity-model "Zero Trust Maturity Model")
-   [CISA: #StopRansomware](https://www.stopransomware.gov/ "#StopRansomware")
-   [CISA: #StopRansomware Guide](https://www.cisa.gov/news-events/alerts/2023/05/23/cisa-and-partners-update-stopransomware-guide-developed-through-joint-ransomware-task-force-jrtf "#StopRansomware Guide")
-   [CISA: CSET Tool Sets Sights on Ransomware Threat](https://github.com/cisagov/cset/releases/tag/v10.3.0.0 "Ransomware Readiness Assessment CSET v10.3")


## Reference

* [CISA and FBI Publish Joint Advisory on QakBot Infrastructure | CISA](https://www.cisa.gov/news-events/alerts/2023/08/30/cisa-and-fbi-publish-joint-advisory-qakbot-infrastructure)
* [Identification and Disruption of QakBot Infrastructure | CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-242a)
