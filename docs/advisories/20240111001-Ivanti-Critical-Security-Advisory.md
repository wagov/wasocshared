# Ivanti Multiple Vulnerabilities Added in CISA Known Exploits List - 20240111001

## Overview

CISA and their partners released joint Cybersecurity Advisory [Threat Actors Exploit Multiple Vulnerabilities in Ivanti Connect Secure and Policy Secure Gateways](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060b)

Threat actors can exploit in a chain to bypass authentication, craft malicious requests, and execute arbitrary commands with elevated privileges.

## What is vulnerable?

The following vulnerabilities impact **all supported versions of Ivanti Connect Secure and Ivanti Policy Secure gateways**.

| CVE  | Severity | CVSS | Summary | Exploitation| Dated|
| ------- | ------------ | ---- | ------- | --| --|
| [CVE-2023-46805](https://www.cve.org/CVERecord?id=CVE-2023-46805) | **High** | 8.2  | An authentication bypass vulnerability in the web component allows a remote attacker to access restricted resources by bypassing control checks.| Yes|1 Feb, 2024|
| [CVE-2024-21887](https://www.cve.org/CVERecord?id=CVE-2024-21887) | **Critical** | 9.1  | A command injection vulnerability in web components allows an authenticated administrator to send specially crafted requests and execute arbitrary commands on the appliance. This vulnerability can be exploited over the internet. |Yes|1 Feb, 2024|
| [CVE-2024-21893](https://www.cve.org/CVERecord?id=CVE-2024-21893) | **High** | 8.2  | A server-side request forgery vulnerability in the SAML component of Ivanti Connect Secure (9.x, 22.x) and Ivanti Policy Secure (9.x, 22.x) and Ivanti Neurons for ZTA allows an attacker to access certain restricted resources without authentication. |Yes|1 Feb, 2024|

## What has been observed?

Ivanti have seen evidence of threat actors attempting to manipulate Ivanti’s internal integrity checker (ICT). CISA has added the above CVEs to their Known Exploited Vulnerabilities Catalog.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):


- [Ivanti original security advisory](https://forums.ivanti.com/s/article/CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/news-events/alerts/2024/02/29/cisa-and-partners-release-advisory-threat-actors-exploiting-ivanti-connect-secure-and-policy-secure)
