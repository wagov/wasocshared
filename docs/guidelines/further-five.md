# ACSC Strategies to Mitigate Cyber Security Incidents

The below are all from [ACSC Strategies to Mitigate Cyber Security Incidents – Mitigation Details](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/strategies-mitigate-cyber-security-incidents/strategies-mitigate-cyber-security-incidents-mitigation-details).

## Further Five

The Further Five below have been included in the 2024 [WA Government Cyber Security Policy](https://www.wa.gov.au/government/publications/wa-government-cyber-security-policy).

!!! note "Further Five"
    - [Server application hardening](#server-application-hardening) especially internet-accessible web applications (sanitise input and use TLS not SSL) and databases, as well as applications that access important (sensitive/high-availability) data.
    - [Block spoofed emails](#block-spoofed-emails). Use Sender Policy Framework (SPF) or Sender ID to check incoming emails. Use ‘hard fail’ SPF TXT and DMARC DNS records to mitigate emails that spoof the organisation’s domain.
    - [Network segmentation](#network-segmentation). Deny traffic between computers unless required. Constrain devices with low assurance (e.g. BYOD and IoT). Restrict access to network drives and data repositories based on user duties.
    - [Continuous incident detection and response](#continuous-incident-detection-and-response) with automated immediate analysis of centralised time-synchronised logs of allowed and denied computer events, authentication, file access and network activity.
    - [Personnel management](#personnel-management) e.g. ongoing vetting especially for users with privileged access, immediately disable all accounts of departing users, and remind users of their security obligations and penalties.

### Server application hardening

Server application hardening especially internet-accessible web applications (sanitise input and use TLS not SSL) and databases, as well as other server applications that access important (sensitive or high-availability) data (e.g. customer, finance, human resources and other data storage systems).

Server application hardening helps the organisation to conduct its business with a reduced security risk of malicious data access, theft, exposure, corruption and loss.

#### Implementation guidance

OWASP guidance helps to mitigate web application security vulnerabilities such as SQL injection, and covers code review, data validation and sanitisation, user and session management, protection of data in transit and storage, error handling, user authentication, logging and auditing.

!!! info
    Further guidance on server application hardening are available below.

    - Further guidance on system hardening is available in the *[Guidelines for System Hardening](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-system-hardening "Guidelines for System Hardening")* publication.
    - Further guidance on protecting web applications and users is available in the *[Protecting Web Application and Users](https://www.cyber.gov.au/sites/default/files/2023-03/PROTECT%20-%20Protecting%20Web%20Applications%20and%20Users%20%28October%202021%29.pdf "Protecting Web Applications and Users")* publication.
    - Further guidance on secure software development is available in the *[Guidelines for Software Development](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-software-development)* publication.

### Block spoofed emails

Block spoofed emails. Use Sender Policy Framework (SPF) or Sender ID to check incoming emails. Use 'hard fail' SPF TXT and DMARC DNS records to mitigate emails that spoof the organisation's domain.

SPF, or alternative implementations such as Sender ID, reduce the likelihood of spoofed emails being delivered to the targeted user.

#### Implementation guidance

Configure 'hard fail' SPF TXT DNS records for the organisation's domains and subdomains, and configure a wildcard SPF TXT DNS record to match non-existent subdomains.

Sender ID is an alternative version of SPF that checks the legitimacy of the sender's email address that is displayed to the email recipient. Additional implementations include DomainKeys Identified Mail (DKIM).

Domain-based Message Authentication, Reporting and Conformance (DMARC) enables a domain owner to specify a policy stating what action the recipient's email server should take if it receives an email that has failed an SPF check and/or a DKIM check. DMARC also contains a reporting feature which enables a domain owner to obtain some visibility of whether their domain is being spoofed in emails sent by adversaries.

Configure a DMARC DNS record for the organisation's domain, specifying that emails from the organisation's domain and subdomains should be rejected if they fail SPF checks (and/or DKIM checks if DKIM is configured for the organisation's domain). In the absence of a DMARC DNS record, the ACSC responded to a cyber security incident involving a major free webmail provider that delivered a spoofed email to the recipient's inbox even though the email failed SPF checks.

Organisations can conservatively deploy DMARC if they are concerned about legitimate emails sent from their domain being incorrectly rejected.

Reject incoming emails that have the organisation's domain as the email sender but do not originate from email servers approved by the organisation.

!!! info
    Further guidance on spoofed email mitigation strategies is available in the *[How to Combat Fake Emails](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/email-hardening/how-combat-fake-emails "How to Combat Fake Emails")* publication.

### Network segmentation

Network segmentation. Deny traffic between computers unless required. Constrain devices with low assurance (e.g. 'Bring Your Own Device' (BYOD) and 'Internet of Things' (IoT)). Restrict user access to network drives and data repositories based on user duties.

Network segmentation helps to prevent adversaries from propagating throughout the organisation's network. If implemented correctly, it can make it significantly more difficult for adversaries to locate and gain access to the organisation's important (sensitive or high-availability) data.

#### Implementation guidance

Restrict access based on the connectivity required, user job role, business function, trust boundaries and the extent to which data is important.

Develop and enforce a ruleset controlling which computers are allowed to communicate with other computers. For example, on most corporate networks, direct network communication between user computers should not be required or allowed.

Network controls that can assist with restricting network access include switches, virtual LANs, enclaves, data diodes, firewalls, routers and Network Access Control.

Permissions on files and network drives (file shares) can be used to limit access to data.

Constrain VPN and other remote access, wireless connections, IoT devices, as well as user-owned laptops, smartphones and tablets which are part of a BYOD implementation.

Organisations using operating system virtualisation, (especially third party) cloud computing infrastructure, or providing users with BYOD or remote access to the organisation's network, might require controls that are less dependent on the physical architecture of the network. Such controls include 'micro-segmentation' firewalling implemented by the virtualisation platform layer, software-based firewalling implemented in individual computers and virtual machines, and 'IPsec Server and Domain Isolation'.

The use of IPsec authentication can ensure that a specific network port or ports on a sensitive server can only be accessed by specific computers such as those computers belonging to administrators.

Important servers such as Active Directory and other authentication servers should only be able to be administered from a limited number of intermediary servers referred to as 'jump servers', 'jump hosts' or 'jump boxes'. Jump servers should be closely monitored, be well secured, limit which users and network devices are able to connect to them, and typically have no internet access. Some jump servers might require limited internet access if they are used to administer defined computers located outside of the organisation's local network.

Organisations with critically important data might choose to store and access it using air-gapped computers that are not accessible from the internet. Security patches and other data can be transferred to and from such air gapped computers in accordance with a robust media transfer policy and processes.

Adversaries could propagate throughout the network by leveraging the organisation's existing systems used to distribute software such as patches for security vulnerabilities, login programs or scheduled tasks configured via Group Policy Objects, updated anti-malware detection engine software, or the computer Standard Operating Environment master image. Alternatively, adversaries could turn the organisation's intranet website into a watering hole to compromise users when they visit. Therefore, protect software distribution systems from modifications which are malicious or otherwise unauthorised, combined with implementing a robust change management process.

!!! info
    Further guidance on network segmentation is available in the *[Implementing Network Segmentation and Segregation](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/network-hardening/implementing-network-segmentation-and-segregation "Implementing Network Segmentation and Segregation")* publication.

    Information about BYOD and other enterprise mobility solutions is available in the *[Bring Your Own Device for Executives](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/remote-working-and-secure-mobility/secure-mobility/bring-your-own-device-executives "Bring Your Own Device for Executives")* and *[Risk Management of Enterprise Mobility Including Bring Your Own Device](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/remote-working-and-secure-mobility/secure-mobility/risk-management-enterprise-mobility-including-bring-your-own-device "Risk Management of Enterprise Mobility Including Bring Your Own Device")* publications.

### Continuous incident detection and response

Continuous incident detection and response with automated immediate analysis of centralised time-synchronised logs of allowed and denied computer events, authentication, file access and network activity.

Performing continuous incident detection and response increases the organisation's ability to rapidly detect and respond to cyber security incidents in a timely manner to minimise business impact.

#### General implementation guidance

Use a Security Information and Event Management (SIEM) solution to perform real-time automated aggregation and correlation of logs from multiple sources to identify patterns of suspicious behaviour, including behaviour that deviates from the baseline of typical patterns of system usage by users.

Modern SIEM solutions typically contain features to assist with interpreting, analysing and providing context to log data, prioritising alerts, incorporating incident response workflow and automating the process wherever possible, while using data storage structures that improve scalability and enable flexible data searches and queries that rapidly return their results.

When choosing a SIEM solution, determine what exactly the vendor means if they advertise their product as leveraging threat intelligence, big data analytics, heuristics, machine learning, artificial intelligence, maths/statistics, or baselining normal user and system behaviour.

Store logs for at least 18 months, or longer if required by regulatory compliance.

Regularly test the organisation's incident response plan, processes and technical capabilities.

To help make the most of limited staff resources, leverage automation and context to focus on high priority security events and avoid false positives.

#### Implementation guidance leveraging computer-related logs

Important logs include logs generated by security products, as well as Active Directory event logs and other logs associated with user authentication including VPN and other remote access connections.

Perform timely log analysis focusing on:

- Most Likely Targets, especially users who have administrative privileges to operating systems or applications such as databases
- application control logs revealing attempted but blocked program execution, as well as logs generated by other security products
- gaps in logs where there should be periodic activity, for example, an absence of expected daily security product logs usually generated by computers of users who are in the office and are believed to be using their computers, potentially indicating that adversaries have disabled the security products
- user actions outside of business hours, noting that malware compromising a user's account might appear in logs as though the malware's actions are the user's actions
- new or changed services or Windows Registry keys used to automatically run programs on bootup or user login
- new or changed files that are executable
- access to critical asset computers that store or process important (sensitive or high-availability) data
- access to files on network drives
- unauthorised attempts to access or modify event logs
- [use of tools shipped with Microsoft Windows](https://lolbas-project.github.io/) to perform code execution, reconnaissance and network propagation (e.g. cscript.exe, wscript.exe, cmd.exe, mshta.exe, ipconfig.exe, net.exe, net1.exe, netstat.exe, reg.exe, wmic.exe, powershell.exe, powershell_ise.exe, at.exe, schtasks.exe, tasklist.exe, regsvr32.exe, rundll32.exe, gpresult.exe and systeminfo.exe)
- user authentication and use of account credentials.

When performing log analysis of user authentication and use of account credentials, focus on:

- user authentication from a user who is currently on holiday or other leave
- user authentication from computers other than the user's usual computer, especially if from computers that are located outside of the user's geographical location
- VPN and other remote access connections from countries that the associated user is not located in
- a single IP address attempting to authenticate as multiple different users
- VPN and other remote access connections by a user from two different IP addresses concurrently
- failed login attempts for accounts with administrative privileges
- user accounts that become locked out because of too many incorrect passphrase attempts
- administrative service accounts unexpectedly logging into other computers
- creation of user accounts, or disabled accounts being re-enabled, especially accounts with administrative privileges
- modifications to user account properties, such as 'Store password using reversible encryption' or 'Password never expires' configuration options being activated.

#### Implementation guidance leveraging network-related logs

Maintain a network map and an inventory of devices connected to the network to help baseline normal behaviour on the network and highlight anomalous network activity.

Important logs include DNS, web proxy logs containing connection details including User-Agent values, DHCP leases, firewall logs detailing network traffic entering and leaving the organisation's network as well as logs of (especially outbound) blocked network traffic, and metadata such as Network Flow data.

Perform timely log analysis focusing on connections and the amount of data transferred by Most Likely Targets to highlight abnormal internal network traffic such as suspicious reconnaissance enumeration of both network drives (file shares) and user data including honeytoken accounts. Also focus on abnormal external network traffic crossing perimeter boundaries such as:

- periodic beaconing traffic
- HTTP/HTTPS sessions with an unusual ratio of outgoing traffic to incoming traffic
- HTTP/HTTPS traffic with a 'User-Agent' header value that is not associated with legitimate software used by the organisation
- DNS lookups for domain names that don't exist and aren't an obvious user typo, indicating malware communicating to a domain that is yet to be registered by adversaries
- DNS lookups for domain names that resolve to a localhost IP address such as 127.0.0.1, indicating malware that adversaries are not ready to communicate with
- large amounts of traffic
- traffic outside of business hours
- long lived connections.

#### Implementation guidance applicable to ransomware

Analyse and action real-time log alerts generated by file activity monitoring tools to identify suspicious rapid and numerous file changes reflecting unapproved data deletion or modification such as encryption.

#### Implementation guidance applicable to malicious insiders

Analyse and action real-time log alerts generated by file activity monitoring tools to identify suspicious rapid and numerous file copying or changes.

Logs should be analysed by staff who have no other privileges or job roles in order to help mitigate a malicious insider with administrative privileges ignoring or deleting logs of their own malicious actions.

Perform timely log analysis focusing on:

- use of removable storage media and connected devices especially USB storage devices
- computer usage outside of business hours
- data access and printing which is excessive compared to the normal baseline for a user and their peer colleagues
- data transfers to unapproved cloud computing services including personal webmail, as well as the use of unapproved VPNs from the organisation's network.

#### Implementation guidance applicable to incident response

Developing and implementing an incident response capability requires support from technical staff and business representatives, including data owners, corporate communications, public relations and legal staff. Organisations need to regularly test and update their incident response plan, processes and technical capabilities, focusing on decreasing the duration of time taken to detect cyber security incidents and respond to them.

When a targeted cyber intrusion is identified, it needs to be understood to a reasonable extent prior to remediation. Otherwise, the organisation plays 'whack a mole', cleaning compromised computers, as well as blocking network access to internet infrastructure known to be controlled by adversaries, while the same adversaries simply compromise additional computers using different malware and different internet infrastructure to avoid detection.

For targeted cyber intrusions of higher sophistication, the ACSC can assist Australian government organisations with responding. This includes developing a strategic plan to contain and eradicate the intrusion, and providing guidance to improve the organisation's cyber security posture in preparation for adversaries attempting to regain access to the organisation's computers.

### Personnel management

Personnel management e.g. ongoing vetting especially for users with privileged access, immediately disable all accounts (especially remote access accounts) of departing users, and remind users of their security obligations and penalties.

Personnel management assists to avoid employees having malicious intent, developing malicious intent, or carrying out their malicious intentions undiscovered until after damage has been done.

Some malicious insiders are motivated by money, coercion, ideology, ego or excitement, and might steal a copy of customer details or intellectual property. Other malicious insiders are motivated by revenge or disgruntlement due to reasons such as a negative job performance review, a denied promotion or involuntary termination of employment, and might cause damage such as destroying data and preventing computers/networks from functioning.

#### Implementation guidance

Perform pre-employment screening and ongoing vetting, consisting of verification of previous employment and education for all employees, as well as a criminal history background check at least for employees who have privileged access.

Immediately disable all accounts and require sanitisation or return of mobile computing devices for departing employees and remind them of their security obligations and penalties for violations. Require departing employees to also return items that could facilitate access to organisational computers and data, including their identification pass and keys used to access the organisation's buildings and IT facilities.

Educate employees to never share or otherwise expose their passphrase to other employees, including via 'shoulder surfing'. Educate employees to lock their computer screen whenever they are away from their computer.

Organisational executives and management can reduce some motivations for employees to become malicious insiders by facilitating a culture of appreciated and engaged employees who have fair remuneration and merit-based career advancement opportunities.

For the relatively small number of organisations where employees have access to highly classified data or other extremely sensitive data, a psychological assessment should be performed by qualified personnel to explore topics including allegiances and beliefs as well as character weaknesses which could be leveraged and manipulated by adversaries. Employees should be encouraged to advise the personnel security team of unusual behaviour exhibited by other employees as well as their own significant life changes such as financial, relationship and health problems.

!!! info
    Further information can be found within ACSC’s publication [Guidelines for Personnel Security | Cyber.gov.au](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-personnel-security).
