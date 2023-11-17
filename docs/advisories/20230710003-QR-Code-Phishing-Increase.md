# Increase-in-QR-Code-Phishing-Technique - 20230710003

Overview
--------

The Office of Digital Government (DGov) has observed a number of effective email phishing campaigns that contain QR code images instead of phishing links.

DGov has also observed these campaigns styling emails and phishing pages to impersonate organisations and tailoring the email contents for individuals, referring to the recipient by name. Victims are pressured into taking action through false claims such as (but not limited to) sudden password expiry and loss of access to services.

Victims typically then scan the QR code with their mobile device and are taken to a phishing page impersonating Microsoft login pages.

In addition, **there is evidence that the phishing campaigns use** [**Adversary-in-the-Middle (AiTM)**](https://www.microsoft.com/en-us/security/blog/2022/07/12/from-cookie-theft-to-bec-attackers-use-aitm-phishing-sites-as-entry-point-to-further-financial-fraud/ "https://www.microsoft.com/en-us/security/blog/2022/07/12/from-cookie-theft-to-bec-attackers-use-aitm-phishing-sites-as-entry-point-to-further-financial-fraud/") **techniques to bypass multi-factor authentication (MFA)**.

What is the threat?
-------------------

-   Accounts may be compromised and used to further distribute phishing emails.
-   Potential loss of confidential data.

What has been observed in Western Australia?
-----------------------

-   Threat actors use a mix of legitimate and known bad email addresses to send the phishing emails with varying degrees of success to the target's inbox.
-   DGov has observed credentials being leaked from these campaigns.

Recommendations
------------------------------------

While avoiding QR code scans may be impractical, taking certain [proactive measures](https://cisomag.com/think-before-you-scan-malicious-qr-codes-in-the-wild/ "https://cisomag.com/think-before-you-scan-malicious-qr-codes-in-the-wild/") may help mitigate the risks associated with QR code technology.

- Make sure that users are running security software on any mobile device that has access to corporate resources. The software should be able to protect against device takeover attacks, phishing attacks and other mobile device exploits.
- [Educate users on the cybersecurity dangers](https://www.techtarget.com/searchsecurity/post/4-ways-to-build-a-thoughtful-security-culture "https://www.techtarget.com/searchsecurity/post/4-ways-to-build-a-thoughtful-security-culture") associated with scanning QR codes. Otherwise, users may not realize that QR codes can be problematic.
- Implement [multifactor authentication (MFA)](https://www.techtarget.com/searchsecurity/definition/multifactor-authentication-MFA "https://www.techtarget.com/searchsecurity/definition/multifactor-authentication-mfa") requirements across the organization as an interim, and then gradually work on adopting an authentication solution that does not rely on passwords. Many QR code-based attacks are designed to trick users into entering their passwords so that cybercriminals can steal their credentials. Working toward the elimination of passwords can help to thwart these types of attacks.Do not log in to an application or service via a QR code.
- Remember, there is no need to scan a QR code to receive money. So, never believe it when someone encourages you to do so.
- Never initiate the payment, if you get a notification to put any sensitive information when you scan a QR code.
- Avoid scanning random QR codes from suspicious or unknown sources.
- Do not scan QR codes received via emails from unknown sources.
- Ensure the QR is original and not pasted over with another one.
- Use QR scanner software to view the URL before clicking on it.

References
----------

- [**QR Codes: A Growing Vulnerability to Cybercrimes - Infosecurity Magazine**](https://www.infosecurity-magazine.com/opinions/qr-codes-vulnerability-cybercrimes/#:~:text=QR%20Code%20Fraud%20is%20Rampant&text=In%20fact%2C%20many%20don%27t,information%20and%20inserts%20digital%20infections. "https://www.infosecurity-magazine.com/opinions/qr-codes-vulnerability-cybercrimes/#:~:text=qr%20code%20fraud%20is%20rampant&text=in%20fact%2c%20many%20don%27t,information%20and%20inserts%20digital%20infections.")
- [**Understanding QR code security issues for enterprise devices - TechTarget**](https://www.techtarget.com/searchmobilecomputing/tip/Understanding-QR-code-security-issues-for-enterprise-devices)
