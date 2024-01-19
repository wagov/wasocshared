# Running ad-hoc limited scans against OT environments

Below is a guide to use the standalone runZero command-line scanner to rapidly identify fragile network assets including OT ones from a central location with limited network capabilities.

## References

- [Scanning OT networks (runZero playbook)](https://www.runzero.com/docs/playbooks/scanning-ot-networks/)
- [Can I safely scan my IoT or OT environments? (runZero FAQ)](https://www.runzero.com/docs/troubleshooting-iot-and-ot/)

## Prerequisites

Please make sure you have access to a [standalone command-line scanner](https://www.runzero.com/docs/using-the-scanner/) for your operating system. The below guide defines a configuration that can be copied and modified to run scans against specific IPv4 addresses or CIDRs.

### Minimum scan workstation system requirements

- Processor running at 2.0GHz or faster
- At least 16GiB of memory (8GiB for small environments)
- At least 1GB of free storage space

### Scan Configuration

In the below commands, replace **192.168.1.0/24 192.168.1.1/24** with the IPv4 subnets you would like to scan and **public,private** with the SNMP v1/v2c read communities for the network (if available). The scans have been configured according to runzeros playbook, limiting packets per second to **300** and host simultaneous connections to **20** which is an extremely low rate that should not impact fragile networks or equipment.

## Running a scan

### Windows

```bash
runzero-scanner.exe 192.168.1.0/24 192.168.1.1/24 -r 300 --max-host-rate 20 --max-group-size 2048 --max-ttl 64 -p 21,22,23,69,80,123,135,137,161,179,443,445,3389,5040,5900,7547,8080,8443,62078,65535 --host-ping --probes layer2,netbios,ntp,snmp,ssh,syn,tftp --snmp-comms public,private
```

### Linux/macOs/BSD

```
sudo runzero 192.168.1.0/24 192.168.1.1/24 -r 300 --max-host-rate 20 --max-group-size 2048 --max-ttl 64 -p 21,22,23,69,80,123,135,137,161,179,443,445,3389,5040,5900,7547,8080,8443,62078,65535 --host-ping --probes layer2,netbios,ntp,snmp,ssh,syn,tftp --snmp-comms public,private
```

## Reviewing results

The results will be saved to a rumble-*timestamp* directory in the current folder, key files are the `.jsonl` and the `.html` which include all the asset data.
