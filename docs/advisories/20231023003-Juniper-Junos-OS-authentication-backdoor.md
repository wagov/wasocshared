# Juniper Junos OS authentication backdoor - 20231023003

## Overview

An Incorrect Default Permissions vulnerability in Juniper Networks Junos OS allows an unauthenticated attacker with local access to the device to create a backdoor with root privileges. The issue is caused by improper directory permissions on a certain system directory, allowing an attacker with access to this directory to create a backdoor with root privileges.

## What is the vulnerability?

[**CVE-2023-44194**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44194) - CVSS v3 Base Score: ***8.4***

## What is vulnerable?

This issue affects Juniper Networks Junos OS:

- All versions prior to 20.4R3-S5;
- 21.1 versions prior to 21.1R3-S4;
- 21.2 versions prior to 21.2R3-S4;
- 21.3 versions prior to 21.3R3-S3;
- 21.4 versions prior to 21.4R3-S1.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

Review the following bulletin for further information: [Juniper Junos OS 2023-10 Security bulletin](https://supportportal.juniper.net/s/article/2023-10-Security-Bulletin-Junos-OS-An-unauthenticated-attacker-with-local-access-to-the-device-can-create-a-backdoor-with-root-privileges-CVE-2023-44194?language=en_US)
