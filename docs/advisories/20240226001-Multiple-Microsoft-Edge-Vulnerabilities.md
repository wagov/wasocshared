# Microsoft Edge (Chromium-based) Spoofing and Information Disclosure Vulnerabilities - 20240226001

## Overview

Microsoft has released security advisories relating to multiple vulnerabilities present in select Microsoft Edge versions. An attacker who successfully exploited these vulnerabilities could:

- Cover and spoof elements of the UI.
- Lead to a browser sandbox escape.

## What is vulnerable?

| Product(s) Affected | Summary | Severity     | CVSS |
| ------------------- | ------- | ------------ | ---- |
| **versions before** <br> 122.0.2365.52 |  [CVE-2024-26188](https://nvd.nist.gov/vuln/detail/CVE-2024-26188)       | **Low** | 4.3  |
| **versions before** <br> 122.0.2365.52 |  [CVE-2024-26192](https://nvd.nist.gov/vuln/detail/CVE-2024-26192)   | **High** | 8.2 |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-26188
- https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-26192