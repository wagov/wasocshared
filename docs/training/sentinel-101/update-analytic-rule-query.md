# Updating a Sentinel Analytic Rule KQL Query
This page contains instructions to update an analytic rule's KQL query in Sentinel. This process is simple and requires minimal actions to be performed.

1. Go to the affected **Sentinel** workspace.

    If you are unsure where to find your workspaces, visit this link -> [https://portal.azure.com/sentinel](https://portal.azure.com/#browse/microsoft.securityinsightsarg%2Fsentinel).

2. Once you have selected your Sentinel workspace, on the left hand side of the screen, navigate to **Configuration** -> **Analytics**.
    
    (You may need to expand the sub-menus).

3. **Search** for and **select** the affected **analytic rule**. 

4. Click on the **Edit** button.

    If the rule flyout menu is not opening when selecting the rule, go to the right of the rule and click on the **3 dots button** -> **Edit**.

5. Select the **Set rule logic** tab.

    ![Analytic Rule Set Rule Logic Tab](../../images/AnalyticRuleSetRuleLogicTab.png)

6. Locate the **Rule query** section.

    *Edit the existing query in place, or paste in the updated query into the query text box.*

7. Select the **Review + create** tab.  

    ![Analytic Rule Review and Create Tab](../../images/AnalyticRuleReviewAndCreateTab.png)

8. At the *bottom of the page* -> click on the **Save button** to save the changes to the analytic rule.