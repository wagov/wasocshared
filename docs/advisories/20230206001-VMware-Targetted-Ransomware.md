# VMware ESXi servers targetted by ESXiArgs ransomware - 20230206001

## Overview
An article published by BleepingComputer is noting an increasing amount of reports of attackers actively targeting unpatched VMware ESXi servers containing a Remote Code Execution (RCE) vulnerability to deploy a new "ESXiArgs" ransomware.

VMWare released an official advisory for the CVE on **23rd Februrary 2021**: [https://www.vmware.com/security/advisories/VMSA-2021-0002.html](https://www.vmware.com/security/advisories/VMSA-2021-0002.html)

## What is the vulnerability?
[**CVE-2021-21974**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21974) - CVSS v3 Base Score **8.8**: OpenSLP as used in ESXi (7.0 before ESXi70U1c-17325551, 6.7 before ESXi670-202102401-SG, 6.5 before ESXi650-202102101-SG) has a heap-overflow vulnerability. A malicious actor residing within the same network segment as ESXi who has access to port 427 may be able to trigger the heap-overflow issue in OpenSLP service resulting in remote code execution.

## What is vulnerable?
The vulnerability exists in the following products:
- ESXi versions 7.x prior to ESXi70U1c-17325551
- ESXi versions 6.7.x prior to ESXi670-202102401-SG
- ESXi versions 6.5.x prior to ESXi650-202102101-SG

## Recommendation
Due to the report of active exploitation, it is strongly recommended to patch this vulnerability within 2 weeks across all affected platforms as per vendor instructions: [https://www.vmware.com/security/advisories/VMSA-2021-0002.html](https://www.vmware.com/security/advisories/VMSA-2021-0002.html)

### Additional Resources:
- BleepingComputer article "*Massive ESXiArgs ransomware attack targets VMware ESXi servers worldwide*": [https://www.bleepingcomputer.com/news/security/massive-esxiargs-ransomware-attack-targets-vmware-esxi-servers-worldwide/](https://www.bleepingcomputer.com/news/security/massive-esxiargs-ransomware-attack-targets-vmware-esxi-servers-worldwide/)