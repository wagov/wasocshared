# Wazuh Critical Vulnerability - 20250813005

## Overview

The WA SOC has been made aware of a critical vulnerability in Wazuh servers.

An unsafe deserialization vulnerability allows for remote code execution, giving attackers the ability to evaluate arbitrary python code on the Wazuh server through API access or a Wazuh agent.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Wazuh server      | 4.4.0 to 4.9.0 (inclusive)    | [CVE-2025-24016](https://nvd.nist.gov/vuln/detail/CVE-2025-24016)                                                                        | 9.9          | **Critical**                                   |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Wazuh: <https://wazuh.com/blog/addressing-the-cve-2025-24016-vulnerability/>

## Additional References

- GitHub POC: <https://github.com/wazuh/wazuh/security/advisories/GHSA-hcrc-79hj-m3qh>
