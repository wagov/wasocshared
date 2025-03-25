# Next.js Critical Vulnerability - 20250325002

## Overview

A critical security flaw has been disclosed in the Next.js React framework that could be potentially exploited to bypass authorization checks under certain conditions.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                                                          | CVE                                                                                                                  | CVSS | Severity |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---- | -------- |
| Vercel Next.js      | 15.x prior to 15.2.3 <br> 14.x prior to 14.2.25 <br> 13.x prior to 13.5.9 <br> 12.x prior to 12.3.5 <br> 11.x requires a workaround | [ CVE-2025-29927](https://nvd.nist.gov/vuln/detail/CVE-2025-29927 "https://nvd.nist.gov/vuln/detail/CVE-2025-29927") | 9.1  | Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Vercel Github: <https://github.com/vercel/next.js/security/advisories/GHSA-f82v-jwr5-mffw>

## Additional References

- TheHackerNews: <https://thehackernews.com/2025/03/critical-nextjs-vulnerability-allows.html>
