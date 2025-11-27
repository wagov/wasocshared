# NPM Supply Chain Compromise Activity - 20251127001

## Overview

Since the publication of Advisory 20250919002, the WASOC has observed a newly published article detailing newly observed active, large-scale supply chain attacks involving a destructive malware variant spreading through the npm ecosystem, including Indicators of Compromise (IOCs).

This report states to uncovered multiple infected packages containing what appears to be an evolved version of the "Shai-Hulud" malware.

## What has been observed?

This newly observed article reports that the threat leverages compromised maintainer accounts to publish trojanized versions of legitimate npm packages that execute credential theft and exfiltration code during installation. The article also includes a deep analysis of npm package distribution across cloud and code environments.

## Recommendation

The WASOC recommends that administrators review and remove affected versions of npm packages from their environments:

- Wiz article: <https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack>
