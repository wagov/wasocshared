# OpenClaw Authentication Bypass and Privilege Escalation - 20260330001

## Overview

The OpenClaw project has released a patch to address a vulnerability in OpenClaw that may allow for unauthorised privilege escalation on an affected device.

A valid bootstrap setup code could be verified more than once before the pairing request was approved, allowing a second verification attempt to mutate a pending device pairing and request broader scopes, including escalation from a lower operator scope to 'operator.admin'.

## What is vulnerable?

| Product(s) Affected | Version(s)    | CVE                                                               | CVSS | Severity     |
| ------------------- | ------------- | ----------------------------------------------------------------- | ---- | ------------ |
| OpenClaw            | \<= 2026.3.13 | [CVE-2026-32987](https://nvd.nist.gov/vuln/detail/CVE-2026-32987) | 9.3  | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- OpenClaw: <https://github.com/openclaw/openclaw/security/advisories/GHSA-63f5-hhc7-cx6p>

## Additional References

- Tenable: <https://www.tenable.com/cve/CVE-2026-32987>
