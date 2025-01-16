# Fortinet Critical Update - 20250116001

## Overview

The WA SOC has been made aware of a hard-coded cryptographic key vulnerability in FortiSwitch that may allow a remote unauthenticated attacker in posession of the key to execute unauthorized code.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| FortiSwitch      | 7.4.0 <br> 7.2.0 - 7.2.5 <br> 7.0.0 - 7.0.7 <br> 6.4.0 - 6.4.13 <br> 6.2.0 - 6.2.7 <br> 6.0.0 - 6.0.7| [CVE-2023-37936](https://nvd.nist.gov/vuln/detail/CVE-2023-37936)                                                                        | 9.8          | **Critical**                                   |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 48 hours:

- Fortinet: <https://fortiguard.fortinet.com/psirt/FG-IR-23-260>

## Additional References

- BleepingComputer: <https://www.bleepingcomputer.com/news/security/fortinet-warns-of-auth-bypass-zero-day-exploited-to-hijack-firewalls/>