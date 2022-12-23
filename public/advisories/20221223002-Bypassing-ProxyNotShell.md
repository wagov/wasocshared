# New Exploit Method for Bypassing ProxyNotShell Mitigations - 20221223002

## Overview
**NOTE:** This advisory only pertains to users who have not applied Microsoft **Exchange update (KB5019758)** from November 2022 or later.

A novel method for exploiting the "ProxyNotShell" remote code execution (RCE) vulnerability has been recently disclosed by [Crowdstrike](https://www.crowdstrike.com/blog/owassrf-exploit-analysis-and-recommendations/). 

## What is the vulnerability ?

The new exploit method, dubbed Outlook **Web Access Server-Side Request Forgery (OWASSRF)**, likely chains [CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080) with [CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082) to effectively bypass the URL rewrite [mitigation rules](https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/) provided by **Microsoft** prior to the November patch Tuesday fixed release for ProxyNotShell.

Instead of leveraging [CVE-2022-41040](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040) from the original ProxyNotShell CVE pairing, post requests have been made through the Outlook Web Access (OWA) endpoint, which is believed to leverage [CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080). 

**[CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080)** - Microsoft Exchange Server Elevation of Privilege Vulnerability

**[CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082)** - Microsoft Exchange Server Remote Code Execution Vulnerability

## What is vulnerable ? 
The following on-prem versions of Exchange that have not applied the November 8, 2022 [KB5019758](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-november-8-2022-kb5019758-2b3b039b-68b9-4f35-9064-6b286f495b1d) update are vulnerable:

- Microsoft Exchange Server **2013, 2016, 2019**

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

This [CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080) has not been publicly detailed yet and is marked as **"exploitation more likely"** by 
Microsoft. **CVE-2022-41080** has been referenced in other exploit chains to achieve RCE.

Reporting suggests this method is currently being exploited in the wild to deploy **Ransomware**.  

## Recommendation
The Office of Digital Government (DGov) recommends organisations apply the latest Exchange patches to avoid exploitation.

- Review Crowdstrike’s [blog post](https://www.crowdstrike.com/blog/owassrf-exploit-analysis-and-recommendations/)
here ().
- Apply the latest [Microsoft Exchange](https://msrc.microsoft.com/update-guide/deployments) update. 
    - Ensure at minimum your patch is Exchange update (KB5019758) from November 2022 or later.
- Disable remote PowerShell for non-administrative users where possible. Guidance can be found here: [Exchange Server](https://learn.microsoft.com/en-us/powershell/exchange/control-remote-powershell-access-to-exchange-servers?view=exchange-ps&viewFallbackFrom=exchange-ps%22%20%5Cl%20%22use-the-exchange-management-shell-to-enable-or-disable-remote-powershell-access-for-a-user) and [Exchange Online](https://learn.microsoft.com/en-us/powershell/exchange/disable-access-to-exchange-online-powershell?view=exchange-ps).
- Review [Crowdstrike’s script](https://github.com/CrowdStrike/OWASSRF) to detect exploitation in IIS and Remote PowerShell logs.
- Ensure X-Forwarded-For header is [configured](https://techcommunity.microsoft.com/t5/iis-support-blog/how-to-use-x-forwarded-for-header-to-log-actual-client-ip/ba-p/873115) to log true external IP addresses for request to proxied services. Guidance available here.

