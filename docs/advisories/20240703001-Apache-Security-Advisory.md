# Apache Security Advisory - 20240703001

## Overview

The WA SOC has been made aware of multiple vulnerabilities in Apache HTTP Server ranging from Denial of Service (DoS) attacks to Remote Code Execution (RCE) and unauthorised access, which require immediate action.   


## What is vulnerable?

| Products Affected | CVE  | CVSS   | Severity  |
| ----------------- | --------------------------------- | ------------- | ------------------------------- |
| Apache HTTP Server versions before 2.4.60 | [CVE-2024-36387](https://nvd.nist.gov/vuln/detail/CVE-2024-36387)<br>[CVE-2024-38472](https://nvd.nist.gov/vuln/detail/CVE-2024-38472)<br>[CVE-2024-38473](https://nvd.nist.gov/vuln/detail/CVE-2024-38473)<br>[CVE-2024-38474](https://nvd.nist.gov/vuln/detail/CVE-2024-38474)<br>[CVE-2024-38475](https://nvd.nist.gov/vuln/detail/CVE-2024-38475)<br>[CVE-2024-38476](https://nvd.nist.gov/vuln/detail/CVE-2024-38476)<br>[CVE-2024-38477](https://nvd.nist.gov/vuln/detail/CVE-2024-38477)<br>[CVE-2024-39573](https://nvd.nist.gov/vuln/detail/CVE-2024-39573) | 7.5<br>7.5<br>8.1<br>8.1<br>9.1<br>8.1<br>7.5<br>7.5  | **High**<br>**High**<br>**High**<br>**High**<br>**Critical**<br>**High**<br>**High**<br>**High** |


## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48h...* (refer [Patch Management](../guidelines/patch-management.md)):

- Apache Release Notes: <https://httpd.apache.org/security/vulnerabilities_24.html>

## Additional References

- SecurityOnline: <https://securityonline.info/multiple-vulnerabilities-in-apache-http-server-demand-immediate-action/>
