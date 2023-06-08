# Mozilla Security Updates for Thunderbird and Firefox - 20221214002

## Overview

Mozilla has released security updates to address vulnerabilities in Thunderbird, Firefox ESR, and Firefox. An attacker could exploit these vulnerabilities to take control of an affected system.

## What is the threat?

Mozilla have confirmed forms of compromise include:

* Potentially running commands on a user's computer via .atloc and .ftploc files
* Memory corruption leading to running arbitrary code
* Filename truncation to remove the valid extension, leaving a malicious extension in its place
* Partially escaping the sandbox to read arbitrary files via clipboard-related IPC messages
* Potentially exploitable crashes

## What is vulnerable?

* [Thunderbird 102.6](https://www.mozilla.org/en-US/security/advisories/mfsa2022-53/)
* [Firefox ESR 102.6](https://www.mozilla.org/en-US/security/advisories/mfsa2022-52/)
* [Firefox 108](https://www.mozilla.org/en-US/security/advisories/mfsa2022-51/)

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC encourages users and administrators to review the security advisory for the above mentioned Mozilla's products

### Reference

* Mozilla Security Advisories - [https://www.mozilla.org/en-US/security/advisories/](https://www.mozilla.org/en-US/security/advisories/)
