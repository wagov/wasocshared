# Ivanti Neurons for ITSM and Standalone Sentry Security Updates - 20240322002

## Overview

The WA SOC has been made aware of released patches for two 2023 Ivanty critical vulnerabilities CVE-2023-41724 and CVE-2023-46808 in Ivanti Neurons and Ivanti Standalone Sentry


## What is vulnerable?

| CVE    | Severity     | CVSS | Product(s) Affected | Summary | Dated |
| ------ | ------------ | ---- | ------------------- | ------- | ----- |
| [CVE-2023-41724](https://forums.ivanti.com/s/article/KB-CVE-2023-41724-Remote-Code-Execution-for-Ivanti-Standalone-Sentry?language=en_US) | **Critical** | 9.6 | **versions before 9.17.0, 9.18.0, and 9.19.0** |  (Remote Code Execution) for Ivanti Standalone Sentry <br>An unauthenticated threat actor can execute arbitrary commands on the underlying operating system of the appliance within the same physical or logical network. | 21/03/2024 |
| [CVE-2023-41724](https://forums.ivanti.com/s/article/CVE-2023-46808-Authenticated-Remote-File-Write-for-Ivanti-Neurons-for-ITSM?language=en_US) | **Critical** | 9.9 | **versions before 9.17.0, 9.18.0, and 9.19.0** | (Authenticated Remote File Write) for Ivanti Neurons for ITSM <br> An authenticated remote user can perform file writes to ITSM server. Successful exploitation can be used to write files to sensitive directories which may allow attackers execution of commands in the context of web application’s user.  | 21/03/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- [KB-CVE-2023-41724 (Remote Code Execution) for Ivanti Standalone Sentry](https://forums.ivanti.com/s/article/KB-CVE-2023-41724-Remote-Code-Execution-for-Ivanti-Standalone-Sentry?language=en_US)
- [CVE-2023-46808 (Authenticated Remote File Write) for Ivanti Neurons for ITSM](https://forums.ivanti.com/s/article/CVE-2023-46808-Authenticated-Remote-File-Write-for-Ivanti-Neurons-for-ITSM?language=en_US)

## Additional References

- 
