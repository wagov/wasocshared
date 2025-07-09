# SAP New Critical Vulnerabilities Updates - 202509004

## Overview

SAP has released their monthly Security Patch Notes that include six new **Critical** severity vulnerabilities. Successful exploitations could allow a remote unauthenticated attack to send malicious payload request in a specific encoding format. The servlet will then decode this malicious request which will result in deserialisation of data in the application leading to execution of arbitrary OS command on target as SAP Administrator.


## What is vulnerable?

| Product(s) Affected                                         | Version(s)                                | CVE                                                               | CVSS | Severity     |
| ----------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| SAP Supplier Relationship Management (Live Auction Cockpit) | SRM_SERVER 7.14                           | [CVE-2025-30012](https://www.cve.org/CVERecord?id=CVE-2025-30012) | 10   | **Critical** |
| SAP S/4HANA and SAP SCM (Characteristic Propagation) | SCMAPO 713, 714 <br>S4CORE 102, 103, 104 <br>S4COREOP 105, 106, 107, 108 <br>SCM 700, 701, 702, 712  | [CVE-2025-42967](https://www.cve.org/CVERecord?id=CVE-2025-42967) | 9.9  | **Critical** |
| SAP NetWeaver Enterprise Portal Federated Portal Network    | EP-RUNTIME 7.50                           | [CVE-2025-42980](https://www.cve.org/CVERecord?id=CVE-2025-42980) | 9.1  | **Critical** |
| SAP NetWeaver Application Server for Java (Log Viewer)      | LMNWABASICAPPS 7.50                       | [CVE-2025-42963](https://www.cve.org/CVERecord?id=CVE-2025-42963) | 9.1  | **Critical** |
| SAP NetWeaver Enterprise Portal Administration              | EP-RUNTIME 7.50                           | [CVE-2025-42964](https://www.cve.org/CVERecord?id=CVE-2025-42964) | 9.1  | **Critical** |
| SAP NetWeaver (XML Data Archiving Service)                  | J2EE-APPS 7.50                            | [CVE-2025-42966](https://www.cve.org/CVERecord?id=CVE-2025-42966) | 9.1  | **Critical** |


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected products within the expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- SAP Security Patch Day Bulletin - July 2025: <https://support.sap.com/en/my-support/knowledge-base/security-notes-news/july-2025.html>