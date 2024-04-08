# Adobe Releases Security Updates for Multiple Products - 20240214003

## Overview

Adobe has released security updates to address vulnerabilities in Adobe software. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is vulnerable?

---

| CVE ID                                                                                                            | Product(s) Affected                                                                                                                            | Severity |     |       
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --- |
| Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') (CVE-2024-20720)       | [Adobe Commerce and Magento](https://helpx.adobe.com/security/products/magento/apsb24-03.html)  2.4.6-p3 and earlier                           | **Critical** |     |
| Improper Authentication  [CVE-2024-20738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20738)          | [Adobe FrameMaker Publishing Server](https://helpx.adobe.com/security/products/framemaker-publishing-server/apsb24-10.html) 24.0.3 and earlier | **Critical** |     |
| Out-of-bounds Write (CVE-2024-20740, CVE-2024-20743)                                                              | [Adobe Substance 3D Painter](https://helpx.adobe.com/security/products/substance3d_painter/apsb24-04.html) 9.1.1 and earlier                   | **High** |     |
| Buffer Overflow (CVE-2024-20723)                                                                                  | [Adobe Substance 3D Painter](https://helpx.adobe.com/security/products/substance3d_painter/apsb24-04.html) 9.1.1 and earlier                   | **High** |     |
| Out-of-bounds Read (CVE-2024-20741, CVE-2024-20742, CVE-2024-20722, CVE-2024-20724, CVE-2024-20725)               | [Adobe Substance 3D Painter](https://helpx.adobe.com/security/products/substance3d_painter/apsb24-04.html) 9.1.1 and earlier                   | **High** |     |
| Heap-based Buffer Overflow [CVE-2024-20739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20739)        | [Adobe Audition ](https://helpx.adobe.com/security/products/audition/apsb24-11.html)  24.0.3 and earlier                                       | **High** |     |
| Integer Overflow or Wraparound [CVE-2024-20730](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20730)     | [Adobe Acrobat and Reader](https://helpx.adobe.com/security/products/acrobat/apsb24-07.html) 23.008.20470 and earlier                          | **High** |     |
| Out-of-bounds Write (CVE-2024-20726, CVE-2024-20727, CVE-2024-20728)                                              | [Adobe Acrobat and Reader](https://helpx.adobe.com/security/products/acrobat/apsb24-07.html) 23.008.20470 and earlier                          | **High** |     |
| Use After Free (CVE-2024-20729, CVE-2024-20731, CVE-2024-20734)                                                   | [Adobe Acrobat and Reader](https://helpx.adobe.com/security/products/acrobat/apsb24-07.html) 23.008.20470 and earlier                          | **High** |     |
| Out-of-bounds Read (CVE-2024-20750)                                                                               | [Adobe Substance 3D Designer](https://helpx.adobe.com/security/products/substance3d_designer/apsb24-13.html) version 13.1.0 and earlier        | **High** |     |
| Uncontrolled Resource Consumption [CVE-2024-20716](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20716) | [Adobe Commerce and Magento](https://helpx.adobe.com/security/products/magento/apsb24-03.html)  2.4.6-p3 and earlier                           | **Medium** |     |
| Cross-site Scripting (Stored XSS) (CVE-2024-20719, CVE-2024-20717)                                                | [Adobe Commerce and Magento](https://helpx.adobe.com/security/products/magento/apsb24-03.html)  2.4.6-p3 and earlier                           | **Medium** |     |
| Cross-Site Request Forgery (CSRF) (CVE-2024-20718)                                                                | [Adobe Commerce and Magento](https://helpx.adobe.com/security/products/magento/apsb24-03.html)  2.4.6-p3 and earlier                           | **Medium** |     |
| Improper Input Validation (CVE-2024-20733)                                                                        | [Adobe Acrobat and Reader](https://helpx.adobe.com/security/products/acrobat/apsb24-07.html) 23.008.20470 and earlier                          | **Medium** |     |
| Out-of-bounds Read (CVE-2024-20735, CVE-2024-20736, CVE-2024-20747, CVE-2024-20748, CVE-2024-20749)               | [Adobe Acrobat and Reader](https://helpx.adobe.com/security/products/acrobat/apsb24-07.html) 23.008.20470 and earlier                          | **Medium** |     |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

## Additional References

- [cisa.gov](https://www.cisa.gov/news-events/alerts/2024/02/13/adobe-releases-security-updates-multiple-products)
