# Apple critical security updates - 20221223002

## Overview

Webkit has a vulnerability related to type safety potentially allowing for execution of privileged code if malicious content is loaded.

Apple is aware of a report that this issue may have been actively exploited against versions of iOS released before iOS 15.1.

## What is vulnerable?

[**CVE-2022-42821**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42821): This issue affects devices running versions _**lower**_ than the following:

- Safari 16.2
- tvOS 16.2
- macOS Ventura 13.1
- iOS 15.7.2
- iPadOS 15.7.2
- iOS 16.1.2

This also includes devices running the following MacOS:

- MacOS Monterey
- MacOS Big Sur

## What has been observed ?

CISA has listed this vulnerabilty in their [Known Exploited Vulnerabilties](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog.

## Recommendation

Due to the report of active exploitation, it is strongly recommended to patch this vulnerability within 2 weeks across all affected platforms.
