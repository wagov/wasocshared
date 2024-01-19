# Defending Continuous Integration/Continuous Delivery (CI/CD) Environments - 20230630005

## Overview

The National Security Agency (NSA) and the Cybersecurity and Infrastructure Security
Agency (CISA) are releasing this cybersecurity information sheet (CSI) to provide
recommendations and best practices for improving defenses in cloud implementations
of development, security, and operations (DevSecOps).

This CSI explains how to integrate security best practices into typical software development and operations
(DevOps) Continuous Integration/Continuous Delivery (CI/CD) environments, without
regard for the specific tools being adapted, and leverages several forms of government
guidance to collect and present proper security and privacy controls to harden CI/CD
cloud deployments.

## What is the vulnerability?

- **Insecure first-party code** - Code that is checked in by authorized developers but that contains security-related bugs that are not detected by either the software developers or by security tooling.
- **Insecure third-party code** - Insecure code that is compiled into a CI/CD pipeline from a third-party source, such as an open source project.
- **Poisoned pipeline execution** - Exploitation of a development/test/production environment that allows the attacker to insert code of its choosing.
- **Insufficient pipeline access controls** - Unauthorized access to source code repositories or build tools.
- **Insecure system configuration** - Various infrastructure, network, and application configurations vulnerable to known exploitation techniques.
- **Usage of insecure third-party services** - Using services created by an external individual or organization that intentionally or negligently includes security vulnerabilities.
- **Exposure of secrets** - Security key compromise and insecure secrets management within the pipeline, such as hardcoding access keys or passwords into infrastructure as code (laC) templates.

## Recommendation

The WA SOC recommends administrators to apply the following mitigations outlined in the **NSA/CISA [Cybersecurity Information Sheet](https://media.defense.gov/2023/Jun/28/2003249466/-1/-1/0/CSI_DEFENDING_CI_CD_ENVIRONMENTS.PDF)**:

- **Authentication and access mitigations**:

    - Use NSA-recommended cryptography

    - Minimize the use of long-term credentials

    - Add signature to CI/CD configuration and verify it

    - Utilize two-person rules (2PR) for all code updates

    - Implement least-privilege policies for CI/CD access

    - Secure user accounts

    - Secure secrets

- **Development environment mitigations**:

    - Maintain up-to-date software and operating systems

    - Keep CI/CD tools up-to-date

    - Remove unnecessary applications

    - Implement endpoint detection and response (EDR) tools

    - Integrate security scanning as part of the CI/CD pipeline

    - Restrict untrusted libraries and tools

    - Analyze committed code

    - Remove any temporary resources

    - Keep audit logs

- **Development process mitigations**:

    - Integrate security scanning as part of the CI/CD pipeline

    - Restrict untrusted libraries and tools

    - Analyze committed code

    - Remove any temporary resources

    - Keep audit logs

    - Implement software bill of materials (SBOM) and software composition analysis (SCA)

    - Plan, build, and test for resiliency

## Additional References

- [NSA/CISA - CSI_DEFENDING_CI_CD_ENVIRONMENTS.PDF (defense.gov)](https://media.defense.gov/2023/Jun/28/2003249466/-1/-1/0/CSI_DEFENDING_CI_CD_ENVIRONMENTS.PDF)
