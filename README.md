# Insurance Risk Analytics

## Project Overview

This project focuses on insurance risk analytics for AlphaCare Insurance Solutions (ACIS), a South African auto-insurance company preparing for an aggressive growth phase. The objective is to support the transition from intuition-based pricing to analytics-driven decision making using historical insurance claim data.

The analysis uses an 18-month historical dataset (February 2014 – August 2015) containing policy, premium, claim, customer, and vehicle-related information.

The project is divided into four major tasks:

- Task 1: Exploratory Data Analysis (EDA)
- Task 2: Data Version Control (DVC)
- Task 3: A/B Hypothesis Testing
- Task 4: Statistical Modeling and Premium Optimization

---

## Business Objective

The core business problem is improving insurance pricing accuracy while identifying low-risk customer segments where premiums can be reduced competitively to attract new customers.

Two key insurance metrics are central to the analysis:

### Loss Ratio

Loss Ratio measures the proportion of premiums paid out as claims.

Loss Ratio = TotalClaims / TotalPremium

- High loss ratio → higher insurance risk and lower profitability
- Low loss ratio → more profitable customer segments

### Margin

Margin evaluates insurer profitability.

Margin = TotalPremium − TotalClaims

- Positive margin → profitable policies
- Negative margin → unprofitable policies

The project aims to identify patterns in claims, profitability, and customer risk profiles to support data-driven underwriting decisions.

---

## Repository Structure

```bash
Insurance-risk-analytics/
│
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks for EDA and analysis
├── src/                   # Reusable utility scripts
├── tests/                 # Unit tests
├── .dvc/                  # DVC configuration
├── requirements.txt
├── README.md
└── .gitignore

# Task 1: Exploratory Data Analysis (EDA)
### Objectives
-  Understand data structure and quality
-  Analyze claim and premium distributions
-  Identify geographic and demographic risk patterns
-  Detect outliers and claim severity trends
-  Explore profitability using Loss Ratio and Margin metrics
### Key Analyses
-  Descriptive statistics
-  Missing value assessment
-  Univariate analysis
-  Bivariate and multivariate analysis
-  Geographic comparisons by province
-  Vehicle risk analysis
-  Temporal claim trend analysis
-  Outlier detection
### Example Insights
-  Luxury vehicle brands tend to have higher claim severity.
-  Provinces exhibit different loss ratios and profitability profiles.
-  High-value vehicles are associated with larger insurance claims.
-  Monthly claim trends reveal potential seasonal risk escalation patterns.
# Task 2: Data Version Control (DVC)
### Objectives
-  Ensure reproducibility of datasets and experiments
-  Enable auditability of data transformations
-  Track dataset versions efficiently
### DVC Workflow
-  Initialized DVC repository
-  Configured local remote storage
-  Added datasets using DVC tracking
-  Created cleaned dataset versions
### Importance

In regulated insurance environments, reproducibility and auditability are critical. DVC enables consistent tracking of data transformations and supports reliable analytical workflows.
# Technologies Used
-  Python
-  Pandas
-  NumPy
-  Matplotlib
-  Seaborn
-  Scikit-learn
-  Git
-  DVC
# Installation

-  Clone the repository:

git clone https://github.com/yenguandroid/Insurance-risk-analytics.git
-  Navigate into the project:

cd Insurance-risk-analytics

-  Create virtual environment:

python -m venv venv

-  Activate virtual environment:

Windows
venv\Scripts\activate

-  Install dependencies:

pip install -r requirements.txt
-  DVC Commands

Initialize DVC:

dvc init

-  Track dataset:

dvc add data/insurance_data.csv

Push dataset to remote storage:

dvc push