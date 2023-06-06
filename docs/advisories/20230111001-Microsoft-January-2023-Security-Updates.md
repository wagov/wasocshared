# Microsoft January 2023 Security Updates - 20230111001

## Overview
Microsoft's January 2023 security updates fix 98 vulnerabilities, including remote code execution, bypass security features, or elevate privileges, to address multiple vulnerabilities in Microsoft software. An attacker could exploit some of these vulnerabilities to take control of an affected system. 

The Office of Digital Government (DGov) encourages Western Australian Government organisations to regularly check Microsoft’s [Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2023-Jan) regarding these CVEs, and implement any actions and updates as required.

## What is the vulnerability ?
Out of Microsoft's 118 vulnerabilities security updated, a few more notable due to the high severity score: 


-----------------------------------------------------------------------------------------------------------------------------

| CVE | Vulnerability Name | Security Update Released | Threat Description | Action |
| --- | --- | --- | --- | --- |
| [CVE-2023-21674](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21674) CVSSv3: **8.8 HIGH** | Windows Advanced Local Procedure Call (ALPC) Elevation of Privilege Vulnerability | 2023-01-10 | Microsoft Windows Cryptographic Next Generation (CNG) Key Isolation Service contains an unspecified vulnerability which allows an attacker to gain SYSTEM-level privileges. | **Immediately** apply updates per vendor instructions due to vulnerability already being exploited. |
| [CVE-2022-21549](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21549) CVSSv3: **8.8 HIGH** | Windows SMB Witness Service Elevation of Privilege Vulnerability | 2023-01-10 | An attacker could execute a specially crafted malicious script that executes an RPC call to an RPC host. This could result in elevation of privilege on the server. An attacker who successfully exploited this vulnerability could execute RPC functions that are restricted to privileged accounts only. | **Immediately** apply updates per vendor instructions. |
| [CVE-2023-21561](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21561) CVSSv3: **8.8 HIGH** | Microsoft Cryptographic Services Elevation of Privilege Vulnerability | 2023-01-10 | The vulnerability allows a remote attacker to perform a denial of service (DoS) attack. The vulnerability exists due to insufficient validation of user-supplied input in Windows iSCSI Service. A remote attacker can pass specially crafted input to the application and perform a denial of service (DoS) attack. | **Immediately** apply updates per vendor instructions. |
| [CVE-2023-21563](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21563) | BitLocker Security Feature Bypass Vulnerability | 2023-01-10| A successful attacker could bypass the BitLocker Device Encryption feature on the system storage device. An attacker with physical access to the target could exploit this vulnerability to gain access to encrypted data.. | Apply updates per vendor instructions. |
| [CVE-2023-21527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21527) | Windows iSCSI Service Denial of Service Vulnerability | 2023-01-10 | The vulnerability allows a remote attacker to perform a denial of service (DoS) attack. The vulnerability exists due to insufficient validation of user-supplied input in Windows iSCSI Service. A remote attacker can pass specially crafted input to the application and perform a denial of service (DoS) attack. | Apply updates per vendor instructions. |
--------------------------------------------------------------------------------------------------------------------------



## What is vulnerable ? 
The total number of issue types identified by Microsoft in each vulnerability category are listed below:

- 39 Elevation of Privilege Vulnerabilities
- 4 Security Feature Bypass Vulnerabilities
- 33 Remote Code Execution Vulnerabilities
- 10 Information Disclosure Vulnerabilities
- 10 Denial of Service Vulnerabilities
- 2 Spoofing Vulnerabilities

## Recommendation
The WA SOC recommends administrators immediately apply the solutions and updates as per vendor instructions to all affected platforms: https://msrc.microsoft.com/update-guide/deployments

## Additional References:
* https://www.cisa.gov/uscert/ncas/current-activity/2023/01/10/microsoft-releases-january-2023-security-updates
* https://nvd.nist.gov/vuln/detail/CVE-2023-21674
* https://nvd.nist.gov/vuln/detail/CVE-2023-21549
* https://nvd.nist.gov/vuln/detail/CVE-2023-21561
* https://nvd.nist.gov/vuln/detail/CVE-2023-21563
* https://nvd.nist.gov/vuln/detail/CVE-2023-21527