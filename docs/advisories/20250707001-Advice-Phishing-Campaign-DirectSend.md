# Phishing Campaigns Using M365 Direct Send - 20250707001

## Overview

The WA SOC has been made aware of threat actors abusing the Direct Send feature in Microsoft 365 (M365) in a novel phishing campaign.

This feature allows internal network devices such as printers to send emails **without verification**, permitting threat actors to bypass authentication and deliver spoofed phishing emails inside an organisational network.

## Recommendation

The WA SOC recommends administrators perform the following:

- Varonis blog post: <https://www.varonis.com/blog/direct-send-exploit>
    - Review both '*Detection: What to look for*' and '*Indicators of Compromise (IOCs)*' sections to perform scoping of any potentially related activity,
    - Review '*Real-world example: Direct Send in action*' section to perform discovery of potentially related malicious emails for further investigation,
    - Review the '*Prevention: What you can do to protect your org*' section for relevant information.
