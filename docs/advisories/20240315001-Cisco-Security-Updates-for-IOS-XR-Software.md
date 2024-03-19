# Cisco Security Updates for IOS XR Software - 20240315001

## Overview

Cisco released security updates for March 2024 to address vulnerabilities in its multiplae products. A cyber threat actor could exploit one of these vulnerabilities to take control of an affected device.

## What is vulnerable?

| Product(s) Affected  | Version  | CVE   | Severity | CVSS  | Dated|
| ------------ | -------| ------- | ------------- | -------- | ------- |
| **PPP over Ethernet (PPPoE) termination feature of Cisco IOS XR Software** in Cisco ASR 9000 Series with Lightspeed and Lightspeed-Plus based line cards: <br> A9K-16X100GE-TR; A99-16X100GE-X-SE; A99-32X100GE-TR; A9K-4HG-FLEX-TR; A9K-4HG-FLEX-SE; A99-4HG-FLEX-TR; A99-4HG-FLEX-SE; A9K-8HG-FLEX-TR; A9K-8HG-FLEX-SE; A9K-20HG-FLEX-TR; A9K-20HG-FLEX-SE; A99-32X100GE-X-TR; A99-32X100GE-X-SE; A99-10X400GE-X-TR; A99-10X400GE-X-SE | [7.8 and earlier<br> 7.9 <br> 7.10 <br> 7.11](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-pppma-JKWFgneW#vp) | [CVE-2024-20327](https://www.opencve.io/cve/CVE-2024-20327) | **High** | **7.4** |13 Mar, 2024|
| **SSH client feature of Cisco IOS XR Software** in following Cisco products: <br> 8000 Series Routers <br> IOS XRd Control Plane <br> IOS XRd vRouter <br> NCS 540 Series Routers that are running the NCS540L images <br> NCS 5700 Series Routers (NCS-57B1-5DSE-SYS, NCS-57B1-6D24-SYS, and NCS-57C1-48Q6-SYS)   | [7.3.2<br>7.4<br>7.5<br>7.6<br>7.7<br>7.8<br>7.9<br>7.10](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-ssh-privesc-eWDMKew3#vp) | [CVE-2024-20320](https://www.opencve.io/cve/CVE-2024-20320) | **High** | **7.8** |13 Mar, 2024|
| **Cisco IOS XR 64-bit Software with affected Layer 2 transport configuration enabled** in following Cisco products: <br> ASR 9000 Series Aggregation Services Routers that have a Lightspeed-based or Lightspeed-Plus-based line card installed <br> ASR 9902 Compact High-Performance Routers<br> ASR 9903 Compact High-Performance Routers<br> IOS XRd vRouters<br>IOS XRv 9000 Routers | [7.8 and earlier<br> 7.9 <br> 7.10](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-xrl2vpn-jesrU3fc#vp)   | [CVE-2024-20318](https://www.opencve.io/cve/CVE-2024-20318) | **High** | **7.4** |13 Mar, 2024|
| **Cisco IOS XR Software iPXE Boot Signature Bypass Vulnerability** | [version](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-ipxe-sigbypass-pymfyqgB#vp)   | [CVE-2023-20236](https://nvd.nist.gov/vuln/detail/CVE-2023-20236) | **High** | **7.8** | 14 Mar, 2024|
| **Cisco IOS XR Software Authenticated CLI Secure Copy Protocol and SFTP Denial of Service Vulnerability** | [version](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-scp-dos-kb6sUUHw#vp)   | [CVE-2024-20262](https://nvd.nist.gov/vuln/detail/CVE-2024-20262) | **Medium** | **6.5** |13 Mar, 2024|
| **Cisco IOS XR Software MPLS and Pseudowire Interfaces Access Control List Bypass Vulnerabilities** | [version](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-acl-bypass-RZU5NL3e#vp)  | [CVE-2024-20315](https://nvd.nist.gov/vuln/detail/CVE-2024-20315) <br>[CVE-2024-20322](https://nvd.nist.gov/vuln/detail/CVE-2024-20322) | **Medium** | **5.8** |13 Mar, 2024|
| **Cisco IOS XR Software DHCP Version 4 Server Denial of Service Vulnerability** | [version](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-dhcp-dos-3tgPKRdm#vp)  | [CVE-2024-20266](https://nvd.nist.gov/vuln/detail/CVE-2024-20266)  | **Medium** | **5.3** |13 Mar, 2024|
| **Cisco IOS XR Software SNMP Management Plane Protection ACL Bypass Vulnerability** | [version](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snmp-uhv6ZDeF#vp)  | [CVE-2024-20319](https://nvd.nist.gov/vuln/detail/CVE-2024-20319)  | **Medium** | **4.3** |13 Mar, 2024|


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):


- [Cisco security advisories - March 2024](https://sec.cloudapps.cisco.com/security/center/publicationListing.x)
