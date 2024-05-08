# Google Android Security Advisory May 2024 - 20240508001

## Overview

Multiple vulnerabilities have been discovered in Google Android OS, the most severe of which could allow for privilege escalation.

Successful exploitation of the most severe of these vulnerabilities could allow for privilege escalation. Depending on the privileges associated with the exploited component, an attacker could then install programs; view, change, or delete data; or create new accounts with full rights.

## What is vulnerable?

Vulnerabilities are grouped under the component they affect. Issues are described in the tables below and include CVE ID, associated references, type of vulnerability, severity, and updated AOSP versions (where applicable):

### Framework

The most severe vulnerability in this section could lead to local escalation of privilege with no additional execution privileges needed.

| CVE            | References                                                                                                          | Type | Severity | Updated AOSP versions |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ---- | -------- | --------------------- |
| CVE-2024-0024  | [A-293602317](https://android.googlesource.com/platform/frameworks/base/+/6a9250ec7fc9801a883cedd7860076f42fb518ac) | EoP  | High     | 12, 12L, 13, 14       |
| CVE-2024-0025  | [A-279428283](https://android.googlesource.com/platform/frameworks/base/+/d49662560e366dbf69bf7d59d00e73905d03e6d5) | EoP  | High     | 12, 12L, 13, 14       |
| CVE-2024-23705 | [A-293602970](https://android.googlesource.com/platform/frameworks/base/+/032bee6dc118ce1cc3fde92463b2954c1450f2e8) | EoP  | High     | 12, 12L, 13, 14       |
| CVE-2024-23708 | [A-293301736](https://android.googlesource.com/platform/frameworks/base/+/0c095c365ede36257e829769194f9596a598e560) | EoP  | High     | 12, 12L, 13, 14       |

### System

The most severe vulnerability in this section could lead to local escalation of privilege with no additional execution privileges needed.

| CVE            | References                                                                                                                         | Type | Severity | Updated AOSP versions |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---- | -------- | --------------------- |
| CVE-2024-23706 | [A-328068777](https://android.googlesource.com/platform/packages/modules/HealthFitness/+/6e6896c3fd8139779ff8d51a99ee06667e849d87) | EoP  | Critical | 14                    |
| CVE-2024-0043  | [A-295549388](https://android.googlesource.com/platform/packages/modules/Permission/+/8141e8f4dd77b9f8fb485e23ddf028c57fcd4fca)    | EoP  | High     | 12, 12L, 13, 14       |
| CVE-2024-23707 | [A-316891059](https://android.googlesource.com/platform/packages/apps/Settings/+/f1d0079c91734168c150f839168544f407b17b06)         | EoP  | High     | 14                    |
| CVE-2024-23709 | [A-317780080](https://android.googlesource.com/platform/external/sonivox/+/3f798575d2d39cd190797427d13471d6e7ceae4c)               | ID   | High     | 12, 12L, 13, 14       |

### Kernel

The vulnerability in this section could lead to local escalation of privilege in the kernel with no additional execution privileges needed.

| CVE           | References                                                                    | Type | Severity | Subcomponent |
| ------------- | ----------------------------------------------------------------------------- | ---- | -------- | ------------ |
| CVE-2023-4622 | [A-299123598](https://android.googlesource.com/kernel/common/+/e6ed59127c865) | EoP  | High     | Unix         |

### Kernel LTS

The following kernel versions have been updated. Kernel version updates are dependent on the version of Android OS at the time of device launch.

| References  | Android Launch Version | Kernel Launch Version | Minimum Update Version |
| ----------- | ---------------------- | --------------------- | ---------------------- |
| A-304554927 | 12                     | 5.4                   | 5.4.254                |
| A-304560886 | 13                     | 5.15                  | 5.15.123               |
| A-304560975 | 12                     | 5.10                  | 5.10.189               |
| A-304560987 | 13                     | 5.10                  | 5.10.189               |
| A-304561454 | 14                     | 5.15                  | 5.15.123               |
| A-304561455 | 14                     | 6.1                   | 6.1.43                 |

### Arm components

These vulnerabilities affect Arm components and further details are available directly from Arm. The severity assessment of these issues is provided directly by Arm.

| CVE           | References     | Severity | Subcomponent |
| ------------- | -------------- | -------- | ------------ |
| CVE-2023-6363 | A-303632069 \* | High     | Mali         |
| CVE-2024-1067 | A-329506905 \* | High     | Mali         |
| CVE-2024-1395 | A-329506991 \* | High     | Mali         |

### MediaTek components

These vulnerabilities affect MediaTek components and further details are available directly from MediaTek. The severity assessment of these issues is provided directly by MediaTek.

| CVE            | References                    | Severity | Subcomponent |
| -------------- | ----------------------------- | -------- | ------------ |
| CVE-2023-32871 | A-309364193 M-ALPS08355514 \* | High     | DA           |
| CVE-2023-32873 | A-327972597 M-ALPS08583919 \* | High     | keyInstall   |
| CVE-2024-20056 | A-327973818 M-ALPS08528185 \* | High     | preloader    |
| CVE-2024-20057 | A-327973819 M-ALPS08587881 \* | High     | keyInstall   |

### Qualcomm components

These vulnerabilities affect Qualcomm components and are described in further detail in the appropriate Qualcomm security bulletin or security alert. The severity assessment of these issues is provided directly by Qualcomm.

| CVE            | References                                                                                                                                         | Severity | Subcomponent |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------ |
| CVE-2024-21471 | [A-318393843](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/809ee24fe5607ecc72e9cde737410ad94264ff91) | High     | Display      |
| CVE-2024-21475 | [A-323919078](https://git.codelinaro.org/clo/la/kernel/msm-4.14/-/commit/bdb176c8afd933f26a135aba4d4a0384fb13d156)                                 | High     | Video        |
| CVE-2024-23351 | [A-323918714](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/d7c818d1695cac10489ef1fe28e0d38c602656d9) | High     | Display      |
| CVE-2024-23354 | [A-323919320](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/88eb3006d32f72c53039fd37ea45926dee08882b) | High     | Display      |

### Qualcomm closed-source components

These vulnerabilities affect Qualcomm closed-source components and are described in further detail in the appropriate Qualcomm security bulletin or security alert. The severity assessment of these issues is provided directly by Qualcomm.

| CVE            | References     | Severity | Subcomponent            |
| -------------- | -------------- | -------- | ----------------------- |
| CVE-2023-33119 | A-309461253 \* | High     | Closed-source component |
| CVE-2023-43529 | A-309460466 \* | High     | Closed-source component |
| CVE-2023-43530 | A-309461471 \* | High     | Closed-source component |
| CVE-2023-43531 | A-309461198 \* | High     | Closed-source component |
| CVE-2024-21477 | A-323918871 \* | High     | Closed-source component |
| CVE-2024-21480 | A-323918475 \* | High     | Closed-source component |

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- Users are advised to apply appropriate patches to mitigate against potential threats.

- [Android Security Bulletin—May 2024](https://source.android.com/docs/security/bulletin/2024-05-01)

## Additional References

- [CIS - Multiple Vulnerabilities in Google Android OS Could Allow for Privilege Escalation](https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-google-android-os-could-allow-for-privilege-escalation_2024-045)
