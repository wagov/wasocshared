# Fortinet Vulnerabilities for FortiOS / FortiProxy / Buffer underflow in administrative interface - 20230308001

## Overview

A buffer underwrite ('buffer underflow') vulnerability in FortiOS & FortiProxy administrative interface may allow a remote unauthenticated attacker to execute arbitrary code on the device and/or perform a DoS on the GUI, via specifically crafted requests.

## Exploitation status

Fortinet is not aware of any instance where this vulnerability was exploited in the wild. We continuously review and test the security of our products, and this vulnerability was internally discovered within that frame.

## What is the vulnerability ?

- The vulnerability requires remote access to the FortiOS or FortiProxy administrative interface.
- The vulnerability can allow Remote Code Execution. It can also be used to perform Denial of Service.

**[CVE-2023-25610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-25610)** - FortiOS Critical vulnerability  (CVE-2023-25610).

CVE-2023-25610 Unauthenticated Stored Cross-Site Scripting (XSS) in Simple Ajax Chat \<= 20220115 allows an attacker to store the malicious code. However, the attack requires specific conditions, making it hard to exploit.

## What is vulnerable ?

### Affected products related to **CVE-2023-25610**

- FortiOS version 7.2.0 through 7.2.3
- FortiOS version 7.0.0 through 7.0.9
- FortiOS version 6.4.0 through 6.4.11
- FortiOS version 6.2.0 through 6.2.12
- FortiOS 6.0 all versions
- FortiProxy version 7.2.0 through 7.2.2
- FortiProxy version 7.0.0 through 7.0.8
- FortiProxy version 2.0.0 through 2.0.11
- FortiProxy 1.2 all versions
- FortiProxy 1.1 all versions

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

- Review the identified systems, and vendor notes to determine if your systems are affected.
- Apply patches. If unable to do so, implement the workarounds in the security advisory.
- Determine if remote access to admin interfaces is configured and required for your system. Limit access to the admin interface where appropriate.

Read the following Fortinet advisories and apply the remediations:

- FortiOS / FortiProxy - Heap buffer underflow in administrative interface [https://www.fortiguard.com/psirt/FG-IR-23-001](https://www.fortiguard.com/psirt/FG-IR-23-00)

### Reference

- FortiOS / FortiProxy - Heap buffer underflow in administrative interface <https://www.fortiguard.com/psirt/FG-IR-23-001>
