# Downfall and Zenbleed - Modern Processor Attacks - 20230810001

## Overview

In recent months, two major CPU vulnerabilities have been announced that affect both Intel and AMD CPU's. These two brands account for almost all CPU's in modern computing and therefore considerable risk exists for those using unpatched hardware. These vulnerabilities dubbed Downfall (Intel) and Zenbleed (AMD - previous advisory [here](https://soc.cyber.wa.gov.au//advisories/20230726001-AMD-Zenbleed-Flaw-Leaks-Sensitive-Data/)) allow attackers to obtain sensitive information in shared computer environments, including cloud-hosted servers. Agencies are encouraged to reach out to their vendors and MSPs to ensure they are protected from these risks.

## What is the vulnerability?

### AMD

[**CVE-2023-20593**](https://nvd.nist.gov/vuln/detail/CVE-2023-20593) - *Zenbleed*

An issue in *Zen 2* CPUs, under specific microarchitectural circumstances, may allow an attacker to potentially access sensitive information.

### Intel

[**CVE-2022-40982**](https://nvd.nist.gov/vuln/detail/CVE-2022-40982) - *Downfall*

The [vulnerability](https://downfall.page/) is caused by memory optimization features in Intel processors that unintentionally reveal internal hardware registers to software. This allows untrusted software to access data stored by other programs, which should not normally be accessible.


## What is vulnerable?

### AMD

The vulnerability affects all AMD Zen2 Processors. A more comprehensive list of affected processors is available in an article [here](https://www.tomshardware.com/news/zenbleed-bug-allows-data-theft-from-amds-zen-2-processors-patches-released).

### Intel

Intel Core processors from the 6th Skylake to (including) the 11th Tiger Lake generation are affected. A more comprehensive list of affected processors will be available [here](https://www.intel.com/content/www/us/en/developer/topic-technology/software-security-guidance/processors-affected-consolidated-product-cpu-model.html).

## Recommendation

The WA SOC recommends administrators pay close attention to latest available updates on their hardware using AMD or Intel processors and reach out to their vendors, IT staff and Managed Service Providers (MSP) to ensure they are mitigating risks. Risks from unchecked MSPs are of particular concern due to [recent history](https://www.cyber.gov.au/sites/default/files/2023-03/msp_investigation_report.pdf) of compromises.


## Additional References

- [Google Security Blog - Downfall and Zenbleed](https://security.googleblog.com/2023/08/downfall-and-zenbleed-googlers-helping.html)

- [Zenbleed - Technical Write-Up by Tavis Ormandy](https://lock.cmpxchg8b.com/zenbleed.html)

- [Downfall Attacks](https://downfall.page/)
