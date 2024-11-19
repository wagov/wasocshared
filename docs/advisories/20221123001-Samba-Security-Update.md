# Samba Security Update - 20221123001

## Overview

The Kerberos libraries used by Samba provide a mechanism for authenticating a user or service by means of tickets that can contain
**Privilege Attribute Certificates (PACs)**.

Both the **Heimdal and MIT Kerberos libraries**, and so the embedded Heimdal shipped by Samba suffer from an integer multiplication
overflow when calculating how many bytes to allocate for a buffer for the parsed PAC.

## What is the vulnerability ?

**CVE-2022-42898** - Samba's Kerberos libraries and Active Directory Domain Controller (AD DC) failed to guard against integer overflows when parsing a PAC on a 32-bit system, which allowed an attacker with a forged PAC to corrupt the heap.

## What is vulnerable ?

All versions of Samba prior to:

- 4.15.12
- 4.16.7
- 4.17.3

On a 32-bit system an overflow allows placement of 16-byte chunks of entirely attacker-controlled data. (Because the user's control over this calculation is limited to an unsigned 32-bit value, 64-bit systems are not impacted).

The server most vulnerable is the **Key Distribution Centre (KDC)**, as it will parse an attacker-controlled PAC in the **Service for User to Proxy (S4U2Proxy)** handler.

The secondary risk is to Kerberos-enabled file server installations in a non-AD realm. A non-AD Heimdal KDC controlling such a realm may pass on an attacker-controlled PAC within the service ticket.

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing this Alert.

## Recommendation

Samba administrators are advised to upgrade to these releases or apply the patch as soon as possible.

Patches addressing these issues have been posted to correct the defect [https://www.samba.org/samba/security/](https://www.samba.org/samba/security/)

- No workaround on a 32-bit systems as an **AD DC**
- File Servers are only impacted if in a non-AD domain
- 64-bit systems are not exploitable

### Reference

- Samba Security Releases [https://www.samba.org/samba/history/security.html](https://www.samba.org/samba/history/security.html)
