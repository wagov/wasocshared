# OpenStack Releases Critical Security Advisory - 20240729002

## Overview

The WA SOC has been made aware of a vulnerability affecting OpenStack Nova products.

## What is vulnerable?

| Product(s) Affected | Version(s)                                                                        | CVE                                                               | CVSS | Severity |
| ------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- | -------- |
| OpenStack Nova      | ***all versions*** before 27.4.1 </br> 28.0 before 28.2.1</br> 29.0 before 29.1.1 | [CVE-2024-40767](https://nvd.nist.gov/vuln/detail/CVE-2024-40767) | 6.8  | Medium   |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- OpenStack: <https://security.openstack.org/ossa/OSSA-2024-002.html>

## Additional References

- Securityonline: <https://securityonline.info/cve-2024-40767-openstack-nova-vulnerability-exposes-cloud-servers-to-data-theft-risk/>
- Tenable: <https://www.tenable.com/cve/CVE-2024-40767>
