# WASOC Workbook HOW TO Guide
## Use of the GAP Analysis Workbook
1. Select the Subscription, Workspace, and TimeRange parameters. These will apply across all the tabs and threat-hunting queries.
![1](/utilities/screenshots/wrkbk-TH-1.png)
2. Select one of the three tabs to start with threat hunting. Queries will automatically run using the selected parameters from step 1.
- Threat Hunting Queries - A number of various queries to detect some of the most common attacks
- Open Source Thret Intelligence - Query that uses open source TI feeds to detect malicious activity
- Pivoting - Queries to pivot on activities from compromised assets to detect malicious
![2](/utilities/screenshots/wrkbk-TH-2.png)
3. When performing the initial investigation under the pivoting tab, update the fields with compromised entities. The below queries will run automatically and show the results.
![3](/utilities/screenshots/wrkbk-TH-3.png)
4. Adding additional queries can be done by copying existing queries and changing the query and the naming.
a. Select 'Edit' on the whole workbook and click Edit from onj the specific group
![4](/utilities/screenshots/wrkbk-TH-4.png)
b. Clone one of the existing queries
![5](/utilities/screenshots/wrkbk-TH-5.png)
c. Under Settings tab, change the query with the new one
![6](/utilities/screenshots/wrkbk-TH-6.png)
d. Under 'Advanced Settings' tab, change the naming of the query. Ensure the parameters TimeRange and Workspace are as per the globally assigned parameters.
![7](/utilities/screenshots/wrkbk-TH-7.png)
5. Save the workbook