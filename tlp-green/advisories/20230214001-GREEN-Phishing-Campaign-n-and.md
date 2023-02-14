# Phishing campaign with confirmed account compromises - 20230214001

## Overview
The WA SOC has observed a growing phishing campaign across multiple agencies seeking credential data. Accounts have been confirmed compromised and signins have been seen from threat actor infrastructure.

## IOCs below

- Senders:
    - alessandro.mutti@n-andgroup.com
    - Andrew.pitt@n-andgroup.com
    - andrea.stradella@n-anditalia.com
    - andrea.stroppa@n-anditalia.com
- Subject: Attention Required
- IPv4 Address (AiTM proxy): 5.161.180.3
- IPv4 Address (Signin attempts): 20.163.76.195
- Domain: `*.pagemaker.link`
- Domain: `microsoftlogin-secured[.]ucalfp[.]org`

Users clicking the link will be taken to a page on the site pagemaker.link which is a legitimate site that is being used by malicious actors.

Kusto query for relevant emails
```kusto
EmailUrlInfo
| where Url contains "pagemaker.link"
| distinct Url
```

Known bad links from above query (warning: these have not been defanged)
```
# Source: EmailUrlInfo
https://work-link-14v8l.pagemaker.link/
https://rodgersinstruments.com/cronjob/mailcampaigns/link/nzq4ng==/mtg0/?link=https://notice25673993040240404notice477488-pk2lp.pagemaker.link/notice-25673993040240404
accesswire.com/social_visits.ashx?articleid=662178&networkid=ins&link=https://notice5673993040240404notice477488-jqnre.pagemaker.link/notice-5673993040240404-notice-477488
https://notice5673993040240404notice477488-jqnre.pagemaker.link/notice-5673993040240404-notice-477488
https://accesswire.com/social_visits.ashx?articleid=662178&networkid=Ins&link=https://07970-179-439-notice-07970-179-439-7n5q2.pagemaker.link/07970-179-439-notice-07970-179-439
https://ewater-9jv19.pagemaker.link/e-water
https://api.targetx.com/email-interact/redirect?id=MTEwMDAwMzQ3IE5vbmUgNjQwOTQgVE1TXzAwMzM4MDAwMDJ3RVBMdEFBTw%3D%3D&link=https://1672240560757716-9504-6zneg.pagemaker.link/1672240560757716-9504
https://accesswire.com/social_visits.ashx?articleid=662178&networkid=Ins&link=https://notice5673993040240404notice477488-jqnre.pagemaker.link/notice-5673993040240404-notice-477488
https://accesswire.com/social_visits.ashx?articleid=662178&amp;networkid=Ins&amp;link=https://notice5673993040240404notice477488-jqnre.pagemaker.link/notice-5673993040240404-notice-477488
https://buyamerican.com/landing/count.php?link=https://notice5673993040240404notice477488-ev2rr.pagemaker.link/notice-5673993040240404-notice-477488
https://ultrawidesnowboards.com/url?link=https://84260notice93751notice632418notice-pk64p.pagemaker.link/84260-notice-93751-notice-632418-notice
http://aquamarintour.ru/out.php?link=https://654321notice897654notice321490notice-lg4l4.pagemaker.link/654321-notice-897654-notice-321490-notice

# Source: urlscan.io
anotice5673993040240404notice477488-dxvze.pagemaker.link
notice2673993040240205notice477488-ev2rr-lg45r.pagemaker.link
0192-bsh299-lo19-notice-01892-865-7152-y-001-nz890-jq86l.pagemaker.link
3264354897000notice3264354897000-44qjx.pagemaker.link
notice5673993040240404notice477488-kner8.pagemaker.link
notice5673993040240404notice477488-jqnre.pagemaker.link
3245344533notice32456645455783-x5zj2.pagemaker.link
notice1122673993040240404notice477488-mx2r9.pagemaker.link
notice5673993040240404notice477488-ev2rr.pagemaker.link
01623-480107notice01623-480107-dxj44.pagemaker.link
notice25673993040240404notice477488-pk2lp.pagemaker.link
07970-179-439-notice-07970-179-439-7n5q2.pagemaker.link
notice5673993040240404notice477488-dxvze.pagemaker.link
```

## Recommendation
The WA SOC recommends administrators apply the advice provided by the ACSC [Phishing - scam emails | Cyber.gov.au](https://www.cyber.gov.au/acsc/view-all-content/threats/phishing).

Additionally:
- Search for and delete associated phishing emails
- Reset password for the users that have clicked the URLs.
- Add IOC to block list.
