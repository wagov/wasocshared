# 3CX Active Intrusion Campaign - 20230330001

## Overview

Multiple sources observing malicious activity from a legtimate application 3CXDesktopApp, which used as softphone application from 3CX.

Crowdstrike has released:

- [Guidance for hunting indicator of potential compromise](https://www.reddit.com/r/crowdstrike/comments/125r3uu/20230329_situational_awareness_crowdstrike/)

## What is vulnerable?

The 3CX Softphone Application and an observed signed malicious installer.

## What has been observed?

The 3CX Softphone installer application has been modified to distibute a malicious payload. The installed application has been observed:

- beaconing to actor controlled infrastructure
- secondary payload distribution
- hands on keyboard activity

## Resources

- [ACSC | Supply chain compromise of 3CX DesktopApp](https://www.cyber.gov.au/acsc/view-all-content/alerts/supply-chain-compromise-3cx-desktopapp)
- [Hackers compromise 3CX desktop app in a supply chain attack - BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-compromise-3cx-desktop-app-in-a-supply-chain-attack/)
- [YARA Signature from Neo23x0](https://github.com/Neo23x0/signature-base/blob/master/yara/gen_mal_3cx_compromise_mar23.yar)
- [Sigma YAML from SigmaHQ](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_malware_3cx_compromise.yml)

## Recommendation

- Locate the presence of 3CXDesktopApp software in your environment by using the queries outlined above.
- Ensure relevant EDR solution is deployed to applicable systems.
- Ensure “Suspicious Processes” is enabled in applicable Prevention Policies.

- [YARA Signature from Neo23x0](https://github.com/Neo23x0/signature-base/blob/master/yara/gen_mal_3cx_compromise_mar23.yar)
- [Sigma YAML from SigmaHQ](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_malware_3cx_compromise.yml)
- Hunt for historical presence of atomic indicators in third-party tooling (if available).
