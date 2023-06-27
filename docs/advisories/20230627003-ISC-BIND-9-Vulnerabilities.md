# ISC Releases Security Advisories for Multiple Versions of BIND 9 - 20230627003

## Overview

The Internet Systems Consortium (ISC) has released security advisories that address vulnerabilities affecting multiple versions of the ISC’s Berkeley Internet Name Domain (BIND) 9. A remote attacker could exploit these vulnerabilities to potentially cause denial-of-service conditions.

## What is the vulnerability?

[**CVE-2023-2828**](https://nvd.nist.gov/vuln/detail/CVE-2023-2828) - CVSS v3 Base Score: ***7.5***\
[**CVE-2023-2829**](https://nvd.nist.gov/vuln/detail/CVE-2023-2829) - CVSS v3 Base Score: ***7.5***\
[**CVE-2023-2911**](https://nvd.nist.gov/vuln/detail/CVE-2023-2911) - CVSS v3 Base Score: ***7.5***

## What is vulnerable?

The vulnerability affects the following products:

BIND
- 9.11.0 -> 9.16.41
- 9.18.0 -> 9.18.15
- 9.19.0 -> 9.19.13

BIND Supported Preview Edition
- 9.11.3-S1 -> 9.16.41-S1
- 9.18.11-S1 -> 9.18.15-S1

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices:

- [CVE-2023-2828: named's configured cache size limit can be significantly exceeded](https://kb.isc.org/v1/docs/cve-2023-2828)
- [CVE-2023-2829: Malformed NSEC records can cause named to terminate unexpectedly when synth-from-dnssec is enabled](https://kb.isc.org/v1/docs/cve-2023-2829)
- [CVE-2023-2911: Exceeding the recursive-clients quota may cause named to terminate unexpectedly when stale-answer-client-timeout is set to 0](https://kb.isc.org/v1/docs/cve-2023-2911)

## Additional References

- [CISA](https://www.cisa.gov/news-events/alerts/2023/06/22/isc-releases-security-advisories-multiple-versions-bind-9)
