# Broadcom VMware Critical Update - 20240919002

## Overview

Broadcom released security updates to address a critical vulnerability in VMware vCenter Server that could lead to remote code execution.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE # | CVSS v4/v3 | Severity |
|---------------------|------------|-------|------------|----------|
|vCenter Server       | 8.0 < U3b <br> 7.0 < U3s | CVE-2024-38812 <br> CVE-2024-38813 | 9.8 <br> 7.5 | **Critical** <br> **High**|
|VMware Cloud Foundation| 5.x < 8.0 U3b <br> 4.x < 7.0 U3s | CVE-2024-38812 <br> CVE-2024-38813 | 9.8 <br> 7.5 | **Critical** <br> **High** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hrs...* (refer [Patch Management](../guidelines/patch-management.md)):

- Broadcom Advisory: <https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24968>

## Additional References

- SecurityAffairs article: <https://securityaffairs.com/168536/security/vmware-vcenter-server-cve-2024-38812.html>
