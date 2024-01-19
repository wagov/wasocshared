# VMware vCenter Server updates address out-of-bounds write and information disclosure vulnerabilities - 20231026001

## Overview

VMware has released updates to address the VMware vCenter Server Out-of-Bounds Write and information disclosure vulnerabilities which would allow threat actors to perform remote code execution and access unauthorised data respectively.

## What is the vulnerability?

[**CVE-2023-34048**](https://nvd.nist.gov/vuln/detail/CVE-2023-34048) - CVSS v3 Base Score: ***9.8***

- This vulnerability allows malicious actor(s) with network access to vCenter Server to perform remote code execution.

[**CVE-2023-34056**](https://nvd.nist.gov/vuln/detail/CVE-2023-34056) - CVSS v3 Base Score: ***4.3***

- A malicious actor with non-administrative privileges to vCenter Server may leverage this issue to access unauthorized data.

## What is vulnerable?

The vulnerability affects the following products:

- VMware vCenter Server 8.0
- VMware vCenter Server 7.0
- VMware Cloud Foundation (VMware vCenter Server) 5.x, 4.x

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

| Product                                         | Version  | CVE Identifier                 | CVSSv3   | Severity | Fixed Version                                                                                                   | Workarounds | Additional Documentation                      |
| ----------------------------------------------- | -------- | ------------------------------ | -------- | -------- | --------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------- |
| VMware vCenter Server                           | 8.0      | CVE-2023-34048, CVE-2023-34056 | 9.8, 4.3 | Critical | [8.0U2](https://customerconnect.vmware.com/downloads/details?downloadGroup=VC80U2&productId=1345&rPId=110105)   | None        | [FAQ](https://via.vmw.com/vmsa-2023-0023-qna) |
| VMware vCenter Server                           | 8.0      | CVE-2023-34048                 | 9.8      | Critical | [8.0U1d](https://customerconnect.vmware.com/downloads/details?downloadGroup=VC80U1D&productId=1345&rPId=112378) | None        | [FAQ](https://via.vmw.com/vmsa-2023-0023-qna) |
| VMware vCenter Server                           | 7.0      | CVE-2023-34048, CVE-2023-34056 | 9.8, 4.3 | Critical | [7.0U3o](https://customerconnect.vmware.com/downloads/details?downloadGroup=VC70U3O&productId=974&rPId=110262)  | None        | [FAQ](https://via.vmw.com/vmsa-2023-0023-qna) |
| VMware Cloud Foundation (VMware vCenter Server) | 5.x, 4.x | CVE-2023-34048, CVE-2023-34056 | 9.8, 4.3 | Critical | [KB88287](https://kb.vmware.com/s/article/88287)                                                                | None        | [FAQ](https://via.vmw.com/vmsa-2023-0023-qna) |

## Additional References

- [VMSA-2023-0023 (vmware.com)](https://www.vmware.com/security/advisories/VMSA-2023-0023.html)
- [VMware Addresses Multiple Vulnerabilities in vCenter Server (CVE-2023-34048 & CVE-2023-34056) -- Qualys ThreatPROTECT](https://threatprotect.qualys.com/2023/10/25/vmware-addresses-multiple-vulnerabilities-in-vcenter-server-cve-2023-34048-cve-2023-34056/)
