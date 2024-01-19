# Fortinet Security Updates for Multiple Products - 20231218002

## Overview

Fortinet has released security updates to address vulnerabilities in multiple Fortinet products. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

[**CVE-2023-41678**](https://nvd.nist.gov/vuln/detail/CVE-2023-41678) - CVSS v3 Base Score: ***8.8***

A double free in cache management vulnerability, affects the following products:

- Fortinet FortiOS versions 7.0.0 to 7.0.5
- FortiPAM versions (1.0.0 to 1.0.3, 1.1.0 to 1.1.1)

[**CVE-2022-27488**](https://nvd.nist.gov/vuln/detail/CVE-2022-27488) - CVSS v3 Base Score: ***8.3***

A cross-site request forgery (CSRF) vulnerabilty, affects the following products:

- Fortinet FortiVoiceEnterprise versions 6.4.0 to 6.4.7, 6.0.0 to 6.0.11
- FortiSwitch versions 7.0.0 t0 7.0.4, 6.4.0 to 6.4.10, 6.2.0 to 6.2.7, 6.0.x
- FortiMail versions 7.0.0 to 7.0.3, 6.4.0 to 6.4.6, 6.2.x, 6.0.x
- FortiRecorder versions 6.4.0 to 6.4.2, 6.0.x, 2.7.x, 2.6.x
- FortiNDR version 1.x.x

[**CVE-2022-27488**](https://nvd.nist.gov/vuln/detail/CVE-2022-27488) - CVSS v3 Base Score: ***8.3***

A use of externally-controlled format string vulnerability, affects the following products:

- Fortinet FortiProxy versions 7.2.0 to 7.2.4, 7.0.0 to 7.0.10
- FortiOS versions 7.4.0, 7.2.0 to 7.2.4, 7.0.0 to 7.0.11, 6.4.0 to 6.4.12, 6.2.0 to 6.2.15, 6.0.0 to 6.0.17
- FortiPAM versions 1.0.0 to 1.0.3

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Fortinet upgrade path tool](https://docs.fortinet.com/upgrade-tool)
- [CISA](https://www.cisa.gov/news-events/alerts/2023/12/14/fortinet-releases-security-updates-multiple-products)
