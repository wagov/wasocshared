# Samba Security Release Updates - 20221219001

## Overview

The Samba Team has released security updates to address vulnerabilities in multiple versions of Samba. An attacker could exploit some of these vulnerabilities to take control of an affected system.

## What is the vulnerability ?

- [**CVE-2022-38023**](https://www.samba.org/samba/security/CVE-2022-38023.html) - RC4/HMAC-MD5 NetLogon Secure Channel is weak and should be avoided
- [**CVE-2022-37966**](https://www.samba.org/samba/security/CVE-2022-37966.html) - RC4-HMAC Kerberos session keys issued to modern servers
- [**CVE-2022-37967**](https://www.samba.org/samba/security/CVE-2022-37967.html) - Kerberos constrained delegation ticket forgery possible against Samba AD DC
- [**CVE-2022-45141**](https://www.samba.org/samba/security/CVE-2022-45141.html) - Samba AD DC using Heimdal can be forced to issue rc4-hmac encrypted Kerberos tickets

## What is vulnerable ?

- **CVE-2022-38023** - The "RC4" protection of the NetLogon Secure channel uses the same algorithms as rc4-hmac cryptography in Kerberos, and so must also be assumed to be weak.

- **CVE-2022-37966** - This is the Samba CVE for the Windows Kerberos RC4-HMAC Elevation of Privilege Vulnerability disclosed by Microsoft on Nov 8 2022. A Samba Active Directory DC will issue weak rc4-hmac session keys for use between modern clients and servers despite all modern Kerberos implementations supporting the aes256-cts-hmac-sha1-96 cipher. On Samba Active Directory DCs and members 'kerberos encryption types = legacy' would force rc4-hmac as a client even if the server supports aes128-cts-hmac-sha1-96 and/or aes256-cts-hmac-sha1-96.

- **CVE-2022-37967** - This is the Samba CVE for the Windows Kerberos **Elevation of Privilege Vulnerability** disclosed by Microsoft on Nov 8 2022.  A service account with the special constrained delegation permission could forge a more powerful ticket than the one it was presented with.

- **CVE-2022-45141** - Since the Windows Kerberos RC4-HMAC Elevation of Privilege Vulnerability was disclosed by Microsoft on Nov 8 2022 and per RFC8429 it is assumed that rc4-hmac is weak.  Vulnerable Samba Active Directory DCs will issue rc4-hmac encrypted tickets despite the target server supporting better encryption (eg aes256-cts-hmac-sha1-96).

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

Additionally, **Samba 4.15.13**, **4.16.8** and **4.17.4** have been issued as security releases to correct the defect.

Samba administrators are advised to upgrade to these releases or apply the patch as soon as possible.

### Reference

- [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38023](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38023)
- [https://nvd.nist.gov/vuln/detail/CVE-2022-37966](https://nvd.nist.gov/vuln/detail/CVE-2022-37966)
- [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37967)
