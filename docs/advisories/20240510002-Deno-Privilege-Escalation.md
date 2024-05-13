# Deno Privilege Escalation - 20240510002

## Overview

Deno is an open-source runtime for JavaScript and TypeScript that provides a secure and productive environment for building applications. It offers features such as sandboxed execution, secure permissions, and a built-in package manager. However, a vulnerability has been discovered in Deno that allows for permission escalation via the opening of privileged files without the necessary **--deny** flag.

## What is vulnerable?

| CVE            | Severity | CVSS | Product(s) Affected | Summary                                                                                                                                | Dated      |
| -------------- | -------- | ---- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| CVE-2024-34346 | **High** | 8.4  | versions \<1.43     | The Deno sandbox can be weakened by granting read/write access to privileged files in various locations on Unix and Windows platforms. | 8 May 2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe for their organisations risk level (refer [Patch Management](../guidelines/patch-management.md)):

- Update to 1.43.1 or higher, or implement workarounds - https://github.com/denoland/deno/security/advisories/GHSA-23rx-c3g5-hv9w

## Additional References

- https://nvd.nist.gov/vuln/detail/CVE-2024-34346
- https://www.tenable.com/cve/CVE-2024-34346
