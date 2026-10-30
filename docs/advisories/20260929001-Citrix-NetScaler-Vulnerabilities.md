# Citrix NetScaler Vulnerabilities - 20260929001

## Overview

Citrix has published a security bulletin relating to multiple vulnerabilities affecting NetScaler ADC, NetScaler Gateway, and NetScaler ADC FIPS. Successful exploitation could allow attackers to remotely execute arbitrary code, bypass security controls, hijack traffic, or cause denial-of-service conditions on affected NetScaler ADC and Gateway appliances.

## What is vulnerable?

| Product(s) Affected                 | Version(s)                                             | CVE             | CVSS | Severity     |
| ----------------------------------- | ------------------------------------------------------ | --------------- | ---- | ------------ |
| NetScaler ADC/NetScaler Gateway/FIPS| 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 | [CVE-2026-88771](https://nvd.nist.gov/vuln/detail/CVE-2026-88771)  | 9.5  | **Critical** |
| NetScaler ADC/NetScaler Gateway/FIPS| 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 |  [CVE-2026-88772](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)  | 9.5  | **Critical** |
| NetScaler ADC/NetScaler Gateway/FIPS | 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 |  [CVE-2026-88773](https://nvd.nist.gov/vuln/detail/CVE-2026-88773)  | 9.3  | **Critical** |
| NetScaler ADC/NetScaler Gateway/FIPS | 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 |  [CVE-2026-88774](https://nvd.nist.gov/vuln/detail/CVE-2026-88774)  | 7.0  | High         |
| NetScaler ADC/NetScaler Gateway/FIPS | 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 |  [CVE-2026-88775](https://nvd.nist.gov/vuln/detail/CVE-2026-88775)  | 8.8  | High         |
| NetScaler ADC/NetScaler Gateway/FIPS | 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 |  [CVE-2026-88776](https://nvd.nist.gov/vuln/detail/CVE-2026-88776)  | 8.8  | High         |
| NetScaler ADC/NetScaler Gateway/FIPS | 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 |  [CVE-2026-88777](https://nvd.nist.gov/vuln/detail/CVE-2026-88777)  | 8.8  | High         |
| NetScaler ADC/NetScaler Gateway/FIPS | 14.1 prior to 14.1-73.37 <br> 13.1 prior to 13.1-64.23 <br> prior 14.1-73.37 FIPS <br> NDcPP prior 13.1-37.279 |  [CVE-2026-88778](https://nvd.nist.gov/vuln/detail/CVE-2026-88778)  | 8.8  | High         |



## What has been observed?

CISA has added one or more of the mentioned items to their [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Citrix: <https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696939>

### Additional Resources

- ASD: https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products