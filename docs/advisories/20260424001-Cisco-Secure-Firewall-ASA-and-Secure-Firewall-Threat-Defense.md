# Continued Evolution of Persistence Against Cisco Secure Firewall ASA and Secure Firewall Threat Defense - 20260424001

## Overview

The WASOC has been made aware of new information on a previously unknown persistence mechanism that is preserved across even when upgrading on Cisco Firepower and Secure Firewall products running ASA or FTD software.

CISA and NCSC have identified new malware deployed as part of the historical exploitation of [CVE-2025-20333](https://www.cve.org/CVERecord?id=CVE-2025-20333) and [CVE-2025-20362](https://www.cve.org/CVERecord?id=CVE-2025-20362), affecting devices running Cisco Secure ASA Software or Cisco Secure FTD Software.

Previous WASOC Advisory: <https://soc.cyber.wa.gov.au/advisories/20250926001-Cisco-ASA-Active-Exploitation/>

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- CISCO: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-persist-CISAED25-03>

## Additional References

- CISA: <https://www.cisa.gov/news-events/analysis-reports/ar26-113a>
- WASOC: <https://soc.cyber.wa.gov.au/advisories/20250926001-Cisco-ASA-Active-Exploitation/>
