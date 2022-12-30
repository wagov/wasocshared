# Microsoft Windows: Multiple known exploited vulnerabilities - 202211100002

## Overview
The WA SOC has observed 4 new vulnerabilities affecting Microsoft Windows applications and services, notably **CVE-2022-41128** has a CVSSv3 of **8.8**.

## What is the vulnerability ?

| CVE | Vulnerability Name | Security Update Released | Threat Description | Action |
| --- | --- | --- | --- | --- |
| [CVE-2022-41091](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41091)  | Microsoft Windows *Mark of the Web (MOTW)* Security Feature Bypass Vulnerability | 2022-11-08 | Microsoft Windows Mark of the Web (MOTW) contains a security feature bypass vulnerability resulting in a limited loss of integrity and availability of security features. | Apply updates per vendor instructions. |
| [CVE-2022-41073](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-41073) | Microsoft Windows *Print Spooler* Privilege Escalation Vulnerability | 2022-11-08 | Microsoft Windows Print Spooler contains an unspecified vulnerability which allows an attacker to gain SYSTEM-level privileges. | Apply updates per vendor instructions. |
| [CVE-2022-41125](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-41125) | Microsoft Windows *CNG Key Isolation* Service Privilege Escalation Vulnerability | 2022-11-08 | Microsoft Windows Cryptographic Next Generation (CNG) Key Isolation Service contains an unspecified vulnerability which allows an attacker to gain SYSTEM-level privileges. | Apply updates per vendor instructions. |
| [CVE-2022-41128](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41128) | Microsoft Windows *Scripting Languages* Remote Code Execution Vulnerability | 2022-11-08 | Microsoft Windows contains an unspecified vulnerability in the JScript9 scripting language which allows for remote code execution. | Apply updates per vendor instructions. |


## What has been observed ?
No active exploitation has been reported in the WA sector, however there are reports of exploitation as reported by Microsoft.

| CVE | Exploited | Publicly Disclosed |
| --- | --- | --- |
| CVE-2022-41091 | Yes | Yes |
| CVE-2022-41073 | Yes | No |
| CVE-2022-41125 | Yes | No |
| CVE-2022-41128 | Yes | No |

## Recommendation
Affected customers of Microsoft Windows are recommended to install the relevant updated versions of their environment as soon as possible. Refer to each relevant reference URL below for the appropriate **Security Update** Download link.

### Reference:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-41091
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-41073
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-41125
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41128
