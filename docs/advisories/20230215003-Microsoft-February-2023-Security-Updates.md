# Microsoft February 2023 Security Updates - 20230215003

## Overview

Microsoft's February 2023 security updates fix 77 vulnerabilities, including remote code execution, bypass security features, or elevate privileges, to address multiple vulnerabilities in Microsoft software. An attacker could exploit some of these vulnerabilities to take control of an affected system.

The Office of Digital Government (DGov) encourages Western Australian Government organisations to regularly check Microsoft’s [Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2023-Feb) regarding these CVEs, and implement any actions and updates as required.

## What is the vulnerability ?

Out of Microsoft's 77 vulnerabilities remediated, 9 have been identified as **critical**, and 3 listed below as **actively exploited zero-days**:

---

| CVE                                                                                                         | Vulnerability Name                                                         | Security Update Released | Threat Description                                                                                                                                                                                                                                                                                                                                                             | Action                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CVE-2023-21823](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21823) CVSSv3: **7.8 HIGH** | Windows Graphics Component Remote Code Execution Vulnerability             | 2023-02-14               | An attacker who successfully exploited this vulnerability could gain SYSTEM privileges.                                                                                                                                                                                                                                                                                        | The Microsoft Store will automatically update affected customers. It is possible for customers to disable automatic updates for the Microsoft Store. The Microsoft Store will not automatically install this update for those customers and will require manual updating. |
| [CVE-2023-21715](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21715) CVSSv3: **7.3 HIGH** | Microsoft Publisher Security Features Bypass Vulnerability                 | 2023-02-14               | An authenticated attacker could exploit the vulnerability by convincing a victim, through social engineering, to download and open a specially crafted file from a website which could lead to a local attack on the victim computer. An attacker who successfully exploited this vulnerability could bypass Office macro policies used to block untrusted or malicious files. | **Immediately** apply updates per vendor instructions.                                                                                                                                                                                                                    |
| [CVE-2023-23376](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23376) CVSSv3: **7.8 HIGH** | Windows Common Log File System Driver Elevation of Privilege Vulnerability | 2023-02-14               | Windows Common Log File System Driver contains an unspecified vulnerability which allows an attacker to gain SYSTEM privileges.                                                                                                                                                                                                                                                | **Immediately** apply updates per vendor instructions.                                                                                                                                                                                                                    |

---

## Which vulnerabilities have a critical severity ?

- [CVE-2023-21689](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21689) - Windows Protected EAP (PEAP)
- [CVE-2023-21690](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21690) - Windows Protected EAP (PEAP)
- [CVE-2023-21692](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21692) - Windows Protected EAP (PEAP)
- [CVE-2023-21803](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21803) - Windows iSCSI
- [CVE-2023-23381](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23381) - Visual Studio
- [CVE-2023-21815](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21815) - Visual Studio
- [CVE-2023-21718](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21718) - Visual Studio
- [CVE-2023-21716](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21716) - Microsoft Office Word
- [CVE-2023-21808](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21808) - .NET and Visual Studio

## What is vulnerable ?

The total number of issue types identified by Microsoft in each vulnerability category are listed below:

- 12 Elevation of Privilege Vulnerabilities
- 2 Security Feature Bypass Vulnerabilities
- 38 Remote Code Execution Vulnerabilities
- 8 Information Disclosure Vulnerabilities
- 10 Denial of Service Vulnerabilities
- 8 Spoofing Vulnerabilities

## Recommendation

The WA SOC recommends administrators immediately apply the solutions and updates as per vendor instructions to all affected platforms: <https://msrc.microsoft.com/update-guide/deployments>

## Additional References

- <https://www.cisa.gov/uscert/ncas/current-activity/2023/02/14/microsoft-releases-february-2023-security-updates>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21823>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21715>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-23376>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21689>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21690>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21692>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21803>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-23381>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21815>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21718>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21716>
- <https://nvd.nist.gov/vuln/detail/CVE-2023-21808>
