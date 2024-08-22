# Microsoft Discloses Multiple ZeroDay Vulnerabilities - 20240814001

## Overview

CISA has added six known exploited Microsoft product vulnerabilities to the Catalog based on the evidence of active exploitation. Additionally, there are multiple vulnerabilities included within the Monthy Update release with a severity rating of 'Critical'.

## What is vulnerable?

### Known Exploited items:

| Vulnerability                                                                              | CVE                                                               | CVSS | Severity |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ---- | -------- |
| Microsoft Project Remote Code Execution Vulnerability                                      | [CVE-2024-38189](https://nvd.nist.gov/vuln/detail/CVE-2024-38189) | 8.8  | High     |
| Microsoft Windows Scripting Engine Memory Corruption Vulnerability                         | [CVE-2024-38178](https://nvd.nist.gov/vuln/detail/CVE-2024-38178) | 7.5  | High     |
| Microsoft Windows SmartScreen Security Feature Bypass Vulnerability                        | [CVE-2024-38213](https://nvd.nist.gov/vuln/detail/CVE-2024-38213) | 6.5  | Medium   |
| Microsoft Windows Ancillary Function Driver for WinSock Privilege Escalation Vulnerability | [CVE-2024-38193](https://nvd.nist.gov/vuln/detail/CVE-2024-38193) | 7.8  | High     |
| Microsoft Windows Kernel Privilege Escalation Vulnerability                                | [CVE-2024-38106](https://nvd.nist.gov/vuln/detail/CVE-2024-38106) | 7.0  | High     |
| Microsoft Windows Power Dependency Coordinator Privilege Escalation Vulnerability          | [CVE-2024-38107](https://nvd.nist.gov/vuln/detail/CVE-2024-38107) | 7.8  | High     |

### Additional Critical items included in the Monthly Update release:

| Vulnerability                                | CVE                                                                                          | CVSS | Severity |
| -------------------------------------------- | -------------------------------------------------------------------------------------------- | ---- | -------- |
| Windows TCP/IP                               | [CVE-2024-38063](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38063) | 9.8  | Critical |
| Azure Stack                                  | [CVE-2024-38108](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38108) | 9.3  | Critical |
| Azure Health Bot                             | [CVE-2024-38109](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38109) | 9.1  | Critical |
| Reliable Multicast Transport Driver (RMCAST) | [CVE-2024-38140](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38140) | 9.8  | Critical |
| Windows Network Virtualization               | [CVE-2024-38159](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38159) | 9.1  | Critical |
| Windows Network Virtualization               | [CVE-2024-38160](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38160) | 9.1  | Critical |
| Line Printer Daemon Service (LPD)            | [CVE-2024-38199](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38199) | 9.8  | Critical |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft August 2024 Security Updates full release notes: <https://msrc.microsoft.com/update-guide/releaseNote/2024-Aug>

## Additional References

- CISA Catalog: <https://www.cisa.gov/news-events/alerts/2024/08/13/cisa-adds-six-known-exploited-vulnerabilities-catalog>
- Center for Internet Security advisory : <https://www.cisecurity.org/advisory/critical-patches-issued-for-microsoft-products-august-13-2024_2024-089>
- Bleeping Computer article: <https://www.bleepingcomputer.com/news/microsoft/microsoft-august-2024-patch-tuesday-fixes-9-zero-days-6-exploited/>

## Change Log:

- 2024-08-14: Article published.
- 2024-08-15: Included additional CVEs rated 'Critical'.
