# CISA ICS Advisory: Hitachi Energy IEC 61850 MMS-Server - 20230405001

## Overview
CISA released one Industrial Control Systems (ICS) advisory on March 30, 2023 used within the Energy sector.

## What is the vulnerability?
[**CVE-2022-3353**](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2022-3353) - CVSS v3 ***5.9***: Improper Resource Shutdown or Release

- A vulnerability exists in the IEC 61850 communication stack that affects multiple Hitachi Energy products. An attacker could exploit the vulnerability by using a specially crafted message sequence, to force the IEC 61850 MMS-server communication stack, to stop accepting new MMS-client connections. Already existing/established client-server connections are not affected.

## What is vulnerable? 
For the complete list of affected products, please refer to the CISA Advisory listed below.

## Recommendation
The WA SOC recommends administrators review the list of affected products and apply the listed "Mitigations" as per vendor instructions where applicable: [https://www.cisa.gov/news-events/ics-advisories/icsa-23-089-01](https://www.cisa.gov/news-events/ics-advisories/icsa-23-089-01)