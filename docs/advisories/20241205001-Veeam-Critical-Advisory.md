# Veeam Critical Advisory - 20241205001

## Overview

Veeam has released a security advisory detailing a vulnerability discovered within the Veeam Service Provider Console (VSPC), where from the VSPC management agent machine, under condition that the management agent is authorised on the server, it is possible to perform Remote Code Execution (RCE) and remove arbitrary files on the VSPC server machine.

## What is vulnerable?

| Product(s) Affected                      | Version(s)  | CVE #                                                             | CVSS v4/v3 | Severity |
| ---------------------------------------- | ----------- | ----------------------------------------------------------------- | ---------- | -------- |
| Veeam Service Provider Console (VSPC)    |             | [CVE-2024-42449](https://www.cve.org/CVERecord?id=CVE-2024-42449) |     9.9    | Critical |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Veeam Security Advisory: <https://www.veeam.com/kb4679>

#### This vulnerability does not affect other Veeam products (e.g., Veeam Backup & Replication, Veeam Agent for Microsoft Windows, Veeam ONE).

## 3rd Party Article(s):

- Tenable CVEs News List: <https://www.tenable.com/cve/CVE-2024-42448>
- Help Net Security Article: <https://www.helpnetsecurity.com/2024/12/03/vspc-vulnerabilities-cve-2024-42448-cve-2024-42449/>