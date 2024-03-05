# Cisco Patches NX-OS DoS Vulnerabilities - 20240305001

## Overview

Cisco have released updates for their NX-OS products that address high severity Denial of Service (DoS) vulnerabilities which could cause a vulnerable device to stop processing network traffic or restart. There are no workarounds.

## What is vulnerable?

Affected Cisco products:

- Nexus 3000 Series Switches
- Nexus 5500 Platform Switches
- Nexus 5600 Platform Switches
- Nexus 6000 Series Switches
- Nexus 7000 Series Switches
- Nexus 9000 Series Switches in standalone NX-OS mode
- Cisco Nexus 9500 R-Series Line Cards

For more details about the vulnerable products, please refer to the *Recommendation* section below.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* if the products are internet facing (refer [Patch Management](../guidelines/patch-management.md)):

- [Cisco NX-OS Software MPLS Encapsulated IPv6 Denial of Service Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ipv6-mpls-dos-R9ycXkwM)
- [Cisco NX-OS Software External Border Gateway Protocol Denial of Service Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nxos-ebgp-dos-L3QCwVJ)
