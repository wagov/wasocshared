# Microsoft TI Report for Storm-0987 - 20230717001

## Overview

Microsoft Threat Intelligence has released a report detailing the activities of a Russian cybercrime organisation, known as Storm-0978 or RomCom, involved in ransomware and espionage.

## Summary

The primary delivery method is via phishing with lures related to political affairs, targeting mostly European government and military organisations however activity has also been observed in telecommunications and finance industries.

In addition, the actor has trojanised versions of popular software that include Adobe products, Solarwinds products, Advanced IP Scanner, Signal and KeePass. To host the trojanized installers for delivery, Storm-0978 typically registers malicious domains mimicking the legitimate software (for example, the malicious domain _advanced-ip-scaner\[.\]com_).

User education and strong endpoint security are recommended mitigations for defending against Storm-0978 and similar advanced actors. The full report can be read [here](https://www.microsoft.com/en-us/security/blog/2023/07/11/storm-0978-attacks-reveal-financial-and-espionage-motives/).

## Recommended Mitigations

Microsoft recommends the following mitigations to reduce the impact of activity associated with Storm-0978’s operations.

- Turn on cloud-delivered protection in Microsoft Defender Antivirus or the equivalent for your antivirus product. Cloud-based machine learning protections block a majority of new and unknown variants.
- Run EDR in block mode so that Microsoft Defender for Endpoint can block malicious artifacts, if non-Microsoft antivirus doesn’t detect the threat or when Microsoft Defender Antivirus is running in passive mode.
- Defender for Office 365 customers should ensure that Safe Attachments and Safe Links protection is enabled for users with  Zero-hour Auto Purge (ZAP) to remove emails when a URL gets weaponized post-delivery.
- Microsoft 365 Defender customers can turn on attack surface reduction rules to prevent common attack techniques used in ransomware attacks

## Reference

- [Storm-0978 attacks reveal financial and espionage motives](https://www.microsoft.com/en-us/security/blog/2023/07/11/storm-0978-attacks-reveal-financial-and-espionage-motives/)
