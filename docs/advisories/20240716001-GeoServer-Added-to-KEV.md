# GeoServer Critical Vulnerability Added to Known Exploited Catalog - 20240716001

## Overview

Since the publication of [Advisory 20240704002](https://soc.cyber.wa.gov.au/advisories/20240704002-GeoServer-Urgent-Advisory/#what-is-vulnerable), relating to a severe security flaw in GeoServer, CISA has added the item to their Known Exploited Vulnerability Catalog.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE # | CVSS v4/v3 | Severity |
| --- | --- |--- |--- |--- |
| GeoServer | 2.23 before 2.23.6 </br> 2.24 before 2.24.4 </br> 2.25 before 2.25.2 | [NVD - CVE-2024-36401](https://nvd.nist.gov/vuln/detail/CVE-2024-36401) | 9.8 | Critical |
| GeoTools | All versions before 29.6 </br> 30 before 30.4 </br> 31 before 31.2 | [NVD - CVE-2024-36401](https://nvd.nist.gov/vuln/detail/CVE-2024-36401) | 9.8 | Critical |

## What has been observed?

CISA has added this vulnerability to their [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 48 hours (refer [Patch Management](../guidelines/patch-management.md)):

- <https://geoserver.org/announcements/vulnerability/2024/06/18/geoserver-2-25-2-released.html>
