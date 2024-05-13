# TunnelVision Vulnerability Allows Hijacking of VPN Traffic via DHCP Manipulation - 20240509003

## Overview

The WA SOC has been made aware a new attack technique called "decloaking" that can bypass VPN encapsulation and force a user's traffic off their VPN tunnel using built-in DHCP features. This technique allows an attacker to snoop on a user's unencrypted traffic, while the VPN connection appears to remain active and the kill switch is not triggered.

By leveraging DHCP option 121 to inject routing rules that take priority over the VPN's routing, it causes traffic to bypass the VPN tunnel. It is effective against a wide range of operating systems and VPN providers, as it targets the underlying network stack rather than the VPN protocol itself.

## What is vulnerable?

| CVE                                                             | Severity | CVSS | Product(s) Affected | Summary                                                                                                                                                                                                                                                                                                                                                                | Dated      |
| --------------------------------------------------------------- | -------- | ---- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [CVE-2024-3661](https://nvd.nist.gov/vuln/detail/CVE-2024-3661) | **High** | 7.6  | **versions before** | DHCP can add routes to a client’s routing table via the classless static route option (121). VPN-based security solutions that rely on routes to redirect traffic can be forced to leak traffic over the physical interface. An attacker on the same local network can read, disrupt, or possibly modify network traffic that was expected to be protected by the VPN. | 05/06/2024 |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

System and network administrators should familiarise themselves with the vulnerability and attempt to mitigate where possible. As there is no single universal fix, this may vary for different organisations. Some possible steps may be to ensure there are no rogue DHCP servers present on networks and advising users who utilise unsecured networks of the potential risks even when using a VPN.

## Additional References

- [Leviathan Security - TunnelVision](https://www.leviathansecurity.com/blog/tunnelvision)
