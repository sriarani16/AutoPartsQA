import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import plotly.express as px

from analysis.quality import (
    load_data,
    detect_duplicates,
    detect_missing_brands,
    detect_missing_vehicles,
    detect_invalid_prices,
    detect_spelling_issues,
    compute_quality_score,
)

st.set_page_config(page_title="Auto Parts Data Quality Dashboard", layout="wide")

df = load_data()

st.title("Auto Parts Data Quality Dashboard")

# --- Top metrics ---
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Total Parts", len(df))

with col2:
    st.metric("Duplicate Records", len(detect_duplicates(df)))

with col3:
    st.metric("Missing Vehicle Models", len(detect_missing_vehicles(df)))

with col4:
    st.metric("Missing Brands", len(detect_missing_brands(df)))

with col5:
    st.metric("Invalid Prices", len(detect_invalid_prices(df)))

with col6:
    st.metric("Overall Data Quality", f"{compute_quality_score(df)}%")

st.markdown("---")

# --- Charts section ---
st.subheader("Charts")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Duplicate Parts", "Missing Values", "Top Manufacturers", "Most Common Errors"]
)

with tab1:
    dup = detect_duplicates(df)
    if not dup.empty:
        dup_counts = dup.groupby(["Brand", "PartName"]).size().reset_index(name="count")
        fig = px.bar(
            dup_counts,
            x="PartName",
            y="count",
            color="Brand",
            title="Duplicate Parts by Brand",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No duplicate records detected.")

with tab2:
    missing_counts = df.isnull().sum().reset_index()
    missing_counts.columns = ["column", "missing"]
    fig = px.bar(
        missing_counts,
        x="column",
        y="missing",
        title="Missing Values per Column",
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    brand_counts = df["Brand"].value_counts().reset_index()
    brand_counts.columns = ["Brand", "count"]
    fig = px.bar(
        brand_counts,
        x="Brand",
        y="count",
        title="Top Manufacturers (by parts count)",
    )
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    errors = {
        "Duplicates": len(detect_duplicates(df)),
        "Missing Brands": len(detect_missing_brands(df)),
        "Missing Vehicles": len(detect_missing_vehicles(df)),
        "Invalid Prices": len(detect_invalid_prices(df)),
        "Spelling Issues": len(detect_spelling_issues(df)),
    }
    err_df = pd.DataFrame(
        {"Error Type": list(errors.keys()), "Count": list(errors.values())}
    )
    fig = px.bar(
        err_df,
        x="Error Type",
        y="Count",
        title="Most Common Data Quality Errors",
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)
