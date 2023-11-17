# Microsoft Sharepoint Server 19 Authentication Bypass PoC - 20231002006

## Overview

A proof-of-concept (PoC) exploit code has surfaced on GitHub for a critical authentication bypass vulnerability in **Microsoft SharePoint Server**, allowing privilege escalation.

**CVE-2023-29357** and **CVE-2023-24955** can be combined to achieve remote code execution on affected versions of SharePoint 2019.

## What is the vulnerability?

- [**CVE-2023-29357**](https://www.cve.org/CVERecord?id=CVE-2023-29357) - CVSS v3 Base Score: ***9.8***: Microsoft SharePoint Server Elevation of Privilege Vulnerability allows a remote, unauthenticated attacker to exploit the vulnerability by sending a spoofed JWT authentication token to a vulnerable server, granting them elevated privileges of an authenticated user on the target. No end-user interaction is required.

- [**CVE-2023-24955**](https://www.cve.org/CVERecord?id=CVE-2023-24955) - CVSS v3 Base Score: ***7.2***: Microsoft SharePoint Server Remote Code Execution Vulnerability is a remote code execution vulnerability affecting Microsoft SharePoint Server. The vulnerability allows an authenticated Site Owner to execute code on an affected SharePoint Server.

## What is vulnerable?

The vulnerabilities exist in the following products:

- **CVE-2023-29357**:
  - Microsoft SharePoint Server 2019

- **CVE-2023-24955**:
  - Microsoft SharePoint Server Subscription Edition
  - Microsoft SharePoint Server 2019
  - Microsoft SharePoint Enterprise Server 2016

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://learn.microsoft.com/en-us/officeupdates/sharepoint-updates>

### Additional Resources

- <https://www.bleepingcomputer.com/news/security/exploit-released-for-microsoft-sharepoint-server-auth-bypass-flaw/#:~:text=%22An%20attacker%20who%20has%20gained,when%20it%20patched%20the%20vulnerability>