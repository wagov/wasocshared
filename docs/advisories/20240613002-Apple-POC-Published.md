# Apple Exploitation PoC Published - 20240613002

## Overview

The WA SOC has been made aware of a proof-of-concept (PoC) exploit code pulished affecting multiple Apple platforms. This vulnerability has the potential to elevate privileges, granting malicious apps unauthorized access to system services and sensitive user data.

## What is vulnerable?

| Products Affected.  | CVE  | CVSS | Severity     |
| ------------------- | ---- | ---- | ------------ |
| tvOS </br> macOS </br> visionOS </br> iOS and iPadOS | [CVE-2024-27801](https://nvd.nist.gov/vuln/detail/CVE-2024-27801) | TBD  | TBD |  

## What has been observed?

There is no evidence of active exploitation in the wild at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):

- tvOS: <https://support.apple.com/en-us/HT214102>
- macOS: <https://support.apple.com/en-us/HT214106>
- visionOS: <https://support.apple.com/en-us/HT214108>
- iOS and iPadOS: <https://support.apple.com/en-us/HT214101>

## Additional References

- SecurityOnline article: <https://securityonline.info/cve-2024-27801-critical-vulnerability-discovered-in-apple-ecosystem-poc-published/>
