# GoAnywhere Active Campaign - 20230331001

## Overview

On 01-February-2023, Fortra (formerly HelpSystems) posted a security advisory for a remote pre-authentication remote code execution vulnerability in their GoAnywhere MFT (managed file transfer) solution. Please note that the advisory requires a (free) account in order to view and is not publicly accessible.

This campaign [has been related](https://www.cybersecuritydive.com/news/ransomware-spree-goanywhere/646152/) to the [CLOP Ransomeware Group](https://www.cisa.gov/sites/default/files/publications/202103231400_Analyst_Note_CL0P_TLP_WHITE.pdf).

On 02-February-2023, security reporter Brian Krebs published a warning on Mastodon about an actively exploited zero-day vulnerability for the product and included the contents of the advisory in his post.

## What is the vulnerability?

[**CVE-2023-0669**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0669) - CVSS v3 Base Score: ***7.2***

- Fortra GoAnywhere MFT suffers from a pre-authentication command injection vulnerability in the License Response Servlet due to deserializing an arbitrary attacker-controlled object. This issue was patched in version 7.1.2.

## What is vulnerable?

The vulnerability affects ***versions below 7.1.2***

## Recommendation

On 07-February-2023, Forta released patch 7.1.2 to address this actively exploited vulnerability.
The WA SOC recommends administrators apply the latest released patches as per vendor instructions to all affected devices.

## Additional References

- Rapid7 Article - [https://www.rapid7.com/blog/post/2023/02/03/exploitation-of-goanywhere-mft-zero-day-vulnerability/](https://www.rapid7.com/blog/post/2023/02/03/exploitation-of-goanywhere-mft-zero-day-vulnerability/)
- Forta (formerly HelpSystems) GoAnywhere MFT Release Notes - [https://hstechdocs.helpsystems.com/releasenotes/Content/\_ProductPages/GoAnywhere/GAMFT.htm](https://hstechdocs.helpsystems.com/releasenotes/Content/_ProductPages/GoAnywhere/GAMFT.htm)
