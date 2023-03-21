# Malicious campaign targeting Australian governments and private organisations - 20230321001

## Overview
DGov is aware of an ongoing malicious campaign, targeting websites and services of Australian governments and private organisations. The threat is comprised of a collective of Issue Motivated Groups (IMGs) reportedly seeking retribution in response to alleged religious sensitivities caused by an Australian organisation.

To date, the campaign has been observed conducting [distributed denial-of-service](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.cyber.gov.au%2Facsc%2Fview-all-content%2Fthreats%2Fdenial-service&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539359118%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=kVJ5UlAZnaZsVF%2BKouefpCquKYdqIx059qzoPW0Q55Q%3D&reserved=0) (DDoS), defacement of websites and data breaches of website content from exposed vulnerabilities.

DGov recommends WA government organisations review the below information and undertake actions as required.

## What is the threat?
Known to be operating since November 20233, **Team Insane PK** are a hacktivist group with members believed to be located in Pakistan and Indonesia. The group communicates via Telegram, Twitter (suspended), Instagram and TikTok. Australian operation tags include: #OpAustralia, #OpsJentik, #Team_insane_pk and #insanearmy.

The group, together with primary affiliates including *Eagle Cyber Crew, GanoSecTeam and Mysterious Team Bangladesh,* perform **Distributed Denial-of-Service (DDoS)** attacks against targets which they believe have shown disrespect to their motivational triggers which include; religious respect (Islam), the treatment of Muslim women, Kashmir (#FreeKashmir) and general non-specific human rights.

Currently is not known if there are any monetary or corporate drivers motivating the group.

## What has been observed?
DGov is aware of DDoS attacks on Victorian government networks.

The ACSC has been notified of targeted entities experiencing outages to their external websites but have not received any reports of significant disruption to services as a result of this activity.

Team Insane PK have claimed to have performed successful DDoS attacks against various Australian organisations, including Victorian government.

**Tactics, Techniques and Procedures**

The following tactics, techniques and procedures have been observed in incidents involving Victorian government networks.

**Team Insane PK behaviour includes:**

-   Utilising publicly available exploits, mainly targeting:

-   PHP
-   WordPress

-   Website defacement
-   Distributed Denial of Service (DDoS)
-   Utilisation of credential dumps
-   Google Hacking/DORK queries

**Mitre Attack -- Tactics and Techniques**

-   [TA0043 -- **Reconnaissance**](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fattack.mitre.org%2Ftactics%2FTA0043%2F&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=Eq9UX3x1h%2FcOUNonnka2nYGUXBOqecrLZaDjO%2BhJ9m8%3D&reserved=0)**:**

-   T1595 -- Active Scanning

-   .001 -- Scanning IP Blocks
-   .002 -- Vulnerability Scanning

-   T1592 -- Gather Victim Host Information
-   T1589 -- Gather Victim Identity Information
-   T1590 -- Gather Victim Network Information
-   T1591 -- Gather Victim Org Information
-   T1597 -- Search Closed Sources

-   [TA0001 -- **Initial Access**](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fattack.mitre.org%2Ftactics%2FTA0001%2F&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=mvQ59j4htGwgNbaY4oE9sQ65CCx7brWhrip3Mt8dpc0%3D&reserved=0)**:**

-   T1190 -- Exploit Public-Facing Application
-   T1078 -- Valid Accounts

-   .001 -- Default Accounts
-   .003 -- Local Accounts
-   .004 - Cloud Accounts


## Recommendation


**Actions:**

Defending your internet-facing applications from attack and improving application security will deter attackers from targeting your applications.

CIRS recommends Victorian government organisations:

-   Block the above IOCs that have been observed.
-   Consider blocking connections from TOR nodes to your environment if possible.
-   Review the following guidance and implement the relevant DDoS defences where possible in your environment:

-   [Preparing for and Responding to Denial-of-Service Attacks](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.cyber.gov.au%2Facsc%2Fview-all-content%2Fpublications%2Fpreparing-and-responding-denial-service-attacks&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=HZFeYT6MGBttGb6%2BNjMcI4WTgSgtHbXC8dU16PwifkE%3D&reserved=0) ([cyber.gov.au](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.cyber.gov.au%2F&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=kD9JKV8u8D3LYv7pk6kQg1J8A54zSwRCp4GEJDmhqJM%3D&reserved=0))
-   [Securing Content Management Systems](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.cyber.gov.au%2Facsc%2Fview-all-content%2Fpublications%2Fsecuring-content-management-systems&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=h9gXynVObLcFHz2y33tZ%2BTm8Gp47ioHaUJJarDzcKDk%3D&reserved=0) ([cyber.gov.au](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.cyber.gov.au%2F&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=kD9JKV8u8D3LYv7pk6kQg1J8A54zSwRCp4GEJDmhqJM%3D&reserved=0))

-   Review your DDoS playbook and Incident Response plan
-   If you require assistance with this, please contact CIRS.
-   Maintain a heightened level of monitoring for the above TTP's and any DDoS attack indicators.
-   If you observe any TTP's or IOCs associated with this campaign, please contact CIRS.

**Further Considerations**

-   Ensure WordPress Versions and Plugins are up to date
-   Cloud hosted WAF services can implement a Content Delivery Network (CDN) that includes highly effective DDoS protections

-   [Google Cloud DDoS protection](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcloud.google.com%2Farmor&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=XmGVNDVBMPYhmrpPLJVkTOpKqYg%2FkAO66oZfkT9ayGA%3D&reserved=0)
-   [Azure DDoS protection](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fddos-protection%2Fddos-protection-overview&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=lzy%2BO8kMR2D8ZnQ3fqhQpyh32vF4lemhUeAYbK7lJ%2B0%3D&reserved=0)
-   [AWS DDoS protection](https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Faws.amazon.com%2Fshield%2F&data=05%7C01%7Ccybersecurity%40dpc.wa.gov.au%7Cc76d01d00d6d465e3d1208db29d163b7%7Cd48144b5571f4b689721e41bc0071e17%7C0%7C0%7C638149751539515331%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=mk2rLFWBRkpJPSRMst9MPvlG%2BaBxPO7sYJMs6VLLtvI%3D&reserved=0)

-   Update PHP regularly
-   Secure your network

-   Regularly apply patching to your websites
-   Implement Multifactor Authentication (MFA) wherever is possible
-   Disable unused services
-   Secure your APIs

-   Apply traffic filtering tools
-   Limiting API requests in a given time period, particularly for anonymous requests

 |

## IoCs
103[.]251[.]167[.]21
107[.]189[.]8[.]181
109[.]248[.]150[.]45
128[.]127[.]104[.]80
142[.]44[.]170[.]136
144[.]172[.]118[.]59
159[.]89[.]228[.]253
185[.]220[.]100[.]244
185[.]220[.]100[.]246
185[.]220[.]100[.]247
185[.]220[.]100[.]249
185[.]220[.]100[.]251
185[.]220[.]100[.]252
185[.]220[.]100[.]253
185[.]220[.]100[.]255
185[.]220[.]101[.]130
185[.]220[.]101[.]142
185[.]220[.]101[.]175
185[.]220[.]101[.]185
185[.]220[.]101[.]23
185[.]220[.]101[.]33
185[.]220[.]101[.]35
185[.]220[.]101[.]36
185[.]220[.]101[.]37
185[.]220[.]101[.]42
185[.]220[.]101[.]47
185[.]220[.]101[.]54
185[.]220[.]101[.]60
185[.]220[.]101[.]80
185[.]220[.]103[.]7
185[.]243[.]218[.]110
185[.]243[.]218[.]46
185[.]246[.]188[.]74
186[.]179[.]100[.]99
195[.]235[.]98[.]146
218[.]161[.]2[.]77
23[.]129[.]64[.]135
23[.]129[.]64[.]210
23[.]129[.]64[.]222
23[.]129[.]64[.]225
23[.]129[.]64[.]226
23[.]137[.]251[.]32
38[.]97[.]116[.]244
42[.]200[.]94[.]158
45[.]142[.]122[.]219
45[.]154[.]98[.]33
51[.]89[.]153[.]112
79[.]137[.]202[.]92
89[.]58[.]27[.]84
92[.]205[.]129[.]7
