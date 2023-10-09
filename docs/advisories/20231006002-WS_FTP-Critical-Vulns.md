# WS_FTP Server Critical Vulnerabilities - 20231006002

## Overview

A patch for WS_FTP Server has been released addressing a number of serious vulnerabilities, including a **CVSS: 10** vulnerability.

An attacker could leverage this vulnerability to perform file operations (delete, rename, rmdir, mkdir) on files and folders outside of their authorized WS_FTP folder path and folders on the underlying operating system.

## What is the vulnerability?

- [**CVE-2023-40044**](https://nvd.nist.gov/vuln/detail/CVE-2023-40044) - CVSS v3 Base Score: ***10.0***
- [**CVE-2023-42657**](https://nvd.nist.gov/vuln/detail/CVE-2023-42657) - CVSS v3 Base Score: ***9.9***
- [**CVE-2023-40045**](https://nvd.nist.gov/vuln/detail/CVE-2023-40045) - CVSS v3 Base Score: ***8.3***
- [**CVE-2023-40046**](https://nvd.nist.gov/vuln/detail/CVE-2023-40046) - CVSS v3 Base Score: ***8.2***

For a full list of vulnerabilities and their descriptions, please review the [post by Progress](https://community.progress.com/s/article/WS-FTP-Server-Critical-Vulnerability-September-2023).

## What is vulnerable?

All versions previous versions to the patch of WS_FTP Server are affected by the vulnerabilities.

The vulnerabilities affects the following products:

- WS_FTP Server prior to 8.7.4 and 8.8.2

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe based on the recommendations in the [Patch Management Guideline](../guidelines/patch-management.md):

- [Progress - WS_FTP Server Critical Vulnerability - (September 2023)](https://community.progress.com/s/article/WS-FTP-Server-Critical-Vulnerability-September-2023)
