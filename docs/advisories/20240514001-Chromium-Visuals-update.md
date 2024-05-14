# Chromium Visuals Updates - 20240514001

## Overview

Patching has been released for a High severity vulnerability in Google Chromium Visuals, for which an exploit exists in the wild.


## What is vulnerable?

| CVE           | Severity | CVSS | Product(s) Affected                                                      | Summary                                                                                                                                      | Dated       |
| ------------- | -------- | ---- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| CVE-2024-4671 | **High** | 8.8  | **versions before** 124.0.6367.201/.202 for Mac and Windows and 124.0.6367.201 for Linux | Use-after-free vulnerability that allows a remote attacker to exploit heap corruption via a crafted HTML page. | 13 May 2024 |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://chromereleases.googleblog.com/2024/05/stable-channel-update-for-desktop_9.html


## Additional References

- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.zdnet.com/article/update-your-chrome-browser-asap-google-has-confirmed-a-zero-day-exploited-in-the-wild/
- Note that NVD entry has not yet been created at time of writing this advisory - https://nvd.nist.gov/vuln/detail/CVE-2024-4671
