# F5 BIG-IP and iControl REST Vulnerabilities and Exposures - 20221117001

## Overview
The WA SOC has observed several vulnerabilities and exposures in **F5 BIG-IP and BIG-IQ devices** running a customized distribution of CentOS detailed in F5's [Base Operating Systems](https://support.f5.com/csp/article/K121) support article.

Note: the presence of SELinux hardening on F5 devices is an excellent safeguard that made exploitation attempts more difficult.

## What is the vulnerability?
The WA SOC has also observed several bypasses of security controls that F5 does not consider vulnerabilities with a reasonable attack surface ([K05403841](https://support.f5.com/csp/article/K05403841)):
-   [CVE-2022-41622](https://support.f5.com/csp/article/K94221585): BIG-IP and BIG-IQ are vulnerable to unauthenticated remote code execution via cross-site request forgery (CSRF)
-   [CVE-2022-41800](https://support.f5.com/csp/article/K13325942): Appliance mode iControl REST is vulnerable to authenticated remote code execution via RPM spec injection

## What is vulnerable ?

The affected products are detailed in the vendor advisories below:

-   ID1145045 - Local privilege escalation via bad UNIX socket permissions ([CWE-269](https://cwe.mitre.org/data/definitions/269.html))
-   ID1144093 - SELinux bypass via incorrect file context ([CWE-732](https://cwe.mitre.org/data/definitions/732.html))
-   ID1144057 - SELinux bypass via command injection in an update script ([CWE-78](https://cwe.mitre.org/data/definitions/78.html))

## What has been observed ?
There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation
The WA SOC recommends organisations with affected products to follow the applicable **Recommended Actions** in the following F5 Knowledgbase Article as soon as possible: [K05403841: BIG-IP and BIG-IQ improvements disclosed by Rapid7.](https://support.f5.com/csp/article/K05403841)

### Reference:
* K05403841: BIG-IP and BIG-IQ improvements disclosed by Rapid7 -[ https://support.f5.com/csp/article/K05403841](https://support.f5.com/csp/article/K05403841)
* Base operating systems of F5 products - [https://support.f5.com/csp/article/K121](https://support.f5.com/csp/article/K121)
* Most recent versions of F5 software - [https://support.f5.com/csp/article/K2200](https://support.f5.com/csp/article/K2200)
