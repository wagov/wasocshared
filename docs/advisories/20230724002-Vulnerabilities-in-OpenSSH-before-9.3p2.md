# Vulnerabilities in OpenSSH before 9.3p2 - 20230724002

## Overview

The WA SOC has observed a vulnerability in the PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system.

## What is the vulnerability?

[**CVE-2023-38408**](https://nvd.nist.gov/vuln/detail/CVE-2023-38408)

The vulnerability allows specific libaries loaded via ssh-agent(1)'s PKCS#11 support could be abused to achieve remote code execution via a forwarded agent socket if the following
conditions are met:

- Exploitation requires the presence of specific libraries on the victim system.

- Remote exploitation requires that the agent was forwarded to an attacker-controlled system.

## What is vulnerable?

The vulnerability affects the following products:

- Versions of OpenSSH before 9.3p2

## Recommendation

The WA SOC recommends administrators to update OpenSSH to the lastest update within an expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)).


## Additional References

- [OpenSSH: Release Notes](https://www.openssh.com/releasenotes.html#9.3p2)

- [CVE-2023-38408: Remote Code Execution in OpenSSH's forwarded ssh-agent | Qualys Security Blog](https://blog.qualys.com/vulnerabilities-threat-research/2023/07/19/cve-2023-38408-remote-code-execution-in-opensshs-forwarded-ssh-agent)
