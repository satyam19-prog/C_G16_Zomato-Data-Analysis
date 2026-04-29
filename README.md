Readme · MD
Copy

# Zomato Delivery Operations Analytics
 
> **Newton School of Technology | Data Visualization & Analytics — Capstone 2**
> A 2-week industry simulation converting raw Zomato delivery data into actionable business intelligence using Python, GitHub, and Tableau.
 
---
 
## Project Overview
 
| Field | Details |
|---|---|
| **Project Title** | Zomato Delivery Operations Analytics |
| **Sector** | Food Technology and Delivery Operations |
| **Team ID** | G16 |
| **Section** | C |
| **Faculty Mentor** | Archit Sir |
| **Institute** | Newton School of Technology |
| **GitHub Repository** | https://github.com/kushpuri07/C_G16_Zomato-Data-Analysis |
| **Tableau Dashboard** | https://public.tableau.com/views/Zomato_Delivery_Analysis/Dashboard1 |
 
### Team Members
 
| Role | Name | GitHub Username |
|---|---|---|
| Project Lead & Visualization Lead | Kush Puri | `https://github.com/kushpuri07` |
| Design & Visualization | Nitanshu Goyal | `https://github.com/nitanshu12` |
| Analysis & Visualization | Satyam Singh | `https://github.com/satyam19-prog` |
| Statistical Analysis & Visualization | Neeraj Singh | `https://github.com/Neeraj-singh140805` |
| PPT & Quality Lead | Augustya Purohit | `https://github.com/augustyapurohit` |
| Strategy Lead | Shubhaang Kataruka | `https://github.com/S-h-u-b-h-1` |
 
---
 
## Business Problem
 
India's food delivery market is growing at a CAGR exceeding 15% through 2027, making delivery time one of the most critical competitive differentiators for platforms like Zomato. Delays caused by traffic congestion, adverse weather, festival-period surges, and under-resourced delivery partners directly translate into customer dissatisfaction, negative ratings, and order cancellations.
 
**Core Business Question**
 
> Which operational factors — traffic density, weather conditions, vehicle type, delivery partner ratings, and festival periods — most significantly impact food delivery time on Zomato, and what targeted interventions can reduce average delivery time by at least 15 percent?
 
**Decision Supported**
 
> This analysis enables operations managers and executive stakeholders to implement data-backed interventions in routing, partner deployment, and resource planning to measurably reduce average delivery time and improve customer satisfaction.
 
---
 
## Dataset
 
| Attribute | Details |
|---|---|
| **Source Name** | Kaggle — Zomato Delivery Operations Analytics Dataset by Saurabh Badole |
| **Direct Access Link** | https://www.kaggle.com/datasets/saurabhbadole/zomato-delivery-operations-analytics-dataset |
| **Row Count** | 45,584 |
| **Column Count** | 20 (original) · 25 (post feature engineering) |
| **Time Period Covered** | February 2022 to April 2022 |
| **Format** | CSV |
 
### Key Columns Used
 
| Column Name | Description | Role in Analysis |
|---|---|---|
| `Time_taken (min)` | Total delivery time in minutes | Target variable / primary KPI |
| `Road_traffic_density` | Traffic density level during delivery (Low / Medium / High / Jam) | Key delay driver / filter |
| `Weather_conditions` | Prevailing weather at time of delivery | Delay driver / segmentation |
| `Festival` | Whether a festival was ongoing at time of order (Yes / No) | Delay driver / KPI |
| `City` | City type of delivery location (Metropolitan / Urban / Semi-Urban) | Geographic segmentation / filter |
| `Delivery_person_Ratings` | Customer rating given to the delivery partner | Performance KPI / correlation |
| `Type_of_vehicle` | Type of vehicle used for delivery | Fleet analysis / filter |
| `multiple_deliveries` | Number of simultaneous deliveries carried | Batching impact analysis |
| `Delivery_person_Age` | Age of the delivery partner in years | Partner demographics |
| `Vehicle_condition` | Condition rating of the delivery vehicle (0–3) | Fleet maintenance KPI |
| `Order_Date` | Date on which the order was placed | Time-series / trend analysis |
| `Order_Hour` | Hour at which the order was placed (feature engineered) | Peak demand analysis |
 
For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).
 
---
 
## KPI Framework
 
| KPI | Definition | Stakeholder |
|---|---|---|
| Average Delivery Time | Mean of `Time_taken (min)` across all orders | Executive |
| Total Orders | Count of unique order IDs | Executive |
| Average Partner Rating | Mean of `Delivery_person_Ratings` | Executive |
| Peak Order Day | Day of week with highest order volume | Executive |
| Worst Traffic Density | Traffic level associated with the highest average delivery time | Operations |
| Worst Weather Condition | Weather type associated with the highest average delivery time | Operations |
| Festival Time Difference | Difference in avg delivery time between Festival and Non-Festival orders | Operations |
| Average Multiple Deliveries | Mean number of simultaneous deliveries per order | Operations |
| Average Partner Age | Mean age of all active delivery partners | Partner Performance |
| Top Vehicle Used | Vehicle type with the highest order volume | Partner Performance |
| Top Rated Average Time | Avg delivery time for partners with rating ≥ 4.8 | Partner Performance |
 
---
 
## Tableau Dashboard
 
| Item | Details |
|---|---|
| **Dashboard URL** | https://public.tableau.com/views/Zomato_Delivery_Analysis/Dashboard1?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link |
| **Executive View** | High-level KPI summary: avg delivery time, total orders, avg partner rating, peak day, city-wise performance, order type mix, and hourly/weekly demand trends |
| **Operational View** | Delay driver analysis across traffic density, weather conditions, festival periods, multiple deliveries, and vehicle types |
| **Partner Performance View** | Driver demographics, rating vs delivery time correlation, vehicle condition impact, and age-group performance segmentation |
| **Main Filters** | City type, Road traffic density, Weather conditions, Festival (Yes/No), Vehicle type, Day of week |
 
Dashboard screenshots are stored in [`tableau/screenshots/`](tableau/screenshots/) and the public link is documented in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).
 
---
 
## Key Insights
 
1. **Jam traffic conditions increase average delivery time by 5 to 7 minutes** compared to low traffic, representing the single largest controllable contributor to delivery delays.
2. **Semi-Urban areas record an average delivery time of 49 minutes — nearly double the Urban average of 20 minutes**, indicating a structural under-investment in delivery infrastructure and partner density in semi-urban zones.
3. **Cloudy weather is associated with the highest average delivery times**, suggesting that reduced visibility has a greater operational impact than precipitation-based conditions such as storms or sandstorms.
4. **Delivery partners rated 4.8 and above deliver orders 1.9 minutes faster than the fleet average**, confirming that partner quality is a measurable and actionable driver of operational efficiency.
5. **Each additional simultaneous delivery is associated with a measurable increase in total delivery time**, indicating that indiscriminate order batching beyond a threshold reduces both efficiency and customer satisfaction.
6. **Festival periods do not consistently increase delivery times when staffing is proactively scaled**, as evidenced by the negative festival time difference observed in the data.
7. **Electric scooters demonstrate lower average delivery times than motorcycles and bicycles**, suggesting they represent a high-value fleet investment for urban operations.
8. **Peak order hours at lunch (13:00–15:00) and dinner (19:00–22:00) are consistent and predictable**, enabling precise time-based partner deployment strategies.
9. **Delivery partners in the 30–35 age group demonstrate the highest average delivery times, while under-25 partners show the lowest**, suggesting younger partners may be more route-adaptive.
10. **Vehicle condition has a measurable negative correlation with delivery time**: partners operating vehicles in poor condition take approximately 2.76 minutes longer on average.
11. **Motorcycle and scooter deliveries account for the majority of all orders**, while bicycle deliveries represent a small but consistently slower segment warranting route-specific optimisation.
12. **Wednesday records the highest order volume across the week**, contradicting the common assumption that weekends drive peak demand and suggesting mid-week promotional and staffing adjustments are warranted.
---
 
## Recommendations
 
| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Jam traffic adds 5–7 min to delivery time | Integrate real-time traffic data into the Zomato dispatch algorithm to auto-reroute partners away from jam-density zones during peak hours | 8–12% reduction in avg delivery time during peak traffic periods |
| 2 | Cloudy and foggy weather are the worst delay-associated conditions | Establish a weather monitoring protocol that automatically triggers additional partner deployment when cloudy or foggy conditions are forecast | ~15% reduction in weather-related delays |
| 3 | High-rated partners (≥4.8) deliver 1.9 min faster than the fleet average | Create a tiered incentive structure rewarding top-rated partners with priority order allocation and performance bonuses | Expanding this cohort to 30% of the active fleet could reduce fleet-wide avg delivery time by ~0.6 min with compounding satisfaction benefits |
| 4 | Each additional simultaneous delivery increases delivery time linearly | Enforce a cap of 2 simultaneous deliveries per partner during peak hours (13:00–15:00 and 19:00–22:00) | Consistent delivery time protection during the highest-demand periods |
| 5 | Semi-Urban areas are 29 min slower than Urban on average | Prioritise increasing partner density, dark kitchen placement, and route coverage in semi-urban zones | A 20% increase in semi-urban partner density is estimated to reduce semi-urban avg delivery time by ~10 min |
 
---
 
## Analytical Pipeline
 
The project follows a structured 7-step workflow:
 
1. **Define** — Sector selected (Food Technology), problem statement scoped around delivery time drivers, mentor approval obtained at Gate 1.
2. **Extract** — Raw dataset sourced from Kaggle (45,584 rows, 20 columns) and committed to `data/raw/`; data dictionary drafted in `docs/`.
3. **Clean and Transform** — Full ETL pipeline built in `notebooks/02_cleaning.ipynb`: column name correction, categorical value correction (e.g. `Metropolitian` → `Metropolitan`), missing value imputation across 8 columns, datetime conversion, and feature engineering of 5 new time-based columns.
4. **Analyze** — EDA and statistical analysis in notebooks `03` and `04`: distribution analysis, city/weather/traffic segmentation, One-Way ANOVA, Independent T-Test, Pearson Correlation, and Linear Regression.
5. **Visualize** — Three interactive Tableau dashboards built and published on Tableau Public: Executive Overview, Operational Analysis, and Partner Performance.
6. **Recommend** — 5 data-backed business recommendations delivered, each linked to a specific insight and accompanied by an estimated impact.
7. **Report** — Final project report and presentation deck completed and exported to PDF in `reports/`.
---
 
## Statistical Analysis Summary
 
| Test | Variables | Method | Result |
|---|---|---|---|
| Test 1 | Traffic Density vs Delivery Time | One-Way ANOVA | Statistically significant (p < 0.05) |
| Test 2 | Festival vs Delivery Time | Independent T-Test | Statistically significant (p < 0.05) |
| Test 3 | Weather Conditions vs Delivery Time | One-Way ANOVA | Statistically significant (p < 0.05) |
| Test 4 | Multiple Deliveries vs Delivery Time | One-Way ANOVA | Statistically significant (p < 0.05) |
 
Pearson correlation confirmed that multiple deliveries show the strongest positive correlation with delivery time. Vehicle condition and partner ratings both show weak negative correlations. A multiple linear regression model trained on 6 features (traffic, weather, city, multiple deliveries, ratings, vehicle condition) returned a moderate R-squared score, confirming collective predictive utility.
 
---
 
## Repository Structure
 
```text
C_G16_Zomato-Data-Analysis/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output: Zomato_Cleaned.csv (25 columns, 0 nulls)
|
|-- notebooks/
|   |-- 01_extraction.ipynb          # Data loading, inspection, null profiling
|   |-- 02_cleaning.ipynb            # ETL pipeline: imputation, correction, feature engineering
|   |-- 03_eda.ipynb                 # Exploratory analysis: distributions, trends, outliers
|   |-- 04_statistical_analysis.ipynb # ANOVA, T-Test, Pearson correlation, Linear Regression
|   `-- 05_final_load_prep.ipynb     # KPI computation and final data load
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/                 # Dashboard screenshots
|   `-- dashboard_links.md           # Tableau Public URL
|
|-- reports/
|   |-- project_report.pdf
|   `-- presentation.pdf
|
|-- docs/
|   `-- data_dictionary.md
|
|-- DVA-oriented-Resume/
`-- DVA-focused-Portfolio/
```
 
---
 
## Tech Stack
 
| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, EDA, statistical analysis, KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |
 
**Python libraries used:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `sklearn`
 
---
 
## Evaluation Rubric
 
| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |
 
---
 
## Contribution Matrix
 
| Team Member | Role | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
|---|---|---|---|---|---|---|---|---|
| Kush Puri | Project Lead, Visualization Lead | Support | Owner | Support | Support | Owner | Support | Support |
| Nitanshu Goyal | Design | Support | Support | Support | Support | Owner | Support | Support |
| Satyam Singh | Analysis | Support | Support | Owner | Support | Support | Owner | Support |
| Neeraj Singh | Statistical Analysis & Visualization | Owner | Support | Support | Owner | Support | Support | Support |
| Augustya Purohit | PPT & Quality Lead | Support | Support | Support | Support | Support | Support | Owner |
| Shubhaang Kataruka | Strategy Lead | Support | Support | Support | Support | Support | Owner | Support |
 
_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._
 
---
 
## Limitations and Future Scope
 
**Limitations**
- The dataset is synthetically generated and should be validated against live Zomato transactional data before implementing recommendations.
- The dataset covers a limited time window (Feb–Apr 2022) and may not capture seasonal variation across all quarters.
- Customer-side data (order value, cuisine preference, satisfaction scores) were not available, limiting demand-side analysis.
- The linear regression model produced a moderate R-squared score, indicating that a significant portion of delivery time variance is explained by factors not present in the dataset.
**Future Scope**
- Integration of real-time GPS and traffic API data to enable live delivery time prediction.
- Application of advanced ML models (Random Forest, XGBoost) to improve delivery time prediction accuracy.
- Customer churn analysis linking delivery delays to repeat order behaviour and rating outcomes.
- Expansion to tier-2 and tier-3 Indian cities for a nationally representative analysis.
---
 
## Academic Integrity
 
All analysis, code, and recommendations in this repository are the original work of Team G16, Section C. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.
 
---
 
*Newton School of Technology — Data Visualization & Analytics | Capstone 2 | Section C, Team G16*