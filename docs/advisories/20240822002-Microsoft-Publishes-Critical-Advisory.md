# Microsoft Publishes Critical CVE Advisory - 20240822002

## Overview

Microsoft publishes critical advisory for Azure Managed Instance for Apache Cassandra Elevation of Privilege Vulnerability. An improper access control vulnerability in the Azure Managed Instance for Apache Cassandra allows an authenticated attacker to elevate privileges over a network.

## What is vulnerable?

| Product(s) Affected                         | Version(s)                               | CVE                                                               | CVSS | Severity     |
| ------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------- | ---- | ------------ |
| Azure Managed Instance for Apache Cassandra | clusters updated before 20th August 2024 | [CVE-2024-38175](https://www.cve.org/CVERecord?id=CVE-2024-38175) | 9.6  | **Critical** |

## What has been observed?

Microsoft is aware of functional exploitation in the wild. There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft CVE article: <https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38175>
