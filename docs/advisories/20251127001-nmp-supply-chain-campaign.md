# GitLab NPM Supply Chain Security Advisory - 20251127001

## Overview

Since the publication of Advisory 20250919002, GitLab has published a security advisory relating to newly observed active, large-scale supply chain attacks involving a destructive malware variant spreading through the npm ecosystem, including Indicators of Compromise (IOCs).

GitLab also reports to uncovered multiple infected packages containing what appears to be an evolved version of the "Shai-Hulud" malware.


## What has been observed?

GitLab has published a security advisory containing potential Indicators of Compromise (IOCs).

Recently published articles report that the threat leverages compromised maintainer accounts to publish trojanized versions of legitimate npm packages that execute credential theft and exfiltration code during installation.


## Recommendation

The WASOC recommends that administrators review and remove affected versions of npm packages from their environments:

- GitLab security advisory: <https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/>

## Additional Resources

- Wiz article: <https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack>
- ArcticWolf article: <https://arcticwolf.com/resources/blog/shai-hulud-malware-targets-numerous-npm-packages-second-wave-npm-supply-chain-attack/>
