# State-Sponsored Cyber Actor Living off the Land to Evade Detection - 20230525001

## Overview
In May 2023, the Australian Signals Directorate's (ASD) Australian Cyber Security Centre (ACSC) , in conjunction with our international partners, released the Cybersecurity Advisory "People's Republic of China State-Sponsored Cyber Actor Living Off the Land to Evade Detection".

The authoring agencies assess there is significant risk these **Tactics, Techniques and Procedures (TTPs)** could be employed by the actor against **Critical Infrastructure (CI)** and other sectors worldwide.

## What is the Threat ?

The advisory details the TTP's employed by the threat actor, which primarily involve the use of built-in Windows tools on compromised hosts to achieve their objectives. This is known as "living off the land", and allows the actor to evade detection by blending in with normal Windows system and network activity, and avoid triggering security alerts by installing new tools.

This enables the cyber actor to blend in with routine Windows system and network activities, limit activity and data captured in default logging configurations, and avoid **endpoint detection and response (EDR)** products that could alert to the introduction of third-party applications on the host or network. Private sector partners have identified that this activity affects networks across U.S. critical infrastructure sectors, and the authoring agencies believe the actor could apply the same techniques against these and other sectors worldwide.


## What has been observed ?
There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing. 

This advisory highlights a recently-discovered cluster of activity affecting networks across US critical infrastructure sectors, and provides threat hunting advice and best practices for network defenders to detect related activity.

## Recommendation
The WA SOC recommends that given the potential threat is to **CI sectors outside the US**, the ACSC strongly encourages Australian organisations to review the advisory, reported TTPs and **indicators of compromise (IOCs)** and investigate their networks for signs of potential malicious activity. By design, "living off the land" is intended to resemble legitimate system and network activity, so any findings should not be assumed malicious without further investigation.

To maximise opportunities to detect malicious activity, the ACSC recommends Australian organisations review and optimise their logging configurations.

To hunt for this activity, agencies should encourage network defenders to use the actor's commands and detection signatures provided in [this advisory](https://cisa.gov/news-events/cybersecurity-advisories/aa23-144a). Agencies should further encourage network defenders to view the **Indicators of Compromise (IOCs)** and mitigations summaries to detect this activity.

Advice to support both the detection and investigation of malicious activity is available at [Windows Event Logging and Forwarding](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-monitoring/windows-event-logging-and-forwarding "Windows Event Logging and Forwarding").

## Additional References:

For further information, please see:

-   [People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection advisory](https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection "People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection")
-   [Volt Typhoon targets US critical infrastructure with living-off-the-land techniques](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
