# MongoDB Compromise - 20231218004

## Overview

The WASOC has been made aware of an security incident involving MongoDB and their MongoDB Atlas services. MongoDB detected unauthorised access to coporate systems that hosted MongoDB customer metadata and contact information.
MongoDB has stipulated that at the moment there is no evidence of exposure of customer data stored in MongoDB Atlas.

## Indicators

**Update(19-12-2023):** Initial MongoDB investigation has correlated that a unauthorised user had utilised **Mullvad VPN** to access coporate systems. 

The known indicators are as follows: 

- 107.150.22.47
- 138.199.6.199
- 146.70.187.157
- 179.43.189.85
- 185.156.46.165
- 198.44.136.69
- 198.44.136.71
- 198.44.140.133
- 198.44.140.199
- 199.116.118.207
- 206.217.205.88
- 66.63.167.152
- 66.63.167.154
- 87.249.134.10
- 96.44.191.132

The WA SOC recommends to review the indicators against [Atlas Access logs](https://www.mongodb.com/docs/atlas/access-tracking/) for potential un-authorised access.

## What is the vulnerability?

No evidence at this time of any vulnerabilities.

## What is vulnerable?

No evidence at this time of any vulnerabilities.

## What has been observed?

There is no evidence of exploitation or data exfiltration affecting Western Australian Government MongoDB Atlas instances.

## Recommendation

The WA SOC recommends that administrators implement phishing resistant MFA on all accounts and regularly rotate password credentials.

## Additional References

- [**MongoDB Alert**](https://www.mongodb.com/alerts)
