# Ivanti Connect Secure and Ivanti Policy Secure Gateways - 20240111001

## Overview

Ivanti has released a security advisory relating to critical vulnerabilities in their products Ivanti Connect Secure (formerly known as Pulse Connect Secure) and Ivanti Policy Secure Gateways.

If CVE-2024-21887 is used in conjunction with CVE-2023-46805, exploitation does not require authentication and enables a threat actor to craft malicious requests and execute arbitrary commands on the system.

## What is vulnerable?

The following vulnerabilities impact **all supported versions of Ivanti Connect Secure and Ivanti Policy Secure gateways**.

| CVE                                                               | Severity     | CVSS | Summary                                                                                                                                                                                                                              |
| ----------------------------------------------------------------- | ------------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [CVE-2023-46805](https://www.cve.org/CVERecord?id=CVE-2023-46805) | **High**     | 8.2  | An authentication bypass vulnerability in the web component allows a remote attacker to access restricted resources by bypassing control checks.                                                                                     |
| [CVE-2024-21887](https://www.cve.org/CVERecord?id=CVE-2024-21887) | **Critical** | 9.1  | A command injection vulnerability in web components allows an authenticated administrator to send specially crafted requests and execute arbitrary commands on the appliance. This vulnerability can be exploited over the internet. |

## What has been observed?

Ivanti have seen evidence of threat actors attempting to manipulate Ivanti’s internal integrity checker (ICT). CISA has added the above CVEs to their Known Exploited Vulnerabilities Catalog.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://forums.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US>

### Additional References

- Ivanti original security advisory "C*VE-2023-46805 (Authentication Bypass) & CVE-2024-21887 (Command Injection) for Ivanti Connect Secure and Ivanti Policy Secure Gateways*": <https://forums.ivanti.com/s/article/CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US>
- CISA Known Exploited Vulnerabilities Catalog: <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>
