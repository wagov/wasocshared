# VMware ESXiArgs Ransomware Recovery Script Release - 20230208001

## Overview
CISA has released a recovery script for organisations that have fallen victim to ESXiArgs ransomware. The ESXiArgs ransomware encrypts configuration files on vulnerable ESXi servers, potentially rendering virtual machines (VMs) unusable. 

ESXi is VMware’s hypervisor, a technology that allows organisations to host several virtualised computers running multiple operating systems on a single physical server.

## What is the vulnerability?
- [**CVE-2021-21974 from VMSA-2021-0002**](https://www.vmware.com/security/advisories/VMSA-2021-0002.html) - **9.8 CRITICAL** - CVSSv3 Score. ESXi OpenSLP heap-overflow vulnerability. A malicious actor residing within the same network segment as ESXi who has access to port 427 may be able to trigger a heap-overflow issue in the OpenSLP service resulting in remote code execution.

- [**CVE-2020-3992 from VMSA-2020-0023**](https://www.vmware.com/security/advisories/VMSA-2020-0023.html) - **9.8 CRITICAL** - ESXi OpenSLP remote code execution vulnerability. A malicious actor residing in the management network who has access to port 427 on an ESXi machine may be able to trigger a use-after-free in the OpenSLP service resulting in remote code execution.

## What is vulnerable? 
The vulnerability affects the following products:
- VMware ESXi
- VMware vCenter Server (vCenter Server)
- VMware Cloud Foundation (Cloud Foundation)
- VMware Workstation Pro / Player (Workstation)
- VMware Fusion Pro / Fusion (Fusion)


## Recommendation
The WA SOC recommends organisations impacted by ESXiArgs evaluate the script and guidance provided in the accompanying [**README file**](https://github.com/cisagov/ESXiArgs-Recover/blob/main/README.md) to determine if it is fit for attempting to recover access to files in their environment.

Organisations can access the recovery script here: https://github.com/cisagov/ESXiArgs-Recover

## Additional References:
* https://www.cisa.gov/uscert/ncas/current-activity/2023/02/07/cisa-releases-esxiargs-ransomware-recovery-script
* https://github.com/cisagov/ESXiArgs-Recover/blob/main/README.md
* https://www.techrepublic.com/article/massive-ransomware-operation-targets-vmware-esxi/
* https://nakedsecurity.sophos.com/2023/02/07/using-vmware-worried-about-esxi-ransomware-check-your-patches-now/