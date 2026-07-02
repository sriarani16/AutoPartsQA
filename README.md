# 🚗 AutoPartsQA – Automotive Data Quality & Analytics Platform

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 🌐 Live Demo

👉 https://autopartsapp.streamlit.app

---

# 📘 Overview

**AutoPartsQA** is an end-to-end **Automotive Data Quality & Analytics Platform** that validates, cleans, scores, and visualizes automotive parts data using a modern enterprise-style data pipeline.

The platform integrates:

- PostgreSQL for raw and cleaned data storage
- SQLAlchemy for database connectivity
- Pandas for data processing
- Streamlit for interactive dashboards
- RapidFuzz for AI-powered duplicate detection
- Timestamped versioning for cleaned datasets

The system identifies data quality issues early, computes a **Data Quality Score**, and provides actionable insights to improve dataset reliability.

---

# 🚨 Business Problem

Automotive companies receive inventory data from multiple suppliers. Poor-quality data can result in:

- Incorrect part matching
- Duplicate inventory
- Pricing errors
- Failed ordering workflows
- Poor search results
- Reduced customer satisfaction

**AutoPartsQA** solves these challenges through automated validation, cleaning, analytics, and interactive reporting.

---

# 🔍 Key Features

## 🧼 1. Automated Data Cleaning Pipeline

- Missing value detection
- Duplicate detection
- Invalid price validation
- Brand normalization (`utils/brand_cleaner.py`)
- Category inference (`utils/category_detector.py`)
- Data type conversion
- Data formatting

---

## 🧠 2. AI-Powered Duplicate Detection

Using **RapidFuzz**, the platform detects:

- Similar part names
- Similar manufacturer/model combinations
- Potential duplicates missed by exact matching

---

## 🗄 3. PostgreSQL Integration

### Raw Data

Data can be loaded from:

- CSV files
- PostgreSQL `parts` table

### Cleaned Data

Cleaned datasets are automatically stored as timestamped tables, for example:

```text
parts_cleaned_20260702_120558
parts_cleaned_20260702_121010
```

The dashboard always loads the latest cleaned version using:

```python
load_latest_cleaned_data()
```

This provides:

- Version history
- Data lineage
- Historical tracking

---

## 📊 4. Interactive Streamlit Dashboard

The dashboard provides:

- Dataset Summary
- Data Quality Score
- Missing Values Analysis
- Duplicate Records
- Invalid Price Detection
- Brand Distribution
- Category Statistics
- AI Duplicate Detection
- Raw Data Explorer
- Save Cleaned Data to PostgreSQL

---

# 🏗 System Architecture

```text
                CSV Files / PostgreSQL
                         │
                         ▼
                  Data Loading Layer
                         │
                         ▼
              Cleaning & Validation Layer
      (Pandas • SQLAlchemy • Brand Cleaner • Category Detector)
                         │
                         ▼
          Timestamped Cleaned PostgreSQL Tables
                         │
                         ▼
             Interactive Streamlit Dashboard
```

---

# 🛠 Technology Stack

- Python 3.11
- PostgreSQL
- SQLAlchemy
- Pandas
- NumPy
- RapidFuzz
- Plotly
- Streamlit
- Git
- GitHub

---

# 📁 Project Structure

```text
AutoPartsQA/

├── analysis/
│   ├── cleaning.py
│   ├── quality.py
│   ├── ai_duplicates.py
│   └── __init__.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── __init__.py
│   ├── connect.py
│   ├── load_raw_data.py
│   ├── load_latest_cleaned_data.py
│   ├── save_cleaned_data.py
│   ├── create_tables.sql
│   └── insert_sample_data.sql
│
├── utils/
│   ├── brand_cleaner.py
│   └── category_detector.py
│
├── sql/
│   ├── schema.sql
│   └── validation_queries.sql
│
├── data/
│   └── parts.csv
│
├── images/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/sriarani16/AutoPartsQA.git
cd AutoPartsQA
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

## Create the PostgreSQL Database

```sql
CREATE DATABASE autopartsqa;
```

## Run the Database Schema

```bash
psql -d autopartsqa -f sql/schema.sql
```

## Insert Sample Data

```bash
psql -d autopartsqa -f database/insert_sample_data.sql
```

---

# ▶ Running the Dashboard

```bash
streamlit run dashboard/app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

# 📊 Dashboard Preview

Add your dashboard screenshots inside the **images/** folder.

```markdown
![Dashboard Overview](images/dashboard.png)
```

Example screenshots you can include:

- Dashboard Home
- Data Quality Score
- Brand Distribution
- Category Analysis
- AI Duplicate Detection
- Raw Data Explorer

---

# 📈 Data Quality Metrics

The platform automatically evaluates:

- Overall Data Quality Score
- Missing Value Percentage
- Duplicate Records
- Invalid Price Count
- Brand Consistency
- Category Completeness
- AI Similarity Matches

---

# 🚀 Future Enhancements

- CSV Upload Interface
- Automated Cleaning Recommendations
- REST API Integration
- Docker Deployment
- AWS EC2 + RDS Hosting
- Scheduled Quality Monitoring
- Historical Trend Analysis
- User Authentication
- Export Cleaned Datasets
- Power BI Integration

---

# 🎓 Learning Outcomes

This project demonstrates practical experience in:

- Data Quality Engineering
- Data Cleaning Pipelines
- SQL & PostgreSQL
- Python Programming
- SQLAlchemy ORM
- Streamlit Dashboard Development
- AI-Based Duplicate Detection
- Data Analytics
- Business Intelligence
- Versioned Data Storage

---

# 👤 Author

**Sriarani Surenther**

📍 Hamilton, New Zealand

- GitHub: https://github.com/sriarani16
- LinkedIn: https://www.linkedin.com/in/sriarani-surenther

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for educational and commercial purposes.

---

⭐ If you found this project useful, consider giving it a **star** on GitHub.
