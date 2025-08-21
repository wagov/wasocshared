# Commvault Bug Chain Vulnerabilities - 20250821001

## Overview

The WASOC has observed reports of published working proof-of-concept exploits for unauthenticated remote code execution bug chains affecting Commvault products for Linux and Windows. If exploited, these vulnerabilities allow attackers to execute API calls without requiring user credentials, conduct remote code executions, exploit default credentials to gain administrator control, and perform unauthorised file system access through a path traversal issue.

Commvault has released patches addressing associated vulnerabilities.

## What is vulnerable?

| Products                        | Versions Affected                                         | CVE                                                                                                                                                                                                                                                                                       | CVSS                              | Severity                                    |
| ------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------- |
| Commvault for Linux and Windows | 11.36.x prior to 11.36.60 <br> 11.32.x prior to 11.32.102 | [CVE-2025-57790](https://nvd.nist.gov/vuln/detail/CVE-2025-57790) </br> [CVE-2025-57791](https://nvd.nist.gov/vuln/detail/CVE-2025-57791) </br> [CVE-2025-57788](https://nvd.nist.gov/vuln/detail/CVE-2025-57788) </br> [CVE-2025-57789](https://nvd.nist.gov/vuln/detail/CVE-2025-57789) | 8.7 </br> 6.9 </br> 6.9 </br> 5.3 | High </br> Medium </br> Medium </br> Medium |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Commvault advisories: <https://documentation.commvault.com/securityadvisories/>

### Additional Resources

- The Register: <https://www.theregister.com/2025/08/20/commvault_bug_chains_patched/>
