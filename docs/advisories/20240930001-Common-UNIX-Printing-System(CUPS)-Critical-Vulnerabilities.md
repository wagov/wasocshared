# Common UNIX Printing System (CUPS) Critical Vulnerabilities - 20240930001

## Overview

The WA SOC has been made aware of several critical vulnerabilities involving the Common UNIX Printing System (CUPS). These vulnerabilities could allow a remote, unauthenticated attacker to execute commands when a print job starts on the targeted device by replacing IPP URLs with a malicious one, resulting in data theft or damage to critical production systems.

## What is vulnerable?

| Affected Component     | Description                                                                  | CVE                                                          | CVSSv3 | Severity  |
| -----------------------| -----------------------------------------------------------------------------|--------------------------------------------------------------|--------|---------- |
| libcupsfilters         | libscupsfilters Improper Input Validation or Sanitization Vulnerability      | [CVE-2024-47076](https://www.tenable.com/cve/CVE-2024-47076) | 8.6    | High      |
| libppd                 | libppd Improper Input Validation or Sanitization Vulnerability               | [CVE-2024-47175](https://www.tenable.com/cve/CVE-2024-47175) | 8.6    | High      |
| cups-browsed           | cups-browsed Binding to an Unrestricted IP Address Vulnerability             | [CVE-2024-47176](https://www.tenable.com/cve/CVE-2024-47176) | 8.4    | High      |
| cups-filters           | cups-filters Command Injection Vulnerability                                 | [CVE-2024-47177](https://www.tenable.com/cve/CVE-2024-47177) | 9.1    | Critical  |       

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- Tenable article: <https://www.tenable.com/blog/cve-2024-47076-cve-2024-47175-cve-2024-47176-cve-2024-47177-faq-cups-vulnerabilities>

# Additional References

- Security Affairs article: <https://securityaffairs.com/169001/hacking/cups-flaws-allow-rce-on-linux-systems.html>
