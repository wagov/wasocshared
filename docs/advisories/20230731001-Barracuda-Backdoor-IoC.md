# Malware Analysis Reports on Barracuda Backdoors - 20230104001

## Overview

Update to [**Barracuda Networks Releases Update to Address ESG Vulnerability - 20230616001**](https://soc.cyber.wa.gov.au/advisories/20230616001-Barracuda-Networks-Releases-Update-to-Address-ESG-Vulnerability/?h=barrac)

CISA has published three [**malware analysis reports**](https://www.cisa.gov/news-events/alerts/2023/07/28/cisa-releases-malware-analysis-reports-barracuda-backdoors) on malware variants associated with the remote command injection vulnerability that exists in the Barracuda Email Security Gateway [**CVE-2023-2868**](https://nvd.nist.gov/vuln/detail/CVE-2023-2868). These reports contain Indicators of Compromise (IoC) that are assosiated with each of these malware variants.

## Malware Analysis Reports

- [**SUBMARINE Backdoor**](https://www.cisa.gov/news-events/analysis-reports/ar23-209a)– SUBMARINE is a novel persistent backdoor executed with root privileges that lives in a Structured Query Language (SQL) database on the ESG appliance. SUBMARINE comprises multiple artifacts—including a SQL trigger, shell scripts, and a loaded library for a Linux daemon—that together enable execution with root privileges, persistence, command and control, and cleanup. CISA also analyzed artifacts related to SUBMARINE that contained the contents of the compromised SQL database. This malware poses a severe threat for lateral movement.

- [**SEASPY Backdoor**](https://www.cisa.gov/news-events/analysis-reports/ar23-209b)– SEASPY is a persistent and passive backdoor that masquerades as a legitimate Barracuda service. SEASPY monitors traffic from the actor’s C2 server. When the right packet sequence is captured, it establishes a Transmission Control Protocol (TCP) reverse shell to the C2 server. The shell allows the threat actors to execute arbitrary commands on the ESG appliance.\

- [**Barracuda Exploit Payload & Backdoor**](https://www.cisa.gov/news-events/analysis-reports/ar23-209c) - The payload exploits CVE-2023-2868, leading to dropping and execution of a reverse shell backdoor on ESG appliance. The reverse shell establishes communication with the threat actor’s command and control (C2) server, from where it downloads the SEASPY backdoor to the ESG appliance. The actors delivered the payload to the victim via a phishing email with a malicious attachment.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WASOC recommends administrators review the associated indicators against their relevant Email Gateway Solutions and remediate were necessary. 
