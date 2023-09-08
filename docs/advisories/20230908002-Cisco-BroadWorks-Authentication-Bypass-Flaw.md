# Cisco BroadWorks impacted by critical authentication bypass flaw - 20230908002

## Overview

The WA SOC has observed a critical vulnerability in the single sign-on (SSO) implementation of Cisco BroadWorks Application Delivery Platform and Cisco BroadWorks Xtended Services Platform, a cloud communication services platform allowing an unauthenticated remote attacker to forge the credentials required to bypass an affected system.


## What is the vulnerability?

[**CVE-2023-20238**](https://nvd.nist.gov/vuln/detail/CVE-2023-20238) - CVSS v3 Base Score: ***10.0***

## What is vulnerable?

The vulnerability affects the Cisco Application Delivery Platform and BroadWorks Xtended Services Platform release having one of the following applications enabled;

-   AuthenticationService
-   BWCallCenter
-   BWReceptionist
-   CustomMediaFilesRetrieval
-   ModeratorClientApp
-   PublicECLQuery
-   PublicReporting
-   UCAPI
-   Xsi-Actions
-   Xsi-Events
-   Xsi-MMTel
-   Xsi-VTR

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Cisco Security Advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bw-auth-bypass-kCggMWhX#vp)

## Additional References

- [Bleeping Computer](https://www.bleepingcomputer.com/news/security/cisco-broadworks-impacted-by-critical-authentication-bypass-flaw/)
