import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Placement_Data_Full_Class.csv")
st.title("📊 Analytics Dashboard")
st.caption("Explore the dataset and understand the Machine Learning model.")

st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Students",
    215
)

col2.metric(
    "Accuracy",
    "88.37%"
)

col3.metric(
    "Models",
    "3"
)

col4.metric(
    "Features",
    "14"
)

st.divider()
col1, col2 = st.columns(2)

# -----------------------------
# Placement Distribution
# -----------------------------

with col1:

    st.subheader("🥧 Placement Distribution")

    placement_count = df["status"].value_counts()

    fig, ax = plt.subplots(figsize=(4,4))

    ax.pie(
        placement_count,
        labels=placement_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

# -----------------------------
# Gender Distribution
# -----------------------------

with col2:

    st.subheader("👨 Gender Distribution")

    gender_count = df["gender"].value_counts()

    fig, ax = plt.subplots(figsize=(4,4))

    ax.bar(
        gender_count.index,
        gender_count.values,
        color=["#FF9800", "#9C27B0"]
    )

    for i, v in enumerate(gender_count.values):
        ax.text(i, v + 2, str(v), ha="center", fontsize=11)

    ax.set_xlabel("Gender")
    ax.set_ylabel("Students")

    plt.tight_layout()

    st.pyplot(fig)

st.divider()



col1, col2 = st.columns(2)

with col1:

    st.subheader("💼 Work Experience")

    work_count = df["workex"].value_counts()

    fig, ax = plt.subplots(figsize=(4,4))

    ax.bar(
        work_count.index,
        work_count.values
    )

    for i, v in enumerate(work_count.values):
        ax.text(i, v + 2, str(v), ha="center", fontsize=11)

    ax.set_xlabel("Work Experience")
    ax.set_ylabel("Students")

    plt.tight_layout()

    st.pyplot(fig)

with col2:

    st.subheader("📚 Degree Percentage")

    fig, ax = plt.subplots(figsize=(4,4))

    ax.hist(
        df["degree_p"],
        bins=10
    )

    ax.set_xlabel("Degree %")
    ax.set_ylabel("Students")

    plt.tight_layout()

    st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:

    st.subheader("💰 Salary Distribution")

    salary = df["salary"].dropna()

    fig, ax = plt.subplots(figsize=(4,4))

    ax.hist(
        salary,
        bins=10,
        color="#4CAF50"
    )

    ax.set_xlabel("Salary")
    ax.set_ylabel("Students")

    plt.tight_layout()

    st.pyplot(fig)

with col2:

    st.subheader("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=["number"])

    fig, ax = plt.subplots(figsize=(6,5))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="Blues",
        ax=ax
    )

    plt.tight_layout()

    st.pyplot(fig)
st.header("📌 Key Insights")

st.info("📊 Nearly 69% of students in the dataset were placed.")

st.success("🎯 Degree percentage and Employability Test have a strong impact on placement.")

st.warning("💼 Students with work experience generally have better placement chances.")

st.info("🤖 Logistic Regression achieved an accuracy of 88.37%.")

