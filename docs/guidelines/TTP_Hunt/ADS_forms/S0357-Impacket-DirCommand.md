## S0357 - Potential Impacket Execution "dir" command

Actor may use Impacket’s wmiexec, which redirects output to a file within the victim host’s ADMIN$ share (C:\\Windows) containing an epoch timestamp in its name.

!!! example
    ```
    cmd.exe /Q /c dir 1> \\127.0.0.1\\ADMIN$\_\_1684944005.9400265 2>&1
    ```

!!! tip "Related"
    Volt Typhoon activity

!!! abstract "Reference"
    - <https://www.cyber.gov.au/about-us/advisories/prc-state-sponsored-cyber-actor-living-off-the-land-to-evade-detection>
    - <https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/>
    - <https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-277a>
    - <https://github.com/Azure/Azure-Sentinel/blob/3833100de05ce61d6972c43dd5af7b9706e4674c/Solutions/Windows%20Security%20Events/Hunting%20Queries/CommandsexecutedbyWMIonnewhosts-potentialImpacket.yaml#L21>

### ATT&CK TACTICS<br>

{{mitre("S0357")}}

Data Source(s): [Process](https://attack.mitre.org/datasources/DS0009/), [Command](https://attack.mitre.org/datasources/DS0017/)

### SENTINEL RULE QUERY<br>

```
let c1 = dynamic(["cmd.exe", "2>&1", "ADMIN$"]);
find where InitiatingProcessCommandLine has_all (c1) or ProcessCommandLine has_all (c1) or CommandLine has_all (c1) 
```

### Triage

1. Identify user/service triggering the activity
1. Check time of activity if within business hours
1. Investigate further if the activity is expected and approved

### VERSION

Version 1.0 (date: 10/07/2023)
