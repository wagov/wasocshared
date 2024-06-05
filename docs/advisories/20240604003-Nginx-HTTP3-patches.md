# NGINX HTTP/3 Vulnerability Patches Released - 20240604003

## Overview

NGINX has released security updates that address four vulnerabilities. These issues affect NGINX systems compiled with the ngx_http_v3_module module, where the configuration contains a listen directive with the quic option enabled. The HTTP/3 QUIC module is considered an experimental feature and is not compiled by default in NGINX OSS, but it is compiled by default in NGINX Plus.

## What is vulnerable?

| CVE  | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ---- | ------------ | ---- | ------------------- | ------- | ----- |
| [CVE-2024-32760](https://nvd.nist.gov/vuln/detail/CVE-2024-32760) | **Medium** | 6.5  | Nginx 1.25.0-1.25.5, 1.26.0 | When NGINX Plus or NGINX OSS are configured to use the HTTP/3 QUIC module, undisclosed HTTP/3 encoder instructions can cause NGINX worker processes to terminate or cause or other potential impact.        | 29/05/2024      |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 2 weeks (refer [Patch Management](../guidelines/patch-management.md)):

- [nginx security advisory (CVE-2024-31079, CVE-2024-32760, CVE-2024-34161, CVE-2024-35200)](https://mailman.nginx.org/pipermail/nginx-announce/2024/GMY32CSHFH6VFTN76HJNX7WNEX4RLHF6.html)
