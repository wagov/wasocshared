# Mozilla Releases Multiple Security Updates - 20231123002

## Overview

Mozilla has released security updates to address vulnerabilities in Firefox and Thunderbird. A cyber threat actor could exploit some of these vulnerabilities to take control of an affected system.

## What is vulnerable?

| Product | CVE | Score | Brief Description |
| --- | --- | --- | --- | 
| **Firefox iOS 120** | [**CVE-2023-49060**](https://nvd.nist.gov/vuln/detail/CVE-2023-49060) | TBA | An attacker could have accessed internal pages or data by ex-filtrating a security key from ReaderMode via the referrerpolicy attribute. | 
|  | [**CVE-2023-49061**](https://nvd.nist.gov/vuln/detail/CVE-2023-49061) | TBA | An attacker could have performed HTML template injection via Reader Mode and exfiltrated user information. | 
| **Firefox 120** | [**CVE-2023-6204**](https://nvd.nist.gov/vuln/detail/CVE-2023-6204) | TBA | On some systems—depending on the graphics settings and drivers—it was possible to force an out-of-bounds read and leak memory data into the images created on the canvas element. | 
|  | [**CVE-2023-6205**](https://nvd.nist.gov/vuln/detail/CVE-2023-6205) | TBA | It was possible to cause the use of a MessagePort after it had already been freed, which could potentially have led to an exploitable crash. | 
|  | [**CVE-2023-6206**](https://nvd.nist.gov/vuln/detail/CVE-2023-6206) | TBA | The black fade animation when exiting fullscreen is roughly the length of the anti-clickjacking delay on permission prompts. It was possible to use this fact to surprise users by luring them to click where the permission grant button would be about to appear. | 
|  | [**CVE-2023-6207**](https://nvd.nist.gov/vuln/detail/CVE-2023-6207) | TBA | Ownership mismanagement led to a use-after-free in ReadableByteStreams | 
|  | [**CVE-2023-6208**](https://nvd.nist.gov/vuln/detail/CVE-2023-6208) | TBA | When using X11, text selected by the page using the Selection API was erroneously copied into the primary selection, a temporary storage not unlike the clipboard. | 
|  | [**CVE-2023-6209**](https://nvd.nist.gov/vuln/detail/CVE-2023-6209) | TBA | Relative URLs starting with three slashes were incorrectly parsed, and a path-traversal "/../" part in the path could be used to override the specified host. This could contribute to security problems in web sites. | 
|  | [**CVE-2023-6210**](https://nvd.nist.gov/vuln/detail/CVE-2023-6210) | TBA | When an https: web page created a pop-up from a "javascript:" URL, that pop-up was incorrectly allowed to load blockable content such as iframes from insecure http: URLs | 
|  | [**CVE-2023-6211**](https://nvd.nist.gov/vuln/detail/CVE-2023-6211) | TBA | If an attacker needed a user to load an insecure http: page and knew that user had enabled HTTPS-only mode, the attacker could have tricked the user into clicking to grant an HTTPS-only exception if they could get the user to participate in a clicking game. | 
|  | [**CVE-2023-6212**](https://nvd.nist.gov/vuln/detail/CVE-2023-6212) | TBA | Memory safety bugs present in Firefox 119, Firefox ESR 115.4, and Thunderbird 115.4. Some of these bugs showed evidence of memory corruption and we presume that with enough effort some of these could have been exploited to run arbitrary code. | 
|  | [**CVE-2023-6213**](https://nvd.nist.gov/vuln/detail/CVE-2023-6213) | TBA | Memory safety bugs present in Firefox 119. Some of these bugs showed evidence of memory corruption and we presume that with enough effort some of these could have been exploited to run arbitrary code. | 
| **Firefox ESR 115.5** | [**CVE-2023-6204**](https://nvd.nist.gov/vuln/detail/CVE-2023-6204) | TBA | On some systems—depending on the graphics settings and drivers—it was possible to force an out-of-bounds read and leak memory data into the images created on the canvas element. | 
|  | [**CVE-2023-6205**](https://nvd.nist.gov/vuln/detail/CVE-2023-6205) | TBA | It was possible to cause the use of a MessagePort after it had already been freed, which could potentially have led to an exploitable crash. | 
|  | [**CVE-2023-6206**](https://nvd.nist.gov/vuln/detail/CVE-2023-6206) | TBA | The black fade animation when exiting fullscreen is roughly the length of the anti-clickjacking delay on permission prompts. It was possible to use this fact to surprise users by luring them to click where the permission grant button would be about to appear. | 
|  | [**CVE-2023-6207**](https://nvd.nist.gov/vuln/detail/CVE-2023-6207) | TBA | Ownership mismanagement led to a use-after-free in ReadableByteStreams | 
|  | [**CVE-2023-6208**](https://nvd.nist.gov/vuln/detail/CVE-2023-6208) | TBA | When using X11, text selected by the page using the Selection API was erroneously copied into the primary selection, a temporary storage not unlike the clipboard. | 
|  | [**CVE-2023-6209**](https://nvd.nist.gov/vuln/detail/CVE-2023-6209) | TBA | Relative URLs starting with three slashes were incorrectly parsed, and a path-traversal "/../" part in the path could be used to override the specified host. This could contribute to security problems in web sites. | 
|  | [**CVE-2023-6212**](https://nvd.nist.gov/vuln/detail/CVE-2023-6212) | TBA | Memory safety bugs present in Firefox 119, Firefox ESR 115.4, and Thunderbird 115.4. Some of these bugs showed evidence of memory corruption and we presume that with enough effort some of these could have been exploited to run arbitrary code. | 
| **Thunderbird 115.5.0** | [**CVE-2023-6204**](https://nvd.nist.gov/vuln/detail/CVE-2023-6204) | TBA | On some systems—depending on the graphics settings and drivers—it was possible to force an out-of-bounds read and leak memory data into the images created on the canvas element. | 
|  | [**CVE-2023-6205**](https://nvd.nist.gov/vuln/detail/CVE-2023-6205) | TBA | It was possible to cause the use of a MessagePort after it had already been freed, which could potentially have led to an exploitable crash. | 
|  | [**CVE-2023-6206**](https://nvd.nist.gov/vuln/detail/CVE-2023-6206) | TBA | The black fade animation when exiting fullscreen is roughly the length of the anti-clickjacking delay on permission prompts. It was possible to use this fact to surprise users by luring them to click where the permission grant button would be about to appear. | 
|  | [**CVE-2023-6207**](https://nvd.nist.gov/vuln/detail/CVE-2023-6207) | TBA | Ownership mismanagement led to a use-after-free in ReadableByteStreams | 
|  | [**CVE-2023-6208**](https://nvd.nist.gov/vuln/detail/CVE-2023-6208) | TBA | When using X11, text selected by the page using the Selection API was erroneously copied into the primary selection, a temporary storage not unlike the clipboard. | 
|  | [**CVE-2023-6209**](https://nvd.nist.gov/vuln/detail/CVE-2023-6209) | TBA | Relative URLs starting with three slashes were incorrectly parsed, and a path-traversal "/../" part in the path could be used to override the specified host. This could contribute to security problems in web sites. | 
|  | [**CVE-2023-6212**](https://nvd.nist.gov/vuln/detail/CVE-2023-6212) | TBA | Memory safety bugs present in Firefox 119, Firefox ESR 115.4, and Thunderbird 115.4. Some of these bugs showed evidence of memory corruption and we presume that with enough effort some of these could have been exploited to run arbitrary code. | 

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

-   [Firefox iOS 120](https://www.mozilla.org/en-US/security/advisories/mfsa2023-51/ "Security Vulnerabilities fixed in Firefox for iOS 120")
-   [Firefox 120](https://www.mozilla.org/en-US/security/advisories/mfsa2023-49/ "Security Vulnerabilities fixed in Firefox 120")
-   [Firefox ESR 115.5](https://www.mozilla.org/en-US/security/advisories/mfsa2023-50/ "Security Vulnerabilities fixed in Firefox ESR 115.5")
-   [Thunderbird 115.5.0](https://www.mozilla.org/en-US/security/advisories/mfsa2023-52/ "Security Vulnerabilities fixed in Thunderbird 115.5.0")
