# Security Operations Workstation Self-Build (Linux, macOS, Windows)

Recommended software for use for general activities. The majority of the below software should be cross-platform (Linux, macOS, Windows) unless otherwise noted.

## 1. Base Utilities

- [Adobe Acrobat Reader DC](https://www.adobe.com/au/acrobat/pdf-reader.html) - View, sign, collaborate on and annotate PDF files
- [draw.io Diagrams](https://www.diagrams.net/) - Security-first diagramming for teams
- [7zip](https://www.7-zip.org/) - a file archiver with a high compression ratio that supports a lot of formats
- [Tailscale](https://tailscale.com/download) - Zero config VPN. Installs on any device in minutes, manages firewall rules for you, and works from anywhere.
- [(Windows) Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) - Bundling of the Sysinternals Troubleshooting Utilities
- [(Windows) PowerToys](https://docs.microsoft.com/en-us/windows/powertoys/) - Microsoft PowerToys is a set of utilities for power users to tune and streamline their Windows experience for greater productivity.

## 2. Development

- [Visual Studio Code](https://code.visualstudio.com) - a code editor redefined and optimized for building and debugging modern web and cloud applications.
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - the fastest way to containerize applications.
- [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop) - web-based interactive development environment for notebooks, code, and data.
- [Git](https://git-scm.com/) - a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency

## 3. Virtual Machines

- [Oracle VirtualBox](https://www.virtualbox.org/) - a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.
- [(Windows) Windows Sandbox](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview) - a lightweight desktop environment to safely run applications in isolation. Software installed inside the Windows Sandbox environment remains "sandboxed" and runs separately from the host machine.
- [(Linux, Windows) VMWare Workstation Player](https://www.vmware.com/au/products/workstation-player.html) - Easily run multiple operating systems as virtual machines on your Windows or Linux PC with VMware Workstation Player.
- [Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview) - a complete Ubuntu terminal environment, allowing you to develop cross-platform applications without leaving windows
- [Kali linux](https://www.kali.org/docs/wsl/win-kex/#install-win-kex) - an open-source, Debian-based Linux distribution geared towards various information security tasks, such as Penetration Testing, Security Research, Computer Forensics and Reverse Engineering
- [SIFT Workstation](https://www.sans.org/tools/sift-workstation/) - a computer forensics distribution that installs all necessary tools on Ubuntu to perform a detailed digital forensic and incident response examination. It is compatible with expert witness format (E01), advanced forensic format (AFF), raw (dd), and memory analysis evidence formats.

## 4. GIS & Mapping

- [QGIS](https://www.qgis.org/en/site/) - Create, edit, visualise, analyse and publish geospatial information on Windows, Mac, Linux, BSD and mobile devices

## 5. Windows Quick Start

Quick install steps using [winget](https://docs.microsoft.com/en-us/windows/package-manager/winget/) for the majority of the above on Windows.

```powershell
# Base Utilities
winget install "Sysinternals Suite" -s msstore
winget install "Adobe Acrobat Reader DC" -s msstore
winget install "draw.io Diagrams" -s msstore
winget install 7zip.7zip
winget install Microsoft.PowerToys --source winget
# Development
winget install "Visual Studio Code" -s msstore
wsl --install -d Ubuntu
## https://github.com/teamdfir/sift-cli#installation
wsl --install -d kali-linux
winget install Git.Git
winget install oracle.virtualbox
winget install vmware.workstationplayer
# GIS & Mapping
winget install OSGeo.QGIS
```

## 6. WSL2 setup

To fix DNS (gets blocked out of the box by windows firewall) and get azure cli, docker & jupyterlab working quickly in WSL2, run the below in the [Ubuntu 22.04](https://apps.microsoft.com/store/detail/ubuntu-22041-lts/9PN20MSR04DW) WSL2 env

```bash
echo -e "[network]\ngenerateResolvConf = false" | sudo tee /etc/wsl.conf
echo "nameserver 9.9.9.9" | sudo tee /etc/resolv.conf
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
curl -fsSL https://get.docker.com | bash
sudo apt -y install python3-pip && sudo pip3 install jupyterlab pandas matplotlib azure-cli
# Run below each time you boot WSL to start docker
sudo service docker start
# Run below to start jupyterlab, then ctrl-click the link to use it
jupyter-lab
```
