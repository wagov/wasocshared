# Critical vulnerabilities in Citrix Gateway and Application Delivery Controller (ADC) devices - 20221215001

## Overview

This Alert is relevant to organisations who deploy and maintain configurations for Citrix appliances to facilitate remote access for their users. The Alert is intended to be understood by slightly more technical users who maintain systems – there is no action for the end users to take.

The Australian Cyber Security Centre (ACSC) is aware of a critical vulnerability affecting many versions of Citrix Gateway and ADC.  Citrix ADC are widely used by organisations to provide remote desktop services to remote users, including allowing users to work from home.

## What is the vulnerability ?

Exploitation of the vulnerability could allow a malicious actor to perform remote code execution against hosts running the affected versions of Citrix.

**[CVE-2022-27518](https://www.tenable.com/blog/cve-2022-27518-unauthenticated-rce-in-citrix-adc-and-gateway)** - Unauthenticated Remote Code Execution (RCE) in Citrix ADC and Gateway.

## What is vulnerable ?

The RCE vulnerability is impacting **Citrix ADC** or **Citrix Gateway** when configured as a **Security Assertion Markup Language (SAML)** service provider (SP) or a **SAML** identity provider (IdP).

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

The ACSC is aware the vulnerability may have been exploited in the wild. The ACSC is not aware of successful exploitation attempts against Australian organisations.

## Recommendation

Australian organisations that use **Citrix Gateway** or **ADC** should install the latest updated versions, **read Citrix Security Bulletin CTX474995** and take the recommended actions.

- The Security Bulletin published by Citrix is available at: <https://support.citrix.com/article/CTX474995/citrix-adc-and-citrix-gateway-security-bulletin-for-cve202227518>
- A Cybersecurity Advisory has also been published by the United States' National Security Agency (NSA), which is available at: <https://www.nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance/>

### Reference

- Citrix security bulletin [CTX457836](https://support.citrix.com/article/CTX474995/citrix-adc-and-citrix-gateway-security-bulletin-for-cve202227518)
- NSA's advisory [APT5: Citrix ADC Threat Hunting Guidance](https://media.defense.gov/2022/Dec/13/2003131586/-1/-1/0/CSA-APT5-CITRIXADC-V1.PDF)
