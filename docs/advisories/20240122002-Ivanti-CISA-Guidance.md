# CISA Issues Emergency Directive on Ivanti Vulnerabilities  - 20240122002

## Overview

Since the publishing of [Advisory 20240119003](https://soc.cyber.wa.gov.au//advisories/20240119003-Ivanti-Critical-Security-Advisory), CISA has issued an Emergency Directive (ED 24-01) in response to active vulnerabilities in Ivanti Connect Secure and Ivanti Policy Secure.

At the time of writing, this directive is **only meant for United States operated Federal Civilian Executive Branch (FCEB) agencies**, however CISA strongly encourages all organizations to address the vulnerabilities in Ivanti Connect Secure and Ivanti Policy Secure.


## What has been observed?

Since publishing, **Ivanti have updated their Security Advisory** (link below) on January 20 with "*Update workaround section about known race condition when pushing device configurations. This condition can impact negatively the XML remediation leaving customers vulnerable.*"

Additionally, CISA have noted they will update their alert page (link below) with further mitigations and patches as they become available.


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://forums.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US>


### Additional Resources

- CISA article "CISA Issues Emergency Directive on Ivanti Vulnerabilities": <https://www.cisa.gov/news-events/alerts/2024/01/19/cisa-issues-emergency-directive-ivanti-vulnerabilities>
- CISA alert "Ivanti Releases Security Update for Connect Secure and Policy Secure Gateways": <https://www.cisa.gov/news-events/alerts/2024/01/10/ivanti-releases-security-update-connect-secure-and-policy-secure-gateways>