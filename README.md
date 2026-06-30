# 📘 AutoPartsQA — Data Quality Analysis Platform

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

AutoPartsQA is a **Python and Streamlit-based data quality analysis platform** designed to identify, analyze, and visualize data quality issues in automotive parts datasets.

The application performs automated validation checks, calculates an overall data quality score, and presents interactive visualizations to help identify data issues before they affect downstream analytics or machine learning workflows.

This project demonstrates practical experience with **Python, Pandas, SQL-ready data validation, dashboard development, and data quality engineering**, making it highly relevant for Data Science, Data Analytics, and Data Engineering roles.

---

# 🚀 Features

## 🔍 Automated Data Quality Checks

The platform automatically detects:

- Missing manufacturer/brand names
- Missing vehicle models
- Missing part names
- Invalid or non-numeric prices
- Duplicate records
- Inconsistent manufacturer naming
- Overall dataset completeness

---

## 📊 Interactive Dashboard

Built using **Streamlit**, the dashboard provides:

- Dataset summary
- Data quality score
- Missing value statistics
- Duplicate record analysis
- Top manufacturers
- Error distribution charts
- Interactive data explorer

---

## 📈 Data Quality Score

The application automatically calculates an overall **Data Quality Score** based on detected issues, providing a quick assessment of dataset health.

Example metrics include:

- Dataset Completeness
- Duplicate Percentage
- Invalid Price Count
- Missing Manufacturer Count
- Missing Vehicle Models

---

# 🧠 Project Architecture

```
AutoPartsQA/
│
├── analysis/
│   ├── cleaning.py
│   ├── quality.py
│   └── __init__.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── parts.csv
│
├── sql/
│   └── (future SQL validation scripts)
│
├── images/
│   └── dashboard.png
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Technology Stack

- Python 3.9+
- Pandas
- NumPy
- Streamlit
- Plotly
- Git & GitHub

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/sriarani16/AutoPartsQA.git

cd AutoPartsQA
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

The application will open at:

```
http://localhost:8501
```

---

# 📊 Example Dashboard

> Add a screenshot after running the application.

```markdown
![Dashboard](images/dashboard.png)
```

Example dashboard sections:

- Data Quality Score
- Missing Value Analysis
- Duplicate Detection
- Invalid Price Detection
- Manufacturer Statistics
- Interactive Charts
- Raw Dataset Viewer

---

# 📂 Sample Dataset

The included sample dataset contains automotive parts information such as:

| Column | Description |
|----------|-------------|
| Part ID | Unique part identifier |
| Part Name | Name of the replacement part |
| Brand | Manufacturer |
| Vehicle Model | Supported vehicle |
| Price | Selling price |
| Category | Part category |

The dataset intentionally includes quality issues to demonstrate the platform's validation capabilities.

---

# 🔍 Data Validation Rules

Current validation checks include:

- Missing values
- Duplicate records
- Invalid prices
- Empty fields
- Inconsistent manufacturer names
- Dataset completeness

Future versions will include:

- Foreign key validation
- Referential integrity checks
- Schema validation
- Business rule validation

---

# 📈 Example Analysis

The dashboard helps answer questions such as:

- How many duplicate records exist?
- Which manufacturers have the most missing information?
- What percentage of prices are invalid?
- Which vehicle models contain incomplete records?
- What is the current overall data quality score?

---

# 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

Steps:

1. Push the repository to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new application.
4. Select:

```
dashboard/app.py
```

5. Deploy.

---
## 🌐 Live Demo
Your app is live here:

👉 [https://autopartsqa.streamlit.app](https://autopartsqa-xxxxx.streamlit.app
)


# 🔮 Future Enhancements

Planned improvements include:

- CSV file upload
- SQL validation rules
- AI-assisted manufacturer name correction
- Data cleaning recommendations
- Export cleaned datasets
- Historical quality tracking
- REST API for automated quality scoring
- Unit testing
- Docker deployment
- Cloud deployment (AWS)

---

# 🎯 Project Goals

This project was developed to:

- Practice real-world data quality engineering
- Build interactive analytical dashboards
- Improve Python and Pandas skills
- Demonstrate practical data validation techniques
- Showcase portfolio-ready software development
- Simulate enterprise data quality workflows used in industry

---

# 👨‍💻 Author

**Sriarani Surenther**

📍 Hamilton, New Zealand

GitHub:
https://github.com/sriarani16

LinkedIn:
https://www.linkedin.com/in/sriarani-surenther

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star!
