# ManageEngine Critical Vunerabilities - 20260924001

## Overview

The WASOC has been made aware of an exposed Google Cloud service-account private key in the Applications Manager installer and a remote code execution vulnerability in the GINA client as well as the OpManager Notification Profile module.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| ManageEngine Applications Manager      | Versions 182200 and below    | [CVE-2026-86708](https://nvd.nist.gov/vuln/detail/CVE-2026-86708)                                   | 10           | **Critical**                                                   |
| ManageEngine ADSelfService Plus        | Versions 7000 and below      | [CVE-2026-74849](https://nvd.nist.gov/vuln/detail/CVE-2026-74849)                                   | 9.8          | **Critical**                                                   |
| ManageEngine OpManager MSP             | Versions 12.8.709 and below  | [CVE-2026-19599](https://nvd.nist.gov/vuln/detail/CVE-2026-19599)                                   | 9.9          | **Critical**                                                   |
## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Zohocorp: <https://www.manageengine.com/products/applications_manager/security-updates/security-updates-cve-2026-86708.html>
- Zohocorp: <https://www.manageengine.com/products/self-service-password/advisory/CVE-2026-74849.html>
- Zohocorp: <https://www.manageengine.com/itom/advisory/cve-2026-19599.html>

