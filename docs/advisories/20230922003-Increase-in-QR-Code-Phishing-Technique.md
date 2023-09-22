  
# Increase in QR Code Phishing (Quishing)- 20230922003

## Overview

The WA SOC has observed an increase in QR code related phishing across multiple organisations. Building up on our previous advisory dated; 10th of July 2023, found [here](20230710003-QR-Code-Phishing-Increase.md) we are providing further guidance and notification to inform organisations about the increased use of Quishing activity by Threat actors.



## Delivery

The primary method of delivery of the QR codes are via phishing emails sent directly to user's inbox by compromised email addresses of legitimate companies.

## What is the threat?

The QR code for Quishing will most likely be scanned with user's mobile phone, and any clicks events or URL re-directs would not be detected by SIEM/Email security gateway.


## Recommendation:

- Increase end-user awareness on phishing attacks from QR code.
- Agencies' Sec Ops team(s) can perform proactive KQL threat hunting on possible QR Code phishing email sent to agencies' user(s).
- Upon finding any successfully delivered phishing email to user’s inbox, confirm with user(s) whether they scanned the QR code and filled-in any credentials.

## Detection

Data sources, detection queries and triage information for the Quishing attacks are provided on the [**WASOC TTP Detection Guideline page as shown below**](../guidelines/TTP_Hunt/ADS_forms/T1566.001-QR-CodePhishingAttachment(Quishing).md).


{% include "./guidelines/TTP_Hunt/ADS_forms/T1566.001-QR-CodePhishingAttachment(Quishing).md" %}