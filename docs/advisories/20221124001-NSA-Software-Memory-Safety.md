# NSA - Software Memory Safety - 20221124001

## Overview

Memory issues in software comprise a large portion of the exploitable vulnerabilities in existence. **NSA** advises organizations to consider making a strategic shift from programming languages that provide little or no inherent memory protection, such as C/C++, to a memory safe language when possible.

Memory safe languages provide differing degrees of memory usage protections, so available code hardening defenses, such as compiler options, tool analysis, and operating system configurations, should be used for their protections as well. By using memory safe languages and available code hardening defenses, many memory vulnerabilities can be prevented, mitigated, or made very difficult for cyber actors to exploit.

## What is the vulnerability ?

Malicious cyber actors can exploit these vulnerabilities for remote code execution or other adverse effects, which can often compromise a device and be the first step in large-scale network intrusions.

## What is vulnerable ?

While developers often perform rigorous testing to prepare the logic in software for surprising conditions, exploitable software vulnerabilities are still frequently based on memory issues. Examples include overflowing a memory buffer and leveraging issues with how software allocates and deallocates memory. [Microsoft®](https://github.com/Microsoft/MSRC-Security-Research/blob/master/presentations/2019_02_BlueHatIL/2019_01%20-%20BlueHatIL%20-%20Trends%2C%20challenge%2C%20and%20shifts%20in%20software%20vulnerability%20mitigation.pdf) revealed at a conference in 2019 that from 2006 to 2018 70 percent of their vulnerabilities were due to memory safety issues.

## What has been observed ?

There is no evidence of exploitation affecting Western Australian Government networks at the time of publishing.

## Recommendation

- **Memory safe languages** can help prevent programmers from introducing certain types of memory-related issues. Memory is managed automatically as part of the computer language; it does not rely on the programmer adding code to implement memory protections.

- **Application Security Testing** Several mechanisms can be used to harden non-memory safe languages to make them more memory safe. Analyzing the software using **static and dynamic application security testing (SAST and DAST)** can identify memory use issues in software.

- **Anti-exploitation features** such as the compilation and execution environment can be used to make it more difficult for cyber actors to exploit memory management issues. Most of these added features focus on limiting where code can be executed in memory and making memory layout unpredictable.

- **NSA advises** organizations to consider making a strategic shift from programming languages that provide little or no inherent memory protection to a memory safe language when possible.

### Reference

- The National Security Agency (NSA) Cybersecurity Information Sheet [https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF)
