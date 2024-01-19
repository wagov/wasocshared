# Drupal Releases Security Advisory for Bypass Vulnerability in Drupal Core - 20230426007

## Overview

Drupal has released an advisory that highlights a 'moderately critical' access bypass vulnerability in Drupal Core.

Due to incorrect file path sanitisation, an actor may be able to gain access to private files in certain situations.

Drupal states that the vulnerability is not mass exploitable.

## What is the vulnerability?

[Drupal core - Moderately critical - Access bypass - SA-CORE-2023-005](https://www.drupal.org/sa-core-2023-005)

There are currently no CVE's associated with this vulnerability.

## What is vulnerable?

The vulnerability affects the following products:

- Drupal 7
- All Drupal 7 sites on Windows web servers are vulnerable.
- Drupal 7 sites on Linux web servers are vulnerable with certain file directory structures, or if a vulnerable contributed or custom file access module is installed.
- Drupal 9 and 10
- Drupal 9 and 10 sites are only vulnerable if certain contributed or custom file access modules are installed.

## What has been observed?

CISA has issued an alert for the vulnerability and encourages users and administrators to review the Drupal security advisory and apply the relevant updates.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices: [Drupal core - Moderately critical - Access bypass - SA-CORE-2023-005](https://www.drupal.org/sa-core-2023-005).

## Additional References

- [CISA - Drupal Releases Security Advisory to Address Vulnerability in Drupal Core](https://www.cisa.gov/news-events/alerts/2023/04/21/drupal-releases-security-advisory-address-vulnerability-drupal-core)
