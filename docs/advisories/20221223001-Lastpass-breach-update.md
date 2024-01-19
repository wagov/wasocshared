# Lastpass breach update (ACTION NEEDED: customer details and vaults accessed in November 2022) - 20221223001

## Overview

[Lastpass has publicly disclosed](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/) that threat actors have accessed personal information and related metadata, including company names, end-user names, billing addresses, email addresses, telephone numbers, and IP addresses customers used to access LastPass services. The threat actors also copied a backup of customer vault data that included unencrypted data such as website URLs and encrypted data fields such as website usernames and passwords, secure notes, and form-filled data.

## What is the threat?

Any organisation or individual using Lastpass could be exposed as **platform metadata and vault backups (including credentials)** were **accessed by threat actors in November 2022** after initial access in August 2022. Given the highly privileged access credentials saved in cloud password managers such as Lastpass, threat actors will likely expend significant effort attempting to defeat the master password protection on vaults, including cross-referencing identities with other breaches and brute-forcing identities known to have accessed privileged website URLs.

The architectural fault leading to the significance of this impact (co-located cloud storage containing metadata, service logs, key material and encrypted vaults) should be noted. These **weaknesses likely exist across other online password management services** that don't have appropriate separation of sensitive information.

## Recommendation

- **Immediately update credentials for privileged accounts and services** that have been saved in Lastpass cloud vaults.
- **Update the remaining credentials** for accounts and services that have been saved in a Lastpass cloud vault and have not been updated since **December 2022**.
- **Review usage of password managers**, ensuring that service providers and management teams ensure clear separation of sensitive information **(key material, credential vaults and usage metadata / service logs should be separated)** to provide defense in depth if information is accessed by a threat actor.
- Modern open-source password managers such as [KeePassXC](https://keepassxc.org) support additional factors including [separate key files and hardware tokens](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_opening_an_existing_database) which are recommended for privileged account credential storage and break glass accounts.
- Browser extensions and other integrations that run on every site including privileged sites (such as password managers) should used with caution. Well designed extensions [(KeePassXC-Browser)](https://github.com/keepassxreboot/keepassxc-browser) avoid storing credentials in the browser and don't log service access details or usage outside of users encrypted password vaults.

### Reference

- [Lastpass Update as of Thursday, December 22, 2022 (Lastpass Blog)](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/)
- [LastPass users: Your info and password vault data are now in hackers’ hands (Ars Technica)](https://arstechnica.com/information-technology/2022/12/lastpass-says-hackers-have-obtained-vault-data-and-a-wealth-of-customer-info/)
