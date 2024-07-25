# Docker Releases Critical Security Advisory - 20240725002

## Overview

Docker has released a security advisory relating to a vulnerability in certain versions of Docker Engine, which could allow an attacker to bypass authorization plugins (AuthZ) under specific circumstances.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                                                                                                                                                     | CVE                                             | CVSS | Severity     |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---- | ------------ |
| Docker              | v19.03.15 and below <br> v20.10.27 and below <br> v23.0.14 and below <br> v24.0.9 and below <br> v25.0.5 and below <br> v26.0.2 and below <br> v26.1.4 and below <br> v27.0.3 and below <br> v27.1.0 and below | https://nvd.nist.gov/vuln/detail/CVE-2024-41110 | 9.9  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hrs...* (refer [Patch Management](../guidelines/patch-management.md)):

- Docker: <https://www.docker.com/blog/docker-security-advisory-docker-engine-authz-plugin/>
