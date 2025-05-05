# Cyber Security Playbooks

Over time the WA SOC is establishing a set of playbooks, primarily focused on incident response that are suitable for cyber security teams with operational processes aligned to the [CISA Cybersecurity Incident and Vulnerability Response Playbooks (508C)](../pdfs/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf) and the [MITRE 11 Strategies of a World-Class Cybersecurity Operations Center](../pdfs/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf).

## 1. Triage & Investigation

Under Review, see [Sentinel Triage AssistanT (STAT)](https://github.com/briandelmsft/SentinelAutomationModules/blob/main/Docs/readme.md) as an approach to standardise and automate common triage actions.

## 2. Incident Response

![Incident Response](../images/incidentresponse.png)

In the absence of an internal procedure the CERT Societe Generale [IRM-2022 (Incident Response Methodologies 2022)
](https://github.com/wagov/IRM/tree/main/EN) are a good starting point covering the below common scenarios:

1. [Worm Infection (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-1-WormInfection.pdf)
1. [Windows Intrusion (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-2-WindowsIntrusion.pdf)
1. [Unix, Linux Intrusion Detection (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-3-UnixLinuxIntrusionDetection.pdf)
1. [Distributed Denial Of Service - DDOS (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-4-DDOS.pdf)
1. [Malicious Network Behaviour (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-5-MaliciousNetworkBehaviour.pdf)
1. [Website Defacement (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-6-Website-Defacement.pdf)
1. [Windows Malware Detection (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-7-WindowsMalwareDetection.pdf)
1. [Blackmail (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-8-Blackmail.pdf)
1. [Smartphone Malware (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-9-SmartphoneMalware.pdf)
1. [Social Engineering (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-10-SocialEngineering.pdf)
1. [Information Leakage (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-11-InformationLeakage.pdf)
1. [Insider Abuse (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-12-InsiderAbuse.pdf)
1. [Customer Phishing (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-13-Customer_Phishing.pdf)
1. [Scam (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-14-Scam.pdf)
1. [Trademark infringement (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-15-Trademark%20infringement.pdf)
1. [Phishing (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-16-Phishing.pdf)
1. [Ransomware (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-17-Ransomware.pdf)
1. [Large scale compromise (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-18-Large_scale_compromise.pdf)
1. [Third-Party Compromise (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-19-3rd-party_compromise.pdf)
1. [Red Team Detection](https://github.com/wagov/IRM/raw/main/EN/IRM-20-Red_Team_Detection.pdf)
1. [Critical Vulnerability Prioritisation (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-21-Critical_Vulnerability_Prioritization.pdf)
1. [Busniess Email Compromise (pdf)](https://github.com/wagov/IRM/raw/main/EN/IRM-22-Business_Email_Compromise.pdf)

## 3. Vulnerability Response

![Vulnerability Response](../images/vulnerabilityresponse.png)

Under Review, refer to [Technical Example: Patch Operating Systems](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-operating-system) and [Technical Example: Patch Applications](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-patch-applications) for good approaches to automating baseline vulnerability management.

## 4. Threat Hunting

Under Review, [Jupyter Notebooks](https://github.com/github/codespaces-jupyter) are effective, and easily query datalake type repositories, see [Use a Jupyter Notebook and kqlmagic extension to analyze data in Azure Data Explorer](https://learn.microsoft.com/en-us/azure/data-explorer/kqlmagic).

## 5. Digital Forensics

Under Review, see [Collecting Evidence](collecting-evidence.md) and [Dissect (modern forensics tooling)](https://docs.dissect.tools/en/latest/index.html) to augment SIEM activities with in depth captures as needed.
