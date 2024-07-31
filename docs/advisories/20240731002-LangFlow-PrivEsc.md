# Langflow Privilege Escalation - 20240731002

## Overview

The WA SOC has been made aware of a high severity vulnerability in the Langflow framework.

Langflow versions prior to 1.0.13 suffer from a Privilege Escalation vulnerability, allowing a remote and low privileged attacker to gain super admin privileges by performing a mass assignment request on the '/api/v1/users' endpoint.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                       | CVSS          | Severity                                                         |
| ------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
| Langflow       | < 1.0.13    | [CVE-2024-7297](https://nvd.nist.gov/vuln/detail/CVE-2024-7297)                                                                         | 8.8       |High                                   |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *2 weeks* (refer [Patch Management](../guidelines/patch-management.md)):

- [Tenable - Langflow Privilege Escalation through Mass Assignment](https://www.tenable.com/security/research/tra-2024-26)

## Additional References

- GitHub: https://github.com/langflow-ai/langflow/pull/2995
