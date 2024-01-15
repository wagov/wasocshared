# Blog details Microsoft Visual Studio PoC Exploit - 20240115001

## Overview

A blog post has emerged detailing a Proof Of Concept (PoC) exploitation for Microsoft Visual Basic Studio that could be abused by a threat actor to gain elevated privileges on affected systems.


## What is vulnerable?

| Product(s) | Version(s) affected | Severity | CVSS
| --- | --- |--- | --- |
| Microsoft Visual Studio 2015 (Update 3) | from 14.0.0 before 14.0.27560.00 | **High** | 7.8 |
| Microsoft Visual Studio 2017 | all versions before 15.9.59 | **High** | 7.8 |
| Microsoft Visual Studio 2019 | from 16.11.0 before 16.11.33 | **High** | 7.8 |
| Microsoft Visual Studio 2022 | from 17.2.0 before 17.2.23, 17.4.0 before 17.4.15, 17.6.0 before 17.6.11 | **High** | 7.8 |


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 Hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-20656>


## Additional References

- MDSec Blog Article "*CVE-2024-20656 – Local Privilege Escalation in the VSStandardCollectorService150 Service*": <https://www.mdsec.co.uk/2024/01/cve-2024-20656-local-privilege-escalation-in-vsstandardcollectorservice150-service/>