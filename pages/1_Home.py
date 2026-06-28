import streamlit as st
from utils.auth import check_login
from utils.sidebar import show_sidebar

check_login()
show_sidebar()
st.set_page_config(
    page_title="AI Placement Mentor",
    page_icon="🎓",
    layout="wide"
)



# ---------------- HEADER ----------------

st.title("🎓 AI Placement Mentor")
st.success(f"👋 Welcome back, {st.session_state.user_name}!")

st.subheader("AI Powered Placement Prediction & Career Guidance")

st.write(
    """
Predict a student's placement chances using Machine Learning
and receive personalized career recommendations.
"""
)

st.divider()

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model Accuracy",
        "88.37%"
    )

with col2:
    st.metric(
        "Students Analysed",
        "215"
    )

with col3:
    st.metric(
        "ML Models",
        "3"
    )

st.divider()

# ---------------- FEATURES ----------------

st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Placement Prediction")
    st.success("✅ AI Career Recommendations")
    st.success("✅ Placement Probability")

with col2:
    st.info("📊 Dashboard")
    st.info("🤖 Machine Learning")
    st.info("📈 Data Analysis")

st.divider()

st.info("🚀 Click 'Prediction' in the sidebar to predict placement.")

