# Azure VM (Virtual Machines) Basic Training

The below is a program of exercises to understand how to deploy and run a public cloud workload securely.

## 1. Basic Deployment

[Microsoft Documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/) - Main Documentation for learning more about Azure VMs

### 1.1. Prerequisites

- SSH Client installed - [windows](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh) - [linux](https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows)
- Firewall Rule allowance for SSH Protocol (port 22)

### 1.2. Portal Deployment

- [Microsoft Portal Exercise](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal) - Default exercise for deploying VMs via Portal

### 1.3. Sign in to Azure

Sign in to the [Azure portal](https://portal.azure.com).

### 1.4. Create virtual machine

1. Enter *virtual machines* in the search.
1. Under **Services**, select **Virtual machines**.
1. In the **Virtual machines** page, select **Create** and then **Virtual machine**.  The **Create a virtual machine** page opens.
1. In the **Basics** tab, under **Project details**, make sure the correct subscription is selected and then choose to **Create new** resource group. Enter *myResourceGroup* for the name.*.
    Image TODO
1. Under **Instance details**, enter *myVM-name* for the **Virtual machine name**, and choose *Standard_B1ls* for your **Image**. Size availability and pricing are dependent on your region and subscription. Leave the other defaults.
    ![Azure VM Size](../images/azure-vm-image-size.png)
    > NOTE: Some users will now see the option to create VMs in multiple zones. To learn more about this new capability, see [Create virtual machines in an availability zone](https://docs.microsoft.com/en-us/azure/virtual-machines/create-portal-availability-zone?tabs=standard)
1. Under **Administrator account**, select **SSH public key**.
1. In **Username** enter *azureuser*.
1. For **SSH public key source**, leave the default of **Generate new key pair**, and then enter *myKey* for the **Key pair name**.
    > Image TODO
1. Under **Inbound port rules** > **Public inbound ports**, choose **Allow selected ports** and then select **SSH (22)** and **HTTP (80)** from the drop-down.
    > Image TODO
1. Leave the remaining defaults and then select the **Review + create** button at the bottom of the page.
1. On the **Create a virtual machine** page, you can see the details about the VM you are about to create. When you are ready, select **Create**.
1. When the **Generate new key pair** window opens, select **Download private key and create resource**. Your key file will be download as **myKey.pem**. Make sure you know where the `.pem` file was downloaded; you will need the path to it in the next step.
1. In **Disks** section, under **Disk options**, create new *virtual network* as **name-vnet**.
1. Confirm that *Delete public IP and NIC when VM is deleted* is selected.
1. In **Management** section, under **Monitoring**, select *disable*.
1. Click **Review + Create** in the buttom left hand corner, to finalise the creation of the VM. Allow for the validation to complete and click on **create**.
1. Download the created private key and create resource.
1. When the deployment is finished, select **Go to resource**.
1. On the page for your new VM, select the public IP address and copy it to your clipboard.
    > Image TODO

## 2. Connect to virtual machine

Create an SSH connection with the VM.

Linux:

1. If you are on a Mac or Linux machine, open a Bash prompt and set read-only permission on the .pem file using `chmod 400 ~/Downloads/myKey.pem`. If you are on a Windows machine, open a PowerShell prompt.

Linux and Windows:

1. At your prompt, open an SSH connection to your virtual machine. Replace the IP address with the one from your VM, and replace the path to the `.pem` with the path to where the key file was downloaded.

```bash
ssh -i ~/Downloads/myKey.pem azureuser@<Your Public IP Address>
```

> TIP: The SSH key you created can be used the next time your create a VM in Azure. Just select the **Use a key stored in Azure** for **SSH public key source** the next time you create a VM. You already have the private key on your computer, so you won't need to download anything.

### 2.1. Install Docker

Docker is an open source containerization platform. It enables developers to package applications into containers—standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment. Containers simplify delivery of distributed applications, and have become increasingly popular as organizations shift to cloud-native development and hybrid multicloud environments.

Further information reagrding [docker](https://docs.docker.com/get-started/overview/)

```bash
sudo apt-get -y update
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

### 2.2. Install Web Application

Caddy simplifies your infrastructure. It takes care of TLS certificate renewals, OCSP stapling, static file serving, reverse proxying, Kubernetes ingress, and more.

Further information reagrding [caddy](https://caddyserver.com/docs/)

```bash
echo "hello world - My name is <first name>" > index.html
sudo docker run -d -p 80:80 \
    -v $PWD/index.html:/usr/share/caddy/index.html \
    -v caddy_data:/data \
    caddy
```

## 3. Security Hardening

### 3.1. Basic

Basic security hardening is accepatable for testing but is not recommended alone for extensive development and production workloads

#### 3.1.1. Network Security Group (NSG)

1. Whitelist/Allow IP
    > Make a note of the IP address you are currently utilsing
   1. In the VM portal, select **networking** in the *setting* blade.
   2. Select **Inbound port rules**, select the **SSH** rule to edit the rule setting.
   3. Change **source** from *Any* to *IP Addresses*.
   4. In **Source IP addresses/CIDR ranges** add the IP address previously noted.
   5. Click **Save**
   6. Repeat steps for **HTTP** (port 80)
1. NSG Logging (Sentinel)
   1. Sign in to the [portal](https://portal.azure.com).
   2. Select **All services**, then type *network security groups*. When **Network security groups** appear in the search results, select it.
   3. Select the NSG you want to enable logging for.
   4. Under **MONITORING**, select **Diagnostics logs**, and then select **Turn on diagnostics**, as shown in the following picture:
       > Image TODO
   5. Under **Diagnostics settings**, enter, or select the following information, and then select **Save**:
       | Setting                                                                                     | Value                                                          |
       | ---------                                                                                   |---------                                                       |
       | Name                                                                                        | A name of your choosing.  For example: *myNsgDiagnostics*      |
       | **Archive to a storage account**, **Stream to an event hub**, and **Send to Log Analytics** | You can select as many destinations as you choose. To learn more about each, see [Log destinations](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-nsg-manage-log#log-destinations).                                                                                                                                           |
       | LOG                                                                                         | Select either, or both log categories. To learn more about the data logged for each category, see [Log categories](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-nsg-manage-log#log-categories).                                                                                                                                             |
1. View and analyze logs. For more information, see [Query logs in Microsoft Sentinel](https://docs.microsoft.com/en-us/learn/modules/query-logs-azure-sentinel/).

### 3.2. Moderate

#### 3.2.1. Web Application Firewall (WAF)

1. Create an application gateway
   1. Select **Create a resource** on the left menu of the Azure portal. The **New** window appears.
   2. Select **Networking** and then select **Application Gateway** in the **Featured** list.
1. Basics tab
   1. On the **Basics** tab, enter these values for the following application gateway settings:
      - **Resource group**: Select **myResourceGroupAG** for the resource group. If it doesn't exist, select **Create new** to create it.
      - **Application gateway name**: Enter *name_WAF* for the name of the application gateway.
      - **Tier**: select **WAF V2**.
      - **Region**: select **Australia East**
      - **Enable autoscaling**: select **No**
      - **HHTP2**: seclect **Disabled**
      - **WAF Policy**: Select **Create new**, type a name for the new policy *name_waf_policy*, tick **Add bot Portection** and then select **OK**.
        This creates a basic WAF policy with a managed Core Rule Set (CRS).
   2. For Azure to communicate between the resources that you create, it needs a virtual network. You can either create a new virtual network or use an existing one. In this example, you'll create a new virtual network at the same time that you create the application gateway. Application Gateway instances are created in separate subnets. You create two subnets in this example: one for the application gateway, and another for the backend servers.
       - Under **Configure virtual network**, select the the exisitng VM vnet *name-vnet*:
       - **Subnet name** (Create Application Gateway subnet for VM): Click **Manage Subnet Configuration**. <br>The application gateway subnet can contain only application gateways. No other resources are allowed.
       - In VM **subnets**, click **+ Subnets**.
       - In *Add Subnet*, add a name *anme_WAF to the new subnet. Use the Default **Subnet address Range** and Click **save**
       - Back in **Create application Gateway** pane, select newly create *subnet*.
           > Image TODO
   3. On the **Basics** tab, accept the default values for the other settings and then select **Next: Frontends**.
1. Frontends tab
   1. On the **Frontends** tab, verify **Frontend IP address type** is set to **Public**. <br>You can configure the Frontend IP to be Public or Private as per your use case. In this example, you'll choose a Public Frontend IP.
      > **NOTE:** For the Application Gateway v2 SKU, there must be a **Public** frontend IP configuration. You can still have both a Public and a Private frontend IP configuration, but Private only frontend IP configuration (Only ILB mode) is currently not enabled for the v2 SKU.
   2. Select **Add new** for the **Public IP address** and enter *name_waf_public_ip* for the public IP address name, and then select **OK**.
   3. Select **Next: Backends**.
1. Backends tab
    > The backend pool is used to route requests to the backend servers that serve the request. Backend pools can be composed of NICs, virtual machine scale sets, public IP addresses, internal IP addresses, fully qualified domain names (FQDN), and multi-tenant back-ends like Azure App Service. In this example, you'll create an empty backend pool with your application gateway and then add backend targets to the backend pool.
   1. On the **Backends** tab, select **Add a backend pool**.
   2. In the **Add a backend pool** window that opens, enter the following values to create an empty backend pool:
      - **Name**: Enter *name_waf_backend* for the name of the backend pool.
      - **Add backend pool without targets**: Select **No**.
      - Under **Target Type** select *Virtual MAchine*.
      - Select current VM as Target
   3. In the **Add a backend pool** window, select **Add**.
   4. On the **Backends** tab, select **Next: Configuration**.
1. Configuration tab
    > On the **Configuration** tab, you'll connect the frontend and backend pool you created using a routing rule.
   1. Select **Add a routing rule** in the **Routing rules** column.
   2. In the **Add a routing rule** window that opens, enter *name_WAF_rule* for the **Rule name**. Add **priority** of *300*.
   3. A routing rule requires a listener. On the **Listener** tab within the **Add a routing rule** window, enter the following values for the listener:
       - **Listener name**: Enter *name_WAF_rule_Listener* for the name of the listener.
       - **Frontend IP**: Select **Public** to choose the public IP you created for the frontend.
            > Accept the default values for the other settings on the **Listener** tab, then select the **Backend targets** tab to configure the rest of the routing rule.
   4. On the **Backend targets** tab, select **myBackendPool** for the **Backend target**.
   5. For the **HTTP setting**, select **Add new** to add a new HTTP setting. The HTTP setting will determine the behavior of the routing rule. In the **Add an HTTP setting** window that opens, enter *nameHTTPSetting* for the **HTTP setting name** and *80* for the **Backend port**. Accept the default values for the other settings in the **Add an HTTP setting** window, then select **Add** to return to the **Add a routing rule** window.
   6. On the **Add a routing rule** window, select **Add** to save the routing rule and return to the **Configuration** tab.
   7. Select **Next: Tags** and then **Next: Review + create**.
1. Review + create tab
    > Review the settings on the **Review + create** tab, and then select **Create** to create the virtual network, the public IP address, and the application gateway. It may take several minutes for Azure to create the application gateway. Wait until the deployment finishes successfully before moving on to the next section.
    Creation of the WAF can take up to 5 -30 minutes to complete

#### 3.2.2. Configure Firewall

1. In the newly created WAF, under **settings**, seclect *Web Application Firewall*.
1. Under *Configure*:
   - Change **Tier** to **WAF v2**
   - Change **WAF Status** to **enabled**
   - **WAF Mode** to **Prevention**
   - Under **Global Parameters**, turn **Inspect Request Body** to *off*
1. Under **Rules**:
   - Change **Rule Set** to *OWASP 3.2*
1. Click **Save** to commit changes to WAF.

#### 3.2.3. Ingest WAF Logs to Sentinel

1. Select Diagnostic logs.​
1. Select + Add diagnostic setting.​
1. In the Diagnostic setting blade:
   - Type a Name.
   - Select Send to Log Analytics.
   - Choose the log destination workspace.​
   - Select the categories that you want to analyze (recommended: ApplicationGatewayAccessLog, ApplicationGatewayFirewallLog, FrontdoorAccessLog, FrontdoorWebApplicationFirewallLog, WebApplicationFirewallLogs).​
   - Click Save.

### 3.3. Just In Time Access (JIT)

You can enable JIT on a VM from the Azure virtual machines pages of the Azure portal.

> **TIP:** If a VM already has just-in-time enabled, when you go to its configuration page you'll see that just-in-time is enabled and you can use the link to open the just-in-time VM access page in Defender for Cloud, and view and change the settings.

1. From the [Azure portal](https://portal.azure.com), search for and select **Virtual machines**.
1. Select the virtual machine you want to protect with JIT.
1. In the menu, select **Configuration**.
1. Under **Just-in-time access**, select **Enable just-in-time**.
    > This enables just-in-time access for the VM using the following default settings:
    - Windows machines:
        - RDP port 3389
        - Three hours of maximum allowed access
        - Allowed source IP addresses is set to Any
    - Linux machines:
        - SSH port 22
        - Three hours of maximum allowed access
        - Allowed source IP addresses is set to Any
1. To edit any of these values, or add more ports to your JIT configuration, use Microsoft Defender for Cloud's just-in-time page:
    1. From Defender for Cloud's menu, select **Just-in-time VM access**.
    1. From the **Configured** tab, right-click on the VM to which you want to add a port, and select edit.
        > Image TODO
    1. Under **JIT VM access configuration**, you can either edit the existing settings of an already protected port or add a new custom port.
    1. When you've finished editing the ports, select **Save**.

Further documentation on [Just In Time Access](https://docs.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview?tabs=defender-for-container-arch-aks)

## 4. Advanced

### 4.1. Network Watcher

#### 4.1.1. Create a Network Watcher in the portal

Navigate to **All Services** > **Networking** > **Network Watcher**. You can select all the subscriptions you want to enable Network Watcher for. This action creates a Network Watcher in every region that is available.

Image TODO

When you enable Network Watcher using the portal, the name of the Network Watcher instance is automatically set to *NetworkWatcher_region_name* where *region_name* corresponds to the Azure region where the instance is enabled. For example, a Network Watcher enabled in the West Central US region is named *NetworkWatcher_westcentralus*.

The Network Watcher instance is automatically created in a resource group named *NetworkWatcherRG*. The resource group is created if it does not already exist.

If you wish to customize the name of a Network Watcher instance and the resource group it's placed into, you can use PowerShell, the Azure CLI, the REST API, or ARMClient methods described in the sections that follow. In each option, the resource group must exist before you create a Network Watcher in it.  

### 4.2. Firewall

Deploy the firewall into the VNet.

1. On the Azure portal menu or from the **Home** page, select **Create a resource**.
2. Type **firewall** in the search box and press **Enter**.
3. Select **Firewall** and then select **Create**.
4. On the **Create a Firewall** page, use the following table to configure the firewall:

   |Setting  |Value  |
   |---------|---------|
   |Subscription     |\<your subscription\>|
   |Resource group     |**Test-FW-RG** |
   |Name     |**Test-FW01**|
   |Region     |Select the same location that you used previously|
   |Firewall tier|**Standard**|
   |Firewall management|**Use Firewall rules (classic) to manage this firewall**|
   |Choose a virtual network     |**Use existing**: **Test-FW-VN**|
   |Public IP address     |**Add new**<br>**Name**:  **fw-pip**|

5. Accept the other default values, then select **Review + create**.
6. Review the summary, and then select **Create** to create the firewall.

   This will take a few minutes to deploy.
7. After deployment completes, go to the **Test-FW-RG** resource group, and select the **Test-FW01** firewall.
8. Note the firewall private and public IP addresses. You'll use these addresses later.

### 4.3. DDOS Protection

#### 4.3.1. Create a DDoS protection plan

1. Select **Create a resource** in the upper left corner of the Azure portal.
1. Search the term *DDoS*. When **DDoS protection plan** appears in the search results, select it.
1. Select **Create**.
1. Enter or select the following values.

    |Setting        |Value                                              |
    |---------      |---------                                          |
    |Subscription   | Select your subscription.                         |
    |Resource group | Enter exisitng **MyResourceGroup**.|
    |Name           | Enter **MyDdosProtectionPlan**.                     |
    |Region         | Enter **Australia East**.                                  |

1. Select **Review + create** then **Create**

#### 4.3.2. Enable DDoS protection for an existing virtual network

1. Create a DDoS protection plan by completing the steps in [Create a DDoS protection plan](#431-create-a-ddos-protection-plan), if you don't have an existing DDoS protection plan.
1. Enter the name of the virtual network that you want to enable DDoS Protection Standard for in the **Search resources, services, and docs box** at the top of the Azure portal. When the name of the virtual network appears in the search results, select it.
1. Select **DDoS protection**, under **Settings**.
1. Select **Enable**. Under **DDoS protection plan**, select an existing DDoS protection plan, or the plan you created in step 1, and then click **Save**. The plan you select can be in the same, or different subscription than the virtual network, but both subscriptions must be associated to the same Azure Active Directory tenant.
