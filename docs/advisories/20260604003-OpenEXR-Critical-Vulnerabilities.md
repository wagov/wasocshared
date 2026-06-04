# OpenEXR Critical Vulnerabilites - 20260604003

## Overview

The WASOC has been made aware of two critical vulnerabilities affecting OpenEXR. The vulnerabilities arise from improper handling of untrusted EXR image data and may be triggered when a specially crafted EXR file is processed.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
|--------------------|------------|-----|------|----------|
| OpenEXR | 3.0.0 to before 3.2.9<br>3.3.0 to before 3.3.11<br>3.4.0 to before 3.4.11 | [CVE-2026-42216](https://nvd.nist.gov/vuln/detail/CVE-2026-42216) | 9.1| **Critical** |
| OpenEXR | 3.0.0 to before 3.2.9<br>3.3.0 to before 3.3.11<br>3.4.0 to before 3.4.11 | [CVE-2026-42217](https://nvd.nist.gov/vuln/detail/CVE-2026-42217) | 9.8 | **Critical** |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- OpenEXR Advisory: <https://github.com/AcademySoftwareFoundation/openexr/security/advisories/GHSA-65j8-95g9-jgj4>
- OpenEXR Advisory: <https://github.com/AcademySoftwareFoundation/openexr/security/advisories/GHSA-3c67-4wwp-w52m>

## Additional References

- NIST: <https://nvd.nist.gov/vuln/detail/CVE-2026-42216>
- NIST: <https://nvd.nist.gov/vuln/detail/CVE-2026-42217>
