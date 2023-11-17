# ISC Releases Security Advisories for BIND 9 - 20230926003

## Overview

The Internet Systems Consortium (ISC) has released security advisories to address vulnerabilities affecting ISC’s Berkeley Internet Name Domain (BIND) 9. A malicious cyber actor could exploit these vulnerabilities to cause denial-of-service conditions.

## What is the vulnerability?

[**CVE-2023-4236**](https://nvd.nist.gov/vuln/detail/CVE-2023-4236) - CVSS v3 Base Score: ***7.5***: A flaw in the networking code handling DNS-over-TLS queries may cause named to terminate unexpectedly due to an assertion failure. This happens when internal data structures are incorrectly reused under significant DNS-over-TLS query load.

[**CVE-2023-3341**](https://nvd.nist.gov/vuln/detail/CVE-2023-3341) - CVSS v3 Base Score: ***7.5***: The code that processes control channel messages sent to named calls certain functions recursively during packet parsing. Recursion depth is only limited by the maximum accepted packet size; depending on the environment, this may cause the packet-parsing code to run out of available stack memory, causing named to terminate unexpectedly.

## What is vulnerable?

The vulnerability affects the following products:

- BIND versions (including) **9.18.0 to and including 9.18.18**
- BIND Supported Preview Edition versions **9.18.11-S1 to and including 9.18.18-S1**

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- BIND CVE-2023-4236: <https://kb.isc.org/v1/docs/cve-2023-4236>
- BIND Supported Preview Edition CVE-2023-3341: <https://kb.isc.org/v1/docs/cve-2023-3341>
