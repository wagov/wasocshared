# Apache Spark Command Injection Vulnerability - 20230308003

## Overview
The WA SOC has received an adivsory from CISA regarding Apache Spark having known exploits detected in the wild, elevating the risk to organisations.

## What is the vulnerability?

| CVE | Vulnerability Name | Advisory Released | Threat Description | Action |
| --- | --- | --- | --- | --- |
| [**CVE-2022-33891**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33891) - CVSSv3: ***8.8 HIGH*** | Apache Spark Command Injection Vulnerabilit | 2023-03-08 | Apache Spark contains a command injection vulnerability via Spark User Interface (UI) when Access Control Lists (ACLs) are enabled. | Apply updates per vendor instructions. |

## What is vulnerable? 
The vulnerability affects the following products:
- Apache Spark versions 3.0.3 and earlier, versions 3.1.1 to 3.1.2, and versions 3.2.0 to 3.2.1.

## Recommendation
The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices: [https://spark.apache.org/security.html](https://spark.apache.org/security.html)

## Additional References:
* [NIST CVE-2022-33891](https://nvd.nist.gov/vuln/detail/CVE-2022-33891)
* [MITRE CVE-2022-33891](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33891)