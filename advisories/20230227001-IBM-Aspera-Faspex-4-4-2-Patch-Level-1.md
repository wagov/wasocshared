# IBM Aspera Faspex 4.4.2 Patch Level 1 - 20230227001

## Overview
IBM Aspera Faspex 4.4.2 Patch Level 1 and earlier could allow a remote attacker to execute arbitrary code on the system, caused by a YAML deserialization flaw. 


## What is the vulnerability?
By sending a specially crafted obsolete API call, an attacker could exploit this vulnerability to execute arbitrary code on the system. 

| CWE-ID | CWE Name 
| --- | --- |
| [CWE-502](http://cwe.mitre.org/data/definitions/502.html) | Deserialization of Untrusted Data |   |

  [**CVE - CVE-2022-47986 (mitre.org)**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47986)  IBM Aspera Faspex 4.4.2 Patch Level 1

## What is vulnerable? 
The obsolete API call was removed in Faspex 4.4.2 PL2. IBM X-Force ID: 243512.

## Recommendation
Refer to the appropriate IBM Security Bulletin for patch, upgrade or suggested workaround information. See References.

## Additional References:
-   [MISC:https://exchange.xforce.ibmcloud.com/vulnerabilities/243512](https://exchange.xforce.ibmcloud.com/vulnerabilities/243512)
-   [URL:https://exchange.xforce.ibmcloud.com/vulnerabilities/243512](https://exchange.xforce.ibmcloud.com/vulnerabilities/243512)
-   [MISC:https://www.ibm.com/support/pages/node/6952319](https://www.ibm.com/support/pages/node/6952319)
-   [URL:https://www.ibm.com/support/pages/node/6952319](https://www.ibm.com/support/pages/node/6952319)