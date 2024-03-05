# Adobe Acrobat Reader Multiple Vulnerabilities - 20240305002

## Overview

Adobe Acrobat Reader contains multiple vulnerabilities that could lead to remote code execution if exploited correctly.

## What is vulnerable?

Affected Adobe products:

- Adobe Acrobat Reader 2023.006.20380

For more details about the vulnerablilities, please refer to the *Recommendation* section below.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* if the products are internet facing (refer [Patch Management](../guidelines/patch-management.md)):

- [Adobe Acrobat Reader Font CharStrings CharStringsOffset out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1910)
- [Adobe Acrobat Reader Font avar SegmentMaps out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1909)
- [Adobe Acrobat Reader FileAttachment PDAnnot destroy use-after-free vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1901)
- [Adobe Acrobat Reader Annot3D object zoom event use-after-free vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1890)
- [Adobe Acrobat Reader Font CPAL integer overflow vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1906)
- [Adobe Acrobat Reader Font CharStrings INDEX out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1908)
- [Adobe Acrobat Reader Font CPAL numColorRecords out-of-bounds read vulnerability](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1905)
