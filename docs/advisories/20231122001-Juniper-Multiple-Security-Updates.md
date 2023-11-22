# Juniper Addresses Multiple Vulnerabilities in Secure Analytics - 20231122001

## Overview

Juniper Networks have released a security advisory relating to multiple security vulnerabilities being resolved for Juniper Secure Analytics in version 7.5.0 UP7 IF02.

## What is the vulnerability?

| CVE | CVSS v3 Score | Brief Description |
| --- | ---| --- |
| [**CVE-2020-22218**](https://nvd.nist.gov/vuln/detail/CVE-2020-22218) | 7.5 | An issue was discovered in function _libssh2_packet_add in libssh2 1.10.0 allows attackers to access out of bounds memory. |
| [**CVE-2023-20593**](https://nvd.nist.gov/vuln/detail/CVE-2023-20593) | 5.5 | An issue in "Zen 2" CPUs, under specific microarchitectural circumstances, may allow an attacker to potentially access sensitive information. |
| [**CVE-2023-35788**](https://nvd.nist.gov/vuln/detail/CVE-2023-35788) | 7.8 | An issue was discovered in fl_set_geneve_opt in net/sched/cls_flower.c in the Linux kernel before 6.3.7. It allows an out-of-bounds write in the flower classifier code via TCA_FLOWER_KEY_ENC_OPTS_GENEVE packets. This may result in denial of service or privilege escalation. |
| [**CVE-2022-44730**](https://nvd.nist.gov/vuln/detail/CVE-2022-44730) | 4.4 | Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache XML Graphics Batik.This issue affects Apache XML Graphics Batik: 1.16. A malicious SVG can probe user profile / data and send it directly as parameter to a URL. |
| [**CVE-2022-44729**](https://nvd.nist.gov/vuln/detail/CVE-2022-44729) | 7.1 | Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache XML Graphics Batik.This issue affects Apache XML Graphics Batik: 1.16. On version 1.16, a malicious SVG could trigger loading external resources by default, causing resource consumption or in some cases even information disclosure. Users are recommended to upgrade to version 1.17 or later. |
| [**CVE-2023-20900**](https://nvd.nist.gov/vuln/detail/CVE-2023-20900) | 7.5 | A malicious actor that has been granted Guest Operation Privileges in a target virtual machine may be able to elevate their privileges if that target virtual machine has been assigned a more privileged Guest Alias |
| [**CVE-2023-3341**](https://nvd.nist.gov/vuln/detail/CVE-2023-3341) | 7.5 | The code that processes control channel messages sent to `named` calls certain functions recursively during packet parsing. Recursion depth is only limited by the maximum accepted packet size; depending on the environment, this may cause the packet-parsing code to run out of available stack memory, causing `named` to terminate unexpectedly. Since each incoming control channel message is fully parsed before its contents are authenticated, exploiting this flaw does not require the attacker to hold a valid RNDC key; only network access to the control channel's configured TCP port is necessary. This issue affects BIND 9 versions 9.2.0 through 9.16.43, 9.18.0 through 9.18.18, 9.19.0 through 9.19.16, 9.9.3-S1 through 9.16.43-S1, and 9.18.0-S1 through 9.18.18-S1. |
| [**CVE-2023-3899**](https://nvd.nist.gov/vuln/detail/CVE-2023-3899) | 7.8 | A vulnerability was found in subscription-manager that allows local privilege escalation due to inadequate authorization. The D-Bus interface com.redhat.RHSM1 exposes a significant number of methods to all users that could change the state of the registration. By using the com.redhat.RHSM1.Config.SetAll() method, a low-privileged local user could tamper with the state of the registration, by unregistering the system or by changing the current entitlements. This flaw allows an attacker to set arbitrary configuration directives for /etc/rhsm/rhsm.conf, which can be abused to cause a local privilege escalation to an unconfined root. |
| [**CVE-2023-43057**](https://nvd.nist.gov/vuln/detail/CVE-2023-43057) | 4.6 | IBM QRadar SIEM 7.5.0 is vulnerable to cross-site scripting. This vulnerability allows users to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session. |

## What is vulnerable?

The vulnerability affects the following products:

- All versions of Juniper Networks Juniper Secure Analytics **all versions before 7.5.0 UP7**.

## What has been observed?

There is no evidence of known exploitation at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://supportportal.juniper.net/s/article/2023-11-Security-Bulletin-JSA-Series-Multiple-vulnerabilities-resolved?language=en_US>
