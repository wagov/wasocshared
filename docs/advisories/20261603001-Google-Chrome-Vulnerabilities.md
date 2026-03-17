# Google Chrome Known Exploited Vulnerabilities - 20261603001

## Overview

Google Chrome has released a high security advisory addressing vulnerabilities that could allow remote code execution by an attacker affecting Google Chrome products. Google is aware of exploitation in the wild for one or more of the mentioned items.

## What is vulnerable?

| Product(s) Affected                                                                                         | Version(s)                                                                                                | CVE                                                                                                                                  | CVSS         | Severity       |
| ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------ | -------------- |
| Chromium-based Browsers <br> - Google Chrome <br> - Microsoft Edge <br> - Brave <br> - Opera <br> - Vivaldi | all versions prior to 146.0.7680.75/76 for Windows/Mac <br> all versions prior to 146.0.7680.75 for Linux | [CVE-2026-3909](https://nvd.nist.gov/vuln/detail/CVE-2026-3909) <br> [CVE-2026-3910](https://nvd.nist.gov/vuln/detail/CVE-2026-3910) | 8.8 <br> 8.8 | High <br> High |

Please Note: Google have noted CVE-2026-3909 has been mentioned within the security notes, however an official fix has not been released at the time of writing, and will be available in a future update.

## What has been observed?

CISA added one or more of the mentioned items in their [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog.
The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Google: <https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_12.html>

## Additional References

- CISA: <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>
