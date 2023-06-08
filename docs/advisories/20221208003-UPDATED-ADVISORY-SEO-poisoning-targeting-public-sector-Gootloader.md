
# UPDATED ADVISORY - SEO poisoning targeting public sector (Gootloader) - 20221208003

## Overview

Since initial advice on the 19th of August 2022 (*Search Engine Optimiztion (SEO) poisoning targeting public sector (Gootloader) Ref: 20220819002*), WA SOC have observed continuous active attempts of SEO poisoning for the deployment of Gootloader malware affecting multiple WA SOC agencies.

Based on multiple evidence we observed, we have updated threat hunting methods and detection for this attack.

### What is the threat?

Based on article written by Trend Micro, Gootkit loader uses **fileless techniques** to download and deliver various ransomware payload such as SunCrypt, and REvil (Sodinokibi) ransomware, Kronos trojans, and Cobalt Strike.

We have observed agency with EDR capabilities have been able to effectively stop GootKit/ Gootloader malware during the execution phase (when user accidentally clicked the malicious .js file). However, it should be noted that persistence mechanism might have been successfully installed to user device.

## Detection

### Detection/ Threat Hunting

Run the following threat hunting search on files and URLs that might be downloaded from GootLoader infected website

#### Non-KQL SIEM, search on the following regex-pattern on Files and File download origin

- File: `\((\d{4,6})\)\.zip`
- File URL origin: `\.php\?(.*=){3}.+$`

#### Microsoft Sentinel KQL / Defender Threat Hunting blade

**Note** - The KQL below will need to be updated to reflect current IoCs if not connected to the DGov STIX / TAXII

```kusto
// ******************************************************************************************************************
// Date   : 28-Oct-2022
// Version: 1.0
// Author : DGov
//
// Description: 
// - Detect Gootloader file downloads and outbound network events to identified Gootloader C2 infra.
// - Agency need to maintain lists of C2 domain URL manually below
// - The Regex 1 detect file naming pattern, and 
// - The Regex 2 detect download link URL name pattern
//
// ******************************************************************************************************************
//
let url=dynamic(["setman.es","tavernelentrepot.be","termowood.net","textfabrik.de","sfl.hu","seyhanaluminyum.com","theodoraross.com","theairtrekstory.com","tavernelentrepot.be","serphero.com","shisharealty.com","sheffieldcoronarysociety.org.uk","thomadaneau.com","theodoraross.com","theairtrekstory.com","secora.cl"]);
let regx1=@"\((\d{4,6})\)\.zip";
let regx2=@"\.php\?(.*=){3}.+$";
union withsource=tablename_ DeviceNetworkEvents,DeviceFileEvents
| where RemoteUrl has_any (url) or FileOriginUrl has_any (url) or (FileName matches regex regx1 and FileOriginUrl matches regex regx2)
```

#### **NEW SENTINEL KQL** - Utilising Threat Intelligence Feed from DGov STIX / TAXII

```kusto
// ******************************************************************************************************************
// Date   : 12-Dec-2022
// Version: 2.1
// Author : DGov
//
// Description: 
// - 2.1 - Removed the IndicatorType parsing due to TI Platform compatibility issue
// - Detect Gootloader file downloads and outbound network events to identified Gootloader C2 infra.
// - Leverage Sentinel STIX/ TAXII Threat Intelligence platform for domain name update
// - The Regex 1 detect file naming pattern, and 
// - The Regex 2 detect download link URL name pattern
//
// ******************************************************************************************************************
//
let tiObservables = ThreatIntelligenceIndicator                                 //Search in specified threat intelligence workspace 
| where TimeGenerated < now() and ExpirationDateTime > now() and Active == true //Only active TI
//
// Select only the most recently ingested copy of an indicator
//
| summarize arg_max(TimeGenerated, *) by IndicatorId
| where ThreatType has "gootloader"     //Specific search for Gootloader threat
| where isnotempty(DomainName)          //Remove any empty values
| summarize DomainName=make_set(DomainName);
let regx1=@"\((\d{4,6})\)\.zip";
let regx2=@"\.php\?(.*=){3}.+$";
union withsource=tablename_ DeviceNetworkEvents,DeviceFileEvents
| where RemoteUrl has_any (tiObservables) or FileOriginUrl has_any (tiObservables) or (FileName matches regex regx1 and FileOriginUrl matches regex regx2)
```

## Reference

- [Gootkit Loader's Updated Tactics and Fileless Delivery of Cobalt Strike | Trend Micro](https://www.trendmicro.com/en_us/research/22/g/gootkit-loaders-updated-tactics-and-fileless-delivery-of-cobalt-strike.html)
- [GootLoaderSites (twitter)](https://twitter.com/GootLoaderSites)
- [Tips for Automatiing IoC Extraction from GootLoader](https://threatresearch.ext.hp.com/tips-for-automating-ioc-extraction-from-gootloader-a-changing-javascript-malware/)
- [2021 Top Malware Strains | CISA](https://www.cisa.gov/uscert/ncas/alerts/aa22-216a)

## Indicators of Compromise

Please be advised of the following observed IOCs for detection in your environment:

### File Names and File hash (Not reliable IOCs, as filenames changed)

### File Hashes

- Water_corporation_enterprise_agreement_2018_wa_29877.zip - **SHA 256** - ab244fc6a64b33743c52436c1c3bb9be12ad05067830cf82edf72a71cb464b01
- water corporation enterprise agreement 2018 wa 29877.js - **SHA 256** - 74a501fe8127fd8e635c89be5d98eae420a2a2d29fdbd67d60c92bc62c1ab128
- Water corporation enterprise agreement 2018 wa (79577).zip - **SHA256** - fa036aac45db7c2eaac588e4bb2082d801e7eeb7deb3b33b89dc0426469333b7
- What is novation agreement in construction (73975).zip - **SHA256** - aaac2e4ed43c7a24e4c12254e576ee5a602465afd5c2df6d5d573ae805035868
- Honor an agreement synonym (39766).zip - **SHA256** - 906580c297c8dd683b17be49294324489393071c35606b9ba4b878a8dbcf1088

### Malicious Files

- Public service and government officers general agreement 2014 (74209).zip
- Water corporation enterprise agreement 2018 wa (49326).zip
- Queensland rail network enterprise agreement (39681)

**Note**: *The file names do not indicate/ related to affected agencies. The file names are tailored to potential SEO keywords that unknowing users might be interested to search in Google*

### Additonal IoCs

- [Sophos IoCs GootLoader - CSV](https://github.com/sophoslabs/IoCs/blob/master/Troj-gootloader.csv)
- [Sophos IoCs GootLoader - Yara](https://github.com/sophoslabs/IoCs/blob/master/Troj-gootloader.yara)
- [Rewterz IoCs GootLoader](https://www.rewterz.com/rewterz-news/rewterz-threat-alert-gootloader-active-iocs-2)
- [Tips for Automating IoC Extraction from GootLoader](https://threatresearch.ext.hp.com/tips-for-automating-ioc-extraction-from-gootloader-a-changing-javascript-malware/)

### Domain Names

- hxxps://www.webdesignbrabant[.]net/faq.php
- hxxps://www.ibpm[.]it/2022/04/10/water-corporation-enterprise-agreement-2018-wa/
- hxxps://www.zen-altitude[.]fr/faq.php
- hxxps://www.setman[.]es/content.php
- tavernelentrepot[.]be/xml.php
- termowood[.]net/xml.php
- textfabrik[.]de/xml.php
- hxxps://www.sfl[.]hu
- hxxps://www.seyhanaluminyum[.]com
- hxps://theodoraross[.]com
- hxxps://theairtrekstory[.]com
- hxxps://tavernelentrepot[.]be
- hxxps://www.serphero[.]com
- hxxps://www.shisharealty[.]com
- hxxps://www.sheffieldcoronarysociety.org[.]uk
- thomadaneau[.]com/xml.php
- theodoraross[.]com/xml.php
- theairtrekstory[.]com/xml.php
- hxxps://www.secora[.]cl

**Source**: [GootLoaderSites (twitter)](https://twitter.com/GootLoaderSites)

**Notes**: The WA SOC has verified the IOC values match real incident data
