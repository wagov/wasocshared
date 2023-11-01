# Citrix Releases Security Updates for Multiple Products - 20231012003

## Overview

Citrix has released multiple updates to address critical vulnerabilities in ADC, NetScaler Gateway and Citrix Hypervisor. Vulnerabilities in Citrix Hypervisor 8.2 CU1 LTSR may allow malicious privileged code executions in guest VMs. The vulnerabilities present in NetScalar ADS and NetScalar gateway's would allow attackers to perform Denial of Service attacks or disclose sensitive information.

## What is the vulnerability?

Vulnerabilities in **NetScaler ADC and NetScaler Gateway**:

- [**CVE-2023-4966**](https://nvd.nist.gov/vuln/detail/CVE-2023-4966) - CVSS v3 Base Score: ***9.4*** - Denial of service

- [**CVE-2023-4967**](https://nvd.nist.gov/vuln/detail/CVE-2023-4967) - CVSS v3 Base Score: ***8.2*** - Denial of service


Vulnerabilities in **Citrix Hypervisor 8.2 CU1 LTSR**:

- [**CVE-2022-1304**](https://nvd.nist.gov/vuln/detail/CVE-2022-1304) - CVSS v3 Base Score: ***7.8*** - Allows an attacker to compromise the host when a specific administrative action is taken.

- [**CVE-2023-20588**](https://nvd.nist.gov/vuln/detail/CVE-2023-20588) - CVSS v3 Base Score: ***5.5*** 

- [**CVE-2023-34324**](https://nvd.nist.gov/vuln/detail/CVE-2023-34324) - CVSS v3 Base Score: ***NA*** - Cause the host to crash or become unresponsive.

- [**CVE-2023-34326**](https://nvd.nist.gov/vuln/detail/CVE-2023-34326) - CVSS v3 Base Score: ***NA*** - Allows an threat actor to compromise an AMD-based host via a passed through PCI device.

- [**CVE-2023-34327**](https://nvd.nist.gov/vuln/detail/CVE-2023-34327) - CVSS v3 Base Score: ***NA*** - Cause a different VM running on the AMD-based host to crash.


## What is vulnerable?

The vulnerability affects the following products:

- **NetScaler ADC** and **NetScaler Gateway**:

    -   NetScaler ADC and NetScaler Gateway 14.1 before 14.1-8.50
    -   NetScaler ADC and NetScaler Gateway 13.1 before 13.1-49.15
    -   NetScaler ADC and NetScaler Gateway 13.0 before 13.0-92.19
    -   NetScaler ADC 13.1-FIPS before 13.1-37.164
    -   NetScaler ADC 12.1-FIPS before 12.1-55.300
    -   NetScaler ADC 12.1-NDcPP before 12.1-55.300

- **Citrix Hypervisor 8.2 CU1 LTSR**

*Note: NetScaler ADC and NetScaler Gateway version 12.1 is now End-of-Life (EOL) and is vulnerable.*


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- **NetScaler ADC and NetScaler Gateway**:

    - NetScaler ADC and NetScaler Gateway 14.1-8.50  and later releases
    - NetScaler ADC and NetScaler Gateway  13.1-49.15  and later releases of 13.1
    - NetScaler ADC and NetScaler Gateway 13.0-92.19 and later releases of 13.0  
    - NetScaler ADC 13.1-FIPS 13.1-37.164 and later releases of 13.1-FIPS  
    - NetScaler ADC 12.1-FIPS 12.1-55.300 and later releases of 12.1-FIPS  
    - NetScaler ADC 12.1-NDcPP 12.1-55.300 and later releases of 12.1-NDcPP 


- **Citrix Hypervisor 8.2 CU1 LTSR**: 

    | Hot Fix Number | - | Article  |
    |-----------|---|----------------------------------------------|
    | CTX575070 | - | [Support Article](https://support.citrix.com/article/CTX575070) |
    | CTX579955 | - | [Support Article](https://support.citrix.com/article/CTX579955) |
    | CTX580401 | - | [Support Article](https://support.citrix.com/article/CTX580401) |
    | CTX581053 | - | [Support Article](https://support.citrix.com/article/CTX581053) |
    | CTX581108 | - | [Support Article](https://support.citrix.com/article/CTX581108) |



### Mitigations for Citrix Hypervisor

- CVE-2022-1304 is only exploitable at the point that the host administrator uses the "Restore Virtual Machine Metatdata" sub-option of the "Backup, Restore and Update" menu item in the on-host xsconsole interface. Customers who do not use this sub-option are not affected by this issue.

- CVE-2023-20588 only affects systems running on AMD Zen1 CPUs. Customers who are using other generations of AMD CPUs or who are not using AMD CPUs are not affected by this issue.

- CVE-2023-34326 only affects systems that have both of a) a PCI device passed through to the guest VM by the host administrator and also b) an AMD CPU. Customers who are not using AMD CPUs and customers who are not using the PCI passthrough feature are not affected by this issue.

- CVE-2023-34327 only affects systems running on AMD CPUs. Customers who are not using AMD CPUs are not affected by this issue.


## Additional References

- [NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2023-4966 and CVE-2023-4967 (citrix.com)](https://support.citrix.com/article/CTX579459/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve20234966-and-cve20234967)

- [Citrix Hypervisor Multiple Security Updates](https://support.citrix.com/article/CTX575089/citrix-hypervisor-multiple-security-updates)