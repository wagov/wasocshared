# Mirai Variant Targeting Multiple IoT Devices  - 20230531001

## Overview

The WA SOC has observed [reports by security researchers](https://unit42.paloaltonetworks.com/mirai-variant-iz1h9/) of an active Mirai variant named IZ1H9 targetting devices running Linux.

Once a device has been compromised, it becomes part of a botnet that is used for attacks such as Distributed Denial of Service (DDoS) attacks.

## What is the vulnerability?

The Mirai variant targets the following vulnerabilities:

- [**CVE-2023-27076**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27076) - CVSS v3 Base Score: ***9.8***
- [**CVE-2023-26801**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26801) - CVSS v3 Base Score: ***9.8***
- [**CVE-2023-26802**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26802) - CVSS v3 Base Score: ***9.8***
- [**Zyxel remote code execution**](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-remote-code-execution-and-denial-of-service-vulnerabilities-of-cpe)

## What is vulnerable?

The vulnerabilities affect the following products:

- Tenda G103 with firmware version 1.0.0.5 - [CVE-2023-27076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27076)
- Multiple LB-LINK devices and firmware versions - Please see [CVE-2023-26801](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26801) for more details
- DCN (Digital China Networks) DCBI-Netlog-LAB v1.0 - [CVE-2023-26802](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26802)
- Multiple Zyxel CPE models and firmware versions - Please see the [Zyxel information page](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-remote-code-execution-and-denial-of-service-vulnerabilities-of-cpe) for more details

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices and reviewing the [research published by the Unit 42 researchers](https://unit42.paloaltonetworks.com/mirai-variant-iz1h9/) for indicators of compromise (IOCs) if relevant to your organisation.
