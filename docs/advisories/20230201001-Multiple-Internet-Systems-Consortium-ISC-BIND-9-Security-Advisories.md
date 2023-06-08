# Multiple Internet Systems Consortium (ISC) BIND 9 Security Advisories - 20230201001

## Overview
--------------------------------------------------------------------------------------------------------------------------------

The Internet Systems Consortium (ISC) has released security advisories that address vulnerabilities affecting multiple versions of the ISC’s [Berkeley Internet Name Domain (BIND) 9](https://www.cisa.gov/uscert/ncas/current-activity/2023/01/27/isc-releases-security-advisories-multiple-versions-bind-9). A remote attacker could exploit these vulnerabilities to potentially cause denial-of-service conditions and system failures.


## What is vulnerable? 
--------------------------------------------------------------------------------------------------------------------------------

Below are the Internet Systems Consortium (ISC) Advisory links and relevant products:

-   [CVE-2022-3094](https://kb.isc.org/v1/docs/cve-2022-3094): **BIND and BIND Supported Preview Edition** - An UPDATE message flood may cause named to exhaust all available memory.
-   [CVE-2022-3488](https://kb.isc.org/v1/docs/cve-2022-3488): **BIND Supported Preview Edition** - BIND Supported Preview Edition named may terminate unexpectedly when processing ECS options in repeated responses to iterative queries.
-   [CVE-2022-3736](https://kb.isc.org/v1/docs/cve-2022-3736): **BIND and BIND Supported Preview Edition** - Named configured to answer from stale cache may terminate unexpectedly while processing RRSIG queries.
-   [CVE-2022-3924](https://kb.isc.org/v1/docs/cve-2022-3924): **BIND and BIND Supported Preview Edition** - Named configured to answer from stale cache may terminate unexpectedly at recursive-clients soft quota.

--------------------------------------------------------------------------------------------------------------------------------

## Recommendation
The WA SOC recommends administrators to review the listed security advisories and apply the solutions as per vendor instructions to all affected products.


## Additional References:
-   CISA Security Advisories page - <https://www.cisa.gov/uscert/ncas/current-activity/2023/01/27/isc-releases-security-advisories-multiple-versions-bind-9>
-   [CVE-2022-3094](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3094) NIST details page - https://nvd.nist.gov/vuln/detail/CVE-2022-3094
-   [CVE-2022-3488](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3488) NIST details page - https://nvd.nist.gov/vuln/detail/CVE-2022-3488
-   [CVE-2022-3736](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3736) NIST details page - https://nvd.nist.gov/vuln/detail/CVE-2022-3736
-   [CVE-2022-3924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3924) NIST details page - https://nvd.nist.gov/vuln/detail/CVE-2022-3924