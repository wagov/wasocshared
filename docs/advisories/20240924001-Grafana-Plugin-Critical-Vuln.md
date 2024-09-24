# Grafana Plugin SDK Information Leakage Vulnerabilty - 20240924001

## Overview

The WA SOC has been made aware of a vulnerability affecting Grafana.

The Grafana plugin SDK bundles build metadata into the binaries it compiles; this metadata includes the repository URI for the plugin being built, as retrieved by running `git remote get-url origin`. If credentials are included in the repository URI (for instance, to allow for fetching of private dependencies), the final binary will contain the full URI, including said credentials.

## What is vulnerable?

| Product(s) Affected | Version(s)             | CVE                                                            | CVSS | Severity     |
| ------------------- | ---------------------- | -------------------------------------------------------------- | ---- | ------------ |
| Grafana Plugin SDK  | all versions <= 0.249.0 | [CVE-2024-8986](https://nvd.nist.gov/vuln/detail/CVE-2024-8986) | 9.1 | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://grafana.com/security/security-advisories/cve-2024-8986/>

## Additional References

- Security Online: <https://securityonline.info/cve-2024-8986-cvss-9-1-critical-grafana-plugin-sdk-flaw-exposes-sensitive-information/>
