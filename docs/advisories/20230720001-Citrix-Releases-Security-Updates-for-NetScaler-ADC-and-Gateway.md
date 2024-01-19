# Citrix Releases Security Updates for NetScaler ADC and Gateway - 20230720001

## Overview

Citrix has released security updates to address multiple vulnerabilities affecting NetScaler ADC and NetScaler Gateway. An attacker can exploit one of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

| CVE ID                                                          | Affected Products          | Description                                         | Pre-requisites                                                                                                              | CVSS                                                                                          |
| --------------------------------------------------------------- | -------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [CVE-2023-3466](https://nvd.nist.gov/vuln/detail/CVE-2023-3466) | Citrix ADC, Citrix Gateway | Reflected Cross-Site Scripting (XSS)                | Requires victim to access an attacker-controlled link in the browser while being on a network with connectivity to the NSIP | [8.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H) |
| [CVE-2023-3467](https://nvd.nist.gov/vuln/detail/CVE-2023-3467) | Citrix ADC, Citrix Gateway | Privilege Escalation to root administrator (nsroot) | Authenticated access to NSIP or SNIP with management interface access                                                       | [8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)   |
| [CVE-2023-3519](https://nvd.nist.gov/vuln/detail/CVE-2023-3519) | Citrix ADC, Citrix Gateway | Unauthenticated remote code execution               | Appliance must be configured as a Gateway (VPN virtual server, ICA Proxy, CVPN, RDP Proxy) OR AAA virtual server            | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) |

## What is vulnerable?

The vulnerability affects the following products:

- NetScaler ADC and NetScaler Gateway 13.1, before 13.1-49.13
- NetScaler ADC and NetScaler Gateway 13.0, before 13.0-91.13
- NetScaler ADC 13.1-FIPS, before 13.1-37.159
- NetScaler ADC 12.1-FIPS, before 12.1-55.297
- NetScaler ADC 12.1-NDcPP, before 12.1-55.297

***Note***: NetScaler ADC and NetScaler Gateway version 12.1 is now End Of Life (EOL) and is vulnerable.

## Recommendation

Citrix explains that exploits of CVE-2023-3519 on unmitigated appliances have been observed.

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- NetScaler ADC and NetScaler Gateway 13.1-49.13  and later releases
- NetScaler ADC and NetScaler Gateway 13.0-91.13  and later releases of 13.0
- NetScaler ADC 13.1-FIPS 13.1-37.159 and later releases of 13.1-FIPS
- NetScaler ADC 12.1-FIPS 12.1-55.297 and later releases of 12.1-FIPS
- NetScaler ADC 12.1-NDcPP 12.1-55.297 and later releases of 12.1-NDcPP

***Note***: For NetScaler ADC and NetScaler Gateway version 12.1 (EOL) product(s), Citrix recommends customers to upgrade their appliances to one of the supported versions that address the vulnerabilities.

## Additional References

- [Citrix ADC and Citrix Gateway Security Bulletin for CVE-2023-3519, CVE-2023-3466, CVE-2023-3467](https://support.citrix.com/article/CTX561482/citrix-adc-and-citrix-gateway-security-bulletin-for-cve20233519-cve20233466-cve20233467)
