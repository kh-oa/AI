import streamlit as st
import pandas as pd

df = pd.read_csv("drug200.csv")

st.title("Thông tin thuốc")

st.subheader("📋 Bảng dữ liệu gốc")
st.dataframe(df)

st.sidebar.header("🔍 Bộ lọc dữ liệu")

age_filter = st.sidebar.slider("Chọn độ tuổi", int(df["Age"].min()), int(df["Age"].max()), (30, 50))
sex_filter = st.sidebar.selectbox("Giới tính", ["All"] + sorted(df["Sex"].unique()))
bp_filter = st.sidebar.selectbox("Huyết áp (BP)", ["All"] + sorted(df["BP"].unique()))
chol_filter = st.sidebar.selectbox("Cholesterol", ["All"] + sorted(df["Cholesterol"].unique()))

filtered_df = df[
    (df["Age"] >= age_filter[0]) &
    (df["Age"] <= age_filter[1])
]

if sex_filter != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == sex_filter]

if bp_filter != "All":
    filtered_df = filtered_df[filtered_df["BP"] == bp_filter]

if chol_filter != "All":
    filtered_df = filtered_df[filtered_df["Cholesterol"] == chol_filter]

st.subheader("📊 Dữ liệu sau khi lọc")
st.dataframe(filtered_df)

st.subheader("📈 Biểu đồ số lượng thuốc theo loại")
st.bar_chart(filtered_df["Drug"].value_counts())
