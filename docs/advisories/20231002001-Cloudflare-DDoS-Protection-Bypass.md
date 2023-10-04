# Cloudflare DDoS protection bypass vulnerability - 20231002001

## Overview

Certitude's researcher Stefan Proksch discovered that Cloudflare's Firewall and DDoS prevention can be bypassed through a specific attack process that leverages logic flaws in cross-tenant security controls. This bypass could put Cloudflare's customers under a heavy burden, rendering the protection systems of the internet firm less effective. [**Read the full article here**](https://certitude.consulting/blog/en/using-cloudflare-to-bypass-cloudflare/)

## What is vulnerable?

Cloudflare uses the SSL/TLS certificate to authenticate any HTTP(S) requests between the service's reverse proxies and the customer's origin server, preventing unauthorized requests from accessing the website. Attackers can bypass this protection as Cloudflare uses a shared certificate for all customers instead of a tenant-specific one, causing all connections originating from Cloudflare to be permitted. 

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

The WA SOC recommends administrators apply the solutions as per the researcher's instructions to all affected devices within expected timeframe of *48 hours...* (refer [Patch Management](../guidelines/patch-management.md)):


## Additional References

- [**Bleeping Computer**](https://www.bleepingcomputer.com/news/security/cloudflare-ddos-protections-ironically-bypassed-using-cloudflare/)
