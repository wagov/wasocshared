# ServiceNow Public Exploitation - 20240726005

## Overview

The WA SOC has been made aware of a growing number of campaigns targeting instances of ServiceNow since the publication of a Proof-of-Concept (PoC) exploit. Threat actors are chaining together ServiceNow flaws using publicly available exploits for unpatched systems containing vulnerabilities that were addressed on July-10.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
| --- | --- | --- | --- | --- |
| Utah, Vancouver, Washinton | Multiple versions | - [CVE-2024-4879](https://nvd.nist.gov/vuln/detail/CVE-2024-4879) </br> - [CVE-2024-5178](https://nvd.nist.gov/vuln/detail/CVE-2024-5178) </br> - [CVE-2024-5217](https://nvd.nist.gov/vuln/detail/CVE-2024-5217) | - 9.3 </br> - 6.9 </br> - 9.2 | - **Critical** </br> - Medium  </br> - **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- CVE-2024-4879: <https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1645154>
- CVE-2024-5178: <https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1648312>
- CVE-2024-5217: <https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1648313>

## Additional References

- Securityonline blog post: <https://securityonline.info/gitlab-patches-six-security-flaws-urges-immediate-update/>
