# Template - Tables

## General markdown formatting

| Heading 1 | 2   | 3   |
| --------- | --- | --- |
| Row 1     |     |     |
| Row 2     |     |     |

***Important Note***: All rows require the same number of column `|` seperators, even if the column will be empty.

---

## Examples of usage

### 20231123001

| Platform                                                | Package      | State        | Errata                                                            | Release Date   |
| ------------------------------------------------------- | ------------ | ------------ | ----------------------------------------------------------------- | -------------- |
| Red Hat Enterprise Linux 8                              | glibc        | Fixed        | [RHSA-2023:5455](https://access.redhat.com/errata/RHSA-2023:5455) | 5 October 2023 |
| Red Hat Enterprise Linux 8                              | glibc        | Fixed        | [RHSA-2023:5455](https://access.redhat.com/errata/RHSA-2023:5455) | 5 October 2023 |
| Red Hat Enterprise Linux 8.6 Extended Update Support    | glibc        | Fixed        | [RHSA-2023:5476](https://access.redhat.com/errata/RHSA-2023:5476) | 5 October 2023 |
| Red Hat Enterprise Linux 9                              | glibc        | Fixed        | [RHSA-2023:5453](https://access.redhat.com/errata/RHSA-2023:5453) | 5 October 2023 |
| Red Hat Enterprise Linux 9                              | glibc        | Fixed        | [RHSA-2023:5453](https://access.redhat.com/errata/RHSA-2023:5453) | 5 October 2023 |
| Red Hat Enterprise Linux 9.0 Extended Update Support    | glibc        | Fixed        | [RHSA-2023:5454](https://access.redhat.com/errata/RHSA-2023:5454) | 5 October 2023 |
| Red Hat Virtualization 4 for Red Hat Enterprise Linux 8 | glibc        | Fixed        | [RHSA-2023:5476](https://access.redhat.com/errata/RHSA-2023:5476) | 5 October 2023 |
| Red Hat Enterprise Linux 6                              | glibc        | Not affected |                                                                   |                |
| Red Hat Enterprise Linux 7                              | glibc        | Not affected |                                                                   |                |
| Red Hat Enterprise Linux 7                              | compat-glibc | Not affected |                                                                   |                |

---

### 20231206001

| CVE ID                                                            | CVSS Score | Overview                                                                                                                                                                                                                                                                                      | Affected Products | Vendor Bulletin                                                                                       |
| ----------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------- |
| [CVE-2023-33106](https://www.cve.org/CVERecord?id=CVE-2023-33106) | TBD        | Memory corruption while submitting a large list of sync points in an AUX command to the IOCTL_KGSL_GPU_AUX_COMMAND.                                                                                                                                                                           | See CVE Link      | [Vendor Bulletin](https://www.qualcomm.com/company/product-security/bulletins/december-2023-bulletin) |
| [CVE-2023-33063](https://www.cve.org/CVERecord?id=CVE-2023-33063) | TBD        | Memory corruption in DSP Services during a remote call from HLOS to DSP.                                                                                                                                                                                                                      | See CVE Link      | [Vendor Bulletin](https://www.qualcomm.com/company/product-security/bulletins/december-2023-bulletin) |
| [CVE-2023-33107](https://www.cve.org/CVERecord?id=CVE-2023-33107) | TBD        | Memory corruption in Graphics Linux while assigning shared virtual memory region during IOCTL call.                                                                                                                                                                                           | See CVE Link      | [Vendor Bulletin](https://www.qualcomm.com/company/product-security/bulletins/december-2023-bulletin) |
| [CVE-2023-22071](https://www.cve.org/CVERecord?id=CVE-2023-22071) | 7.8        | Possible use after free when process shell memory is freed using IOCTL munmap call and process initialization is in progress in Snapdragon Auto, Snapdragon Compute, Snapdragon Connectivity, Snapdragon Consumer IOT, Snapdragon Industrial IOT, Snapdragon Mobile, Snapdragon Voice & Music | See CVE Link      | [Vendor Bulletin](https://www.qualcomm.com/company/product-security/bulletins/may-2022-bulletin)      |

---
