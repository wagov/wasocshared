# Ivanti Sentry Administrator Interface API Authentication Bypass - 20230822003

## Overview

A vulnerability has been discovered in Ivanti Sentry, formerly known as MobileIron Sentry. If exploited, this vulnerability enables an unauthenticated actor to access some sensitive APIs that are used to configure the Ivanti Sentry on the administrator portal (port 8443, commonly MICS). Successful exploitation can be used to change configuration, run system commands, or write files onto the system. Ivanti recommends that customers restrict access to MICS to internal management networks and not expose this to the internet.

## What is the vulnerability?

[**CVE-2023-38035**](https://nvd.nist.gov/vuln/detail/CVE-2023-38035) - CVSS v3 Base Score: ***9.8***

**While the issue has a high CVSS score, there is a low risk of exploitation for customers who do not expose port 8443 to the internet.**

## What is vulnerable?

The vulnerability affects the following products:

- Ivanti Sentry (formerly known as MobileIron Sentry) - versions 9.18 and prior.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks...* (refer [Patch Management](../guidelines/patch-management.md)):

[**Ivanti Knowledge Base**](https://forums.ivanti.com/s/article/KB-API-Authentication-Bypass-on-Sentry-Administrator-Interface-CVE-2023-38035?language=en_US)

## Additional References

- [**Ivanti Advisory**](https://forums.ivanti.com/s/article/CVE-2023-38035-API-Authentication-Bypass-on-Sentry-Administrator-Interface?language=en_US)

- [**Ivanti warns of new actively exploited MobileIron zero-day bug**](https://www.bleepingcomputer.com/news/security/ivanti-warns-of-new-actively-exploited-mobileiron-zero-day-bug/)
