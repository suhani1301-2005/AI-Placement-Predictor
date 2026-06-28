import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
from utils.auth import check_login
from utils.sidebar import show_sidebar

check_login()
show_sidebar()

st.markdown("""
<style>

/* ---------- Main Background ---------- */

.stApp{
    background-color:#F5F7FB;
}

/* ---------- Metric Cards ---------- */

[data-testid="stMetric"]{
    background:white;
    padding:18px;
    border-radius:15px;
    border:1px solid #E6EAF2;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    text-align:center;
    transition:0.3s;
}

[data-testid="stMetric"]:hover{
    transform:translateY(-4px);
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}

/* ---------- Charts ---------- */

.plot-container{
    background:white;
    border-radius:15px;
}

/* ---------- Dataframe ---------- */

[data-testid="stDataFrame"]{
    background:white;
    border-radius:12px;
    overflow:hidden;
    border:1px solid #E5E7EB;
}

/* ---------- Buttons ---------- */

.stButton>button{

    background:#2563EB;
    color:white;

    border:none;

    border-radius:10px;

    padding:10px 20px;

    font-weight:600;

    transition:0.3s;
}

.stButton>button:hover{

    background:#1D4ED8;

}

/* ---------- Download Button ---------- */

.stDownloadButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:bold;

    width:100%;

    padding:12px;
}

/* ---------- Divider ---------- */

hr{
    margin-top:25px;
    margin-bottom:25px;
}

/* ---------- Headings ---------- */

h1{

    color:#1E293B;

    font-weight:700;
}

h2{

    color:#2563EB;

    font-weight:700;
}

h3{

    color:#334155;
}



</style>
""", unsafe_allow_html=True)

from utils.database import fetch_predictions

# Original dataset (used for training)
dataset_df = pd.read_csv("Placement_Data_Full_Class.csv")

# Live user predictions from MySQL
live_df = fetch_predictions()

current_time = datetime.now()

header1, header2 = st.columns([5,1])

with header1:
    st.title("📊 AI Placement Analytics Dashboard")
    st.caption("Historical Dataset Analysis & Live Prediction Monitoring")

with header2:
    st.caption(current_time.strftime("%d %b %Y"))
    st.caption(current_time.strftime("%I:%M %p"))

    if st.button("🔄 Refresh"):
        st.rerun()
st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="👨‍🎓 Total Students",
    value=215,
    delta="Dataset Records"
)

col2.metric(
    label="🎯 Model Accuracy",
    value="88.37%",
    delta="Logistic Regression"
)

col3.metric(
    label="🤖 ML Models Used",
    value="3",
    delta="Trained Algor" \
    "ithms"
)

col4.metric(
    label="📚 Features Used",
    value="14",
    delta="Input Features"
)

st.divider()
st.header("📊 Historical Dataset Analysis")
st.caption(
    "Analyze the original placement dataset used to train the machine learning model."
)
st.divider()
col1, col2 = st.columns(2)


# -----------------------------
# Placement Distribution
# -----------------------------

with col1:

    with st.container(border=True):

        st.subheader("🥧 Placement Distribution")

        placement_count = dataset_df["status"].value_counts()

        fig = px.pie(
            names=placement_count.index,
            values=placement_count.values,
            hole=0.45,
            color_discrete_sequence=["#2563EB", "#60A5FA"]
        )

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="white",
            plot_bgcolor="white"
        )

        st.plotly_chart(fig, use_container_width=True)
# -----------------------------
# Gender Distribution
# -----------------------------

with col2:

    with st.container(border=True):

        st.subheader("👨 Gender Distribution")

        gender_count = dataset_df["gender"].value_counts()

        fig = px.bar(
            x=gender_count.index,
            y=gender_count.values,
            color=gender_count.index,
            text=gender_count.values,
            labels={
                "x": "Gender",
                "y": "Students"
            },
            color_discrete_sequence=["#2563EB", "#EC4899"]
        )

        fig.update_traces(
            textposition="outside",
            marker_line_width=0
        )

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis_title=None,
            yaxis_title="Students",
            font=dict(size=13)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
st.divider()



col1, col2 = st.columns(2)

#WORK Experience
with col1:

    with st.container(border=True):

        st.subheader("💼 Work Experience Analysis")

        work_count = dataset_df["workex"].value_counts()

        fig = px.bar(
            x=work_count.index,
            y=work_count.values,
            color=work_count.index,
            text=work_count.values,
            labels={
                "x": "Work Experience",
                "y": "Students"
            },
            color_discrete_sequence=["#22C55E", "#F59E0B"]
        )

        fig.update_traces(
            textposition="outside",
            marker_line_width=0
        )

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis_title=None,
            yaxis_title="Students",
            font=dict(size=13)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
#DEgree Percentage

with col2:

    with st.container(border=True):

        st.subheader("📚 Degree Percentage Distribution")

        fig = px.histogram(
            dataset_df,
            x="degree_p",
            nbins=12,
            color_discrete_sequence=["#3B82F6"]
        )

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis_title="Degree Percentage",
            yaxis_title="Students",
            font=dict(size=13)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col1:

    with st.container(border=True):

        st.subheader("🔥 Correlation Heatmap")

        numeric_df = dataset_df.select_dtypes(include=["number"])

        fig, ax = plt.subplots(figsize=(6, 4))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            fmt=".2f",
            cmap="Blues",
            linewidths=0.5,
            square=True,
            cbar=True,
            annot_kws={"size":9},
            ax=ax
        )

        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation=45,
            ha="right",
            fontsize=9
        )

        ax.set_yticklabels(
            ax.get_yticklabels(),
            fontsize=9
        )

        plt.tight_layout()

        st.pyplot(fig, use_container_width=True)
with col2:

    with st.container(border=True):

        st.subheader("🔥 Top Features")

        feature_importance = pd.DataFrame(
            {
                "Feature": [
                    "Degree %",
                    "Employability Test",
                    "MBA %",
                    "Work Experience",
                    "HSC %"
                ],
                "Importance": [
                    95,
                    91,
                    84,
                    76,
                    68
                ]
            }
        )

        fig = px.bar(
            feature_importance,
            x="Importance",
            y="Feature",
            orientation="h",
            color="Importance",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="white",
            plot_bgcolor="white",
            coloraxis_showscale=False,
            xaxis_title="Importance Score",
            yaxis_title=""
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
st.header("📌 Key Insights")

st.info("📊 Nearly 69% of students in the dataset were placed.")

st.success("🎯 Degree percentage and Employability Test have a strong impact on placement.")

st.warning("💼 Students with work experience generally have better placement chances.")

st.info("🤖 Logistic Regression achieved an accuracy of 88.37%.")

st.divider()

st.markdown("""
# 📊 Live User Analytics
""")

st.caption(
    "Real-time prediction records stored in the MySQL database."
)

st.success("🟢 Live Analysis")

# ---------------------------------
# Live Metrics
# ---------------------------------

total_predictions = len(live_df)

placed = len(
    live_df[live_df["prediction"] == "Placed"]
)

not_placed = len(
    live_df[live_df["prediction"] == "Not Placed"]
)

avg_probability = live_df["probability"].mean() * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👥 Total Predictions",
    total_predictions,
    "Live Records"
)

col2.metric(
    "🟢 Placed",
    placed,
    f"{placed/total_predictions*100:.1f}%" if total_predictions else "0%"
)

col3.metric(
    "🔴 Not Placed",
    not_placed,
    f"{not_placed/total_predictions*100:.1f}%" if total_predictions else "0%"
)

col4.metric(
    "📈 Avg Probability",
    f"{avg_probability:.2f}%"
)


st.divider()

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("🥧 Live Placement Distribution")

        placement_count = live_df["prediction"].value_counts()

        fig = px.pie(
            names=placement_count.index,
            values=placement_count.values,
            hole=0.45,
            color_discrete_sequence=["#2563EB", "#EF4444"]
        )

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="white",
            plot_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:

    with st.container(border=True):

        st.subheader("👨 Live Gender Distribution")

        gender_count = live_df["gender"].value_counts()

        fig = px.bar(
            x=gender_count.index,
            y=gender_count.values,
            color=gender_count.index,
            text=gender_count.values,
            color_discrete_sequence=["#2563EB", "#EC4899"]
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis_title=None,
            yaxis_title="Users"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

col1, col2 = st.columns(2)

# -------------------------
# Prediction Trend
# -------------------------

with col1:

    st.subheader("📈 Prediction Trend")

    live_df["created_at"] = pd.to_datetime(live_df["created_at"])

    trend = (
        live_df
        .groupby(live_df["created_at"].dt.strftime("%d-%b %H:%M"))
        .size()
        .reset_index(name="Predictions")
    )

    fig = px.line(
        trend,
        x="created_at",
        y="Predictions",
        markers=True,
        color_discrete_sequence=["#2563EB"]
    )

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------------
# Live Work Experience
# -------------------------

with col2:

    st.subheader("💼 Live Work Experience")

    work = live_df["workex"].value_counts()

    fig = px.bar(
        x=work.index,
        y=work.values,
        text=work.values,
        color=work.index,
        color_discrete_sequence=["#22C55E", "#F59E0B"]
    )

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor="white",
        paper_bgcolor="white",
        showlegend=False,
        xaxis_title="Work Experience",
        yaxis_title="Users"
    )

    st.plotly_chart(fig, use_container_width=True)


st.divider()

with st.container(border=True):

    st.subheader("📋 Recent User Predictions")

display_df = live_df[[
    "gender",
    "ssc_p",
    "degree_p",
    "workex",
    "prediction",
    "probability",
    "created_at"
]].copy()

display_df["probability"] = (
    display_df["probability"] * 100
).round(2).astype(str) + "%"

display_df.rename(
    columns={
        "gender": "Gender",
        "ssc_p": "SSC %",
        "degree_p": "Degree %",
        "workex": "Work Experience",
        "prediction": "Prediction",
        "probability": "Probability (%)",
        "created_at": "Prediction Time"
    },
    inplace=True
)

display_df["Prediction"] = display_df["Prediction"].replace({
    "Placed": "🟢 Placed",
    "Not Placed": "🔴 Not Placed"
})

display_df = display_df.sort_values(
    by="Prediction Time",
    ascending=False
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

st.subheader("📥 Export Prediction History")

csv = display_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Prediction History",
    data=csv,
    file_name="prediction_history.csv",
    mime="text/csv",
    use_container_width=True
)