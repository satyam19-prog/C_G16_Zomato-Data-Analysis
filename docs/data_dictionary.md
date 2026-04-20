# 📊 Data Dictionary — Zomato Delivery Operations Analytics

This document defines all fields used in the analysis, cleaning pipeline, KPI computation, and Tableau dashboard for the Zomato Delivery Operations Analytics project.

---

## 📌 Dataset Summary

| Item          | Details                                      |
| ------------- | -------------------------------------------- |
| Dataset name  | Zomato Delivery Operations Analytics Dataset |
| Source        | Kaggle — Saurabh Badole                      |
| Raw file name | zomato_delivery_dataset.csv                  |
| Last updated  | As per Kaggle dataset                        |
| Granularity   | One row per delivery order                   |

---

## 📂 Column Definitions

| Column Name         | Data Type | Description                                               | Example Value       | Used In      | Cleaning Notes                              |
| ------------------- | --------- | --------------------------------------------------------- | ------------------- | ------------ | ------------------------------------------- |
| order_id            | string    | Unique identifier for each order                          | ORD10234            | KPI, EDA     | Checked for duplicates; ensured uniqueness  |
| customer_id         | string    | Unique identifier for each customer                       | CUST5678            | EDA          | Not used in KPIs; retained for reference    |
| restaurant_id       | string    | Unique identifier for restaurant                          | REST901             | EDA          | Standardized format                         |
| delivery_partner_id | string    | Identifier for delivery agent                             | DP345               | EDA          | Missing values handled where applicable     |
| order_time          | datetime  | Timestamp when order was placed                           | 2023-06-15 19:45:00 | EDA, KPI     | Converted to datetime format                |
| delivery_time       | float     | Total time taken for delivery (in minutes)                | 32.5                | KPI, EDA     | Converted to numeric; outliers capped       |
| distance_km         | float     | Distance between restaurant and delivery location (in km) | 4.8                 | KPI, EDA     | Removed unrealistic values                  |
| traffic_level       | string    | Traffic conditions during delivery                        | High                | EDA, Tableau | Standardized categories (Low, Medium, High) |
| weather_condition   | string    | Weather conditions during delivery                        | Rainy               | EDA, Tableau | Normalized text labels                      |
| delivery_status     | string    | Status of order (Delivered / Cancelled)                   | Delivered           | KPI          | Filtered for valid deliveries               |
| customer_rating     | float     | Rating given by customer (1–5 scale)                      | 4.2                 | KPI, EDA     | Missing values handled (imputed or flagged) |
| city                | string    | City where delivery occurred                              | Delhi               | Tableau      | Standardized naming conventions             |

---

## 🧮 Derived Columns

| Derived Column   | Logic                           | Business Meaning                                              |
| ---------------- | ------------------------------- | ------------------------------------------------------------- |
| is_late_delivery | delivery_time > 30 minutes      | Identifies delayed deliveries impacting customer satisfaction |
| delivery_hour    | Extract hour from order_time    | Helps identify peak order times                               |
| delivery_day     | Extract weekday from order_time | Enables day-wise performance analysis                         |
| rating_category  | rating ≥ 4 → High, else Low     | Segments satisfied vs unsatisfied customers                   |
| distance_bucket  | 0–2 km, 2–5 km, 5+ km           | Groups deliveries by distance for efficiency analysis         |

---

## ⚠️ Data Quality Notes

* Missing values observed in **customer_rating** (not all customers provide ratings)
* Potential duplicates in **order_id** — removed during cleaning
* Inconsistent categorical values (e.g., "high", "HIGH", "High") standardized
* Outliers detected in **delivery_time** — capped using IQR method
* Cancelled orders excluded from delivery performance KPIs
* Date/time fields required conversion to proper datetime format
* Distance values checked for anomalies and unrealistic entries

---

## 📌 Notes

* All transformations are documented in `02_cleaning.ipynb`
* Cleaned dataset is stored in `data/processed/`
* This data dictionary supports KPI creation, EDA, and Tableau dashboard design

---
