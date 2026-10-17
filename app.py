import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Coffee Sales Analytics",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Coffee Sales Analytics Dashboard")
st.write(
    "Explore coffee sales data, product performance, "
    "and business insights."
)

st.header("Project Overview")

col1, col2 = st.columns(2)
col1.metric("Analysis Tools", "Python & Pandas")
col2.metric("Visualization Tool", "Power BI")

st.header("Project Files")

files = [
    "Coffee_Sales_Analysis_Results.xlsx",
    "product_analysis.xlsx"
]

available_files = [f for f in files if Path(f).exists()]

if not available_files:
    st.warning("No Excel result files were found.")
else:
    selected_file = st.selectbox(
        "Choose an analysis file",
        available_files
    )

    sheets = pd.read_excel(
        selected_file,
        sheet_name=None
    )

    selected_sheet = st.selectbox(
        "Choose a worksheet",
        list(sheets.keys())
    )

    df = sheets[selected_sheet]

    st.subheader("Data Preview")
    st.dataframe(df, use_container_width=True)

    st.write("Rows:", len(df))
    st.write("Columns:", len(df.columns))

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_cols:
        st.subheader("Explore a Numeric Column")
        column = st.selectbox(
            "Select a column",
            numeric_cols
        )
        st.bar_chart(df[column].dropna())

    st.download_button(
        "Download Excel File",
        data=Path(selected_file).read_bytes(),
        file_name=selected_file,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

st.header("Project Objective")
st.write(
    "Analyze coffee sales data to understand product "
    "performance and support better business decisions."
)

st.caption("Created as a Coffee Sales Analytics project.")
