# Phishing campaign - 20230214001

## Overview
The WA SOC has observed a growing phishing campaign across multiple agencies seeking credential data.

## IOC
- Senders:
    - alessandro.mutti@n-andgroup[.]com
    - Andrew.pitt@n-andgroup[.]com
    - andrea.stradella@n-anditalia[.]com
    - andrea.stroppa@n-anditalia[.]com
- Subject: Attention Required
- IPv4: 5.161.180[.]3

Users clicking the link will be taken to a page on the site pagemaker[.]link which is a legitimate site that is being used by malicious actors.

## Recommendation
The WA SOC recommends administrators apply the advice provided by the ACSC [Phishing - scam emails | Cyber.gov.au](https://www.cyber.gov.au/acsc/view-all-content/threats/phishing).

Additionally:
- Search the phishing emails on Southern Ports’ email security gateway, and delete the phishing emails
- Reset password for the users that have clicked the URLs.
- Add IOC to block list.