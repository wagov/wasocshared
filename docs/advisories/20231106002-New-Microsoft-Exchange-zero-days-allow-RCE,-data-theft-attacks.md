# New Microsoft Exchange zero-days allow RCE, data theft attacks - 20231106002

## Overview

Trend Micro has disclosed zero day vulnerabilities within Microsoft Exchange, which allows attackers to exploit and remotely execute arbitrary code or disclose sensitive information.

## What is the vulnerability?

Note: The vulnerabilities identified do not currently have any CVE's associated with them.

-   [ZDI-23-1578](https://www.zerodayinitiative.com/advisories/ZDI-23-1578/) - CVSS v3 Base Score: ***7.5*** -- A remote code execution (RCE) flaw in the 'ChainedSerializationBinder' class, where user data isn't adequately validated, allowing attackers to deserialize untrusted data. Successful exploitation enables an attacker to execute arbitrary code as 'SYSTEM,' the highest level of privileges on Windows.
-   [ZDI-23-1579](https://www.zerodayinitiative.com/advisories/ZDI-23-1579/) - CVSS v3 Base Score: ***7.1*** -- Located in the 'DownloadDataFromUri' method, this flaw is due to insufficient validation of a URI before resource access. Attackers can exploit it to access sensitive information from Exchange servers.
-   [ZDI-23-1580](https://www.zerodayinitiative.com/advisories/ZDI-23-1580/) - CVSS v3 Base Score: ***7.1*** -- This vulnerability, in the 'DownloadDataFromOfficeMarketPlace' method, also stems from improper URI validation, potentially leading to unauthorized information disclosure.
-   [ZDI-23-1581](https://www.zerodayinitiative.com/advisories/ZDI-23-1581/) - CVSS v3 Base Score: ***7.1*** -- Present in the CreateAttachmentFromUri method, this flaw resembles the previous bugs with inadequate URI validation, again, risking sensitive data exposure.

## What is vulnerable?

The vulnerability affects the following products:

- Exchange

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- Microsoft has not released a fix for the issue(s) identified above. However, it is advised to update to the latest version of Exchange, and any future updates that may become available.

#### Additional Details:
-   Regarding ZDI-23-1578: Customers who have applied the August Security Updates are already protected.
-   Regarding ZDI-23-1579: The technique described requires an attacker to have prior access to email credentials.
-   Regarding ZDI-23-1580: The technique described requires an attacker to have prior access to email credentials, and no evidence was presented that it can be leveraged to access sensitive customer information.
-   Regarding ZDI-23-1581: The technique described requires an attacker to have prior access to email credentials, and no evidence was presented that it can be leveraged to gain elevation of privilege.

## Additional References

- [New Microsoft Exchange zero-days allow RCE, data theft attacks (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-exchange-zero-days-allow-rce-data-theft-attacks/)
