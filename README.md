# 📊 LendingClub Loan Risk Analysis & Visualization
A data analysis and modeling project to assess loan risks and borrower profiles using LendingClub data. Built as part of a data analytics portfolio, this Python project demonstrates skills in data cleaning, feature engineering, custom function/class creation, and insightful data visualization.

## 📌 Project Overview
As a Data Analyst for LendingClub, your task is to build a simple model to predict whether a borrower will fully repay their loan. The analysis explores borrower behavior and loan conditions using key variables like:
* Loan purpose
* Interest rate
* FICO score
* Debt-to-income ratio
* Delinquencies and inquiries

The final output includes custom risk categorization, FICO classification, and multiple visualizations to guide decision-making.

## 📂 Datasets
* loandataset.xlsx: Contains loan details.
* customer_data.csv: Contains borrower demographic and behavioral data.
* These datasets are merged on customerid and id.

## ⚙️ Features & Analysis
🔧 Feature Engineering
* Categorized loan purposes (purpose_category)
* FICO score bucketization (fico_category)
* Rule-based risk tagging (Risk)
* Combined inquiries & derogatory records flag (high_inq_and_derog)

📉 Custom Analytics Class

A reusable class for computing column statistics like mean and median.

📊 Visualizations
* Loan purpose distribution (bar plot)
* Debt-to-Income vs Income (scatter plot)
* FICO score distribution (histogram)
* Risk category vs interest rate (boxen plot)
* Composite subplot with 4 key insights

## 🛠 Technologies & Libraries
* Python 3
* pandas
* matplotlib
* seaborn
