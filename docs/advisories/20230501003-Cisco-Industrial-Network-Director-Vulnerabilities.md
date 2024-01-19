# Cisco Industrial Network Director Vulnerabilities - 20230501003

## Overview

Cisco has released security updates for Cisco Industrial Network Director vulnerbilities.

Multiple vulnerabilities in Cisco Industrial Network Director (IND) could allow an authenticated attacker to inject arbitrary operating system commands or access sensitive data.

## What is the vulnerability?

[**CVE-2023-20036**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20036) - CVSS v3 Base Score: ***9.9***

- This vulnerability is due to improper input validation when uploading a Device Pack. An attacker could exploit this vulnerability by altering the request that is sent when uploading a Device Pack. A successful exploit could allow the attacker to execute arbitrary commands as NT AUTHORITY\\SYSTEM on the underlying operating system of an affected device.

[**CVE-2023-20039**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20039) - CVSS v3 Base Score: ***9.9***

- This vulnerability is due to insufficient default file permissions that are applied to the application data directory. An attacker could exploit this vulnerability by accessing files in the application data directory. A successful exploit could allow the attacker to view sensitive information.

## What is vulnerable?

The vulnerability affects the following products:

- These vulnerabilities affects **Cisco IND** - all versions **prior to 1.10** and versions **after 1.10 upto 1.11.3**.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators to apply the solutions as per vendor instructions to all affected devices/applications.

## Additional References

- [Cisco Security Advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ind-CAeLFk6V#fs)
