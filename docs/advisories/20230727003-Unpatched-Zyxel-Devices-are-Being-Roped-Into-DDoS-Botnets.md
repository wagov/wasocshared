# Unpatched Zyxel Devices are Being Roped Into DDoS Botnets - 20230727003

## Overview

The WA SOC has observed a rapidly evolving botnets exploiting vulnerabilities in upatched Zyxel devices.

## What is the vulnerability?

[**CVE-2023-28771**](https://nvd.nist.gov/vuln/detail/CVE-2023-28771) - CVSS v3 Base Score: ***9.8***

This vulnerability is characterized by a command injection flaw affecting multiple firewall models that could potentially allow an unauthorized attacker to execute arbitrary code by sending a specifically crafted packet to the targeted device.

## Exploitation and Propagation

The attacks commonly utilise download of files tailored for MIPS architecture. In the analysis done by Fortinet, they have identified that the scripts downloads a file named "lolmips" from the IP address 92\[.\]118\[.\]39\[.\]16 and saves it with a ".zw" extension, after which it executes with the "zywall" parameter, indicating its connection to the Zyxel firewall vulnerability.

The attacks usually seen originating from the following IP addresses:

- 193\[.\]32\[.\]162\[.\]190
- 109\[.\]205\[.\]213\[.\]30
- 109\[.\]207\[.\]200\[.\]42
- 109\[.\]207\[.\]200\[.\]47
- 109\[.\]207\[.\]200\[.\]44

These attacks specifically target the command injection vulnerability in the Internet Key Exchange (IKE) packet transmitted over UDP on Zyxel devices. The attackers utilize tools such as curl or wget to download scripts for further actions. Below, you can find the corresponding traffic capture illustrating these activities.

In depth analysis of this exploit can be found in the article [DDoS Botnets Target Zyxel Vulnerability CVE-2023-28771 | FortiGuard Labs (fortinet.com)](https://www.fortinet.com/blog/threat-research/ddos-botnets-target-zyxel-vulnerability-cve-2023-28771).

## C2 Servers

- raw\[.\]pastebin\[.\]com
- hoz\[.\]1337\[.\]cx
- babaroga\[.\]lib
- dragon\[.\]lib
- blacknurse\[.\]lib
- tempest\[.\]lib
- routercontroller\[.\]geek
- dvrcontroller\[.\]libre

Dark.IoT utilizes the OpenNIC server with the IP address "147\[.\]182\[.\]243\[.\]49" for DNS resolution and establishes communication with the C2 servers.

A comprehensive technical analysis of the Botnet activity can be found [here](https://www.fortinet.com/blog/threat-research/ddos-botnets-target-zyxel-vulnerability-cve-2023-28771).

## List of IOC's related to Zyxel DDoS Botnet activity

d618c817e6a93193a499126156a1f7e888008dacdb247a769fd69ce4c0c87b67

a6729c047d776294fa21956157eec0b50efa7447b8e2834b05be31080767006f

729f2fa4d037912a360cb7c4e2c37765da0c38725451600f0258109b672f615e

2c55674e938e7618f7c9273e3da61ce7aeab3dc5626b7b8b4e3fc7cc95d0436f

928d8ccd71edda5891068d703603ba0b70687f746c9da73afa6692b274ea757c

6137a30d8eb932d25664ced747424b15072e676b5d4d27d5b8f3b84f48344217

0c394849ce4f636cc79cc84389b66a0dbdaf14a61a6d87302e807f2153bc6c2b

2fe13ee992cf00778bcc92dc3732305114dca1700dedca7c29342216df236644

034cdcb42d1d7b921b4732230bbdcb4089107490a30b8cd7a62e67b657e33d26

3d69c780fefa0c3a34190989d43268a272004f0623d3e596bc0c92e1744832c9

79f69993110688372a5898d05f1141b7f44f3f5f55cd50b6a493c1d33af141c8

c68211116bbc43c2fe0aba8b598b88b218adc0d995311a4e7030de8acd48076e

51becb81d6bdfe79111974c05f2e4a20a8825a872a92df86cbc98517100b031a

42b4e116c5d2d3e9d4777c7eaa3c3835a126c02673583c2dfb1ae2bf0bf0db48

85d3d93910bfb8410a0e82810d05aa67a6702ce0cdfc38d1d01f2f9471d20150

12c65cfd227d393fd338223eb50140571760de04ef0a21fe3c4636e1bfaf4966

f82f5ec551f9ac3bb5a3b1ace5dd21c35239bd983fd9a36e0e7c07bfb48a3fdd

28fa9225db6d42084123989712313489e255376134f8e77f07b77c345a026304

312022da42ab6df882c44d984f9aceea7f08e217a5ca8ca985c533a1af399cee

## Additional References

- [DDoS Botnets Target Zyxel Vulnerability CVE-2023-28771 | FortiGuard Labs (fortinet.com)](https://www.fortinet.com/blog/threat-research/ddos-botnets-target-zyxel-vulnerability-cve-2023-28771)

- [Fast-Moving DDoS Botnet Exploits Unpatched ZyXel RCE Bug | Threatpost](https://threatpost.com/fast-moving-ddos-botnet-unpatched-zyxel-rce-bug/155059/)

- [Zyxel users still getting hacked by DDoS botnet emerge as public nuisance No. 1 | Ars Technica](https://arstechnica.com/security/2023/07/ddos-botnets-are-still-feeding-on-zyxel-devices-with-vulnerable-critical-flaw/)
