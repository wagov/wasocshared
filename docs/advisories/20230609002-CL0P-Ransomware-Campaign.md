# CL0P Ransomware Campaign - 20230609002

## Overview

In a development to our recent advisory about the [MOVEit File Transfer Vulnerability](20230602001-MOVEit-File-Transfer-Vulnerability.md), further guidance has been released by CISA regarding the ransomware gang known as *CL0P*.


## What has been observed?
According to open source information, beginning on May 27, 2023, CL0P Ransomware Gang, also known as TA505, began exploiting a previously unknown SQL injection vulnerability ([CVE-2023-34362](https://nvd.nist.gov/vuln/detail/CVE-2023-34362 "CVE-2023-34362")) in Progress Software's managed file transfer (MFT) solution known as MOVEit Transfer. Internet-facing MOVEit Transfer web applications were infected with a web shell named LEMURLOOT, which was then used to steal data from underlying MOVEit Transfer databases.


## Recommendation

A publication by CISA contains YARA Rules, File Hashes, Domains, IP Addresses, and other indicators of compromise (IOCs) that organisations can utilise to help detect compromised hosts. 
- [CISA Advisory: CL0P Ransomware Gang Exploits CVE-2023-34362 MOVEit Vulnerability](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a)

It is highly recommended to review these IOCs and investigate potential compromises if your organisation used internet-facing MOVEit File Transfer software.

## Additional References

- [Mandiant - Zero-Day Vulnerability in MOVEit Transfer Exploited for Data Theft](https://www.mandiant.com/resources/blog/zero-day-moveit-data-theft)
- [Progress - MOVEit Transfer Critical Vulnerability](https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-31May2023)
- [Rapid7 - Observed Exploitation of Critical MOVEit Transfer Vulnerability](https://www.rapid7.com/blog/post/2023/06/01/rapid7-observed-exploitation-of-critical-moveit-transfer-vulnerability/)
