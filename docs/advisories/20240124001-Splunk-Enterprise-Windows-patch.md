# Splunk Enterprise Patches High-Severity Vulnerability - 20240124001

## Overview

Splunk has released information about a High severity vulnerability affecting Splunk Enterprise for Windows.

## What is vulnerable?

| CVE ID                                                            | Product(s) Affected                                              | Summary                                                                                                                                                                                                                                               | Severity | CVSS |
| ----------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---- |
| [CVE-2024-23678](https://nvd.nist.gov/vuln/detail/CVE-2024-23678) | Splunk Enterprise for Windows **versions below** 9.0.8 and 9.1.3 | Splunk Enterprise for Windows does not correctly sanitize path input data. This results in the unsafe deserialization of untrusted data from a separate disk partition on the machine. This vulnerability only affects Splunk Enterprise for Windows. | **High** | 7.5  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- https://advisory.splunk.com/advisories/SVD-2024-0108

## Additional References

- SecurityWeek: https://www.securityweek.com/high-severity-vulnerability-patched-in-splunk-enterprise/
