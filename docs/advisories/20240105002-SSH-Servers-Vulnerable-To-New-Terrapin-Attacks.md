# SSH Servers Vulnerable to New Terrapin Attacks - 20240105002

## Overview

The Secure Shell (SSH) transport protocol with certain OpenSSH extensions allows remote attackers to bypass integrity checks such that some packets are omitted (from the extension negotiation message), and a client and server may consequently end up with a connection for which some security features have been downgraded or disabled, aka a Terrapin attack

## What is the vulnerability?

| CVE ID | CVSS Score | Description |
| --- | --- | --- |
| [CVE-2023-48795](https://nvd.nist.gov/vuln/detail/CVE-2023-48795) | 5.9 | SSH transport protocol with certain OpenSSH extensions vulnerable to Terrapin attack|


## What is vulnerable?

The vulnerability affects the following products:

- OpenSSH versions before 9.6 

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *two weeks* (refer [Patch Management](../guidelines/patch-management.md)):

- [Terrapin Scanner](https://github.com/RUB-NDS/Terrapin-Scanner)
- [CVE Mitre](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)
- [Shadow Server Foundation](https://www.shadowserver.org/what-we-do/network-reporting/accessible-ssh-report/)
- [Bleeping computer security news](https://www.bleepingcomputer.com/news/security/nearly-11-million-ssh-servers-vulnerable-to-new-terrapin-attacks/)


