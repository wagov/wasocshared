# Sumo Logic Discovered Evidence of a Potential Security Incident - 20231109002

## Overview

Sumo Logic discovered evidence of a potential security incident. The activity identified used a compromised credential to access a Sumo Logic AWS account.

## Recommendation

It is recommend that customers rotate credentials that are either used to access Sumo Logic or that you have provided to Sumo Logic to access other systems. Specifically:

**You are advised rotate immediately:**

- Sumo Logic API access keys (If you need assistance with this, please contact Sumo Support at <https://support.sumologic.com/support/s/>)

**What you could also rotate as an additional precautionary measure:**

- Third-party credentials that have been stored with Sumo as part of webhook connection configuration

For more information refer to [Sumo Logic Security Notice](https://www.sumologic.com/security-response-center/#eede153a-8f3f-4eff-858d-1b653eaff457)

## Additional References

- [Sumo Logic Security Notice](https://www.sumologic.com/security-response-center/#eede153a-8f3f-4eff-858d-1b653eaff457)
