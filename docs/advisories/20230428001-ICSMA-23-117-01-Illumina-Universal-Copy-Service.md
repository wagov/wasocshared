# ICSMA-23-117-01 Illumina Universal Copy Service - 20230428001

## Overview

CISA has released security advisories for Illumina Universal Copy Service vulnerabilities.

Successful exploitation of these vulnerabilities could allow an attacker to take any action at the operating system level. A threat actor could impact settings, configurations, software, or data on the affected product; a threat actor could interact through the affected product via a connected network.

## What is the vulnerability?

[**CVE-2023-1968**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1968) - [BINDING TO AN UNRESTRICTED IP ADDRESS CWE-1327](https://cwe.mitre.org/data/definitions/1327.html) CVSS v3 10.0

- Instruments with Illumina Universal Copy Service v2.x are vulnerable due to binding to an unrestricted IP address. An unauthenticated malicious actor could use UCS to listen on all IP addresses, including those capable of accepting remote communications.

[**CVE-2023-1966**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1966) - [EXECUTION WITH UNNECESSARY PRIVILEGES CWE-250](https://cwe.mitre.org/data/definitions/250.html) CVSS v3 7.4

- Instruments with Illumina Universal Copy Service v1.x and v2.x contain an unnecessary privileges vulnerability. An unauthenticated malicious actor could upload and execute code remotely at the operating system level, which could allow an attacker to change settings, configurations, software, or access sensitive data on the affected product.

## What is vulnerable?

The vulnerability affects the following products:

- iScan Control Software: v4.0.0/v4.0.5
- iSeq 100: All versions
- MiniSeq Control Software: v2.0 and newer
- MiSeq Control Software: v4.0 (RUO Mode)
- MiSeqDx Operating Software: v4.0.1 and newer
- NextSeq 500/550 and 550Dx Control Software: v4.0 / v4.0 (RUO Mode)
- NextSeq 550Dx Operating Software:  v1.0.0 to 1.3.1 / v1.3.3 and newer
- NextSeq 1000/2000 Control Software: v1.7 and prior
- NovaSeq 6000 Control Software: v1.7 and prior
- NovaSeq Control Software: v1.8

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing

## Recommendation

Illumina recommends using the [UCS Vulnerability Instructions Guide](https://support.illumina.com/downloads/illumina-universal-copy-service-1-0.html) based on the user's specific system configuration to mitigate the vulnerabilities. Illumina recommends users read the instructions before downloading any software.

CISA recommends users take defensive measures to minimize the risk of exploitation of these vulnerabilities. Specifically, users should:

- Minimize network exposure for all control system devices and/or systems, and ensure they are [not accessible from the Internet](https://www.cisa.gov/uscert/ics/alerts/ICS-ALERT-10-301-01).
- Locate control system networks and remote devices behind firewalls and isolate them from business networks.
- When remote access is required, use secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as its connected devices.

CISA reminds organizations to perform proper impact analysis and risk assessment prior to deploying defensive measures.

For a list of other recommendations from CISA refer: [ICS Medical Advisory](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-23-117-01)
