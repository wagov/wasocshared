# Critical Vulnerability in Deprecated VMware EAP - 20240221001

## Overview

The VMware Enhanced Authentication Plug-in (EAP) contains an Arbitrary Authentication Relay vulnerability. VMware has evaluated the severity of this issue to be in the Critical severity range with a maximum CVSSv3 base score of **9.6**. There are no workarounds, if installed, the plug-in should be removed immediately.

A malicious actor could trick a target domain user with EAP installed in their web browser into requesting and relaying service tickets for arbitrary Active Directory Service Principal Names (SPNs).

## What is vulnerable?

| Product(s) Affected | Summary | Severity     | CVSS |
| ------------------- | ------- | ------------ | ---- |
| VMware Enhanced Authentication Plug-in (EAP) - **Any version** | Component is deprecated and should be removed        | **Critical** | 9.6  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of**48 hours** (refer [Patch Management](../guidelines/patch-management.md)):

- [Removing the deprecated VMware Enhanced Authentication Plugin (EAP) to address CVE-2024-22245 and CVE-2024-22250](https://kb.vmware.com/s/article/96442)

## Additional References

- [VMware Secuity Advisory - VMSA-2024-0003](https://www.vmware.com/security/advisories/VMSA-2024-0003.html)
- [BleepingComputer - VMware urges admins to remove deprecated, vulnerable auth plug-in](https://www.bleepingcomputer.com/news/security/vmware-urges-admins-to-remove-deprecated-vulnerable-auth-plug-in/)
