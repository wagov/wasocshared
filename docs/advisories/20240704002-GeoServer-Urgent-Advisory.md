# GeoServer Urgent Advisory - 20240704002

## Overview

A severe security flaw has been discovered in GeoServer. This vulnerability could potentially allow attackers to execute arbitrary code on affected servers, putting sensitive mapping and location data at risk.

## What is vulnerable?

| Products Affected.  | CVE                                                               | CVSS | Severity     |
| ------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| **GeoServer: All versions before 2.25.2** | [CVE-2024-36401](https://nvd.nist.gov/vuln/detail/CVE-2024-36401) |9.8  | **Critical** |
| **GeoServer: All versions before 2.25.2** | [CVE-2024-24749](https://nvd.nist.gov/vuln/detail/CVE-2024-24749) | 7.5 | **High** |
| **GeoServer: All versions before 2.25.2** | [CVE-2024-34696](https://nvd.nist.gov/vuln/detail/CVE-2024-34696) | 4.9  | **Medium** |
| **GeoServer: All versions before 2.25.2** | [CVE-2024-35230](https://nvd.nist.gov/vuln/detail/CVE-2024-35230) | TBD  | **TBD** |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- https://geoserver.org/announcements/vulnerability/2024/06/18/geoserver-2-25-2-released.html