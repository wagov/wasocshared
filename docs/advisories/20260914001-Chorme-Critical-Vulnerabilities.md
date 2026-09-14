# Chrome Multiple Critical Vulnerabilities - 20260914001

## Overview

The WASOC has been made aware of a Google Chrome Stable Channel update addressing multiple security vulnerabilities. Successful exploitation of either vulnerability may compromise the confidentiality, integrity, or availability of affected systems.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Google Chrome (DevTools)      | prior to 152.0.7977.82/.83 and 152.0.7977.82   | [CVE-2026-85042](https://nvd.nist.gov/vuln/detail/cve-2026-85042)                                                                        | 9.6          | **Critical**                                   |
| Google Chrome (Network)        |  prior to 152.0.7977.82/.83 and 152.0.7977.82  | [CVE-2026-85043](https://nvd.nist.gov/vuln/detail/cve-2026-85043)  | 9.1 | **Critical**

## What has been observed?

 CISA has added one of more of the mentioned items to their [Known Exploited Vulnerability](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalogue. The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Google: <https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html>

## Additional References

- Redhat: <https://access.redhat.com/security/cve/cve-2026-85043>
