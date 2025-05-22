# ASD Publishes Advisory On Compromised Fortinet Devices - 20250522001

## Overview

ASD’s ACSC is aware of successful compromises of ESXi servers hosting virtual machines used by Australian State and Local Government clients following compromise of Fortinet devices. ASD’s ACSC has supported the investigation and a more detailed summary of this activity is being drafted. As attempted lateral movement from the compromised VMware ESXi servers to client virtual machines was observed.

## What has been observed?

Malicious processes were found on FortiManager, FortiGate and vCenter devices, conduct regular integrity checks in order to detect any unauthorised modifications or suspicious processes on Fortinet and VMware devices, as well as hosted virtual machines.

## Recommendation

ASD’s ACSC recommends the following actions be conducted in addition to remediating the Fortinet and VMware devices:

- Monitor for any persistent network interactions with any unusual IP addresses.

- Examine any network and access logging around the timeframe of the incident and lateral movement to your network for:

    - Out of place authentications;

    - Unusual activity via service accounts; and

    - Unauthorised account creations.

- Ensure credentials for devices that were accessed are reset, and logging enabled.

- Store logging in a Security Information and Event Management (SIEM) and maintain backups of devices.

- Stay up to date on device patching and maintain awareness of any relevant CVEs that may affect devices.

- Ensure up-to-date network diagrams are maintained, ideally with device functions.


