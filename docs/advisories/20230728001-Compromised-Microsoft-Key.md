# Compromised Microsoft Key - 20230728001

## Overview

Microsoft and CISA recently disclosed a security incident impacting multiple customers of Exchange Online and Outlook.com. According to Microsoft, this incident stemmed from a threat actor attributed to China, Storm-0558, acquiring a private encryption key (MSA key) and using it to forge access tokens for Outlook Web Access (OWA) and Outlook.com.

## What is the vulnerability?

The threat actor reportedly exploited two security issues in Microsoft’s token verification process.

## What is vulnerable?

Microsoft have said that Outlook.com and Exchange Online were the only applications known to have been affected via the token forging technique.

- Outlook.com
- Exchange Online

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

No customer action is required to prevent threat actors from using the techniques described above to access Exchange Online and Outlook.com.

- [Analysis of Storm-0558 techniques](https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/)

## Additional References

- [Compromised Microsoft Key](https://www.wiz.io/blog/storm-0558-compromised-microsoft-key-enables-authentication-of-countless-micr)
- [Microsoft mitigates China-based threat actor Storm-0558 targeting of customer email](https://msrc.microsoft.com/blog/2023/07/microsoft-mitigates-china-based-threat-actor-storm-0558-targeting-of-customer-email/)
