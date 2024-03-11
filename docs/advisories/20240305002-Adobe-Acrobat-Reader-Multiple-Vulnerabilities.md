# Adobe Acrobat Reader Multiple Vulnerabilities - 20240305002

## Overview

Adobe Acrobat Reader contains multiple vulnerabilities that could lead to remote code execution if exploited correctly.

## What is vulnerable?

Affected Adobe products:

- Acrobat Reader versions 20.005.30539, 23.008.20470 and earlier

| CVE                                                                   | Summary                                                                                  | Severity   | CVSS |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------- | ---- |
| [**CVE-2024-20749**](https://nvd.nist.gov/vuln/detail/CVE-2024-20749) | Adobe Acrobat Reader Font CharStrings CharStringsOffset out-of-bounds read vulnerability | **Medium** | 5.5  |
| [**CVE-2024-20735**](https://nvd.nist.gov/vuln/detail/CVE-2024-20735) | Adobe Acrobat Reader Font CPAL numColorRecords out-of-bounds read vulnerability          | **Medium** | 5.5  |
| [**CVE-2024-20747**](https://nvd.nist.gov/vuln/detail/CVE-2024-20747) | Adobe Acrobat Reader Font CharStrings INDEX out-of-bounds read vulnerability             | **Medium** | 5.5  |
| [**CVE-2024-20748**](https://nvd.nist.gov/vuln/detail/CVE-2024-20748) | Adobe Acrobat Reader Font avar SegmentMaps out-of-bounds read vulnerability              | **Medium** | 5.5  |
| [**CVE-2024-20731**](https://nvd.nist.gov/vuln/detail/CVE-2024-20731) | Adobe Acrobat Reader FileAttachment PDAnnot destroy use-after-free vulnerability         | **High**   | 7.8  |
| [**CVE-2024-20729**](https://nvd.nist.gov/vuln/detail/CVE-2024-20729) | Adobe Acrobat Reader Annot3D object zoom event use-after-free vulnerability              | **High**   | 7.8  |
| [**CVE-2024-20730**](https://nvd.nist.gov/vuln/detail/CVE-2024-20730) | Adobe Acrobat Reader Font CPAL integer overflow vulnerability                            | **High**   | 7.8  |

For more details about the vulnerablilities, please refer to the *Recommendation* section below.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions (refer [Patch Management](../guidelines/patch-management.md)):

- [Adobe Security Bulletin](https://helpx.adobe.com/au/security/products/acrobat/apsb24-07.html)
- [Adobe Acrobat Reader Font CharStrings CharStringsOffset out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1910)
- [Adobe Acrobat Reader Font avar SegmentMaps out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1909)
- [Adobe Acrobat Reader FileAttachment PDAnnot destroy use-after-free vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1901)
- [Adobe Acrobat Reader Annot3D object zoom event use-after-free vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1890)
- [Adobe Acrobat Reader Font CPAL integer overflow vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1906)
- [Adobe Acrobat Reader Font CharStrings INDEX out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1908)
- [Adobe Acrobat Reader Font CPAL numColorRecords out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1905)
