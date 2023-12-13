# Adobe Releases Security Updates for Multiple Products - 20231213004

## Overview

Adobe has released security updates to address multiple vulnerabilities in Adobe software. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

| CWE ID | CVSS Score | Overview 
| --- | --- | --- |
| [**CWE-20**](https://cwe.mitre.org/data/definitions/20.html) | 7.8 | The product receives input or data, but it does not validate or incorrectly validates that the input has the properties that are required to process the data safely and correctly. |
| [**CWE-79**](https://cwe.mitre.org/data/definitions/79.html) | 5.4 | The product does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users. |
| [**CWE-125**](https://cwe.mitre.org/data/definitions/125.html) | 7.8 | The product reads data past the end, or before the beginning, of the intended buffer.|
| [**CWE-284**](https://cwe.mitre.org/data/definitions/284.html) | 5.3 | The product does not restrict or incorrectly restricts access to a resource from an unauthorized actor. |
| [**CWE-416**](https://cwe.mitre.org/data/definitions/416.html) | 7.8 | Referencing memory after it has been freed can cause a program to crash, use unexpected values, or execute code. |
| [**CWE-476**](https://cwe.mitre.org/data/definitions/476.html) | 5.5 | A NULL pointer dereference occurs when the application dereferences a pointer that it expects to be valid, but is NULL, typically causing a crash or exit. |
| [**CWE-787**](https://cwe.mitre.org/data/definitions/787.html) | 7.8 | The product writes data past the end, or before the beginning, of the intended buffer. |
| [**CWE-824**](https://cwe.mitre.org/data/definitions/824.html) | 3.3 | The product accesses or uses a pointer that has not been initialized. | Adobe Prelude 22.6 and earlier versions |


## What is Vulnerable?

| Product | Version | Platform | Bulletin |
| --- | --- | --- | --- |
| Adobe Prelude | 22.6  and earlier versions | Windows | [APSB23-67](https://helpx.adobe.com/security/products/prelude/apsb23-67.html) |
| Illustrator 2024 | 28.0 and earlier versions | Windows and macOS | [APSB23-68](https://helpx.adobe.com/security/products/illustrator/apsb23-68.html) |
| Illustrator 2023 | 27.9 and earlier versions | Windows and macOS | [APSB23-68](https://helpx.adobe.com/security/products/illustrator/apsb23-68.html) |
| Adobe InDesign | ID19.0 and earlier versions | Windows and macOS | [APSB23-70](https://helpx.adobe.com/security/products/indesign/apsb23-70.html) |
| Adobe InDesign | ID17.4.2 and earlier version | Windows and macOS | [APSB23-70](https://helpx.adobe.com/security/products/indesign/apsb23-70.html) |
| Adobe Dimension | 3.4.10 and earlier versions | Windows and macOS | [APSB23-71](https://helpx.adobe.com/security/products/dimension/apsb23-71.html) |
| Adobe Experience Manager (AEM) | AEM Cloud Service (CS) | All | [APSB23-72](https://helpx.adobe.com/security/products/experience-manager/apsb23-72.html) |
| Adobe Experience Manager (AEM) | 6.5.18.0 and earlier versions | All | [APSB23-72](https://helpx.adobe.com/security/products/experience-manager/apsb23-72.html) |
| Adobe Substance 3D Stager | 2.1.1 and earlier versions | Windows and macOS | [APSB23-73](https://helpx.adobe.com/security/products/substance3d_stager/apsb23-73.html) |
| Adobe Substance 3D Sampler | 4.2.1 and earlier versions | All | [APSB23-74](https://helpx.adobe.com/security/products/substance3d-sampler/apsb23-74.html) |
| Adobe After Effects | 24.0.3 and earlier versions | Windows and macOS | [ASPB23-75](https://helpx.adobe.com/security/products/after_effects/apsb23-75.html) |
| Adobe After Effects | 23.6.0 and earlier versions | Windows and macOS | [ASPB23-75](https://helpx.adobe.com/security/products/after_effects/apsb23-75.html) |
| Adobe Substance 3D Designer | 13.0.0 and earlier versions | All | [APSB23-76](https://helpx.adobe.com/security/products/substance3d_designer/apsb23-76.html) |


## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)).