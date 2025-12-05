# SEO poisoning targeting public sector (Gootloader) Advisory - 20221028001

## Overview

Since initial advice on the 19th of August 2022 (*SEO poisoning targeting public sector (Gootloader) Ref: 20220819002*), WASOC have observed continuous active attempts of SEO poisoning for the deployment of Gootloader malware affecting multiple WASOC agencies.

Based on multiple evidence we observed, we have updated threat hunting methods and detection for this attack.

### What is the threat?

Based on article written by Trend Micro, Gootkit loader uses fileless techniques to download and deliver various ransomware payload such as SunCrypt, and REvil (Sodinokibi) ransomware, Kronos trojans, and Cobalt Strike.

We have observed agency with EDR capabilities have been able to effectively stop GootKit/ Gootloader malware during the execution phase (when user accidentally clicked the malicious .js file). However, it should be noted that persistence mechanism might have been successfully installed to user device.

## Detection

### Detection/ Threat Hunting

Run the following threat hunting search on files and URLs that might be downloaded from GootLoader infected website

#### Non-KQL SIEM, search on the following regex-pattern on Files and File download origin

- File: `\((\d{4,6})\)\.zip`
- File URL origin: `\.php\?(.*=){3}.+$`

#### Microsoft Sentinel KQL / Defender Threat Hunting blade

```kusto
let url=dynamic(["setman.es","tavernelentrepot.be","termowood.net","textfabrik.de","sfl.hu","seyhanaluminyum.com","theodoraross.com","theairtrekstory.com","tavernelentrepot.be","serphero.com","shisharealty.com","sheffieldcoronarysociety.org.uk","thomadaneau.com","theodoraross.com","theairtrekstory.com","secora.cl"]);
let regx1=@"\((\d{4,6})\)\.zip";
let regx2=@"\.php\?(.*=){3}.+$";
union withsource=tablename_ DeviceNetworkEvents,DeviceFileEvents
| where RemoteUrl has_any (url) or FileOriginUrl has_any (url) or (FileName matches regex regx1 and FileOriginUrl matches regex regx2)
```

## Reference

- [Gootkit Loader's Updated Tactics and Fileless Delivery of Cobalt Strike | Trend Micro](https://www.trendmicro.com/en_us/research/22/g/gootkit-loaders-updated-tactics-and-fileless-delivery-of-cobalt-strike.html)
- [GootLoaderSites (twitter)](https://twitter.com/GootLoaderSites)

## Indicators of Compromise

Please be advised of the following observed IOCs for detection in your environment:

### File Names and File hash (Not reliable IOCs, as filenames changed)

| Artefacts / IOC Type | IOC-Value                                                                                                                             | Description                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| File (Hash)          | Water corporation enterprise agreement 2018 wa (79577).zip<br>SHA256=fa036aac45db7c2eaac588e4bb2082d801e7eeb7deb3b33b89dc0426469333b7 | Gootkit Malicious file - Downloaded |
| File (Hash)          | Public service and government officers general agreement 2014 (74209).zip                                                             | Gootkit Malicious file - Downloaded |
| File (Hash)          | What is novation agreement in construction (73975).zip<br>SHA256=aaac2e4ed43c7a24e4c12254e576ee5a602465afd5c2df6d5d573ae805035868     | Gootkit Malicious file - Downloaded |
| File (Hash)          | Honor an agreement synonym (39766).zip<br>SHA256=906580c297c8dd683b17be49294324489393071c35606b9ba4b878a8dbcf1088                     | Gootkit Malicious file - Downloaded |
| File (Hash)          | Water corporation enterprise agreement 2018 wa (49326).zip                                                                            | Gootkit Malicious file - Downloaded |
| File (Hash)          | Queensland rail network enterprise agreement (39681)                                                                                  | Gootkit Malicious file - Downloaded |

**Note**: *The file names do not indicate/ related to affected agencies. The file names are tailored to potential SEO keywords that unknowing users might be interested to search in Google*

### Domain Names

Note the below domains have not been defanged, please exercise caution when utilising.

```text
https://www.setman.es/content.php
tavernelentrepot.be/xml.php
termowood.net/xml.php
textfabrik.de/xml.php
https://www.sfl.hu
https://www.seyhanaluminyum.com
https://theodoraross.com
https://theairtrekstory.com
https://tavernelentrepot.be
https://www.serphero.com
https://www.shisharealty.com
https://www.sheffieldcoronarysociety.org.uk
thomadaneau.com/xml.php
theodoraross.com/xml.php
theairtrekstory.com/xml.php
https://www.secora.cl
```

**Source**: [GootLoaderSites (twitter)](https://twitter.com/GootLoaderSites)

**Notes**: The WA SOC has verified the IOC values match real incident data
