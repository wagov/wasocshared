# Drupal Security Updates for H5P and File(Field) Paths - 20221216001

## Overview
Drupal has released security updates to address vulnerabilities affecting **H5P** and the **File (Field) Paths** modules for **Drupal 7.x**.   An attacker could exploit these vulnerabilities to access sensitive information and remotely execute code.

## What is the vulnerability ?

**[SA-CONTRIB-2022-064](https://www.drupal.org/sa-contrib-2022-064)** - H5P - Create and Share Rich Content and Applications - Moderately critical - Remote Code Execution (RCE)

This module enables you to create interactive content.  The module doesn't sufficiently stop path traversal attacks through zipped filenames for the uploadable .h5p files.

**[SA-CONTRIB-2022-065](https://www.drupal.org/sa-contrib-2022-065)** - File (Field) Paths - Moderately critical - Access bypass

The File (Field) Paths module extends the default functionality of Drupal's core File module, by adding the ability to use entity-based tokens in destination paths and file names.  The module's default configuration could temporarily expose private files to anonymous visitors.


## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation
Install the latest version:

-  If you use the **H5P** module for **Drupal 7.x**, upgrade to [H5P 7.x-1.51](https://www.drupal.org/project/h5p/releases/7.x-1.51).  This vulnerability is mitigated by the fact that an attacker must have a role with the permission "update h5p libraries". In addition, it is only exploitable on Windows servers.

-  If you use the **File (Field) Paths** module for **Drupal 7.x**, upgrade to [File (Field) Paths 7.x-1.2](https://www.drupal.org/project/filefield_paths/releases/7.x-1.2).  It's possible to make a configuration change to mitigate this problem in the admin UI at `/admin/config/media/file-system/filefield-paths` - the temp file location should use either the temporary:// or private:// stream wrapper if uploaded files should not be exposed publicly.  This vulnerability is mitigated by the fact that an attacker must be able to guess the temporary path used for file upload.

### Reference:

* Drupal Security Advisories - [https://www.drupal.org/security](https://www.drupal.org/security)