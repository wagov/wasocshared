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