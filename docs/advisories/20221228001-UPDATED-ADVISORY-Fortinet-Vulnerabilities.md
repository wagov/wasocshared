# UPDATED ADVISORY - Fortinet Vulnerabilities for FortiOS / FortiProxy / FortiSwitchManager - 20221228001

## Overview
Since initial advice on the 13th of December 2022 ([*Ref: 20221213001*](https://wagov.github.io/wasocshared/#/advisories/20221213001-Fortinet-Vulnerabilities-for-FortiOS-FortiProxy-FortiSwitchManager.md)), FortiGuard Labs has updated their advisory ([https://www.fortiguard.com/psirt/FG-IR-22-398](https://www.fortiguard.com/psirt/FG-IR-22-398)) with **additional indicators of compromise** (IOCs) for FortiOS administrators to utilize in reviewing the integrity of current vulnerable systems in their advisory.  

## What is the threat?
A heap-based buffer overflow vulnerability ([CWE-122](https://cwe.mitre.org/data/definitions/122.html)) in FortiOS SSL-VPN may allow a remote unauthenticated attacker to execute arbitrary code or commands via specifically crafted requests.

## What is vulnerable ? 
FortiGate have listed the following affected prodructs:
- FortiOS version 7.2.0 through 7.2.2
- FortiOS version 7.0.0 through 7.0.8
- FortiOS version 6.4.0 through 6.4.10
- FortiOS version 6.2.0 through 6.2.11
- FortiOS version 6.0.0 through 6.0.15
- FortiOS version 5.6.0 through 5.6.14
- FortiOS version 5.4.0 through 5.4.13
- FortiOS version 5.2.0 through 5.2.15
- FortiOS version 5.0.0 through 5.0.14
- FortiOS-6K7K version 7.0.0 through 7.0.7
- FortiOS-6K7K version 6.4.0 through 6.4.9
- FortiOS-6K7K version 6.2.0 through 6.2.11
- FortiOS-6K7K version 6.0.0 through 6.0.14
- FortiProxy version 7.2.0 through 7.2.1
- FortiProxy version 7.0.0 through 7.0.7
- FortiProxy version 2.0.0 through 2.0.11
- FortiProxy version 1.2.0 through 1.2.13
- FortiProxy version 1.1.0 through 1.1.6
- FortiProxy version 1.0.0 through 1.0.7

## Indicators of Compromise
FortiGate have outline multiple Indicators of Compromise (IOCs) in their advisory: [https://www.fortiguard.com/psirt/FG-IR-22-398](https://www.fortiguard.com/psirt/FG-IR-22-398)

## What has been observed ?
CISA has listed this vulnerabilty in their [Known Exploited Vulnerabilties](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog.

## Recommendation
Due to the report of active exploitation, it is strongly recommended to patch this vulnerability by following the **Solutions** outlined by FortiGate within 2 weeks across all affected platforms.