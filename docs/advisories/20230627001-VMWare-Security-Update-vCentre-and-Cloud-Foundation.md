# VMware Releases Security Updates for for vCenter Server and Cloud Foundation - 20230627001

## Overview

VMware has released a security update to address multiple memory corruption vulnerabilities in vCenter Server and Cloud Foundation. A cyber threat actor could exploit these vulnerabilities to take control of an affected system.

## What is the vulnerability?

* [**CVE-2023-20892**](https://nvd.nist.gov/vuln/detail/CVE-2023-20892) - CVSS v3 Base Score: ***8.1*** - VMware vCentre Server heap overflow vulnerability.
* [**CVE-2023-20893**](https://nvd.nist.gov/vuln/detail/CVE-2023-20893) - CVSS v3 Base Score: ***8.1*** - VMware vCenter Server contains a use-after-free vulnerability.
* [**CVE-2023-20894**](https://nvd.nist.gov/vuln/detail/CVE-2023-20894) - CVSS v3 Base Score: ***8.1*** - VMware vCenter Server out-of-bounds write vulnerability.
* [**CVE-2023-20895**](https://nvd.nist.gov/vuln/detail/CVE-2023-20895) - CVSS v3 Base Score: ***8.1*** - VMware vCenter Server memory corruption vulnerability.
* [**CVE-2023-20896**](https://nvd.nist.gov/vuln/detail/CVE-2023-20896) - CVSS v3 Base Score: ***5.9*** - VMware vCenter Server out-of-bounds read vulnerability.
* [**CVE-2023-20867**](https://nvd.nist.gov/vuln/detail/CVE-2023-20867) - CVSS v3 Base Score: ***3.9*** - VMware Tools host-to-guest confidentiality and integrity vulnerability.

## What is vulnerable?

The vulnerability affects VMware vCenter Server (vCenter Server), VMware Cloud Foundation (Cloud Foundation) and VMware Tools

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing

## Recommendation

The WA SOC recommends administrators apply the updates as per vendor instructions to all affected devices: 
* [**VMSA-2023-0013**](https://www.vmware.com/security/advisories/VMSA-2023-0013.html) (Only CVE-2023-20867)
* [**VMSA-2023-0014**](https://www.vmware.com/security/advisories/VMSA-2023-0014.html) (All other CVE's mentioned)

## Additional References

- [**CISA**](https://www.cisa.gov/news-events/alerts/2023/06/23/vmware-releases-security-update-vcenter-server-and-cloud-foundations)
