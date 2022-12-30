# Citrix Security Bulletin (Gateway and ADC) - 202211100001

## Overview
The WA SOC has observed [3 new vulnerabilities affecting Citrix ADC and gateway products](https://support.citrix.com/article/CTX463706/citrix-gateway-and-citrix-adc-security-bulletin-for-cve202227510-cve202227513-and-cve202227516), notably **CVE-2022-27510** has a CVSSv3 of **9.8**.


## What is the threat?
Appliances that have enabled SSL VPN functionaility or are using ICA Proxy services have an authentication bypass vulnerabilty, that could be exploited for initial access.

## What is the vulnerability ?

| CVE | Description | CVSSv3 |
| --- | --- | --- |
| CVE-2022-27510 | Citrix ADC and Gateway Authentication Bypass Vulnerability | 9.8 |
| CVE-2022-27513 | Citrix ADC and Gateway Insufficient Verification of Data Authenticity Vulnerability | 8.3 |
| CVE-2022-27516 | Citrix ADC and Gateway Protection Mechanism Failure Vulnerability | 5.3 |

## What has been observed ?
No active exploitation has been observed in the WA sector, however internet exposed Citrix SSL VPN endpoints have been detected.

## Recommendation
Affected customers of Citrix ADC and Citrix Gateway are recommended to install the relevant updated versions of Citrix ADC or Citrix Gateway as soon as possible: 

- Citrix ADC and Citrix Gateway 13.1-33.47 and later releases
- Citrix ADC and Citrix Gateway 13.0-88.12 and later releases of 13.0  
- Citrix ADC and Citrix Gateway 12.1-65.21 and later releases of 12.1  
- Citrix ADC 12.1-FIPS 12.1-55.289 and later releases of 12.1-FIPS  
- Citrix ADC 12.1-NDcPP 12.1-55.289 and later releases of 12.1-NDcPP 

**Please note** that Citrix ADC and Citrix Gateway versions prior to 12.1 are EOL and customers on those versions are recommended to upgrade to one of the supported versions. 

Additionally, and unrelated to the aforementioned CVEs, security enhancements to help protect customers against HTTP Request Smuggling attacks have been added in the above versions of Citrix ADC, and Citrix Gateway. Customers may enable these enhancements using the Citrix ADC management interface. Please see https://support.citrix.com/article/CTX472830 for more information. 

### Reference:
- https://support.citrix.com/article/CTX463706/citrix-gateway-and-citrix-adc-security-bulletin-for-cve202227510-cve202227513-and-cve202227516
- https://support.citrix.com/article/CTX472830/citrix-adc-http-request-smuggling-reference-guide