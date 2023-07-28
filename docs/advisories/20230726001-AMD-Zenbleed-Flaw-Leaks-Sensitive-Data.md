# Zenbleed - AMD Zen2 processors vulnerable to sensitive data leak (CVE-2023-20593)

## Overview

Recent security research from Google has found AMD Zen2 processors can leak data causing attackers to potentially collect sensitive information including passwords and encryption keys.

## What is the vulnerability?

[**CVE-2023-20593**](https://nvd.nist.gov/vuln/detail/CVE-2023-20593)

An issue in “Zen 2” CPUs, under specific microarchitectural circumstances, may allow an attacker to potentially access sensitive information. What makes this vulnerability particularly critical is any virtualised services shared by multiple users such as VMs in cloud-hosted data centres can allow attackers on the same hardware to exfiltrate data from VMs.

## What is vulnerable?

The vulnerability affects the following products all Zen2 Processors:

- Ryzen 3000

- Ryzen Pro 3000

- Ryzen Threadripper 3000

- Ryzen 4000 Pro

- Ryzen 4000, 5000, and 7020 with Radeon Graphics

- Epyc Rome datacentre processors

## Recommendation

The WA SOC recommends administrators pay close attention to latest available updates on their hardware using Zen2 processors and ensure patches are applied as soon as they become available. A patch for EPYC 7002 is available now. Other patches are forecast to be available over the next few months:

| CPU | Estimate Patch Date | 
|---- |----------------|
| Ryzen 3000 (desktop) | December 2023 |
| Ryzen 4000G (desktop) | December 2023 | 
| Ryzen 4000 (laptop) | December 2023 |
| Ryzen 5700U/5500U/5300U (laptop) | December 2023 | 
| Ryzen 7020 (laptop) | December 2023 |
| Ryzen Threadripper 3000 | October 2023 | 
| Ryzen Threadripper Pro 3000WX | November/December 2023 |
| EPYC 7002 | Patch available | 

## Additional References

- [AMD EPYC™ Series Update Information](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7008.html)

- [Technical Write-Up by Tavis Ormandy](https://lock.cmpxchg8b.com/zenbleed.html)

- [AMD Zenbleed chip bug leaks secrets fast and easy - The Register](https://www.theregister.com/2023/07/24/amd_zenbleed_bug/)
