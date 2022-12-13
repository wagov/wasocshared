# Fortinet Vulnerabilities for FortiOS / FortiProxy / FortiSwitchManager - 20221213001

## Overview
An authentication bypass using an alternate path or channel vulnerability [CWE-288](https://cwe.mitre.org/data/definitions/288.html) in **FortiOS, FortiProxy and FortiSwitchManager** may allow an unauthenticated attacker to perform operations on the administrative interface via specially crafted HTTP or HTTPS requests.

In addition, A heap-based buffer overflow vulnerability [CWE-122](https://cwe.mitre.org/data/definitions/122.html) in **FortiOS SSL-VPN** may allow a remote unauthenticated attacker to execute arbitrary code or commands via specifically crafted requests.

## What is the vulnerability ?

**[CVE-2022-40684](https://nvd.nist.gov/vuln/detail/CVE-2022-40684)** - Fortinet Multiple Products Authentication Bypass Vulnerability

Forinet is aware of an instance where this vulnerability was exploited, and recommends:

- Immediately validating your systems against the following indicator of compromise (IoCs) in the device's logs:
 `user="Local_Process_Access" `
- Download the config file from the targeted devices, and to add a malicious super_admin account called  `"fortigate-tech-support"`:
`# show system admin\
edit "fortigate-tech-support"\
set accprofile "super_admin"\
set vdom "root"\
set password ENC [...]\
next`

**CVE-2022-42475** - FortiOS heap-based buffer overflow in SSl-VPN

[CVE-2022-42475](https://tenable.com/cve/CVE-2022-42475) is a heap-based buffer overflow in several versions of ForiOS that received a CVSSv3 score of 9.3. A remote, unauthenticated attacker could exploit this vulnerability with a specially crafted request and gain code execution. The blog from Olympe Cyberdefense goes further, stating attackers could gain "full control."

Threat actors have been leveraging vulnerabilities in Fortinet SSL VPN attacks for several years to the extent that the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) issued a [dedicated advisory](https://www.ic3.gov/Media/News/2021/210402.pdf) to these flaws and their exploitation in 2021. 

## What is vulnerable ? 

### Affected Products 

#### Affected products related to **CVE-2022-40686**

- FortiOS devices in versions **7.0.0 to 7.0.6** and from **7.2.0 to 7.2.1**, 
- FortiProxy devices in versions **7.0.0 to 7.0.6** and **7.2.0**, and; 
- FortiSwitchManager versions **7.0.0 and 7.2.0** should review their patch status and update to the latest version.

Please Note:

- FortiOS versions 5.x, 6.x are **NOT impacted**.

#### Affected products related to **CVE-2022-42475**

- FortiOS versions **6.2.0 to 6.2.11** and from **6.4.0 to 6.4.10** and from **7.0.0 to 7.0.8** and from **7.2.0 to 7.2.2**
- FortiOS-6K7K version **6.0.0 to 6.0.14** and from **6.2.0 to 6.2.11** and from **6.4.0 to 6.4.9** and from **7.0.0 through 7.0.7**


## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

Australian organisations that are unable to update should disable the HTTP/HTTPS administrative interface or consider limiting IP addresses that can reach the administrative interface using the local-in-policy as described in the [Fortinet advisory](https://www.fortiguard.com/psirt/FG-IR-22-377).

Read the following Fortinet advisories and apply the remediations:

- FortiOS / FortiProxy / FortiSwitchManager - Authentication bypass on administrative interface [https://www.fortiguard.com/psirt/FG-IR-22-377](https://www.fortiguard.com/psirt/FG-IR-22-377)

### Reference:
* Proof of Concept (PoC) - Fortinet FortiOS / FortiProxy / FortiSwitchManager Authentication Bypass [https://packetstormsecurity.com/files/169431/Fortinet-FortiOS-FortiProxy-FortiSwitchManager-Authentication-Bypass.html](https://packetstormsecurity.com/files/169431/Fortinet-FortiOS-FortiProxy-FortiSwitchManager-Authentication-Bypass.html)