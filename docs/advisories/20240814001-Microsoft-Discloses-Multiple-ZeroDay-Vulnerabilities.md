# Microsoft Discloses Multiple ZeroDay Vulnerabilities - 20240814001

## Overview
CISA has added six known exploited Microsoft product vulnerabilities to the Catalog based on the evidence of active exploitation.

## What is vulnerable?

| Vulnerability       | CVE       | CVSS          | Severity             |
| ------------------- | --------- | ------------- | -------------------- |
| Microsoft Project Remote Code Execution Vulnerability | [CVE-2024-38189](https://nvd.nist.gov/vuln/detail/CVE-2024-38189) | 8.8 | High |
| Microsoft Windows Scripting Engine Memory Corruption Vulnerability | [CVE-2024-38178](https://nvd.nist.gov/vuln/detail/CVE-2024-38178) | 7.5 | High |
| Microsoft Windows SmartScreen Security Feature Bypass Vulnerability | [CVE-2024-38213](https://nvd.nist.gov/vuln/detail/CVE-2024-38213) | 6.5 | Medium |
| Microsoft Windows Ancillary Function Driver for WinSock Privilege Escalation Vulnerability | [CVE-2024-38193](https://nvd.nist.gov/vuln/detail/CVE-2024-38193) | 7.8 | High |
| Microsoft Windows Kernel Privilege Escalation Vulnerability | [CVE-2024-38106](https://nvd.nist.gov/vuln/detail/CVE-2024-38106) | 7.0 | High |
| Microsoft Windows Power Dependency Coordinator Privilege Escalation Vulnerability | [CVE-2024-38107](https://nvd.nist.gov/vuln/detail/CVE-2024-38107) | 7.8 | High |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):


| Vulnerability     | CVE       | Recommended action |  MSRC Security Updates |
| ----------------- | --------- | --------------- | ---------------------- |
| Microsoft Project Remote Code Execution Vulnerability | [CVE-2024-38189](https://nvd.nist.gov/vuln/detail/CVE-2024-38189) | Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable. | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38189 |
| Microsoft Windows Scripting Engine Memory Corruption Vulnerability | [CVE-2024-38178](https://nvd.nist.gov/vuln/detail/CVE-2024-38178) | Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable. |https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38178 |
| Microsoft Windows SmartScreen Security Feature Bypass Vulnerability | [CVE-2024-38213](https://nvd.nist.gov/vuln/detail/CVE-2024-38213) | Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable. | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38213 |
| Microsoft Windows Ancillary Function Driver for WinSock Privilege Escalation Vulnerability | [CVE-2024-38193](https://nvd.nist.gov/vuln/detail/CVE-2024-38193) | 	Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable. | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38193 |
| Microsoft Windows Kernel Privilege Escalation Vulnerability | [CVE-2024-38106](https://nvd.nist.gov/vuln/detail/CVE-2024-38106) |	Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable. | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38106 |
| Microsoft Windows Power Dependency Coordinator Privilege Escalation Vulnerability | [CVE-2024-38107](https://nvd.nist.gov/vuln/detail/CVE-2024-38107) | Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable. | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38107 |

## Additional References

- CISA Catalog: https://www.cisa.gov/news-events/alerts/2024/08/13/cisa-adds-six-known-exploited-vulnerabilities-catalog
- Center for Internet Security advisory : https://www.cisecurity.org/advisory/critical-patches-issued-for-microsoft-products-august-13-2024_2024-089
- Bleeping Computer article: https://www.bleepingcomputer.com/news/microsoft/microsoft-august-2024-patch-tuesday-fixes-9-zero-days-6-exploited/