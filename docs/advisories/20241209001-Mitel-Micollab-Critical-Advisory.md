# Mitel Micollab Critical Advisory - 20241209001

## Overview

A multiple vulnerabilities is currently existed in Mitel Micollab collaboration software. According to ASD's ACSC assessment, there is significant exposure to Mitel Micollab vulnerabilities in Australia and that any exploitation would have significant impact to Australian systems and networks.

## What is vulnerable?

| Product(s) Affected  | Version(s)| CVE #  | CVSS v4/v3 | Severity |
| -- | -- | -- | -- | -- |
| NuPoint Unified Messaging (NPM) within MiCollab| 9.8.0.33 | [**CVE-2024-35286**](https://nvd.nist.gov/vuln/detail/CVE-2024-35286) | 9.8 | Critical |
|NuPoint Unified Messaging (NPM) within MiCollab| 9.8 SP1 FP2 (9.8.1.201) and earlier|[**CVE-2024-41713**](https://nvd.nist.gov/vuln/detail/CVE-2024-41713)|9.8 by vendor|Critical|

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices **immediately** (refer [Patch Management](../guidelines/patch-management.md)):

- Mitel Micollab - CVE-2024-35286 - Security Bulletin: <https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-24-0014>
- Mitel Micollab - CVE-2024-41713 - Security Bulletin: <https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2024-0029>



## 3rd Party Article(s):

- ASD ACSC Advisory: [Critical security vulnerabilities affecting Mitel MiCollab version 9.8 SP1 FP2 (9.8.1.201) and earlier](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/critical-security-vulnerabilities-affecting-mitel-micollab-version-98-sp1-fp2-981201-and-earlier-versions)
