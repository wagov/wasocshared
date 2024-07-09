# Synology Camera Advisory - 20240709002

## Overview

Synology has published an advisory regarding their Synoloy Camera range and several vulnerabilities with the most critical being a 9.8 CVSS. The critical vulnerability (CVE-2024-39349) allows buffer overflow to execute arbitrary code from remote attackers affecting firmware versions before 1.0.7-0298 on devices BC500 and TC500.

## What is vulnerable?

| Products Affected               | CVE                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                              | CVSS | Severity |
| ------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | -------- |
| Synology Camera (BC500 & TC500) | [CVE-2024-39349](https://nvd.nist.gov/vuln/detail/CVE-2024-39349) | A vulnerability regarding buffer copy without checking size of input ('Classic Buffer Overflow') is found in the libjansson component and it does not affect the upstream library. This allows remote attackers to execute arbitrary code via unspecified vectors. The following models with Synology Camera Firmware versions before 1.0.7-0298 may be affected: BC500 and TC500.                       | 9.8  | Critical |
| Synology Camera (BC500 & TC500) | [CVE-2024-39350](https://nvd.nist.gov/vuln/detail/CVE-2024-39350) | A vulnerability regarding authentication bypass by spoofing is found in the RTSP functionality. This allows man-in-the-middle attackers to obtain privileges without consent via unspecified vectors. The following models with Synology Camera Firmware versions before 1.0.7-0298 may be affected: BC500 and TC500.                                                                                    | 7.5  | High     |
| Synology Camera (BC500 & TC500) | [CVE-2023-47802](https://nvd.nist.gov/vuln/detail/CVE-2023-47802) | A vulnerability regarding improper neutralization of special elements used in an OS command ('OS Command Injection') is found in the IP block functionality. This allows remote authenticated users with administrator privileges to execute arbitrary commands via unspecified vectors. The following models with Synology Camera Firmware versions before 1.0.7-0298 may be affected: BC500 and TC500. | 7.2  | High     |
| Synology Camera (BC500 & TC500) | [CVE-2024-39351](https://nvd.nist.gov/vuln/detail/CVE-2024-39351) | A vulnerability regarding improper neutralization of special elements used in an OS command ('OS Command Injection') is found in the NTP configuration. This allows remote authenticated users with administrator privileges to execute arbitrary commands via unspecified vectors. The following models with Synology Camera Firmware versions before 1.0.7-0298 may be affected: BC500 and TC500.      | 7.2  | High     |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe (refer [Patch Management](../guidelines/patch-management.md)):

- BC500	- Upgrade to 1.0.7-0298 or above
- TC500	- Upgrade to 1.0.7-0298 or above

## Additional References

- [Synology Advisory](https://www.synology.com/en-global/security/advisory/Synology_SA_23_15)
- [SecurityOnline News - CVE-2024-39349](https://securityonline.info/cve-2024-39349-cvss-9-8-critical-vulnerability-in-synology-surveillance-cameras/)
