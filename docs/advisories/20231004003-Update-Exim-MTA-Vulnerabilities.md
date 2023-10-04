# UPDATE: Exim MTA Disclose Additional Vulnerabilities - 20231004003

## Overview

Since [Advisory 20231002004](https://soc.cyber.wa.gov.au//advisories/20231002004-Exim-Remote-Code-Execution-Zero-Day-Vulnerability/), Exim have published an advisory detailing additional vulnerabilities for their mail transfer agent (MTA) software.

## What is the vulnerability?

In addition to [**CVE-2023-42115**](https://nvd.nist.gov/vuln/detail/CVE-2023-42115), the vulnerabilities disclosed are as follows:

- [**CVE-2023-42114**](https://nvd.nist.gov/vuln/detail/CVE-2023-42114) - CVSS v3 Base Score: ***3.7***: NTLM Challenge Out-Of-Bounds Read
- [**CVE-2023-42116**](https://nvd.nist.gov/vuln/detail/CVE-2023-42116) - CVSS v3 Base Score: ***8.1***: SMTP Challenge Stack-based Buffer Overflow
- [**CVE-2023-42117**](https://nvd.nist.gov/vuln/detail/CVE-2023-42117) - CVSS v3 Base Score: ***8.1***: Improper Neutralization of Special Elements
- [**CVE-2023-42118**](https://nvd.nist.gov/vuln/detail/CVE-2023-42118) - CVSS v3 Base Score: ***7.5***: libspf2 Integer Underflow
- [**CVE-2023-42119**](https://nvd.nist.gov/vuln/detail/CVE-2023-42119) - CVSS v3 Base Score: ***3.1***: dnsdb Out-Of-Bounds Read

## What is vulnerable?

The vulnerabilities affect all versions of Exim mail transfer agent (MTA) software **before versions 4.96.1 and 4.97**.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the Fixes and Mitigations as per vendor instructions to all affected devices within expected timeframe of *within two weeks* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://www.exim.org/static/doc/security/CVE-2023-zdi.txt>