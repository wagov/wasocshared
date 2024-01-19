# SAP High-Severity Vulnerabilities June 2023 - 20230620003

## Overview

SAP announced the release of eight new security notes as part of its June 2023 Security Patch Day, including two notes that address high-severity vulnerabilities.

## What is the vulnerability?

The issue can be exploited to gain user-level access to the UI5 Varian Management application and compromise confidentiality, integrity, and availability.

- [**CVE-2023-33991**](https://nvd.nist.gov/vuln/detail/CVE-2023-33991) - CVSS v3 Base Score: ***8.2***

## What is vulnerable?

SAP UI5 Variant Management - versions SAP_UI 750, SAP_UI 754, SAP_UI 755, SAP_UI 756, SAP_UI 757, UI_700 200, does not sufficiently encode user-controlled inputs on reading data from the server, resulting in Stored Cross-Site Scripting (Stored XSS) vulnerability.

After successful exploitation, an attacker with user level access can cause high impact on confidentiality, modify some information and can cause unavailability of the application at user level.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices: [SAP Security Patch Day](https://www.sap.com/documents/2022/02/fa865ea4-167e-0010-bca6-c68f7e60039b.html)

## Additional References:

- [SAP Security Patch Day – June 2023](https://www.sap.com/documents/2022/02/fa865ea4-167e-0010-bca6-c68f7e60039b.html)

- [SAP Patches High-Severity Vulnerabilities With June 2023 Security Updates](https://www.securityweek.com/sap-patches-high-severity-vulnerabilities-with-june-2023-security-updates/)
