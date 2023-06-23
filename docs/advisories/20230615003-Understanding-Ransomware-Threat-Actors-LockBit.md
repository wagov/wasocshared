# Understanding Ransomware Threat Actors: LockBit - 20230615003

## Overview

This advisory uses the MITRE ATT&CK for Enterprise framework, version 13.1. See the MITRE ATT&CK Tactics and Techniques section for tables of LockBit’s activity mapped to MITRE ATT&CK® tactics and techniques.

The LockBit RaaS and its affiliates have negatively impacted organizations, both large and small, across the world. In 2022, LockBit was the most active global ransomware group and RaaS provider in terms of the number of victims claimed on their data leak site.

The authoring agencies observe data leak sites, where attackers publish the names and captured data of victims if they do not pay ransom or hush money. Additionally, these sites can be used to record alleged victims who have been threatened with a data leak. The term 'victims' may include those who have been attacked, or those who have been threatened or blackmailed (with the attack having taken place).

Some of the methods LockBit has used to successfully attract affiliates include, but are not limited to:

- Assuring payment by allowing affiliates to receive ransom payments before sending a cut to the core group; this practice stands in stark contrast to other RaaS groups who pay themselves first and then disburse the affiliates' cut.
- Disparaging other RaaS groups in online forums.
- Engaging in publicity-generating activities stunts, such as paying people to get LockBit tattoos and putting a $1 million bounty on information related to the real-world identity of LockBit's lead who goes by the persona "LockBitSupp."
- Developing and maintaining a simplified, point-and-click interface for its ransomware, making it accessible to those with a lower degree of technical skill.

## Delivery

LockBit affiliates have been observed using various freeware and open-source tools that are intended for legal use. When repurposed by LockBit, these tools are then used for a range of malicious cyber activity, such as network reconnaissance, remote access and tunneling, credential dumping, and file exfiltration. Use of PowerShell and batch scripts are observed across most intrusions, which focus on system discovery, reconnaissance, password/credential hunting, and privilege escalation. Artifacts of professional penetration-testing tools such as Metasploit and Cobalt Strike have also been observed.

Table 4 of the [CISA advisory found here](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a), shows a list of tools that are used by LockBit Affiliates.

## What is the vulnerability?

Based on secondary sources, it was noted that affiliates exploit older vulnerabilities like [CVE-2021-22986](https://nvd.nist.gov/vuln/detail/CVE-2021-22986), F5 iControl REST unauthenticated Remote Code Execution Vulnerability, as well as newer vulnerabilities such as:

-   [CVE-2023-0669](https://nvd.nist.gov/vuln/detail/CVE-2023-0669): Fortra GoAnyhwere Managed File Transfer (MFT) Remote Code Execution Vulnerability
-   [CVE-2023-27350](https://nvd.nist.gov/vuln/detail/CVE-2023-27350): PaperCut MF/NG Improper Access Control Vulnerability

LockBit affiliates have been documented exploiting numerous CVEs, including:

-   [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228): Apache Log4j2 Remote Code Execution Vulnerability,
-   [CVE-2021-22986](https://nvd.nist.gov/vuln/detail/CVE-2021-22986): F5 BIG-IP and BIG-IQ Centralized Management iControl REST Remote Code Execution Vulnerability,
-   [CVE-2020-1472: NetLogon Privilege Escalation Vulnerability,](https://nvd.nist.gov/vuln/detail/CVE-2020-1472)
-   [CVE-2019-0708](https://nvd.nist.gov/vuln/detail/CVE-2019-0708): Microsoft Remote Desktop Services Remote Code Execution Vulnerability, and
-   [CVE-2018-13379](https://nvd.nist.gov/vuln/detail/CVE-2018-13379): Fortinet FortiOS Secure Sockets Layer (SSL) Virtual Private Network (VPN) Path Traversal Vulnerability.

## Detection and Remediation

The listed mitigations are ordered by MITRE ATT&CK tactic. Mitigations that apply to multiple MITRE ATT&CK tactics are listed under the tactic that occurs earliest in an incident’s lifecycle. 

### Tactics and techniques

Tables 5-16 in the [CISA Advisory found here](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a), shows a list of LockBit affiliate tactics and techniques.


### Recommended Remediation Steps

A comprehensive list of mitigations organized according to the MITRE ATT&CK tactics and information on implementing additional defence-in-depth measures can be found [here](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a).


## Additional References

- [Understanding Ransomware Threat Actors: LockBit | CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)