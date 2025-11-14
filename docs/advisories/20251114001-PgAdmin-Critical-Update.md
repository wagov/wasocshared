# PgAdmin Critical Update - 20251114001

## Overview

A critical Remote Code Execution (RCE) vulnerability has been identified in pgAdmin 4 versions up to 9.9 when operating in server mode. This issue allows attackers to inject and execute arbitrary commands on the server hosting pgAdmin, posing a critical risk to the integrity and security of the database management system and underlying data.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| pgAdmin      | versions up to 9.9    | [CVE-2025-12762](https://nvd.nist.gov/vuln/detail/CVE-2025-12762)                                                                        | 9.1          | **Critical**                                   |

## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- PgAdmin Github: <https://github.com/advisories/GHSA-w2p4-p4rh-qcm3>