# Fortinet Releases Security Updates for Multiple Products - 20231013001

## Overview

Fortinet has released security updates to address vulnerabilities affecting FortiOS, FortiAnalyzer, FortiManager, and FortiSIEM. A cyber threat actor can exploit one of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

- [**CVE-2023-42791**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42791) - CVSS v3 Base Score: ***8.6***: A relative path traversal [CWE-23](https://cwe.mitre.org/data/definitions/23.html) vulnerability in FortiManager and FortiAnalyzer may allow a remote attacker with low privileges to execute unauthorized code via crafted HTTP requests.

- [**CVE-2023-41679**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41679) - CVSS v3 Base Score: ***7.7***: An improper access control vulnerability [CWE-284](https://cwe.mitre.org/data/definitions/284.html) in FortiManager management interface may allow a remote and authenticated attacker with at least "device management" permission on his profile and belonging to a specific ADOM to add and delete CLI script on other ADOMs  

- [**CVE-2023-42788**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42788) - CVSS v3 Base Score: ***7.6***: An improper neutralization of special elements used in an os command ('OS Command Injection') vulnerability [CWE-78](https://cwe.mitre.org/data/definitions/78.html) in FortiManager & FortiAnalyzer may allow a local attacker with low privileges to execute unauthorized code via specifically crafted arguments to a CLI command.

- [**CVE-2023-25607**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25607) - CVSS v3 Base Score: ***7.4***: An improper neutralization of special elements used in an OS Command ('OS Command Injection') vulnerability [CWE-78](https://cwe.mitre.org/data/definitions/78.html) in FortiManager, FortiAnalyzer and FortiADC  management interface may allow an authenticated attacker with at least READ permissions on system settings to execute arbitrary commands on the underlying shell due to an unsafe usage of the wordexp function.

- [**CVE-2023-41841**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41841) - CVSS v3 Base Score: ***7.4***: An improper authorization vulnerability [CWE-285](https://cwe.mitre.org/data/definitions/285.html) in FortiOS's WEB UI component may allow an authenticated attacker belonging to the prof-admin profile to perform elevated actions.

- [**CVE-2023-40714**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40714) - CVSS v3 Base Score: ***9.7***: A relative path traversal vulnerability [CWE-23](https://cwe.mitre.org/data/definitions/23.html) in FortiSIEM file upload components may allow an authenticated, low privileged user of the FortiSIEM GUI to escalate their privilege and replace arbitrary files on the underlying filesystem via specifically crafted HTTP requests.

## What is vulnerable?

**CVE-2023-42791** -A list of specific versions can be found [here](https://www.fortiguard.com/psirt/FG-IR-23-189).

- FortiManager
- FortiAnalyzer

**CCVE-2023-41679** - A list of specific versions can be found [here](https://www.fortiguard.com/psirt/FG-IR-23-062).

- FortiManager

**CVE-2023-42788** - A list of specific versions can be found [here](https://www.fortiguard.com/psirt/FG-IR-23-167).

- FortiManager
- FortiAnalyzer

**CVE-2023-25607** - A list of specific versions can be found [here](https://www.fortiguard.com/psirt/FG-IR-22-352).

- FortiManager
- FortiAnalyzer
- FortiADC

**CVE-2023-41841** - A list of specific versions can be found [here](https://www.fortiguard.com/psirt/FG-IR-23-318).

- FortiOS

**CVE-2023-40714** - A list of specific versions can be found [here](https://fortiguard.fortinet.com/psirt/FG-IR-23-085).

- FortiSIEM

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours* (refer [Patch Management](../guidelines/patch-management.md)).:

- <https://www.fortiguard.com/psirt/FG-IR-23-189>
- <https://www.fortiguard.com/psirt/FG-IR-23-062>
- <https://www.fortiguard.com/psirt/FG-IR-23-167>
- <https://www.fortiguard.com/psirt/FG-IR-22-352>
- <https://www.fortiguard.com/psirt/FG-IR-23-318>
- <https://www.fortiguard.com/psirt/FG-IR-23-085>