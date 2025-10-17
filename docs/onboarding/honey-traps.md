# WASOC Honey Traps

## Overview

!!! note

    This Honey Trap initiative is now a established service catalogue item from the WASOC, as such, access to this service is now available to WA Government Entities upon request.
    If interested in the services, please raise a request via the [WASOC IRP](https://irp.dpc.wa.gov.au/).

The WASOC is looking to expand the monitoring capability of Western Australian Government entities to better detect for advanced persistent threats (APT) on ICT infrastructure. The WASOC will assist entities with the deployment of honey pots and honey tokens in infrastructure locations that are commonly traversed by Threat Actors prior to a cyber incident.

Honey Traps emcompass both Honey Pots and Honey Tokens. Honey Traps are decoy ICT services or data repositories that replicate the real ICT environment of organisations. These decoys are enticing targets for threat actors to attack and exploit. Once the actor has attacked the target, the Honey Pot or Honey Token will raise an alert due to unauthorised malipulation, thus allowing security teams to detect for broader threats to an entity's ICT environments.

??? note "Participants Prerequisite"

    The service has prerequisites that must be met to have the minimum technical & commitment requirements to onboard to the Honey Trap Program as to take advantage of the full service offering.

    The prerequisites as follows.

    - Must have signed an exisiting MOU (T0,T1,T2) with the WASOC
    - Must have a Microsoft Sentinel workspace located in region **Australia EAST**
    - Must have been already onboarded to the WASOC via [Azure Lighthouse](https://soc.cyber.wa.gov.au//onboarding/#23-azure-subscription-access-delegation)
    - Must have access to the [WASOC IRP](https://irp.dpc.wa.gov.au/) to raise Honey Traps request tickets.
    - Must be able nominate a individual from your organisation to work closely with the WASOC Engineering Team during the pilot.

    The onboarding to the Honey Trap Platform is handled entirely by the WASOC Engineers and can be facilitated upon request via the [WASOC IRP](https://irp.dpc.wa.gov.au/).

    The WASOC is willing to work with entities to adapt the platform as fit for purpose for their environment but may not be able to take full advantage of the service offering.

## Onboarding Process

The WASOC has developed guidance to assist WA Government entities to integrate the Honey Trap platform into their exisiting Sentinel Workspaces. This can be found [here](https://github.com/wagov/wasoc-honeytraps).

## Honey Trap Guidance

The WASOC recommends that entities explore the following locations within their infrastructure to deploy Honey Traps effectively for each applicable honey technology.

### Honey Pots Deployment

Honey Pots are decoy and usually virtual servers/services that mimic the infrastructure in the network where they are placed. Ideally, dependant on the network, the honey pots deployed should appear to be a realistic server/service that would be expected at this location. This level of deception would make the honey pot a more ideal target for threat actors.

Ideal Network Location for Honey Pot deployment:

- [Demilitarized Zone (DMZ)](<https://en.wikipedia.org/wiki/DMZ_(computing)>)
- [Network Segmentations](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Network_Segmentation_Cheat_Sheet.md#introduction)
    - [MiddleWare](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Network_Segmentation_Cheat_Sheet.md#middleware)
    - [Backend](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Network_Segmentation_Cheat_Sheet.md#backend)

### Honey Token Deployment

Honey Tokens are virtual decoy objects suchs as Files, API Tokens, etc that mimic repositories of information that could be leveraged by Threat Actor(s) to escalate attacks on an organisation. Ideally, dependant on the object types and repositiory locations, the honey files should appear to be a realistic object that would be expected at this location. This level of deception would make the honey tokens a more ideal target for threat actors. Honey Tokens deployment is the most applicable technology for modern cloud based environments.

Ideal object repository location for Honey token deployment:

- Internet Facing FileShares
- Internet Facing Servers
- IAM Sign-in Portals
- Databases
- Code Repositories
