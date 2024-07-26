# AWS Security Advisory for Flaws in AWS Client VPN - 20240723001

## Overview

The WA SOC has been made aware of a security vulnerability detected in AWS Client VPN that could potentially allow malicious actors with access to a user’s device to execute arbitrary commands with elevated privileges, including escalating to root privilege. The vulnerabilities stem from buffer overflow issues, a common programming error that can be exploited to overwrite memory and gain unauthorized control over a system.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                               | CVE                                                                                                                                       | CVSS          | Severity          |
| ------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- |
| AWS Client VPN      | versions below 3.11.1 for Windows </br> versions below 3.9.2 for MacOS </br> versions below 3.12.1 Linux | [CVE-2024-30164](https://nvd.nist.gov/vuln/detail/CVE-2024-30164) </br> [CVE-2024-30165](https://nvd.nist.gov/vuln/detail/CVE-2024-30165) | 6.7 </br> 7.1 | Medium </br> High |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *1 month* (refer [Patch Management](../guidelines/patch-management.md)):

- AWS: <https://aws.amazon.com/security/security-bulletins/AWS-2024-008/>

## Reference

- SecurityOnline: <https://securityonline.info/aws-security-update-cve-2024-30164-and-cve-2024-30165-flaws-found-in-client-vpn/>
