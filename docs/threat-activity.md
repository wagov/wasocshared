## Recent Advisories

{{ include_file('docs/advisories.md', 0, 10)  }}

## WA SOC - Recent Threat Activity (May 2023)

Ensuring 3rd party risk assessments for vendors are reviewed and kept up to date as part of agencies [Cyber Supply Chain Risk Management | Cyber.gov.au](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/outsourcing-and-procurement/cyber-supply-chains/cyber-supply-chain-risk-management) is strongly recommended given further news related to SolarWinds: [DOJ Detected SolarWinds Breach Months Before Public Disclosure | WIRED](https://www.wired.com/story/solarwinds-hack-public-disclosure/). Responsible and timely disclosure of key cyber security threat intelligence with the WA SOC and relevant partners is a key learning from the above incident.

Recently key high profile vulnerabilities this month worth staying across include:

- [PaperCut](https://wagov.github.io/wasocshared/#/advisories/20230426003-PaperCut-NG-Improper-Access-Control-Vulnerability)
- [3CXDesktop](https://wagov.github.io/wasocshared/#/advisories/20230421003-Supply-Chain-Attack-3CXDesktopApp)
- [Illumina Copy Service](https://wagov.github.io/wasocshared/#/advisories/20230428001-ICSMA-23-117-01-Illumina-Universal-Copy-Service)

Agencies should review their software asset register(s) and vulnerability remediation (patching) processes to mitigate against the above vulnerabilities. Any exposed printing services should be worth prioritising due to ongoing threat activity.

**Phishing activity remains high** across all organisations with multiple incidents detected weekly. Please refer to the below guides to ensure all external and internal signins are appropriately monitored.

- [Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue, PRT, OAuth)](https://jeffreyappel.nl/tips-for-preventing-against-new-modern-identity-attacks-aitm-mfa-fatigue-prt-oauth/)
  - [Enabling MFA number matching to mitigate MFA fatigue attacks (AAD)](https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match#enable-number-matching-in-the-portal)
- [How to implement Defender for Identity and configure all prerequisites](https://jeffreyappel.nl/how-to-implement-defender-for-identity-and-configure-all-prerequisites/)
