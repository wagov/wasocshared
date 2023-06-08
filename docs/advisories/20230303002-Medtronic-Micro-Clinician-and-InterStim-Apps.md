# Medtronic Micro Clinician and InterStim Apps - 20230303002

## Overview

Medtronic Clinician (A51200) and InterStim X Clinicain App (A51300) contain a vulnerability that exists under certain reset conditions, which could cause the clinician application’s custom password to be reset to a default password. This could result in unauthorized control of the clinician therapy application, which has greater control over therapy parameters than the patient app. Changes still cannot be made outside of the established therapy parameters of the programmer. To gain unauthorized access, an individual would need physical access to the Smart Programmer.

## What is the vulnerability?

[**CVE-2023-25931**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25931) - [**UNVERIFIED PASSWORD CHANGE CWE-620**](https://cwe.mitre.org/data/definitions/620.html)

An unverified password change allows successful exploitation which could cause the clinician application’s custom password to be reset to default, resulting in unauthorized control of the clinician therapy application.

## What is vulnerable?

The vulnerability affects the following versions of Medtronic Clinician Apps:

- Micro Clinician (A51200)
- InterStim X Clinician (A51300)

## Recommendation

The following mitigations have been provided by Medtronic:

- An app update is available as of February 23, 2023 that will fix the vulnerability.
- Users should refer to the Medtronic [Security Bulletin](https://global.medtronic.com/xg-en/product-security/security-bulletins/pelvic-health-interstim-micro.html) for the correct Medtronic Support contact for help updating the app.  

## Additional References

CISA also provides a section for [control systems security recommended practices](https://us-cert.cisa.gov/ics/Recommended-Practices) on the ICS webpage at [cisa.gov/ics](https://cisa.gov/ics). Several CISA products detailing cyber defense best practices are available for reading and download, including [Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies](https://us-cert.cisa.gov/sites/default/files/recommended_practices/NCCIC_ICS-CERT_Defense_in_Depth_2016_S508C.pdf).

Additional mitigation guidance and recommended practices are publicly available on the ICS webpage at [cisa.gov/ics](https://cisa.gov/ics) in the technical information paper, [ICS-TIP-12-146-01B--Targeted Cyber Intrusion Detection and Mitigation Strategies](https://www.cisa.gov/uscert/ics/tips/ICS-TIP-12-146-01B).
