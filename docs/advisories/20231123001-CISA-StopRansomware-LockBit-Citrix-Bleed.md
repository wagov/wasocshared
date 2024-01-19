# LockBit 3.0 affiliates exploiting Citrix Bleed added to CISA #StopRansomware Catalog - 20231123001

## Overview

The Cybersecurity and Infrastructure Security Agency (CISA), Federal Bureau of Investigation (FBI), Multi-State Information Sharing & Analysis Center (MS-ISAC), and Australian Signals Directorate’s Australian Cyber Security Center (ASD’s ACSC) released a joint Advisory to disseminate IOCs, TTPs, and detection methods associated with LockBit 3.0 ransomware exploiting Citrix Bleed (CVE-2023-4966), affecting Citrix NetScaler web application delivery control (ADC) and NetScaler Gateway appliances.

## What is the vulnerability?

[**CVE-2023-4966**](https://nvd.nist.gov/vuln/detail/CVE-2023-4966) - CVSS v3 Base Score: ***9.4***

## What is vulnerable?

The vulnerability exists in the following products:

- NetScaler ADC and NetScaler Gateway 14.1 before 14.1-8.50
- NetScaler ADC and NetScaler Gateway 13.1 before 13.1-49.15
- NetScaler ADC and NetScaler Gateway 13.0 before 13.0-92.19
- NetScaler ADC 13.1-FIPS before 13.1-37.164
- NetScaler ADC 12.1-FIPS before 12.1-55.300
- NetScaler ADC 12.1-NDcPP before 12.1-55.300

## What has been observed?

CISA added this vulnerabilty in their [#StopRansomware](https://www.cisa.gov/news-events/alerts/2023/11/21/cisa-fbi-ms-isac-and-asds-acsc-release-advisory-lockbit-affiliates-exploiting-citrix-bleed) catalog on *November 21, 2023*. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- [**Citrix Knowledge Center**](https://support.citrix.com/article/CTX579459/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve20234966-and-cve20234967)

### Additional Resources

**WASOC Advisories:**

- [**Citrix Bleed ACT NOW - Ensure Citrix ADC & Netscaler have mitigations applied OR are taken offline - 20231115001**](https://soc.cyber.wa.gov.au/advisories/20231115001-Citrix-Bleed)
- [**Mass exploitation of CitrixBleed vulnerability - 20231102002**](https://soc.cyber.wa.gov.au/advisories/20231102002-Mass-exploitation-of-CitrixBleed-vulnerability/)
- [**Citrix Releases Security Updates for Multiple Products - 20231012003**](https://soc.cyber.wa.gov.au/advisories/20231012003-Citrix-Releases-Security-Updates-for-Multiple-Products/)
