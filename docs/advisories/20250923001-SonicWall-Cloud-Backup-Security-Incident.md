# SonicWall Cloud Backup Security Incident - 20250923001

## Overview

The WASOC has been made aware of a newly published SonicWall security advisory to assist their customers with protecting systems impacted by the MySonicWall cloud backup file incident.

## What has been observed?

SonicWall’s investigation found that a malicious actor performed a series of brute force techniques against their `MySonicWall.com` web portal to gain access to a subset of customers’ preference files stored in their cloud backups. While credentials within the files were encrypted, the files also included information that actors can use to gain access to customers’ SonicWall Firewall devices.

## Recommendation

The WASOC recommends administrators review SonicWall's advisory to determine if their environments may potentially be impacted, and perform noted Containment and Mitigation steps if required:

- SonicWall Advisory: <https://www.sonicwall.com/support/knowledge-base/mysonicwall-cloud-backup-file-incident/250915160910330>
