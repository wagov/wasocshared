# Jenkins Critical Vulnerabilities - 20250414001

## Overview


Jenkins published a security advisory addressing vulnerabilities in Jenkins Docker images, specifically jenkins/ssh-agent and jenkins/ssh-slave, which involve the reuse of SSH host keys across containers.

This issue could allow attackers to impersonate SSH build agents.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| jenkins/ssh-agent      | Version <= 6.11.1    | [CVE-2025-32754](https://nvd.nist.gov/vuln/detail/CVE-2025-32754)                                                                        | 9.1          | **Critical**                                   |
|  jenkins/ssh-slave      | All versions    | [CVE-2025-32755](https://nvd.nist.gov/vuln/detail/CVE-2025-32755) | 9.1  |  **Critical** |

## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Jenkins Security Advisory: <https://www.jenkins.io/security/advisory/2025-04-10/>

## Additional References

- SecurityOnline: <https://securityonline.info/jenkins-docker-images-vulnerable-to-ssh-host-key-reuse>