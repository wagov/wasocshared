# BeyondTrust Critical Vulnerability - 20241220002

## Overview

A critical vulnerability has been discovered in BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) products which can allow an unauthenticated attacker to inject commands that are run as a site user.

## What is vulnerable?

| Product(s) Affected                                                         | Version(s)                  | CVE                                                               | CVSS | Severity     |
| --------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products | Versions 24.3.1 and earlier | [CVE-2024-12356](https://nvd.nist.gov/vuln/detail/CVE-2024-12356) | 9.8  | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- BeyondTrust: <https://www.beyondtrust.com/trust-center/security-advisories/bt24-10>

## Additional References

- BleepingComputer: <https://www.bleepingcomputer.com/news/security/beyondtrust-says-hackers-breached-remote-support-saas-instances/>
