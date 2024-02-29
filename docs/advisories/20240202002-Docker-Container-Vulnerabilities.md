# Docker Container Runtime Component Vulnerabilities - 20240202002

## Overview

An attacker could use the core container infrastructure components of docker containers to escape the container and gain unauthorized access to the underlying host operating system from within the container.

## What is vulnerable?

| Component(s) Affected      | CVE                                                               | Severity     | CVSS | Exploitation | Dated |
| -------------------------- | ----------------------------------------------------------------- | ------------ | ---- | --- | -- |
| OCI runc                   | [CVE-2024-21626](https://nvd.nist.gov/vuln/detail/CVE-2024-21626) | **High**     | 8.6  |Yes| 18.02.2024
| Buildkit Mount             | [CVE-2024-23651](https://nvd.nist.gov/vuln/detail/CVE-2024-23651) | **High**     | 7.4  |No| 08.02.2024 |
| Buildkit GRPC SecurityMode | [CVE-2024-23653](https://nvd.nist.gov/vuln/detail/CVE-2024-23653) | **Critical** | 9.8 |No|08.02.2024 |
| BuildKit Buildtime         | [CVE-2024-23652](https://nvd.nist.gov/vuln/detail/CVE-2024-23652) | **Critical** | 9.1  |No|08.02.2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours* (refer [Patch Management](../guidelines/patch-management.md)):

You will likely need to update your Docker daemons and Kubernetes deployments, as well as any container build tools that you use in CI/CD pipelines, on build servers, and on your developers' workstations

- [Runc 1.1.12](https://github.com/opencontainers/runc/releases/tag/v1.1.12) - Fix for CVE-2024-21626
- [Docker buildkit Release 0.12.5](https://www.docker.com/blog/docker-security-advisory-multiple-vulnerabilities-in-runc-buildkit-and-moby/) - Fix for CVE-2024-23651, CVE-2024-23652, and CVE-2024-23653

### Additional Resources

- [Moby and Open Container Vulenrabilities - CISA](https://www.cisa.gov/news-events/alerts/2024/02/01/moby-and-open-container-initiative-release-critical-updates-multiple-vulnerabilities-affecting)
- [Synk "leaky vessels" report](https://snyk.io/blog/leaky-vessels-docker-runc-container-breakout-vulnerabilities/)
