# Cisco IOS and IOS XE HTTP WebUI - 20231018001

## Overview

The WA SOC has observed a vulnerability in the Cisco HTTP WebUI feature of Cisco IOS Software and Cisco IOS XE Software 
when exposed to the internet or untrusted network, which could allow an unauthenticated attacker to create an account on an affected system with privilege level 15 access. The attacker can then use that account to gain control of the affected system. 

## What is the vulnerability?

[**CVE-2023-20198**](https://nvd.nist.gov/vuln/detail/CVE-2023-20198) - CVSS v3 Base Score: ***10.0***

## What is vulnerable?

This vulnerability affects Cisco IOS XE Software if the web UI feature is enabled. The web UI feature is enabled through the ip http server or ip http secure-server commands.


## What has been observed?

The WASOC has been made aware that this vulnerability is currently be actively exploited. [Active Exploited Vulnerbalities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## Recommendation

Cisco strongly recommends that customers disable the HTTP Server feature on all internet-facing systems. To disable the HTTP Server feature, use the no ip http server or no ip http secure-server command in global configuration mode. If both the HTTP server and HTTPS server are in use, both commands are required to disable the HTTP Server feature.

- [Cisco Security Advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z)

**Cisco will provide updates on the status of this investigation and when a software patch is available.**

## Additional References

The WASOC has previously provided an advisory related to [Cisco IOS VPN services](https://soc.cyber.wa.gov.au/advisories/20231011004-Cisco-IOS-Software-Out-of-Bounds-Write-Vulnerability/)
