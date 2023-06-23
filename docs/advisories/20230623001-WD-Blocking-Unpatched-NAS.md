# Western Digital 'My Cloud' Remote Code Execution - 20230623001

## Overview

Western Digital has stated that it has blocked unpatched My Cloud devices from being able to connect to Western Digital's cloud services as of June 15, 2023. This is in response to a severe vulnerability that allows unauthenticated users to gain remote code execution that is being actively exploited.

## What is the vulnerability?

[**CVE-2022-36327**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36327) - CVSS v3 Base Score: ***9.8***

## What is vulnerable?

The vulnerability affects the following products:

- My Cloud PR2100 - firmware versions older than 5.26.202
- My Cloud PR4100 - firmware versions older than 5.26.202
- My Cloud EX4100 - firmware versions older than 5.26.202
- My Cloud EX2 Ultra - firmware versions older than 5.26.202
- My Cloud Mirror G2 - firmware versions older than 5.26.202
- My Cloud DL2100 - firmware versions older than 5.26.202
- My Cloud DL4100 - firmware versions older than 5.26.202
- My Cloud EX2100 - firmware versions older than 5.26.202
- My Cloud - firmware versions older than 5.26.202
- WD Cloud - firmware versions older than 5.26.202
- My Cloud Home – firmware versions older than 9.4.1-101
- My Cloud Home Duo – firmware versions older than 9.4.1-101
- SanDisk ibi – firmware versions older than 9.4.1-101

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices: [Western Digital](https://www.westerndigital.com/support/product-security/wdc-23006-my-cloud-firmware-version-5-26-202)

## Additional References

- [Bleeping Computer- Western Digital boots outdated NAS devices off of My Cloud](https://www.bleepingcomputer.com/news/security/western-digital-boots-outdated-nas-devices-off-of-my-cloud/)
