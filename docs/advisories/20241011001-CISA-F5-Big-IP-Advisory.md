# CISA Publishes F5 BIG-IP Advisory - 20241011001

## Overview

CISA has urged organisations to ensure that those who are using F5 BIG-IP solutions to follow best practices regarding encrypting persistent cookies. F5 have released a best practice guide for those using BIG-IP 11.x-17x in order to encrypt cookies between the BIG-IP system and clients.

## What has been observed?

CISA has observed cyber threats that have leveraged unecrypted persistent cookies managed by the BIG-IP Local Traffic Manager (LTM) module to enumerate other non-internet facing devices on the network.

A malicious cyber actor could leverage the information gathered from unencrypted persistence cookies to infer or identify additional network resources and potentially exploit vulnerabilities found in other devices present on the network.  

## Recommendation

The WA SOC recommends administrators perform the following:

- Review the CISA Advisory: <https://www.cisa.gov/news-events/alerts/2024/10/10/best-practices-configure-big-ip-ltm-systems-encrypt-http-persistence-cookies>
- Review the F5 BIG-IP Best Practice: <https://my.f5.com/manage/s/article/K14784>
    - Review '**Prerequisites and Description**' sections to perform scoping of any potentially related activities,
    - Review and follow '**Procedures**' section where applicable to ensure best practices are being followed.

