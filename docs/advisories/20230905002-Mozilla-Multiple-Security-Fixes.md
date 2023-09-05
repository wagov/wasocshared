# Mozilla Releases Multiple Security Updates for Firefox ESR - 20230905002

## Overview

Mozilla has released security updates to address vulnerabilities in Firefox ESR **all versions below 115.2**. An attacker could exploit some of these vulnerabilities to potentially allow the leak of sensitive information.

## What are the vulnerabilities?

- [**CVE-2023-4573**](https://nvd.nist.gov/vuln/detail/CVE-2023-4573): Memory corruption in IPC CanvasTranslator
- [**CVE-2023-4574**](https://nvd.nist.gov/vuln/detail/CVE-2023-4574): Memory corruption in IPC ColorPickerShownCallback
- [**CVE-2023-4575**](https://nvd.nist.gov/vuln/detail/CVE-2023-4575): Memory corruption in IPC FilePickerShownCallback
- [**CVE-2023-4576**](https://nvd.nist.gov/vuln/detail/CVE-2023-4576): Integer Overflow in RecordedSourceSurfaceCreation
- [**CVE-2023-4577**](https://nvd.nist.gov/vuln/detail/CVE-2023-4577): Memory corruption in JIT UpdateRegExpStatics
- [**CVE-2023-4051**](https://nvd.nist.gov/vuln/detail/CVE-2023-4051): Full screen notification obscured by file open dialog
- [**CVE-2023-4578**](https://nvd.nist.gov/vuln/detail/CVE-2023-4578): Error reporting methods in SpiderMonkey could have triggered an Out of Memory Exception
- [**CVE-2023-4053**](https://nvd.nist.gov/vuln/detail/CVE-2023-4053): Full screen notification obscured by external program
- [**CVE-2023-4580**](https://nvd.nist.gov/vuln/detail/CVE-2023-4580): Push notifications saved to disk unencrypted
- [**CVE-2023-4581**](https://nvd.nist.gov/vuln/detail/CVE-2023-4581): XLL file extensions were downloadable without warnings
- [**CVE-2023-4582**](https://nvd.nist.gov/vuln/detail/CVE-2023-4582): Buffer Overflow in WebGL glGetProgramiv
- [**CVE-2023-4583**](https://nvd.nist.gov/vuln/detail/CVE-2023-4583): Browsing Context potentially not cleared when closing Private Window
- [**CVE-2023-4584**](https://nvd.nist.gov/vuln/detail/CVE-2023-4584): Memory safety bugs fixed in Firefox 117, Firefox ESR 102.15, Firefox ESR 115.2, Thunderbird 102.15, and Thunderbird 115.2
- [**CVE-2023-4585**](https://nvd.nist.gov/vuln/detail/CVE-2023-4585): Memory safety bugs fixed in Firefox 117, Firefox ESR 115.2, and Thunderbird 115.2

## What is vulnerable?

The above listed vulnerabilities affect Firefox ESR **all versions below 115.2**.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month...* (refer [Patch Management](../guidelines/patch-management.md)):

- <https://www.mozilla.org/en-US/security/advisories/mfsa2023-36/>
