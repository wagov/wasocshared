# Apache HTTP Server Triple Vulnerabilities - 20240405003

## Overview

Apache has released a new version (v2.4.59) which has addressed multiple vulnerabilites found within previous versions. A threat actor could exploit these vulnerabilities to cause HTTP splitting or memory exhaustion. 

## What is vulnerable?

| CVE    | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ------ | ------------ | ---- | ------------------- | ------- | ----- |
| [CVE-2024-27316](https://nvd.nist.gov/vuln/detail/CVE-2024-27316) | **High** | 7.5  | **versions <=2.4.58**  |    HTTP/2 incoming headers exceeding the limit are temporarily buffered in nghttp2 in order to generate an informative HTTP 413 response. If a client does not stop sending headers, this leads to memory exhaustion.     |   04/04/2024      |
| [CVE-2024-24795](<https://nvd.nist.gov/vuln/detail/CVE-2024-24795>) | **High** | 7.5  | **versions <=2.4.58** |    HTTP Response splitting in multiple modules in Apache HTTP Server allows an attacker that can inject malicious response headers into backend applications to cause an HTTP desynchronization attack.     |    04/04/2024   |
| [CVE-2023-38709](<https://nvd.nist.gov/vuln/detail/CVE-2023-38709>) | **Critical** | 9.8  | **versions <=2.4.58** |    Faulty input validation in the core of Apache allows malicious or exploitable backend/content generators to split HTTP responses     |    04/04/2024   |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [Apache HTTP Server 2.4 vulnerabilities](https://httpd.apache.org/security/vulnerabilities_24.html)

## Additional References

- https://www.tenable.com/cve/CVE-2024-27316
- https://www.tenable.com/cve/CVE-2024-24795
- https://www.tenable.com/cve/CVE-2023-38709
