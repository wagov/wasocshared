  
# Increased Events from Threat Activity Group DEV-0867 - 20230118001

## Overview
The WA SOC has observed an increase of events relating to threat activity group **DEV-0867**.

## Delivery
The primary delivery method is via email containing a URL.

## Detection and Remediation

### Detection

 1. Identify the presence of the below supplied KQL/ Kusto hunting code
 2. Identify the presence of the below supplied IOCs
 3. Inspect activity from the identified devices and/or users

### Recommended Remediation Steps
1.  Run a full Antivirus scan on the compromised device
2.  Reset the affected user's passwords

## Indicators of Compromise (IOCs)

### Email information
```text
Subject contains "You have received a new shared documents."
SenderMailFromDomain contains "nam.pb-dynmktg[.]com"
SenderFromAddress contains "surveys@email.formspro.microsoft[.]com"
(1st Stage) EmailUrlInfo contains "hXXps://ecv.microsoft[.]com/CIjY5rWKbO"
(2nd Stage) URL "courseas[.]ru"
```

### KQL Query
***Please proceed with caution as the following lines have not been defanged.***

//Email item status
```kusto
EmailEvents
| where Subject endswith "You have received a new shared documents."
| where SenderMailFromDomain contains "nam.pb-dynmktg.com"
| where SenderFromAddress contains "surveys@email.formspro.microsoft.com"
```

//URL Clicks
```kusto
DeviceEvents
| where RemoteUrl contains "courseas.ru"
```
