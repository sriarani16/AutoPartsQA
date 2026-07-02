import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from analysis.cleaning import clean_data

# Path setup
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

import streamlit as st
import pandas as pd
import plotly.express as px

from database.save_cleaned_data import save_cleaned_data

from utils.brand_cleaner import clean_brand
from utils.category_detector import apply_category_detection


# Cached CSV loader
@st.cache_data
def load_data():
    return pd.read_csv("data/parts.csv")

# Streamlit config
st.set_page_config(page_title="AutoPartsQA Dashboard", layout="wide")

st.title("🚗 AutoPartsQA – Automotive Data Quality Dashboard")
st.write("An interactive dashboard for analyzing automotive parts data quality.")

# ---------------------------------------------------------
# Sidebar (ONLY ONCE)
# ---------------------------------------------------------

uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"], key="upload_csv_main")

use_db = st.sidebar.checkbox("Use PostgreSQL Database (RAW)", key="use_db_raw")
use_cleaned_db = st.sidebar.checkbox("Load Cleaned Data from PostgreSQL", key="use_db_cleaned")

# Prevent conflict
if use_db and use_cleaned_db:
    st.sidebar.error("Choose only ONE: RAW data OR CLEANED data")
    st.stop()

apply_brand_correction = st.sidebar.checkbox("Apply Brand Correction", value=True)
enable_category_detection = st.sidebar.checkbox("Apply Category Detection", value=True)

page = st.sidebar.radio(
    "Navigation",
    [
        "Summary",
        "Data Quality Score",
        "Missing Values",
        "Duplicate Records",
        "Invalid Prices",
        "Brand Distribution",
        "Category Statistics",
        "AI Duplicate Detection",
        "Raw Data Explorer",
    ],
)

# ---------------------------------------------------------
# Load data (CSV → CLEANED DB → RAW DB → fallback CSV)
# ---------------------------------------------------------

if uploaded_file:
    raw_df = pd.read_csv(uploaded_file)
    st.sidebar.success("Loaded uploaded CSV")

elif use_cleaned_db:
    from database.load_latest_cleaned_data import load_latest_cleaned_data
    raw_df = load_latest_cleaned_data()

    if raw_df is None:
        st.sidebar.error("No cleaned tables found in PostgreSQL")
        st.stop()

    st.sidebar.success("Loaded CLEANED data from PostgreSQL")

elif use_db:
    from database.load_raw_data import load_raw_data
    raw_df = load_raw_data()
    st.sidebar.success("Loaded RAW data from PostgreSQL")

else:
    raw_df = load_data()
    st.sidebar.info("Loaded default parts.csv")

# ---------------------------------------------------------
# Apply cleaning to a copy
# ---------------------------------------------------------

df = clean_data(raw_df)

if apply_brand_correction:
    df = clean_brand(df)

if enable_category_detection:
    df = apply_category_detection(df)

# ---------------------------------------------------------
# Data Quality Score
# ---------------------------------------------------------

def calculate_quality_score(df: pd.DataFrame) -> float:
    total_rows = len(df)
    total_cells = total_rows * len(df.columns)

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    invalid_prices = (df["price"] <= 0).sum()

    score = 100.0
    score -= (missing / total_cells) * 40
    score -= (duplicates / total_rows) * 30
    score -= (invalid_prices / total_rows) * 30

    return round(score, 2)

quality_score = calculate_quality_score(df)

# ---------------------------------------------------------
# Pages
# ---------------------------------------------------------

if page == "Summary":
    st.header("📊 Dataset Summary")
    st.write(f"Total Records: **{len(df)}**")
    st.write(f"Total Columns: **{len(df.columns)}**")
    st.subheader("Preview")
    st.dataframe(df.head())

elif page == "Data Quality Score":
    st.header("📈 Data Quality Score")
    st.metric("Overall Score", f"{quality_score} %")

elif page == "Missing Values":
    st.header("❗ Missing Values Analysis")
    missing_df = df.isnull().sum().reset_index()
    missing_df.columns = ["column", "missing_count"]
    fig = px.bar(missing_df, x="column", y="missing_count", title="Missing Values by Column", color="missing_count")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(missing_df)

elif page == "Duplicate Records":
    st.header("🔁 Duplicate Records")
    duplicates = raw_df[raw_df.duplicated()]
    st.write(f"Total Duplicates: **{len(duplicates)}**")
    st.dataframe(duplicates)

elif page == "Invalid Prices":
    st.header("💸 Invalid Price Detection")
    invalid_df = raw_df[pd.to_numeric(raw_df["price"], errors="coerce") <= 0]
    st.write(f"Invalid Price Records: **{len(invalid_df)}**")
    st.dataframe(invalid_df)

elif page == "Brand Distribution":
    st.header("🏭 Brand Distribution")
    brand_df = df["manufacturer"].value_counts().reset_index()
    brand_df.columns = ["manufacturer", "count"]
    fig = px.pie(brand_df, names="manufacturer", values="count", title="Brand Distribution")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(brand_df)

elif page == "Category Statistics":
    st.header("📦 Category Statistics")
    category_df = df["category"].value_counts().reset_index()
    category_df.columns = ["category", "count"]
    fig = px.bar(category_df, x="category", y="count", title="Category Distribution", color="count")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(category_df)

elif page == "AI Duplicate Detection":
    st.header("🧠 AI Duplicate Detection")
    from analysis.ai_duplicates import ai_duplicate_detection
    ai_df = ai_duplicate_detection(df)
    st.write(f"AI‑detected similar parts: **{len(ai_df)}**")
    st.dataframe(ai_df)

elif page == "Raw Data Explorer":
    st.header("📄 Raw Data Explorer")
    st.dataframe(df)

    st.write("### Save cleaned data to PostgreSQL")

# ---------------------------------------------------------
# Save cleaned data (versioned tables)
# ---------------------------------------------------------

if st.button("Save Cleaned Data"):
    from database.save_cleaned_data import save_cleaned_data
    table_name = save_cleaned_data(df)
    st.success(f"Cleaned data saved to PostgreSQL table: {table_name}")
