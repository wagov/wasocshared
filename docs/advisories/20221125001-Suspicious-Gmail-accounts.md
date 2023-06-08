# Suspicious Gmail accounts targeting Victorian Government - 20221125001

## Overview

The WA SOC is aware of suspicious emails originating from Gmail accounts being sent to a range of Victorian Government email addresses. The emails contained several attachments and investigation is underway to determine if this campaign is related to a [broader campaign](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)  that has been identified as targeting government accounts worldwide. WA SOC recommends Western Australian Government organisations review this advisory, implement recommendations appropriate to the environment, and remain vigilant to these tactics.

## What is the threat?

Since March 2022, threat actor(s) have been targeting Australian governments with targeted spear-phishing attacks originating from fake Gmail accounts containing several attachments.

While some documents have been assessed as decoys, containing no malicious indicators, other documents have included malicious payloads often via embedded Google Drive links. Notably these emails have multiple recipients in the 'to' and 'cc' fields. It is assessed that the intended targets of these attacks are often in   the 'cc' field of the email to appear innocuous and avoid detection.

**Tactics, Techniques & Procedures (TTP)**

 The following tactics, techniques and procedures have been observed by Victorian Government organisations:

- Multiple Victorian Government organisation recipients both in the 'to' and 'cc' field.  

- Preliminary review of recipients list indicates email addresses are public facing, position-based email accounts

- Multiple documents, mostly containing PDFs on a particular issue or theme.  

- CIRS is currently tracking documents to related to a *Freedom of Information* (FOI) request.  

**Indicators of Compromise (IOCs)**

The following IOCs have been observed by Victorian Government:  

- www[.]tpsgc-pwgsc[.]gc[.]ca
- sydneylivingmuseums[.]com[.]au

**Assessment**

While investigations into this particular campaign are still underway, it is assessed that the current campaign circulating in Victorian Government containing FOI themed emails is likely copycat activity, as opposed to the campaign detailed by TrendMicro.

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.  However, Victorian Government organisations have recently been recipients of suspicious emails with similar characteristics described above.

## Recommendation

- Review the above **IOCs** and search for these in your environment.  
- Review the above **TTPs** and consider reminding staff of organisational requirements regarding opening external links/attachments from unknown or external email addresses.  
- Ensure **DMARC** is enabled where possible.
- Notify the WA SOC if this campaign is identified

### Reference

- [Trend Micro - Earth Preta Spear-Phishing Governments Worldwide](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [AlientVault - Earth Preta Spear-Phishing Governments Worldwide](https://otx.alienvault.com/pulse/637ba3c217cd42bc7e88b448)
