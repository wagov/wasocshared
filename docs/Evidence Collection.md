# Collecting and sharing files with WAGov SOC  

In some cases files will need to be shared with the WAGov SOC for further analysis. The following process will provide the steps to do so.

## Small files 

E.g. **Phishing Email, Malware, or small directories**

Encrypt the files to avoid being detected and blocked by WAGov's Defender. For that, use 7-Zip to encrypt and compress the file using the password **_'infected'_** 

![7-Zip](../images/7zipUsage.jpg)

The encrypted file can be easily shared over email, Teams or directly uploaded to the case. 

## Large files

For acquisition on **Full Disc Image** or **Memory dumps** the following articles can provide some of the tools and steps for that. 

https://learn.microsoft.com/en-us/azure/virtual-machines/snapshot-copy-managed-disk?tabs=portal  
https://aditya-pratap9557.medium.com/windows-memory-forensics-using-open-source-tools-3ec09930732e

For acquisition on **External Facing Service** files generally involves collecting **_wwwroot_** and **_weblogs_** (for IIS this is often the same thing). This involves compressing with 7-Zip and adding a password as explaind above.

## Uploading large files to WAGov SOC
WAGov SOC will provide a link to a blob container where the files can be uploaded. The [Uploading evidence to a blob container](https://wagov.github.io/wasocshared/#/docs/collecting-evidence) has the steps on the process 

## Additional scans and collections

**Host-Based collection** involves collecting all windows logs (usually found under c:\Windows\System32\winevt\Logs\). Other artefacts can also be handy – so we often bundle up collection into tools that perform collection of these extra artefacts automatically.

(1) Housekeeper.ps1 – A powershell script that collects logs / process listing, service and scheduled tasks etc and stores them in a zip. For use on Windows OS’s.

(2) Housekeeper.sh – A bash script that collects logs / process listings, cron jobs etc. and stores them in a zip. For use on Linux OS’s.

(3) Velociraptor-v2.exe – Similar to housekeeper, but collects certain directories (eg. Webroot) of interest.

It is recommended these tools to be renamed before use to hide investigative activity from the actor. All the tools require admin rights for best effect. 

For **Suspected malware infected endpoint** we recommend using [Microsoft Defender Offline scan](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/microsoft-defender-offline?view=o365-worldwide). It runs from outside the normal Windows kernel so it can target malware that attempts to bypass the Windows shell, such as viruses and rootkits that infect or overwrite the master boot record (MBR). 
