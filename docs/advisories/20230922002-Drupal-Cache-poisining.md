# Drupal Core Cache Poisoning - 20230922002

## Overview

Drupal has released a security advisory to address a vulnerability affecting multiple Drupal versions. A malicious cyber actor could exploit this vulnerability to take control of an affected system.

## What is the vulnerability?

[**SA-CORE-2023-006**](https://www.drupal.org/sa-core-2023-006) - CMSS Score: ***Critical - 16/25***

## What is vulnerable?

The vulnerability affects the following versions of **Drupal Core**:

- \>=8.7.0 \<9.5.11
- \>=10.0 \<10.0.11
- \>= 10.1 \<10.1.4

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks...* (refer [Patch Management](../guidelines/patch-management.md)):

- If you are using Drupal 10.1, update to [Drupal 10.1.4](https://www.drupal.org/project/drupal/releases/10.1.4).
- If you are using Drupal 10.0, update to [Drupal 10.0.11](https://www.drupal.org/project/drupal/releases/10.0.11).
- If you are using Drupal 9.5, update to [Drupal 9.5.11](https://www.drupal.org/project/drupal/releases/9.5.11).
