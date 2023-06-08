# VMware Workstation and Fusion updates address multiple security vulnerabilities - 20230501007

## Overview
The WA SOC has observed multiple security vulnerabilities in VMware Workstation and Fusion. Updates and workarounds are available to remediate these vulnerabilities in the affected VMware products.

VMware Workstation and Fusion contain:
1. a stack-based buffer-overflow vulnerability that exists in the functionality for sharing host Bluetooth devices with the virtual machine.
1. an out-of-bounds read vulnerability that exists in the functionality for sharing host Bluetooth devices with the virtual machine.
1. a local privilege escalation vulnerability
1. an out-of-bounds read/write vulnerability in SCSI CD/DVD device emulation

## What is the vulnerability?
[**CVE-2023-20869**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20869) - **Stack-based buffer-overflow** - CVSS v3 Base Score: ***9.3***

[**CVE-2023-20870**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20869) - **Out-of-bounds read vulnerability** - CVSS v3 Base Score: ***7.1***

[**CVE-2023-20871**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20869) - **Local privilege escalation** - CVSS v3 Base Score: ***7.3***

[**CVE-2023-20872**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20872) - **Out-of-bounds read/write vulnerability in SCSI CD/DVD device emulation** - CVSS v3 Base Score: ***7.7***

## What is vulnerable? 
The vulnerability affects the following VMware products:
- Workstation 17.x
- Fusion 13.x (Running on OS X)

## What has been observed?
There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing

## Recommendation
The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices where possible: [VMware Security Advisory](https://www.vmware.com/security/advisories/VMSA-2023-0008.html)
