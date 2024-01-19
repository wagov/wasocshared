# Lazarus Group Targeting Windows IIS Web Servers - 20230531003

## **Overview**

AhnLab Security Emergency response Center (ASEC) has recently confirmed the Lazarus group carrying out attacks against Windows IIS web servers. Windows server systems are being targeted for attacks, and malicious behaviors are being carried out through w3wp.exe, an IIS web server process.

## **What is the Threat?**

The threat actor uses poorly managed or vulnerable web servers as their initial breach routes before executing their malicious commands later.

They place a malicious DLL (msvcr100.dll) in the same folder path as a normal application (Wordconv.exe) via the Windows IIS web server process, w3wp.exe. They then execute the normal application to initiate the execution of the malicious DLL.

## **What has been observed?**

The WASOC has not observed any exploitation as of yet.

## **Indicator of Compromise**

### DLL Side-loading File Path

- C:\\ProgramData\\USOShared\\Wordconv.exe
- C:\\ProgramData\\USOShared\\msvcr100.dll

### File-Hash

diagn.dll

- MD5: e501bb6762c14baafadbde8b0c04bbd6

msvcr100.dll

- MD5: 228732b45ed1ca3cda2b2721f5f5667c

? (Variant malware of msvcr100.dll)

- MD5: 47d380dd587db977bf6458ec767fee3d

cylvc.dll (Variant malware of msvcr100.dll)

- MD5: 4d91cd34a9aae8f2d88e0f77e812cef7

## Reference

- [**AhnLab Report**](https://asec.ahnlab.com/en/53132/)
