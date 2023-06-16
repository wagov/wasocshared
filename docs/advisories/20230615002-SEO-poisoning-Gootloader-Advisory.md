  
# SEO poisoning targeting public sector (Gootloader) Advisory - 20230615002

## Overview
Since initial advice on the 19th of August 2022 (*SEO poisoning targeting public sector (Gootloader) Ref: 20220819002*), WA SOC have observed continuous active attempts of SEO poisoning for the deployment of Gootloader malware affecting multiple WA SOC agencies.

Based on multiple evidence we observed, we have updated threat hunting methods and detection for this attack.

### Detection
Run the following threat hunting search on files and URLs that might be downloaded from GootLoader infected website

Non-KQL SIEM, search on the following regex-pattern on Files and File download origin
-   File: `\((\d{4,6})\)\.zip`
-   File URL origin: `\.php\?(.*=){3}.+$`

Microsoft Sentinel KQL / Defender Threat Hunting blade
|
```
let url=dynamic(["setman.es","tavernelentrepot.be","termowood.net","textfabrik.de","sfl.hu","seyhanaluminyum.com","theodoraross.com","theairtrekstory.com","tavernelentrepot.be","serphero.com","shisharealty.com","sheffieldcoronarysociety.org.uk","thomadaneau.com","theodoraross.com","theairtrekstory.com","secora.cl"]);let regx1=@"\((\d{4,6})\)\.zip";let regx2=@"\.php\?(.*=){3}.+$";union withsource=tablename_ DeviceNetworkEvents,DeviceFileEvents| where RemoteUrl has_any (url) or FileOriginUrl has_any (url) or (FileName matches regex regx1 and FileOriginUrl matches regex regx2)
```
## Indicator of Compromise
Please be advised of the following observed IOCs for detection in your environment:

### FileName
- Water corporation enterprise agreement 2018 wa (73606).zip - 76cdb2bad9582d23c1f6f4d868218d6c(MD5)
- public sector csa agreement 2021 pay rates(18764).zip - 514affc78fccc14b67af699c898ec09a(md5)
- public sector csa agreement 2021 pay rates(60706).zip - af4f04edf5ec0b7555b3b70819acbfdd(MD5)
- public sector csa agreement 2021 pay rates (32089).zip
 f_011b45 - 641eaa8aaa45375ca0743109ac6ca652(MD5)

### Domain Names

Note the below domains have not been defanged, please exercise caution when utilizing.
- k-reform[.]jp/forum[.]php
- lottolong[.]com/blog[.]php
- messagesmusicaux[.]com/search[.]php
- sicherheitsingenieure-huber[.]de/content[.]php

Kusto query 1
//based on regex of filenames being downloaded. 
```
let regx1=@"\((\d{4,6})\)\.zip";\
let regx2=@"\.php\?(.=){3}.+$";\
union Device\
| where TimeGenerated > ago(90d) //Sync to search period\
| where (FileName matches regex regx1 and FileOriginUrl matches regex regx2)\
| extend AlgorithmCustomEntity = "SHA256"//FileHash entity mapping\
| project-reorder TimeGenerated, FileName, FileOriginUrl, RemoteUrl, FileOriginReferrerUrl
```
Kusto query 2
//replace domains with relative gootloader domains
```
let c1 = dynamic([domains]);\
find where RemoteUrl has_any (c1) or FileOriginUrl has_any (c1) or FileOriginReferrerUrl has_any (c1)\
| where TimeGenerated > ago(90d)\
| project-reorder TimeGenerated, FileName, FileOriginUrl, RemoteUrl, FileOriginReferrerUrl
```

### What is the threat?
Based on article written by Trend Micro, Gootkit loader uses fileless techniques to download and deliver various ransomware payload such as SunCrypt, and REvil (Sodinokibi) ransomware, Kronos trojans, and Cobalt Strike.

We have observed agency with EDR capabilities have been able to effectively stop GootKit/ Gootloader malware during the execution phase (when user accidentally clicked the malicious .js file). However, it should be noted that persistence mechanism might have been successfully installed to user device.

### Reference
-   [Gootkit Loader continues to be used on multiple Australian networks](https://www.cyber.gov.au/about-us/advisories/gootkit-loader-continues-be-used-multiple-australian-networks "https://www.cyber.gov.au/about-us/advisories/gootkit-loader-continues-be-used-multiple-australian-networks")
-   [Gootkit Loader's Updated Tactics and Fileless Delivery of Cobalt Strike | Trend Micro](https://www.trendmicro.com/en_us/research/22/g/gootkit-loaders-updated-tactics-and-fileless-delivery-of-cobalt-strike.html "https://www.trendmicro.com/en_us/research/22/g/gootkit-loaders-updated-tactics-and-fileless-delivery-of-cobalt-strike.html")
-   [GootLoaderSites (twitter)](https://twitter.com/GootLoaderSites "https://twitter.com/gootloadersites")

