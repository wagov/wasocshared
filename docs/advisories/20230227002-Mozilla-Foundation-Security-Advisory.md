# Mozilla Releases Security Updates for Thunderbird 102.8 - 20230227002

## Overview

Mozilla has released security updates to address vulnerabilities in Thunderbird 102.8. An attacker could exploit some of these vulnerabilities to take control of an affected system.

## What is the vulnerability?

*Except for CVE-2023--0616, these flaws cannot be exploited through email in the Thunderbird product because scripting is disabled when reading mail, but are potentially risks in browser or browser-like contexts.*

- [CVE-2023-0616: User Interface lockup with messages combining S/MIME and OpenPGP](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-0616)
- [CVE-2023-25728: Content security policy leak in violation reports using iframes](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25728)
- [CVE-2023-25730: Screen hijack via browser fullscreen mode](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25730)
- [CVE-2023-0767: Arbitrary memory write via PKCS 12 in NSS](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-0767)
- [CVE-2023-25735: Potential use-after-free from compartment mismatch in SpiderMonkey](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25735)
- [CVE-2023-25737: Invalid downcast in SVGUtils::SetupStrokeGeometry](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25737)
- [CVE-2023-25739: Use-after-free in mozilla::dom::ScriptLoadContext::~ScriptLoadContext](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25739)
- [CVE-2023-25729: Extensions could have opened external schemes without user knowledge](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25729)
- [CVE-2023-25732: Out of bounds memory write from EncodeInputStream](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25732)
- [CVE-2023-25734: Opening local .url files could cause unexpected network loads](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25734)
- [CVE-2023-25746: Memory safety bugs fixed in Thunderbird 102.8](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25746)
- [CVE-2023-25742: Web Crypto ImportKey crashes tab](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/#CVE-2023-25742)

## What is vulnerable?

The vulnerability affects the following products:

- Thunderbird
- Thunderbird 102.8

## Recommendation

CISA encourages users and administrators to review Mozilla's security advisory for [Thunderbird 102.8](https://www.mozilla.org/en-US/security/advisories/mfsa2023-07/ "Thunderbird 102.8") for more information and apply the necessary updates.

## Additional References

- [Memory safety bugs fixed in Thunderbird 102.8](https://bugzilla.mozilla.org/buglist.cgi?bug_id=1544127%2C1762368%2C1789449%2C1803628%2C1810536)
