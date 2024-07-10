# Splunk RCE Advisory - 20240705001

## Overview

The WA SOC has been made aware of a vulnerability in multiple versions of Splunk Enterprise on Windows. Authenticated users could execute a specially crafted query that they could then use to serialise untrusted data. The attacker could use the query to execute arbitrary code.

## What is vulnerable?

| Products Affected                                                                                                      | CVE                                                               | CVSS | Severity |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| Splunk Enterprise: <br>Version 9.2 **before** 9.2.2<br> Version 9.1 **before** 9.1.5<br> Version 9.0 **before** 9.0.10 | [CVE-2024-36984](https://nvd.nist.gov/vuln/detail/CVE-2024-36984) | 8.8  | High     |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Remote Code Execution through Serialized Session Payload in Splunk Enterprise on Windows
    ](https://advisory.splunk.com/advisories/SVD-2024-0704)

## Additional References

- Splunk Security Content: <https://research.splunk.com/application/1cf58ae1-9177-40b8-a26c-8966040f11ae/>
- Security Affairs: <https://securityaffairs.com/165204/security/splunk-enterprise-and-cloud-platform-flaws.html>
