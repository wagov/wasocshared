# Okta Releases Browser Plugin Advisory - 20240723002

## Overview

The WA SOC has been made aware of a cross-site scripting security vulnerability found in the Okta Browser Plugin (Chrome/Edge/Firefox/Safari). The issue occurs when the plugin prompts the user to save credentials within Okta Personal.

## What is vulnerable?

| Product(s) Affected | Version(s)                       | CVE                                                             | CVSS | Severity |
| ------------------- | -------------------------------- | --------------------------------------------------------------- | ---- | -------- |
| Okta Browser Plugin | Affected at 6.5.0 through 6.31.0 | [CVE-2024-0981](https://nvd.nist.gov/vuln/detail/CVE-2024-0981) | 7.1  | High     |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- Okta: <https://trust.okta.com/security-advisories/okta-browser-plugin-reflected-cross-site-scripting-cve-2024-0981/>

## Reference

- SecurityOnline: <https://securityonline.info/okta-patches-cross-site-scripting-flaw-cve-2024-0981-in-browser-plugin/>
