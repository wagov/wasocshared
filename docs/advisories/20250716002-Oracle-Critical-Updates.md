# Oracle Critical Updates - 20250716002

## Overview

Oracle has published a critical patch advisory that includes 309 patches across multiple products, which includes a count of vulnerabilities that can be exploited over a network without authentication.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| Oracle Application Express     | Version 24.2.4, 24.2.5  | [CVE-CVE-2025-50067](https://nvd.nist.gov/vuln/detail/CVE-2025-50067)                                                                        | 9.0        | **Critical**                                   |
| Oracle Hospitality Applications, Next-Gen SPMS (Apache Tomcat)     | Version 23.1.4, 23.2.2 | [CVE-CVE-CVE-2025-24813](https://nvd.nist.gov/vuln/detail/CVE-2025-24813)                                                                        | 9.8      | **Critical**      
| Oracle HealthCare Applications,Master Index Data Manager (Apache Mina) | Version 5.0.0.0-5.0.9.2 | [CVE-CVE-CVE-2025-52046](https://nvd.nist.gov/vuln/detail/CVE-2025-52046)   | 9.8      | **Critical**     
| Oracle Business Intelligence Enterprise Edition, Analytics Server (Apache Parquet Java) | Version 7.6.0.0.0, 8.2.0.0.0 | [CVE-CVE-CVE-2025-30065](https://nvd.nist.gov/vuln/detail/CVE-2025-30065)   | 10.0      | **Critical**     
| Oracle Retail Xstore Office, Security (Apache Tomcat) | Version 20.0.5, 21.0.4, 22.0.2, 23.0.2, 24.0.1 | [CVE-CVE-CVE-2025-31651](https://nvd.nist.gov/vuln/detail/CVE-2025-31651)   | 9.8      | **Critical**   


## What has been observed?

The WA SOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):

- Oracle Security Advisory: <https://www.oracle.com/security-alerts/cpujul2025.html>

## Additional References

- Tenable: <https://www.tenable.com/blog/oracle-july-2025-critical-patch-update-addresses-165-cves>
