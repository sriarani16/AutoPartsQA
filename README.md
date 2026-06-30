# 🚗 AutoPartsQA – Automotive Data Quality & Analytics Platform

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 🌐 Live Demo

👉 **https://autopartsapp.streamlit.app**

---

# 📘 Overview

AutoPartsQA is an end-to-end **Automotive Data Quality and Analytics Platform** designed to identify, measure, and visualize data quality issues before they impact reporting, analytics, machine learning models, or business operations.

This project simulates a real-world enterprise workflow where automotive parts data is stored in **PostgreSQL**, validated using **SQL and Python**, processed with **Pandas and SQLAlchemy**, and visualized through an interactive **Streamlit** dashboard.

The platform automatically detects data quality issues, calculates an overall **Data Quality Score**, and provides actionable insights to improve dataset reliability.

---

# 🚨 Business Problem

Automotive companies receive parts data from multiple suppliers. Poor-quality data can lead to:

- Incorrect part matching
- Duplicate inventory
- Pricing errors
- Failed ordering workflows
- Poor product search results
- Reduced customer satisfaction

AutoPartsQA helps identify these issues early through automated validation, quality scoring, and interactive reporting.

---

# 🔍 Features

## ✅ Data Validation Engine

Automatically detects:

- Missing manufacturer names
- Missing vehicle models
- Missing categories
- Missing part names
- Invalid or negative prices
- Duplicate records
- Brand inconsistencies
- Overall dataset completeness

---

## 📊 Interactive Data Quality Dashboard

Built using **Streamlit**, the dashboard provides:

- Dataset summary
- Data Quality Score
- Missing values analysis
- Duplicate record analysis
- Invalid price detection
- Brand distribution
- Category statistics
- Interactive charts
- Raw data explorer

---

## 🗄 SQL Validation Rules (PostgreSQL)

Implements validation queries for:

- Duplicate detection
- Missing value identification
- Invalid pricing checks
- Brand statistics
- Category summaries

---

## 📈 Business Analytics

Provides useful business insights including:

- Top manufacturers
- Highest-quality categories
- Duplicate percentage
- Missing data percentage
- Price distribution
- Overall dataset health score

---

# 🏗 System Architecture

```text
                 CSV Dataset
                      │
                      ▼
             PostgreSQL Database
                      │
                      ▼
            SQL Validation Queries
                      │
                      ▼
        Python Data Processing
        (Pandas + SQLAlchemy)
                      │
                      ▼
          Data Quality Engine
                      │
                      ▼
          Streamlit Dashboard
```

---

# 🛠 Technology Stack

- Python
- PostgreSQL
- SQL
- Pandas
- NumPy
- SQLAlchemy
- Streamlit
- Plotly
- Git
- GitHub

---

# 📁 Project Structure

```text
AutoPartsQA/

├── analysis/
│   ├── cleaning.py
│   ├── quality.py
│   └── __init__.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── create_tables.sql
│   └── insert_sample_data.sql
│
├── sql/
│   └── validation_queries.sql
│
├── data/
│   └── parts.csv
│
├── images/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/sriarani16/AutoPartsQA.git

cd AutoPartsQA
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

Create the PostgreSQL database:

```sql
CREATE DATABASE autopartsqa;
```

Create the required tables:

```bash
database/create_tables.sql
```

Insert the sample data:

```bash
database/insert_sample_data.sql
```

---

# ▶ Running the Dashboard

Start the Streamlit application:

```bash
streamlit run dashboard/app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# 📊 Example Dashboard

> Add screenshots of your dashboard inside the **images/** folder and reference them below.

```markdown
![Dashboard Overview](images/dashboard.png)
```

Example dashboard includes:

- Data Quality Score
- Missing Values Report
- Duplicate Analysis
- Invalid Price Detection
- Brand Distribution
- Category Statistics
- Interactive Charts
- Raw Dataset Viewer

---

# 🚀 Future Enhancements

- CSV upload functionality
- Automatic data cleaning recommendations
- AI-powered duplicate detection
- REST API for automated quality validation
- Docker containerization
- AWS cloud deployment
- Scheduled data quality monitoring
- Historical quality tracking
- User authentication
- Export cleaned datasets

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- PostgreSQL database design
- SQL query development
- Python data processing
- Data quality engineering
- Data validation techniques
- Interactive dashboard development
- Business analytics and reporting
- End-to-end data pipeline development

---

# 👤 Author

**Sriarani Surenther**

📍 Hamilton, New Zealand

**LinkedIn**

https://www.linkedin.com/in/sriarani-surenther

**GitHub**

https://github.com/sriarani16

---

# 📄 License

This project is licensed under the **MIT License**, allowing free use, modification, and distribution with appropriate attribution.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Feedback and contributions are always welcome!
