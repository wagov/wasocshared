# WASOC Workbook HOW TO Guide

## Use of the GAP Analysis Workbook

1. The **Data Visibility** tab illustrates the current visibility of data ingested into the Sentinel workspace. These tables are recommended for improved [detections](https://soc.cyber.wa.gov.au/baselines/data-sources/#5-detection-analytics) and [threat hunting](https://soc.cyber.wa.gov.au/guidelines/TTP_Hunt/ttp-detection-guidelines/#threat-hunting-guideline) activities. For more details, please refer to [Baseline for Detection Coverage (MITRE ATT&CK)](https://soc.cyber.wa.gov.au/baselines/data-sources/#baseline-for-detection-coverage-mitre-attck) and [Telemetry to collect (prioritised)](https://soc.cyber.wa.gov.au/onboarding/sentinel-guidance/?h=maturity+model#2-telemetry-to-collect-prioritised) guidelines.
![Data Visibility](/utilities/screenshots/wrkbk-datavis.png)
1. The sections under the **Data Visibility** tab, provide details on the activities that can be seen from these tables. They also include links to the data connectors and the recommended actions.
![Data Visibility](/utilities/screenshots/wrkbk-spltgrps.png)
1. The **Noisy Alerts** tab illustrates the top 5 firing alerts from the previous 30 days that have not been resolved as a [True Positive incident](https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases#closing-an-incident). These are considered as noisy detection rules and require additional measures to mitigate alert fatigue. Please refer to: [Managing your SIEM Sentinel Analytic Rules](https://soc.cyber.wa.gov.au/guidelines/incident-reporting/?h=rules#41-managing-your-siem-sentinel-analytic-rules) for further details.
![Data Visibility](/utilities/screenshots/wrkbk-noisy.png)
1. The **Log Ingestion** tab illustrates Data Ingestion Volume per log category, which is intended to illustrate the allocation of majority of the Sentinel costs. It is important for security teams to understand and manage log ingestion costs. Refer to the [performance and cost optimisation guidelines](https://soc.cyber.wa.gov.au/onboarding/sentinel-guidance/?h=cost#5-performance-and-cost-optimisation) for more details.
![Data Visibility](/utilities/screenshots/wrkbk-logingestion.png)