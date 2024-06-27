# JavaScript Polyfill Supply Chain Attack - 20240626004

## Overview

The JavaScript library Polyfill.io, which is extensively utilized, has been flagged for substantial security vulnerabilities after being acquired by the Chinese firm Funnull. Sansec, a cybersecurity firm, has issued a warning that since the acquisition earlier this year, the polyfill.io service and domain have been compromised to inject harmful code into websites, indicating a supply chain attack which impacts over 100K sites.

## Summary

The polyfill code is dynamically generated based on the HTTP headers, so multiple attack vectors are likely.

In addition, the decrypted malware code redirects users to a sports betting website using a dummy Google analytics domain (www.googie-anaiytics.com). The code is designed to prevent against reverse engineering and only activates on specific mobile devices at specific hours. It also does not turn on when it detects an admin user, and delays execution when a web analytics service is found, presumably so that it does not appear in the statistics.

Currently, the cdn.polyfill.io domain is inexplicably diverted to Cloudflare's mirror. However, because the domain's DNS servers are unaltered, the owners can easily switch it back to their own domains at any time.

Google has also started blocking Google Ads for websites using the affected code to reduce the number of potential targets.

## The Threat?

**End-User**:

-   MITRE Technique:

    -   **Drive-by Compromise** - <https://attack.mitre.org/techniques/T1189/>

    -   **Command and Scripting Interpreter: JavaScript** - <https://attack.mitre.org/techniques/T1059/007/>

-   When a user accessed a website that uses polyfill library, the Polyfill library will perform a request to hxxps://cdn.polyfill.io/v2/polyfill.min.js OR hxxps://cdn.polyfill.io/v3/polyfill.min.js

-   If the user matches certain criterion (i.e. mobile devices, specific mobile OS platform, specific hours, specific user-agent), it will return an original polyfill code injected with malicious code, which will run a malicious javascript. (See <https://github.com/polyfillpolyfill/polyfill-service/issues/2873#issuecomment-2182491302> for details)

-   See below IOCs for identified domain-name used to deliver payload.

**Website Provider (Agencies):**

-   MITRE Techniques: **Supply Chain Compromise** - <https://attack.mitre.org/techniques/T1195/>

-   Agencies that uses the old polyfill library on their websites may cause user's visiting their website vulnerable to the drive-by compromise attack.

-   As of 25 June 2024, Google have started blocking Google Ads for eCommerce sites that uses polyfill[.]io

## What has been observed?
WA SOC has not observed any signs of outbound activities to malicious payload within SOC connected entities. (subject to data connector's availability). (Note: Based on current write-ups, the threat actor seemed to be targeting mobile devices)

## Recommended Actions:
WA SOC recommends entities to perform the following actions:

-   Agency to search for instance of cdn[.]polyfill[.]io in source code across the projects within the organisation

-   Agency may have 2 options in regards to the use of Polyfill:

    -   **Option-1**: Deprecate the usage of polyfill. Reference: <https://x.com/triblondon/status/1761852117579427975>

    -   **Option-2**: If polyfill still needed, use alternatives polyfill library from Fastly and Cloudflare (Reference: <https://blog.cloudflare.com/polyfill-io-now-available-on-cdnjs-reduce-your-supply-chain-risk>, <https://community.fastly.com/t/new-options-for-polyfill-io-users/2540>

## IOC:
|Indicator |Type | Description|
| -- | -- | -- |
|hxxps://kuurza[.]com/redirect?from=bitget|domainName|Payload C&C|
|hxxps://www[.]googie-anaiytics[.]com/html/checkcachehw.js|domainName|Payload C&C|
|hxxps://www[.]googie-anaiytics[.]com/ga.js|domainName|Payload C&C|

## Reference

- https://remysharp.com/2010/10/08/what-is-a-polyfill/
- https://polykill.io/ 
- https://sansec.io/research/polyfill-supply-chain-attack
- https://web.archive.org/web/20240624110153/https://github.com/polyfillpolyfill/polyfill-service/issues/2873