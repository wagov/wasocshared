# Number Matching in Multifactor Authentication - 20230110001

## Overview

Cyber threat actors who have obtained a user's password know they can enter it into an identity platform that uses mobile push-notification-based MFA to generate hundreds of prompts on the user's device over a short period of time.  This activity understandably annoys the user, who may---accidentally or from MFA fatigue--- press accept to stop the prompts. Alternatively, the prompts may confuse the user, who may assume one of the requests is legitimate and approve. As a result of any of these possible scenarios, the user unknowingly grants the cyber threat actor access to their account.

MFA is an essential practice to reduce the threat of cyber threat actors using compromised credentials to gain access to and conduct malicious activity on networks. However, not all forms of MFA are equally secure. Some forms are vulnerable to:

- Phishing,
- "push bombing" attacks,
- exploitation of Signaling System 7 (SS7) protocol vulnerabilities, and/or
- SIM Swap attacks.

## What is the vulnerability ?

These attacks, if successful, may allow a threat actor to gain access to MFA authentication credentials or bypass MFA and access the MFA-protected systems.

## Recommendation

if an organization that uses mobile push-notification-based MFA is unable to implement phishing-resistant MFA, CISA recommends enabling "number matching" on MFA configurations to prevent MFA fatigue.

Number matching is a setting that forces the user to enter numbers from the identity platform into their app to approve the authentication request.  Figures 3 and 4 provide the user's view of an identity platform login screen that uses number matching.

![](../images/2023-01-10_11-33%20MFA.png)

The number matching requirement mitigates MFA fatigue by:

- Requiring access to the login screen to approve requests. Users cannot approve requests without entering the numbers on the login screen.
- Discouraging prompt spam. Each prompt generates a unique set of numbers for every login request. As the user cannot accept the prompts without knowing the numbers, generating multiple prompts is not effective.

## Best Practices for using MFA with Number Matching

**Train users to report**. In addition to implementing the mitigations noted above, CISA recommends training users to report unknown or bulk confirmation requests. Organizations should provide periodic cybersecurity training that includes:

- MFA fatigue
- How to recognize MFA spam
- How to report unknown confirmation request

**Investigate denied push notifications**. CISA recommends that organizations investigate denied push notification request occurrences. When a user denies an MFA requests, they should alert their IT security team, who should investigate the root cause. MFA checks are done after the first factor (e.g., the user's password) is satisfied, so denied MFA requests could mean the user's password is compromised.

## Additional References

- Microsoft MFA Number Matching [https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match](https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match)
- Microsoft Network Policy Server (NPS) with Azure AD Multi-Factor Authentication [https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-nps-extension](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-nps-extension)
- CISA - Implementing Number Matching in MFA applications [https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
- CISA - Implementing Phishing-Resistant MFA [https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)
- Duo Verified Push [Duo Verified Push - [Duo Administration - Policy & Control](https://duo.com/docs/policy#verified-push)
- Okta TOTP - [https://help.okta.com/oie/en-us/Content/Topics/identity-engine/authenticators/configure-okta-verify-options.htm](https://help.okta.com/oie/en-us/Content/Topics/identity-engine/authenticators/configure-okta-verify-options.htm)
