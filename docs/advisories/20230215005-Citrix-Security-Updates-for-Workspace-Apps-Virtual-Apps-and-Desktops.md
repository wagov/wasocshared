# Citrix Security Updates for Workspace Apps, Virtual Apps and Desktops - 20230215005

## Overview
Citrix has released security updates to address high-severity vulnerabilities (CVE-2023-24486, CVE-2023-24484, CVE-2023-24485, and CVE-2023-24483) in Citrix Workspace Apps, Virtual Apps and Desktops. A local user could exploit these vulnerabilities to take control of an affected system.

CISA encourages users and administrators to review Citrix security bulletins: 
- [CTX477616 ](https://support.citrix.com/article/CTX477616/citrix-virtual-apps-and-desktops-security-bulletin-for-cve20232448)
- [CTX477617](https://support.citrix.com/article/CTX477617/citrix-workspace-app-for-windows-security-bulletin-for-cve202324484-cve202324485)
- [CTX477618](https://support.citrix.com/article/CTX477618/citrix-workspace-app-for-linux-security-bulletin-for-cve202324486)

## What is the vulnerability?
[**CVE-2023-24483**] - Privilege Escalation to NT AUTHORITY\SYSTEM on the vulnerable VDA

[**CVE-2023-24484**] - A malicious user can cause log files to be written to a directory that they do not have permission to write to

[**CVE-2023-24485**] - Privilege Escalation on the system running a vulnerable version of Citrix Workspace app for Windows

[**CVE-2023-24486**] - Session takeover

## What is vulnerable?

[CTX477616 ](https://support.citrix.com/article/CTX477616/citrix-virtual-apps-and-desktops-security-bulletin-for-cve20232448) bulletin includes information of a vulnerability has been identified in Citrix Workspace app for Linux that, if exploited, may result in a malicious local user being able to gain access to the Citrix Virtual Apps and Desktops session of another user who is using the same computer from which the ICA session is launched.

[CTX477617](https://support.citrix.com/article/CTX477617/citrix-workspace-app-for-windows-security-bulletin-for-cve202324484-cve202324485) bulletin comprises information of vulnerabilities identified that, collectively, allow a standard Windows user to perform operations as SYSTEM on the computer running Citrix Workspace app.

[CTX477618](https://support.citrix.com/article/CTX477618/citrix-workspace-app-for-linux-security-bulletin-for-cve202324486) incorporates information of a vulnerability that has been identified, if exploited, could result in a local user elevating their privilege level to NT AUTHORITY\SYSTEM on a Citrix Virtual Apps and Desktops Windows VDA. 


## Recommendation
Due to the report of active exploitation, it is strongly recommended to patch this vulnerability within 2 weeks across all affected platforms as per vendor instructions: 

The latest version of Citrix Workspace app for Windows is available from the following Citrix website location: 

https://www.citrix.com/downloads/workspace-app/windows/ 

The latest LTSR version of Citrix Workspace app for Windows is available from the following Citrix website location: 

https://www.citrix.com/downloads/workspace-app/workspace-app-for-windows-long-term-service-release/ 

Citrix Workspace App 1912 LTSR before CU7 Hotfix 2 (19.12.7002) is available from the following Citrix website location:

https://support.citrix.com/article/CTX473064/hotfix-citrix-workspace-app-for-windows-1912-ltsr-cu7-hotfix-2-19127002-english

The latest versions of Citrix Virtual Apps and Desktops are available from the following Citrix website location: 

https://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/

The latest version of Citrix Workspace app for Linux is available from the following Citrix website location: 

https://www.citrix.com/downloads/workspace-app/linux/ 



