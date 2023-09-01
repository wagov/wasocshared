# VMware Releases Security Updates for Aria Operations for Networks - 20230901001

## Overview

Aria Operations for Networks contains an Authentication Bypass vulnerability due to a lack of unique cryptographic key generation. VMware has evaluated the severity of this issue to be in the critical severity range with a maximum CVSSv3 base score of 9.8.

A malicious actor with network access to Aria Operations for Networks could bypass SSH authentication to gain access to the Aria Operations for Networks CLI.

## What is the vulnerability?

VMware Aria Operations for Networks address multiple vulnerabilities. Please review each product's [security bulletin](https://www.vmware.com/security/advisories/VMSA-2023-0018.html#) for details.

- Authentication Bypass Vulnerability [CVE-2023-34039](https://nvd.nist.gov/vuln/detail/CVE-2023-34039) 

- Arbitrary File Write Vulnerability [CVE-2023-20890](https://nvd.nist.gov/vuln/detail/CVE-2023-20890)


## What is vulnerable?

The vulnerability affects the following products:

- VMware Aria Operations for Networks - [6.11](https://customerconnect.vmware.com/en/downloads/info/slug/infrastructure_operations_management/vmware_aria_operations_for_networks/6_x)
- VMware Aria Operations Networks - [6.x](https://kb.vmware.com/s/article/94152)

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all [affected](https://www.vmware.com/security/advisories/VMSA-2023-0018.html#) devices within the expected timeframes.
