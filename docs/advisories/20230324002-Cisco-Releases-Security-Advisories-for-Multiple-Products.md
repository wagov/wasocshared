# Cisco Releases Security Advisories for Multiple Products - 20230324002

## Overview

Cisco has released security advisories for vulnerabilities affecting multiple Cisco products.

These vulnerabilities could allow a remote cyber threat actor to exploit and take control of an affected system.

## What is the vulnerability?

[**CVE-2023-20027**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20027) - Cisco IOS XE Software Virtual Fragmentation Reassembly Denial of Service Vulnerability

[**CVE-2023-20065**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20065) - Cisco IOS XE Software IOx Application Hosting Environment Privilege Escalation Vulnerability

[**CVE-2023-20035**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20035) - Cisco IOS XE SD-WAN Software Command Injection Vulnerability

[**CVE-2023-20072**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20072) - Cisco IOS XE Software Fragmented Tunnel Protocol Packet Denial of Service Vulnerability

[**CVE-2023-20080**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20080) - Cisco IOS and IOS XE Software IPv6 DHCP (DHCPv6) Relay and Server Denial of Service Vulnerability

[**CVE-2023-20067**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20067) - Cisco IOS XE Software for Wireless LAN Controllers HTTP Client Profiling Denial of Service Vulnerability

[**CVE-2023-20055**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20055) - Cisco DNA Center Privilege Escalation Vulnerability

[**CVE-2023-20082**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20082) - Cisco IOS XE Software for Cisco Catalyst 9300 Series Switches Secure Boot Bypass Vulnerability

[**CVE-2023-20112**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20112) - Cisco Access Point Software Association Request Denial of Service Vulnerability

## What is vulnerable?

The vulnerability affects the following products:

| No  | Vulnerability                                                                                            | Affected Products                                                                                                                                                                                                                                                                                    | Additional Info                                                                                                           |
| --- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1   | Cisco IOS XE Software Virtual Fragmentation Reassembly Denial of Service Vulnerability                   | - 1000 Series Integrated Services Routers<br>- 4000 Series Integrated Services Routers<br>- Catalyst 8000V Edge Software Routers<br>- Catalyst 8200 Series Edge Platforms<br>- Catalyst 8300 Series Edge Platforms<br>- Catalyst 8500L Series Edge Platforms<br>- Cloud Services Router 1000V Series | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ipv4-vfr-dos-CXxtFacb)      |
| 2   | Cisco IOS XE Software IOx Application Hosting Environment Privilege Escalation Vulnerability             | This vulnerability affects Cisco products if they are running a vulnerable release of Cisco IOS XE Software                                                                                                                                                                                          | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iox-priv-escalate-Xg8zkyPk) |
| 3   | Cisco IOS XE SD-WAN Software Command Injection Vulnerability                                             | - 1000 Series Integrated Services Routers (ISRs)<br>- 4000 Series ISRs<br>- ASR 1000 Series Aggregation Services Routers<br>- Catalyst 8000 Edge Platforms Family<br>- Cloud Services Router (CSR) 1000V Series                                                                                      | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ios-xe-sdwan-VQAhEjYw)      |
| 4   | Cisco IOS XE Software Fragmented Tunnel Protocol Packet Denial of Service Vulnerability                  | This vulnerability affects Cisco products if they are running Cisco IOS XE Software releases 17.9.1, 17.9.1a, or 17.9.1w and have a tunnel interface configured.                                                                                                                                     | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ios-gre-crash-p6nE5Sq5)     |
| 5   | Cisco IOS and IOS XE Software IPv6 DHCP (DHCPv6) Relay and Server Denial of Service Vulnerability        | This vulnerability affects Cisco devices if they are running a vulnerable release of Cisco IOS or IOS XE Software and have IPv6 and the DHCPv6 relay or server feature enabled                                                                                                                       | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ios-dhcpv6-dos-44cMvdDK)    |
| 6   | Cisco IOS XE Software for Wireless LAN Controllers HTTP Client Profiling Denial of Service Vulnerability | - Catalyst 9800 Embedded Wireless Controllers for Catalyst 9300, 9400, and 9500 Series Switches<br>- Catalyst 9800 Series Wireless Controllers<br>- Catalyst 9800-CL Wireless Controllers for Cloud<br>- Embedded Wireless Controllers on Catalyst Access Points                                     | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ewlc-dos-wFujBHKw)          |
| 7   | Cisco DNA Center Privilege Escalation Vulnerability                                                      | This vulnerability affects Cisco DNA Center in the default configuration.                                                                                                                                                                                                                            | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-dnac-privesc-QFXe74RS)      |
| 8   | Cisco IOS XE Software for Cisco Catalyst 9300 Series Switches Secure Boot Bypass Vulnerability           | This vulnerability affects Cisco Catalyst 9300 Series Switches if they are running Cisco IOS XE Software with a release of Cisco IOS XE ROM Monitor (ROMMON) that is earlier than Release 17.3.7r, Release 17.6.5r, or Release 17.8.1r.                                                              | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-c9300-spi-ace-yejYgnNQ)     |
| 9   | Cisco Access Point Software Association Request Denial of Service Vulnerability                          | - Business 150 APs and 151 Mesh Extenders<br>- Catalyst 9100 APs                                                                                                                                                                                                                                     | [Link](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ap-assoc-dos-D2SunWK2)      |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected products.
