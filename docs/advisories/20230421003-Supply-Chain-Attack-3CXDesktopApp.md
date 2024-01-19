# Supply Chain Attack Against 3CXDesktopApp - 20230421003

## Overview

CISA is aware of open-source reports describing a supply chain attack against 3CX software and their customers. According to the reports, 3CXDesktopApp — a voice and video conferencing app — was trojanized, potentially leading to multi-staged attacks against users employing the vulnerable app.

## What is the vulnerability?

CISA urges users and organizations to review the following reports for more information, and hunt for the listed indicators of compromise (IOCs) for potential malicious activity:

Vendor communications from 3CX:

3CX: [Security Incident Update Saturday 1 April 2023](https://www.3cx.com/blog/news/security-incident-updates/)

3CX: [Uninstalling the Desktop App from Windows and Mac](https://www.3cx.com/blog/news/uninstalling-the-desktop-app/)

3CX: [Security Alert for Electron Windows App | Desktop App](https://www.3cx.com/blog/news/desktopapp-security-alert/)

## What is vulnerable?

The vulnerability affects the following products:

- 3CX DesktopApp: <https://www.cvedetails.com/vulnerability-list/vendor_id-9320/3CX.html>

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

CISA has released a new Malware Analysis Report (MAR) on an infostealer known as [ICONICSTEALER](https://www.cisa.gov/news-events/analysis-reports/ar23-110a). This trojan has been identified as a variant of malware used in the supply chain attack against 3CX’s Desktop App.

CISA recommends users and administrators to review the following resources for more information, and hunt for the listed indicators of compromise (IOCs) for potential malicious activity:

- [MAR-10435108.r1.v1 – ICONICSTEALER](https://www.cisa.gov/news-events/analysis-reports/ar23-110a)

- [Supply Chain Attack Against 3CXDesktopApp](https://www.cisa.gov/news-events/alerts/2023/03/30/supply-chain-attack-against-3cxdesktopapp)

## Additional References

- <https://www.cvedetails.com/vulnerability-list/vendor_id-9320/3CX.html>
- <https://www.cisa.gov/news-events/alerts/2023/04/20/cisa-releases-malware-analysis-report-iconicstealer>
