# Kubernetes Image Builder Vulnerability - 20241016002

## Overview

The WA SOC has been made aware of a security issue discovered in the Kubernetes Image Builder where default credentials are enabled during the image build process. Virtual machine images built using the Proxmox provider do not disable these default credentials, and nodes using the resulting images may be accessible via these default credentials. The credentials can be used to gain root access.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                       | CVSS          | Severity                                                         |
| ------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
| Kubernetes Image Builder      | Versions before v0.1.37    | [CVE-2024-9486](https://nvd.nist.gov/vuln/detail/CVE-2024-9486)                                                                         | 9.8           | **Critical**                                     |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- \<https://github.com/kubernetes/kubernetes/issues/128006>
