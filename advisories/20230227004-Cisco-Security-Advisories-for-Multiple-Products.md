# Cisco Security Advisories for Multiple Products - 20230227004

## Overview
Cisco has released security advisories for vulnerabilities affecting multiple Cisco products. A remote attacker could exploit some of these vulnerabilities to take control of an affected system. 
For updates addressing lower severity vulnerabilities, see the [Cisco Security Advisories](https://tools.cisco.com/security/center/publicationListing.x) page.


## What is the vulnerability?
[**CVE-2023-20011**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20011) - Cisco Application Policy Infrastructure Controller and Cisco Cloud Network Controller Cross-Site Request Forgery Vulnerability.

[**CVE-2023-20089**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20089) - Cisco Nexus 9000 Series Fabric Switches in ACI Mode Link Layer Discovery Protocol Memory Leak Denial of Service Vulnerability.

[**CVE-2023-20032**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20032) - ClamAV HFS+ Partition Scanning Buffer Overflow Vulnerability Affecting Cisco Products.


## What is vulnerable? 
The vulnerability affects the following products:
- [Cisco APIC and Cisco Cloud Network Controller](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-capic-csrfv-DMx6KSwV)

- [Cisco Nexus 9000 Series Fabric Switches in ACI Mode](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aci-lldp-dos-ySCNZOpX)

- [ClamAV HFS+ Partition Scanning Buffer Overflow Vulnerability Affecting Cisco Products: February 2023](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-clamav-q8DThCy)

## Recommendation
The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices: [Vendor URL](Vendor URL)

- **ClamAV HFS+ Partition Scanning Buffer Overflow Vulnerability Affecting Cisco Products**
    - For information about [fixed software releases](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), consult the Cisco bugs identified in the [Vulnerable Products](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-clamav-q8DThCy#vp) section of this advisory.
    When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories](https://www.cisco.com/go/psirt) page, to determine exposure and a complete upgrade solution.

- **Cisco Nexus 9000 Series Fabric Switches in ACI Mode**
   - For help determining the best Cisco NX-OS Software release for a Cisco Nexus Switch, see the following Recommended Releases documents. If a security advisory recommends a later release, Cisco recommends following the advisory guidance.To determine the best release for Cisco UCS Software, see the Recommended Releases documents in the release notes for the device.

        - Cisco MDS Series Switches
        - Cisco Nexus 1000V for VMware Switch
        - Cisco Nexus 3000 Series Switches
        - Cisco Nexus 5500 Platform Switches
        - Cisco Nexus 5600 Platform Switches
        - Cisco Nexus 6000 Series Switches
        - Cisco Nexus 7000 Series Switches
        - Cisco Nexus 9000 Series Switches
        - Cisco Nexus 9000 Series ACI-Mode Switches

    