# VMware Security Update for Cloud Director Appliance - 20231115002

## Overview

VMware has a critical severity range vulnerability in VMware Cloud Director Appliance, that contains an authentication bypass vulnerability in case VMware Cloud Director Appliance was upgraded to 10.5 from an older version.

## What is the vulnerability?

[**CVE-2023-34060**](https://nvd.nist.gov/vuln/detail/CVE-2023-34060) - CVSS v3 Base Score: ***9.8***

## What is vulnerable?

The vulnerability affects the following products:

- VMware Cloud Director Appliance (VCD Appliance) version 10.5 if upgraded from 10.4.x or below.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [VMware Cloud Director 10.5 Workaround](https://kb.vmware.com/s/article/95534)

## Additional References

- [VMware Advisories](https://www.vmware.com/security/advisories/VMSA-2023-0026.html)
