# ASD Publishes Advisory on Ongoing Attack on NPM - 20250919002

## Overview

The Australian Signals Directorate (ASD) have published an advisory reporting a large-scale supply chain attack targeting the npm (Node Package Manager) ecosystem hosting vast repository projects.

Threat actors launched targeted phishing campaigns to compromise accounts of npm maintainers. Once inside, they published malicious versions of widely-used packages such as: debug, chalk, @ctrl/tinycolor.

## What has been observed?

Threat actors have been observed leveraging legitimate tools and functions to execute attacks, making detection more difficult.

This approach poses a significant threat to developers and organisations by enabling malware delivery through trusted npm packages and exposing internal systems, which broadens the attack surface and facilitates more advanced, targeted exploits.

## Recommendation

The WA SOC recommends that administrators assess and implement mitigation as outlined on the following:

- ASD Advisory: <https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/ongoing-targeting-of-online-code-repositories>
- Socket: <https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages>
- CISA: <https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem>

## Additional Resources

- ASD article "Supply chain risk management": <https://www.cyber.gov.au/business-government/supplier-cyber-risk-management/managing-cyber-supply-chains/cyber-supply-chain-risk-management>
- ASD article "Shared vision of SBOM": <https://www.cyber.gov.au/business-government/supplier-cyber-risk-management/managing-cyber-supply-chains/shared-vision-of-software-bill-of-materials-cybersecurity>

### Change Log

- 2025-09-19: Initial publication
- 2025-09-24: Added CISA reference, and ASD additional resources
