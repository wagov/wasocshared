# Apache ActiveMQ Unauthenticated RCE via Deserialization - 20231102001

## Overview

Apache ActiveMQ is vulnerable to Remote Code Execution.The vulnerability may allow a remote attacker with network access to a broker to run arbitrary shell commands by manipulating serialized class types in the OpenWire protocol to cause the broker to instantiate any class on the classpath. Rapid7 [Managed Detection and Response Team](https://www.rapid7.com/blog/post/2023/11/01/etr-suspected-exploitation-of-apache-activemq-cve-2023-46604/) has observed activity exploitation of this vulernability.

## What is the vulnerability?

[**CVE-2023-46604**](https://nvd.nist.gov/vuln/detail/CVE-2023-46604) - CVSS v3 Base Score: ***10.0*** - Remote Code Execution

## What is vulnerable?

The vulnerability affects the following products:

- Affected versions:

    - Apache ActiveMQ 5.18.0 before 5.18.3
    - Apache ActiveMQ 5.17.0 before 5.17.6
    - Apache ActiveMQ 5.16.0 before 5.16.7
    - Apache ActiveMQ before 5.15.16
    - Apache ActiveMQ Legacy OpenWire Module 5.18.0 before 5.18.3
    - Apache ActiveMQ Legacy OpenWire Module 5.17.0 before 5.17.6
    - Apache ActiveMQ Legacy OpenWire Module 5.16.0 before 5.16.7
    - Apache ActiveMQ Legacy OpenWire Module 5.8.0 before 5.15.16

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

Apache recommended to upgrade to version **5.15.16, 5.16.7, 5.17.6, or 5.18.3**, which fixes this issue.

## Additional References

- [NVD - CVE-2023-46604 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2023-46604)

- [Apache Security Bulletin](https://activemq.apache.org/security-advisories.data/CVE-2023-46604)

- [Apache Issue Tracker](https://issues.apache.org/jira/browse/AMQ-9370)
