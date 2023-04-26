# Multiple VMware Aria Operations for Logs Vulnerabilities - 20230426008

## Overview
Two potentially serious vulnerabilities in VMware Aria Operations for Logs (formerly vRealize Log Insight) have been identified.

1. Log deserialization vulnerability that could allow an **unauthenticated** attacker arbitrary code execution as root.
1. Command injection vulnerability that gives an actor with administrative rights the ability to execute arbitrary commands as root.

## What is the vulnerability?

Please see [VMware Aria Operations for Logs (Operations for Logs) update addresses multiple vulnerabilities](https://www.vmware.com/security/advisories/VMSA-2023-0007.html) for an overview of the following vulnerabilities:

- [**CVE-2023-20864**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20864) - **VMware Aria Operations for Logs Deserialization Vulnerability** - CVSS v3 Base Score: ***9.8***
    - An **unauthenticated**, malicious actor with network access to VMware Aria Operations for Logs may be able to execute arbitrary code as root.
- [**CVE-2023-20865**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20865) - **VMware Aria Operations for Logs Command Injection Vulnerability** - CVSS v3 Base Score: ***7.2***
    - A malicious actor with administrative privileges in VMware Aria Operations for Logs can execute arbitrary commands as root.

## What is vulnerable? 
The vulnerability affects the following products:

- VMware Aria Operations for Logs (Operations for Logs) versions:
    - 8.10.2
    - 8.10
    - 8.8.x
    - 8.6.x
    - 4.x

Please view the [response matrix](https://www.vmware.com/security/advisories/VMSA-2023-0007.html) for specific details.

## What has been observed?
CISA has issued an alert for the vulnerabilities and encourages users and administrators to review the security advisory and apply the relevant updates.

## Recommendation
The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices: [VMware Aria Operations for Logs (Operations for Logs) update addresses multiple vulnerabilities](https://www.vmware.com/security/advisories/VMSA-2023-0007.html).