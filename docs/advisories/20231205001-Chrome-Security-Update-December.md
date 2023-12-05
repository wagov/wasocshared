# Google Chrome Critical Security Updates - 20231205001

## Overview

Google has released an update for the Chrome web browser to address multiple serious security vulnerabilities.

Google is aware that an exploit for CVE-2023-6345 exists in the wild.

## What is the vulnerability?

- Integer overflow in Skia [**CVE-2023-6345**](https://nvd.nist.gov/vuln/detail/CVE-2023-6345) - CVSS v3 Base Score: ***9.6 - Active Exploitation*** 
- Type Confusion in Spellcheck [**CVE-2023-6348**](https://nvd.nist.gov/vuln/detail/CVE-2023-6348) - CVSS v3 Base Score: ***N.A***
- Use after free in Mojo [**CVE-2023-6347**](https://nvd.nist.gov/vuln/detail/CVE-2023-6347) - CVSS v3 Base Score: ***8.8***
- Use after free in WebAudio [**CVE-2023-6346**](https://nvd.nist.gov/vuln/detail/CVE-2023-6346) - CVSS v3 Base Score: ***8.8***
- Out of bounds memory access in libavif [**CVE-2023-6350**](https://nvd.nist.gov/vuln/detail/CVE-2023-6350) - CVSS v3 Base Score: ***8.8***
- Use after free in libavif [**CVE-2023-6351**](https://nvd.nist.gov/vuln/detail/CVE-2023-6351) - CVSS v3 Base Score: ***8.8***

## What is vulnerable?

The vulnerability affects the following Google products:

- Google Chrome prior to version 119.0.6045.199

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)):

- [Google - Stable Channel Update for Chrome Desktop](https://chromereleases.googleblog.com/2023/11/stable-channel-update-for-desktop_28.html)


