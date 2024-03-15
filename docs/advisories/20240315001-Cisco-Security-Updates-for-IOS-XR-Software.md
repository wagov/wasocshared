# Cisco Security Updates for IOS XR Software - 20240315001

## Overview

Cisco released security updates to address vulnerabilities in Cisco IOS XR software. A cyber threat actor could exploit one of these vulnerabilities to take control of an affected device.

## What is vulnerable?

| Product(s) Affected                                                                                                                                                                                                                                                                                                                                                                                                                      | Version                                                 | CVE                                                         | Severity | CVSS    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------- | -------- | ------- |
| **PPP over Ethernet (PPPoE) termination feature of Cisco IOS XR Software** in Cisco ASR 9000 Series with Lightspeed and Lightspeed-Plus based line cards: <br> A9K-16X100GE-TR; A99-16X100GE-X-SE; A99-32X100GE-TR; A9K-4HG-FLEX-TR; A9K-4HG-FLEX-SE; A99-4HG-FLEX-TR; A99-4HG-FLEX-SE; A9K-8HG-FLEX-TR; A9K-8HG-FLEX-SE; A9K-20HG-FLEX-TR; A9K-20HG-FLEX-SE; A99-32X100GE-X-TR; A99-32X100GE-X-SE; A99-10X400GE-X-TR; A99-10X400GE-X-SE | 7.8 and earlier<br> 7.9 <br> 7.10 <br> 7.11             | [CVE-2024-20327](https://www.opencve.io/cve/CVE-2024-20327) | **High** | **7.4** |
| **SSH client feature of Cisco IOS XR Software** in following Cisco products: <br> 8000 Series Routers <br> IOS XRd Control Plane <br> IOS XRd vRouter <br> NCS 540 Series Routers that are running the NCS540L images <br> NCS 5700 Series Routers (NCS-57B1-5DSE-SYS, NCS-57B1-6D24-SYS, and NCS-57C1-48Q6-SYS)                                                                                                                         | 7.3.2<br>7.4<br>7.5<br>7.6<br>7.7<br>7.8<br>7.9<br>7.10 | [CVE-2024-20320](https://www.opencve.io/cve/CVE-2024-20320) | **High** | **7.8** |
| **Cisco IOS XR 64-bit Software with affected Layer 2 transport configuration enabled** in following Cisco products: <br> ASR 9000 Series Aggregation Services Routers that have a Lightspeed-based or Lightspeed-Plus-based line card installed <br> ASR 9902 Compact High-Performance Routers<br> ASR 9903 Compact High-Performance Routers<br> IOS XRd vRouters<br>IOS XRv 9000 Routers                                                | 7.8 and earlier<br> 7.9 <br> 7.10                       | [CVE-2024-20318](https://www.opencve.io/cve/CVE-2024-20318) | **High** | **7.4** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [CISA Alerts](https://www.cisa.gov/news-events/alerts/2024/03/14/cisco-releases-security-updates-ios-xr-software)
- [Cisco IOS XR Software for ASR 9000 Series Aggregation Services Routers PPPoE Denial of Service Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-pppma-JKWFgneW)
- [Cisco IOS XR Software SSH Privilege Escalation Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-ssh-privesc-eWDMKew3)
- [Cisco IOS XR Software Layer 2 Services Denial of Service Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-xrl2vpn-jesrU3fc)

## Additional References

- [Cisco security advisories](https://sec.cloudapps.cisco.com/security/center/publicationListing.x)
