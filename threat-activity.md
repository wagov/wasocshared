# WA SOC - Recent Threat Activity (February 2023)


VMWare ESXi exposed to the internet has been heavily exploited by [ESXiArgs ransomware](https://www.bleepingcomputer.com/news/security/massive-esxiargs-ransomware-attack-targets-vmware-esxi-servers-worldwide/) worldwide, though no regional incidents have been seen yet. To stay ontop of internet facing assets, please subscribe to daily exposure alerts from **[The ShadowServer Foundation](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/)** (a highly trusted free resource sponsored by both [AusCERT](https://auscert.org.au/) and the [APNIC Foundation](https://apnic.foundation/) as part of the [ShadowServer Alliance](https://www.shadowserver.org/news/shadowserver-alliance-launch/)). The WA SOC is investigating the best way to incorporate similar alerts into our whole of sector vulnerability monitoring services.

Recently [search engines have been outfoxed by malvertisements](https://arstechnica.com/information-technology/2023/02/until-further-notice-think-twice-before-using-google-to-download-software/) and users utilising search engines to download and install software are highly exposed. Where possible deploying enterprise wide browser policies to [restrict](https://github.com/wagov/Essential8-GPOs#user-application-hardening-7-gpos) or [block](https://github.com/wagov/Essential8-GPOs/blob/main/ublock-origin.md) advertising is strongly recommended.

Browsers ([Microsoft Edge, Chrome, Safari, Firefox](advisories.md)) continue to be heavily targeted by threat actors, along with edge infrastructure ([Cisco, Fortinet, F5, Citrix, VMWare](advisories.md)). 

**Phishing activity remains high** across all organisations with multiple incidents detected weekly. Please refer to the below guides to ensure all external and internal signins are appropriately monitored.

- [Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue, PRT, OAuth)](https://jeffreyappel.nl/tips-for-preventing-against-new-modern-identity-attacks-aitm-mfa-fatigue-prt-oauth/)
    - [Enabling MFA number matching to mitigate MFA fatigue attacks (AAD)](https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match#enable-number-matching-in-the-portal)
- [How to implement Defender for Identity and configure all prerequisites](https://jeffreyappel.nl/how-to-implement-defender-for-identity-and-configure-all-prerequisites/)

