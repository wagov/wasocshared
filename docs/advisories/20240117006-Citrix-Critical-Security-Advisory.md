# Citrix Critical Security Advisory - 20240117006

## Overview

Citrix have released a security advisory for CVE-2023-6548 affecting  NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway).

## What is the vulnerability?

| CVE ID                                                                                             | CVSS Score | Description                                                                  | Dated        |
| -------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------- | ------------ |
| [CVE-2023-6548](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6548)                      | 5.5        | Authenticated (low privileged) remote code execution on Management Interface |              |
| [CVE-2023-6549](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6549)                      | 8.2        | Denial of Service                                                            |              |
| Note: NetScaler ADC and NetScaler Gateway version 12.1 is now End Of Life (EOL) and is vulnerable. |            |                                                                              | 10 May, 2024 |

## What is vulnerable?

The following products and versions are affected:

- NetScaler ADC and NetScaler Gateway 14.1 before 14.1-12.35
- NetScaler ADC and NetScaler Gateway 13.1 before 13.1-51.15
- NetScaler ADC and NetScaler Gateway 13.0 before 13.0-92.21
- NetScaler ADC 13.1-FIPS before 13.1-37.176
- NetScaler ADC 12.1-FIPS before 12.1-55.302
- NetScaler ADC 12.1-NDcPP before 12.1-55.302

## What has been observed?

Citrix has observed exploits of these CVEs on unmitigated appliances.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://www.bleepingcomputer.com/news/security/citrix-warns-of-new-netscaler-zero-days-exploited-in-attacks/>
