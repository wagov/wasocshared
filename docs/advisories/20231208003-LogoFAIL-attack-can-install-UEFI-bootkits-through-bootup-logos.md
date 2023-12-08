# LogoFAIL attack can install UEFI bootkits through bootup logos - 20231208003

## Overview

The WA SOC has observed security vulnerabilities names as LogoFAIL, that allows threat actors to exploit and hijack the execution flow of the booting process and deliver bootkits .


## What is the vulnerability?

[**CVE-2023-5058**](https://nvd.nist.gov/vuln/detail/CVE-2023-5058) - CVSS v3 Base Score: ***N/A*** - Improper Input Validation in the processing of user-supplied splash screen during system boot in Phoenix SecureCore™ Technology™ 4 potentially allows denial-of-service attacks or arbitrary code execution.  

[**CVE-2023-39538**](https://nvd.nist.gov/vuln/detail/CVE-2023-39538) - CVSS v3 Base Score: ***7.5*** - AMI AptioV contains a vulnerability in BIOS where a User may cause an unrestricted upload of a BMP Logo file with dangerous type by Local access. A successful exploit of this vulnerability may lead to a loss of Confidentiality, Integrity, and/or Availability.  

[**CVE-2023-39539**](https://nvd.nist.gov/vuln/detail/CVE-2023-39539) - CVSS v3 Base Score: ***7.5*** - AMI AptioV contains a vulnerability in BIOS where a User may cause an unrestricted upload of a PNG Logo file with dangerous type by Local access. A successful exploit of this vulnerability may lead to a loss of Confidentiality, Integrity, and/or Availability.  

[**CVE-2023-40238**](https://nvd.nist.gov/vuln/detail/CVE-2023-40238) - CVSS v3 Base Score: ***N/A*** - A LogoFAIL issue was discovered in BmpDecoderDxe in Insyde InsydeH2O with kernel 5.2 before 05.28.47, 5.3 before 05.37.47, 5.4 before 05.45.47, 5.5 before 05.53.47, and 5.6 before 05.60.47 for certain Lenovo devices (but later, research found that the vulnerabilities affect beyond just Lenovo devices).  Image parsing of crafted BMP logo files can copy data to a specific address during the DXE phase of UEFI execution. This occurs because of an integer signedness error involving PixelHeight and PixelWidth during RLE4/RLE8 compression.  


## What is vulnerable?

The vulnerability affects multiple devices (large majority of BIOS vendors):

- LogoFAIL is not silicon-specific and can impact x86 and ARM-based devices
- LogoFAIL is UEFI and IBV-specific

More information on the scale of the vulnerabilities or devices affected, refer to articles: 
- [The Far-Reaching Consequences of LogoFAIL | Binarly](https://binarly.io/posts/The_Far_Reaching_Consequences_of_LogoFAIL/index.html) 
- [Finding LogoFAIL: The Dangers of Image Parsing During System Boot | Binarly](https://binarly.io/posts/finding_logofail_the_dangers_of_image_parsing_during_system_boot/index.html) 


## Recommendation

The WA SOC recommends administrators apply fix(es) in a timely manner, as they become available. (refer [Patch Management](../guidelines/patch-management.md)).


## Additional References

- [Finding LogoFAIL: The Dangers of Image Parsing During System Boot | Binarly -- AI -Powered Firmware Supply Chain Security Platform](https://binarly.io/posts/finding_logofail_the_dangers_of_image_parsing_during_system_boot/index.html)
- [NVD - CVE-2023-40238 (nist.gov)](https://nvd.nist.gov/vuln/detail/CVE-2023-40238)