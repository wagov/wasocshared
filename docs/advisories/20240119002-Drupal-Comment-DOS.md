# Drupal Releases Patch for DOS Vulnerability - 20240119002

## Overview

Drupal have released a patch for a moderately critical vulnerability in Drupal core. The vulnerability impacts the comment module, an attacker could make comment reply requests that would trigger a denial of service (DOS).

Sites that do not use the Comment module are not affected.

## What is the vulnerability?

The comment module may allow an attacker to abuse a vulnerability that would result in a denial of service. The vulnerability only affects Drupal instances that have the comment module enabled. As of writing there is no CVE or CVSS score associated with the vulnerability.

## What is vulnerable?

The following products and versions are affected:

- Drupal 8.0 to 10.1.7 (inclusive)
- Drupal 10.2 to 10.2.1 (inclusive)

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of 2 weeks:

- [Drupal core - Moderately critical - Denial of Service - SA-CORE-2024-001](https://www.drupal.org/sa-core-2024-001)
