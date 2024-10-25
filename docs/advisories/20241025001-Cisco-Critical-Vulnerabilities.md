# Cisco Addresses Critical Vulnerabilities - 20241025001

## Overview

The WA SOC has been made aware to critical vulnerabilities affecting Cisco systems that could enable an authenticated remote attacker to execute operating system commands with root privileges.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE | CVSS | Severity |
| ------------------- | ---------- | --- | ---- | -------- |
| Cisco Secure Firewall Management Center (FMC) | all versions <= 7.4.2 | [CVE-2024-20424](https://nvd.nist.gov/vuln/detail/CVE-2024-20424) | 9.9 | **Critical** |
| Cisco Adaptive Security Appliance (ASA) | all versions <= 9.18.3.56 | [CVE-2024-20329](https://nvd.nist.gov/vuln/detail/CVE-2024-20329) | 9.9 | **Critical** | 
| Cisco Firepower Threat Defense (FTD) | all versions <= 7.4.1.1 | [CVE-2024-20412](https://nvd.nist.gov/vuln/detail/CVE-2024-20412) | 9.3 | **Critical** |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Cisco advisory CVE-2024-20424: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ssh-rce-gRAuPEUF>
- Cisco advisory CVE-2024-20329: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-cmd-inj-v3AWDqN7>
- Cisco advisory CVE-2024-20412: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-statcred-dFC8tXT5>

## Additional References

- Security Affairs article: <https://securityaffairs.com/170203/breaking-news/cisco-fixed-tens-of-vulnerabilities-including-actively-exploited-one.html>
