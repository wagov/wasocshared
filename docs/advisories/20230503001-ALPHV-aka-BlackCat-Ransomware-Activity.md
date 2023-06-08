# ALPHV (aka BlackCat) Ransomware Activity - 20230503001

## Overview

The WA SOC has observed reports of recent activity for the Ransomware-as-a-Service organisation ALPHV (aka BlackCat) from within Australia.

As stated in [ACSC's ALPHV profile](https://www.cyber.gov.au/about-us/advisories/2022-004-acsc-ransomware-profile-alphv-aka-blackcat), the ACSC is aware of ALPHV targeting government and critical infrastructure organisations, as well as the energy, finance, construction and other sectors.

ALPHV is known to use encryption of files, threats of data leaks and Distributed Denial of Service (DDOS) attacks if victims do not comply with their demands.

Some common tactics used by ALPHV are:

- Exploiting known vulnerabilities or common security misconfigurations.
- Using legitimate credentials purchased, brute-forced or gained in phishing attacks, including credentials for Remote Desktop Protocol (RDP) connections and commercial Virtual Private Network (VPN) products.
- Utilising PowerShell to alter Windows Defender security settings.
- Utilising PsExec for lateral movement, tool transfer and execution.
- Utilising the publicly available penetration testing tool CobaltStrike for network access and lateral movement.
- Exfiltrating data to publicly available cloud file-sharing services.

## Recommendation

The WA SOC recommends administrators remain vigilant for related activity within their organisation and review [ACSC's ALPHV profile](https://www.cyber.gov.au/about-us/advisories/2022-004-acsc-ransomware-profile-alphv-aka-blackcat) for more detailed information and potential mitigations.
