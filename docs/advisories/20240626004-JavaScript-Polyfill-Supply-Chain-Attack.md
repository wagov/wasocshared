# JavaScript Polyfill Supply Chain Attack - 20240626004

## Overview

The JavaScript library Polyfill.io, which is extensively utilized, has been flagged for substantial security vulnerabilities after being acquired by the Chinese firm Funnull. Sansec, a cybersecurity firm, has issued a warning that since the acquisition earlier this year, the polyfill.io service and domain have been compromised to inject harmful code into websites, indicating a supply chain attack which impacts over 100K sites.

## Summary

The polyfill code is dynamically generated based on the HTTP headers, so multiple attack vectors are likely. 

In addition, the decrypted malware code redirects users to a sports betting website using a dummy Google analytics domain (www.googie-anaiytics.com). The code is designed to prevent against reverse engineering and only activates on specific mobile devices at specific hours. It also does not turn on when it detects an admin user, and delays execution when a web analytics service is found, presumably so that it does not appear in the statistics.

Currently, the cdn.polyfill.io domain is inexplicably diverted to Cloudflare's mirror. However, because the domain's DNS servers are unaltered, the owners can easily switch it back to their own domains at any time.

Google has also started blocking Google Ads for websites using the affected code to reduce the number of potential targets.

## Recommended Mitigations

The WA SOC recommends that any website currently using Polyfill.io to immediately remove its code to avoid potential security breaches. The web administrator are encouraged to support secure and sustainable alternatives to ensure the integrity of their projects.

## Reference

- Bleeping Computer: <https://www.bleepingcomputer.com/news/security/polyfillio-javascript-supply-chain-attack-impacts-over-100k-sites/>
