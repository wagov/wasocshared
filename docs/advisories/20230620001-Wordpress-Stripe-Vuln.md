# WooCommerce Stripe Gateway WordPress Vulnerability - 20230620001

## Overview

A vulnerability in the [WooCommerce Stripe Gateway WordPress plugin](https://wordpress.org/plugins/woocommerce-gateway-stripe/#description) may allow an unauthenticated actor to view order details placed using the plugin by taking advantage of an insecure direct object reference (IDOR) vulnerability.

## What is the vulnerability?

[**CVE-2023-34000**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34000) - CVSS v3 Base Score: ***7.5***

## What is vulnerable?

The vulnerability affects the following products:

- [WooCommerce Stripe Gateway WordPress plugin](https://wordpress.org/plugins/woocommerce-gateway-stripe/#description) - Version 7.4.0 and older.

## What has been observed?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing

## Recommendation

The WA SOC recommends administrators apply the solutions as per vendor instructions to all affected devices: [WooCommerce Stripe Gateway WordPress plugin](https://wordpress.org/plugins/woocommerce-gateway-stripe/)

## Additional References

- [BleepingComputer - WordPress Stripe payment plugin bug leaks customer order details](https://www.bleepingcomputer.com/news/security/wordpress-stripe-payment-plugin-bug-leaks-customer-order-details/)
