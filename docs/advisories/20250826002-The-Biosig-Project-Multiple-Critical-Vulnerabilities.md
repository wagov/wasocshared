# The Biosig Project Multiple Critical Vulnerabilities - 20250826002

## Overview

The WASOC has been made aware of a stack-based buffer overflow vulnerability that exists in the MFER parsing functionality of The Biosig Project libbiosig 3.9.0 and Master Branch (35a819fa). A specially crafted MFER file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.

## What is vulnerable?

| Product(s) Affected | Version(s) | CVE                                                                                                                                      | CVSS         | Severity                                                       |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------- |
| The Biosig Project lobbiosig      | The Biosig Project libbiosig 3.9.0 <br/>The Biosig Project libbiosig Master Branch (35a819fa)  | [CVE-2025-54489](https://nvd.nist.gov/vuln/detail/CVE-2025-54489) <br/> [CVE-2025-54484](https://nvd.nist.gov/vuln/detail/CVE-2025-54484) <br/> [CVE-2025-54494](https://nvd.nist.gov/vuln/detail/CVE-2025-54494) <br/> [CVE-2025-54492](https://nvd.nist.gov/vuln/detail/CVE-2025-54492)  <br/> [CVE-2025-54483](https://nvd.nist.gov/vuln/detail/CVE-2025-54483)  <br/> [CVE-2025-54487](https://nvd.nist.gov/vuln/detail/CVE-2025-54487) <br/> [CVE-2025-54493](https://nvd.nist.gov/vuln/detail/CVE-2025-54493) <br/> [CVE-2025-54490](https://nvd.nist.gov/vuln/detail/CVE-2025-54490)  <br/> [CVE-2025-54491](https://nvd.nist.gov/vuln/detail/CVE-2025-54491) <br/> [CVE-2025-54480](https://nvd.nist.gov/vuln/detail/CVE-2025-54480)  <br/> [CVE-2025-54482](https://nvd.nist.gov/vuln/detail/CVE-2025-54482)  <br/> [CVE-2025-54486](https://nvd.nist.gov/vuln/detail/CVE-2025-54486)  <br/> [CVE-2025-54485](https://nvd.nist.gov/vuln/detail/CVE-2025-54485)  <br/> [CVE-2025-54481](https://nvd.nist.gov/vuln/detail/CVE-2025-54481)  <br/> [CVE-2025-54488](https://nvd.nist.gov/vuln/detail/CVE-2025-54488)                                                                                                                                                                                                                                                     | 9.8          | **Critical**     |


## What has been observed?

The WASOC has not received any reports of exploitation of this vulnerability on Western Australian Government networks at the time of writing.

## Recommendation

The WASOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframes (refer [Patch Management](../guidelines/patch-management.md)):



## Additional References

- TalosIntelligence: <https://talosintelligence.com/vulnerability_reports/TALOS-2025-2234>
