  
# Resurgence of SEO Poisoning - 20230119001

## Overview
The WA SOC has observed a resurgence in SEO Poisoning campaigns.

## Delivery
Historically, SEO Poisoning campaigns are malicious actors setting up fake websites for popular free and open-source software to promote malicious downloads through advertisements in Google search results.

## Detection and Remediation

### Detection
1. Identify the presence of the below supplied KQL/ Kusto hunting code
2. Identify the presence of the below supplied IOCs
3. Inspect activity from the identified devices and/or users

### Recommended Remediation Steps
1.  Run a full Antivirus scan on the compromised device
2.  Reset the affected user's passwords
3.  Implement MFA if required

## Reference
* Blog Article "Hackers push malware via Google search ads for VLC, 7-Zip, CCleaner": [https://www.bleepingcomputer.com/news/security/hackers-push-malware-via-google-search-ads-for-vlc-7-zip-ccleaner/](https://www.bleepingcomputer.com/news/security/hackers-push-malware-via-google-search-ads-for-vlc-7-zip-ccleaner/)
* Internet Crime Crime Complain Center (IC3) Advisory: [https://www.ic3.gov/Media/Y2022/PSA221221](https://www.ic3.gov/Media/Y2022/PSA221221)

## Indicator of Compromise

### KQL Query
***Note the below domains have not been defanged, please exercise caution when utilizing.***
//Known Domain clicks
```kusto
DeviceEvents
| where TimeGenerated >= ago(90d)
| where RemoteUrl in~ ("tecinnovations.online","tecinovations.pw","tecinnovation.space","techinovation.online","techinovation.website","techinovation.site","tecinnovation.fun","techinovation.fun","tecinnovation.online","tecinnovation.website","techinovation.space","tecinnovation.site","vilc.site","audasite.site","audacslty.site","odstraeming.site","odstraeming.space","glmps.site","audasite.website","audasite.online","audasite.space","odstraeming.fun","ostreeming.website","ostreeming.fun","ostreeming.site","odstraeming.online","obmprolect.com","godstreamsview.site","godstreamsview.online","obcproect.site","godstreamsview.website","godstreamsview.fun","godstreamsview.space","odstraeming.website","ostreeming.online","obsproect.site","ostreeming.space","godstreamsviews.online","godstreamsviews.website","godstreamsviews.site","godstreamsviews.space","obcprolect.com","godstreamsviews.fun","odstreamsviews.online","odstreamsviews.website","odstreamsviews.space","odstreamsviews.fun","docstore.app","sgparroquial.app","odstreamsviews.site","qobstreamsviews.space","qobstreamsviews.site","qobstreamsviews.online","qobstreamsviews.fun","qobstreamsviews.website","obsspro.website","obsspro.site","qobstreamsview.website","qobstreamsview.online","qobstreamsview.fun","qobstreamsview.site","obsspro.online","obstremsview.online","obstremswiev.space","obrproject.com","obpproject.com","obstremswiev.site","obstremswiev.online","obstremswiev.fun","oblproject.com")
```

### Domain Names
***Note the below domains have not been defanged, please exercise caution when utilizing.***

```text
tecinnovations.online
tecinovations.pw
tecinnovation.space
techinovation.online
techinovation.website
techinovation.site
tecinnovation.fun
techinovation.fun
tecinnovation.online
tecinnovation.website
techinovation.space
tecinnovation.site
vilc.site
audasite.site
audacslty.site
odstraeming.site
odstraeming.space
glmps.site
audasite.website
audasite.online
audasite.space
odstraeming.fun
ostreeming.website
ostreeming.fun
ostreeming.site
odstraeming.online
obmprolect.com
godstreamsview.site
godstreamsview.online
obcproect.site
godstreamsview.website
godstreamsview.fun
godstreamsview.space
odstraeming.website
ostreeming.online
obsproect.site
ostreeming.space
godstreamsviews.online
godstreamsviews.website
godstreamsviews.site
godstreamsviews.space
obcprolect.com
godstreamsviews.fun
odstreamsviews.online
odstreamsviews.website
odstreamsviews.space
odstreamsviews.fun
docstore.app
sgparroquial.app
odstreamsviews.site
qobstreamsviews.space
qobstreamsviews.site
qobstreamsviews.online
qobstreamsviews.fun
qobstreamsviews.website
obsspro.website
obsspro.site
qobstreamsview.website
qobstreamsview.online
qobstreamsview.fun
qobstreamsview.site
obsspro.online
obstremsview.online
obstremswiev.space
obrproject.com
obpproject.com
obstremswiev.site
obstremswiev.online
obstremswiev.fun
oblproject.com
```

