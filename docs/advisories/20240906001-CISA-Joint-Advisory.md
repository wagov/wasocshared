# CISA Releases New Joint Advisory - 20240906001

## Overview

CISA, along with numerous partners (including the FBI, NSA, ASD's ACSC, and many other national security and intelligence agencies) have released a joint advisory on the Russian General Staff Main Intelligence Directorate (GRU) 161st Specialist Training Center (Unit 29155). GRU Unit 29155 have been responsible for computer network operations against global targets and critical infrastructure for the purposes of espionage, sabotage, and reputational harm since at least 2020.

## What is affected?

| Product(s) Affected | Version(s) | CVE                                                                                                                                       | CVSS          | Severity                                                         |
| ------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
 Ivanti Connect Secure (ICS) and Ivanti Policy Secure (IPS) Gateways      | Versions 9.x and 22.x    | [CVE-2023-46805](https://nvd.nist.gov/vuln/detail/CVE-2023-46805) </br> [CVE-2024-21887](https://nvd.nist.gov/vuln/detail/CVE-2024-21887) | 8.2 </br> 9.1 | High  </br> **Critical** |

## Recommendation

The WA SOC recommends administrators review relevant advisories and apply the recommended actions to all affected devices.

- Russian Military Cyber Actors Target US and Global Critical Infrastructure: <https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-249a>

CISA have attributed activity in a separate advisory with the Adversary Group. The WA SOC recommends Administrators also review noted IOCs located within:

- Update: Destructive Malware Targeting Organizations in Ukraine: <https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-057a>

The key immediate recommended mitigations include:

- Prioritising routine system updates and remediating known exploited vulnerabilities.
- Segmenting networks to prevent the spread of malicious activity.
- Enabling phishing-resistant multifactor authentication (MFA) for all externally facing account services, especially for webmail, virtual private networks (VPNs), and accounts that access critical systems.

### Changelog

- 2024-09-06: Advisory created.
- 2024-09-09: Included “What is affected” section to reflect newly published information and added second "Update" recommendation link.
