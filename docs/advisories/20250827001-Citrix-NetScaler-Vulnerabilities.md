# Citrix NetScaler Critical Vulnerability - 20250827001

## Overview

Citrix has published a security bulletin relating to vulnerabilities discovered in NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway).

Exploitation of the vulnerability could result in denial-of-service and unintended control flow on gateway-configured NetScaler appliances

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                                                                                                                 | CVE                                                                  | CVSS | Severity     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ---- | ------------ |
| NetScaler ADC       | - 14.1 prior to 14.1-47.48 <br> - 13.1 prior to 13.1-59.22 <br>- 13.1-FIPS and NDcPP prior to 13.1-37.241-FIPS and NDcPP <br>-12.1-FIPS and NDcPP: prior to 12.1-55.330-FIPS and NDcPP<br> | [CVE-2025-7775](https://nvd.nist.gov/vuln/detail/CVE-2025-7775)      | 9.2  | **Critical** |
| NetScaler Gateway   | - 14.1 prior to 14.1-47.48 <br> - 13.1 prior to 13.1-59.22                                                                                                                                 | [CVE-2025-7775](https://nvd.nist.gov/vuln/detail/CVE-2025-7775) <br> | 9.2  | **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- CITRIX: <https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694938&articleTitle=NetScaler_ADC_and_NetScaler_Gateway_Security_Bulletin_for_CVE_2025_7775_CVE_2025_7776_and_CVE_2025_8424>

## Additional References

- CISA: <https://www.cisa.gov/news-events/alerts/2025/08/26/cisa-adds-one-known-exploited-vulnerability-catalog>
