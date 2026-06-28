import streamlit as st

from utils.preprocessing import preprocess
from utils.model_utils import predict
from utils.database import save_prediction
from utils.auth import check_login
from utils.sidebar import show_sidebar

check_login()
show_sidebar()
# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------
# HEADER
# ---------------------------------------

st.title("🎯 AI Placement Predictor")

st.markdown(
    """
Predict your placement chances using Machine Learning and
receive personalized career recommendations.
"""
)

st.divider()

# ---------------------------------------
# ACADEMIC INFORMATION
# ---------------------------------------

st.subheader("📚 Academic Information")

col1, col2 = st.columns(2)

with col1:

    ssc = st.number_input(
        "SSC Percentage",
        min_value=0.0,
        max_value=100.0
    )

    degree = st.number_input(
        "Degree Percentage",
        min_value=0.0,
        max_value=100.0
    )

    mba = st.number_input(
        "MBA Percentage",
        min_value=0.0,
        max_value=100.0
    )

with col2:

    hsc = st.number_input(
        "HSC Percentage",
        min_value=0.0,
        max_value=100.0
    )

    etest = st.number_input(
        "Employability Test",
        min_value=0.0,
        max_value=100.0
    )

st.divider()

# ---------------------------------------
# PERSONAL INFORMATION
# ---------------------------------------

st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:

    workex = st.selectbox(
        "Work Experience",
        ["Yes", "No"]
    )

st.divider()

# ---------------------------------------
# EDUCATION DETAILS
# ---------------------------------------

st.subheader("🎓 Education Details")

col1, col2 = st.columns(2)

with col1:

    ssc_board = st.selectbox(
        "SSC Board",
        ["Central", "Others"]
    )

    hsc_stream = st.selectbox(
        "HSC Stream",
        ["Commerce", "Science", "Arts"]
    )

    specialisation = st.selectbox(
        "Specialisation",
        ["Mkt&Fin", "Mkt&HR"]
    )

with col2:

    hsc_board = st.selectbox(
        "HSC Board",
        ["Central", "Others"]
    )

    degree_type = st.selectbox(
        "Degree Type",
        ["Sci&Tech", "Comm&Mgmt", "Others"]
    )

st.divider()

# ---------------------------------------
# BUTTON
# ---------------------------------------

col1, col2, col3 = st.columns([1,2,1])

with col2:

    predict_button = st.button(
        "🚀 Analyze My Profile",
        use_container_width=True
    )

# ---------------------------------------
# PREDICTION
# ---------------------------------------

if predict_button:

    with st.spinner("🤖 AI is analyzing your profile..."):

        input_df = preprocess(
            ssc,
            hsc,
            degree,
            etest,
            mba,
            gender,
            ssc_board,
            hsc_board,
            hsc_stream,
            degree_type,
            workex,
            specialisation
        )

        prediction, probability = predict(input_df)

        # Convert prediction to text
        if prediction == 1:
            prediction_result = "Placed"
        else:
            prediction_result = "Not Placed"

        # Probability of placement
        confidence = probability[1] * 100

        # Save into MySQL
        save_prediction(
            gender,
            ssc,
            hsc,
            degree,
            workex,
            etest,
            mba,
            prediction_result,
            confidence
        )

        st.success("Analysis Complete!")
        st.divider()

        st.header("📊 Prediction Report")

        col1, col2 = st.columns(2)

        # Prediction Result
        with col1:

            if prediction == 1:
                st.success("🎉 Student is likely to be PLACED")
            else:
                st.error("❌ Student is likely to be NOT PLACED")

        # Probability
        with col2:

            confidence = probability[1] * 100

            st.metric(
                "Placement Probability",
                f"{confidence:.2f}%"
            )

        st.progress(confidence / 100)

        st.subheader("Confidence Level")

        if confidence >= 80:
            st.success("🟢 High Confidence Prediction")

        elif confidence >= 60:
            st.warning("🟡 Medium Confidence Prediction")

        else:
            st.error("🔴 Low Confidence Prediction")

            st.divider()

        st.header("📄 Student Summary")

        summary_col1, summary_col2 = st.columns(2)

        with summary_col1:

            st.write(f"**SSC Percentage:** {ssc}")
            st.write(f"**HSC Percentage:** {hsc}")
            st.write(f"**Degree Percentage:** {degree}")
            st.write(f"**MBA Percentage:** {mba}")

        with summary_col2:

            st.write(f"**Employability Test:** {etest}")
            st.write(f"**Gender:** {gender}")
            st.write(f"**Work Experience:** {workex}")
            st.write(f"**Specialisation:** {specialisation}")


            st.divider()

            st.header("🤖 AI Career Recommendations")

            recommendations = []

            if degree < 65:
                recommendations.append("📚 Improve your graduation percentage.")

            if etest < 70:
                recommendations.append("🧠 Practice aptitude daily.")

            if mba < 60:
                recommendations.append("📖 Improve your MBA percentage.")

            if workex == "No":
                recommendations.append("💼 Try to complete at least one internship.")

            if ssc < 70:
                recommendations.append("📘 Strengthen your academic fundamentals.")

            if len(recommendations) == 0:
                recommendations.append("🚀 Excellent profile! Continue DSA and interview preparation.")

            for rec in recommendations:
                st.info(rec)

