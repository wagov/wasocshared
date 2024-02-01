## Microsoft Security Updates - 20240131003

## Overview

Microsoft has released security updates that addresses vulnerabilities in two of their products with security feature bypass vulnerability. An attacker could exploit this by creating a specially crafted X.509 certificate that intentionally introduce or intentionally induces a chain building failure.

## What is vulnerable?

| Product(s) Affected | Summary | Severity     | CVSS |
| ------------------- | ------- | ------------ | ---- |
| [Microsoft.Data.SqlClient and System.Data.SqlClient SQL Data](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-0056) | Security Feature Bypass vulnerability. An attacker who successfully exploited this vulnerability could carry out a machine-in-the-middle (MITM) attack and could decrypt and read or modify TLS traffic between the client and server.  | **High** | 8.7  |
| [NET, .NET Framework, and Visual Studio](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-0057)| Security Feature Bypass Vulnerability. An attacker could exploit this by creating a specially crafted X.509 certificate that intentionally introduce or intentionally induces a chain building failure. | **Critical** | 9.8  |

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [Microsoft security update guide CVE-2024-0056 ](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-0056)
- [Microsoft security update guide CVE-2024-0057](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-0057)

## Additional References

- [NIST vulnerability CVE-2024-0056](https://nvd.nist.gov/vuln/detail/CVE-2024-0056)
- [NIST vulnerability CVE-2024-0057](https://nvd.nist.gov/vuln/detail/CVE-2024-0057)
