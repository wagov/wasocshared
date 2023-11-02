# VMware Tools Local Privilege Escalation and SAML Token Signature Bypass Vulnerabilities - 20231031001

## Overview

The WA SOC has observed multiple vulnerabilities released in VMWare tools.

VMware Tools contains a local privilege escalation vulnerability. A malicious actor with local user access to a guest virtual machine may elevate privileges within the virtual machine.

VMware Tools contains a SAML token signature bypass vulnerability. A malicious actor that has been granted [Guest Operation Privileges](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-security/GUID-6A952214-0E5E-4CCF-9D2A-90948FF643EC.html)  in a target virtual machine may be able to elevate their privileges if that target virtual machine has been assigned a more [privileged Guest Alias](https://vdc-download.vmware.com/vmwb-repository/dcr-public/d1902b0e-d479-46bf-8ac9-cee0e31e8ec0/07ce8dbd-db48-4261-9b8f-c6d3ad8ba472/vim.vm.guest.AliasManager.html)

## What is the vulnerability?

[**CVE-2023-34057**](https://nvd.nist.gov/vuln/detail/CVE-2023-34057) - CVSS v3 Base Score: ***7.8***

[**CVE-2023-34058**](https://nvd.nist.gov/vuln/detail/CVE-2023-34058) - CVSS v3 Base Score: ***7.5***

## What is vulnerable?

The vulnerability affects the following VMWare tools versions:

- before 12.1.1 (running on macOS)
- before 12.3.5 (running on Windows)

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks* (refer [Patch Management](../guidelines/patch-management.md)):

- [VMWare tools release notes for Windows](https://docs.vmware.com/en/VMware-Tools/12.3/rn/vmware-tools-1235-release-notes/index.html)

## Additional References

- [VMWare Security Advisory](https://www.vmware.com/security/advisories/VMSA-2023-0024.html)


