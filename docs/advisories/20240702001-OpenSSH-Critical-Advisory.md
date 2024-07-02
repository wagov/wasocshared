# OpenSSH Critical Advisory - 20240702001

## Overview

OpenSSH has released  fixes for a critical vulnerability present in Portable OpenSSH sshd(8), that may allow arbitrary
code execution with root privileges.

A signal handler race condition found in OpenSSH's server (sshd), where a client does not authenticate within LoginGraceTime seconds (120 by default, 600 in old OpenSSH versions), then sshd's SIGALRM handler is called asynchronously. However, this signal handler calls various functions that are not async-signal-safe, for example, syslog().

## What is vulnerable?

| Products Affected| CVE | CVSS    | Severity |
|--- | ----- | ----|---------- |
| Portable OpenSSH versions between 8.5p1 and 9.7p1 (inclusive)   | [CVE-2024-6387](https://nvd.nist.gov/vuln/detail/CVE-2024-6387)   | 8.1   | **High**    |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [OpenSSH release notes](https://www.openssh.com/releasenotes.html)

## Additional References

- [cissecurity advisory](https://www.cisecurity.org/advisory/a-vulnerability-in-openssh-could-allow-for-remote-code-execution_2024-076)
