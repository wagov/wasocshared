# Joint Cybersecurity Advisory (CSA) - 20230713001

## Overview

The Cybersecurity and Infrastructure Security Agency (CISA) and Federal Bureau of Investigation (FBI) have released a joint [Cybersecurity Advisory (CSA), on enhancing monitoring in Microsoft Exchange Online environments](https://www.cisa.gov/sites/default/files/2023-07/aa23-193a_joint_csa_enhanced_monitoring_to_detect_apt_activity_targeting_outlook_online_1.pdf).

An unexpected malicious events in Microsoft 365 (M365) audit logs, have been observed, whereby licensed users can access items in exchange online mailboxes using any connectivity protocol from any client.Microsoft has determined that advanced persistent threat (APT) actors accessed and exfiltrated unclassified Exchange Online Outlook data. The APT actors use a Microsoft account (MSA) consumer key to forge tokens to impersonate consumer and enterprise users.

## What is vulnerable?

The vulnerability affects Microsoft\`s cloud environments:

- [Microsoft Exchange Online](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Exchange%20Online%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)
- [Microsoft 365 Defender](https://www.cisa.gov/sites/default/files/publications/Microsoft%20365%20Defender%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)
- [Microsoft Azure Active Directory](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Azure%20Active%20Directory%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)
- [Microsoft OneDrive for Business](https://www.cisa.gov/sites/default/files/publications/Microsoft%20OneDrive%20for%20Business%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)
- [Microsoft Power BI](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Power%20BI%20M365%20Minimum%20Viable%20SCB%20v0.1.pdf)
- [Microsoft Power Platform](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Power%20Platform%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)
- [Microsoft Sharepoint Online](https://www.cisa.gov/sites/default/files/publications/Microsoft%20SharePoint%20Online%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)
- [Microsoft Teams](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Teams%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices within expected timeframe of *one month* (refer [Patch Management](../guidelines/patch-management.md)):

- [M365 Secure configuration baseline](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Exchange%20Online%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)
- [SEcure Cloud Business Applications (SCuBA)](%22https://www.cisa.gov/resources-tools/services/secure-cloud-business-applications-scuba-project)

## Additional References

- [CISA and FBI joint Cybersecurity Advisory](https://www.cisa.gov/news-events/alerts/2023/07/12/cisa-and-fbi-release-cybersecurity-advisory-enhanced-monitoring-detect-apt-activity-targeting)
