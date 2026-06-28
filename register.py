import streamlit as st
from utils.database import register_user, email_exists

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="wide"
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main{
    background:#F8FAFC;
}

h1{
    color:#1E3A8A;
    font-weight:700;
}

.stButton>button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:17px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8;
    color:white;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("Create Your Account")

st.caption("Join the AI Placement Predictor Platform")

st.write("")

left, center, right = st.columns([1,2,1])

# ---------------------------------------------------
# REGISTER FORM
# ---------------------------------------------------

with center:

    st.subheader("👤 Register Account")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email Address"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    st.write("")

    c1, c2, c3 = st.columns([1,2,1])

    with c2:

        register = st.button(
            "🚀 Create Account",
            use_container_width=True
        )

    if register:

        if (
            name == ""
            or email == ""
            or password == ""
            or confirm_password == ""
        ):

            st.error("Please fill all the fields.")

        elif password != confirm_password:

            st.error("Passwords do not match.")

        elif email_exists(email):

            st.warning("Email already registered.")

        else:

            register_user(
                name,
                email,
                password
            )

            st.success("🎉 Registration Successful!")

            st.info("You can now login to your account.")

st.write("")

# ---------------------------------------------------
# LOGIN SECTION
# ---------------------------------------------------

st.write("")

col1, col2 = st.columns([5,1])

with col1:
    st.markdown(
        """
        <div style="padding-top:12px;">
        <span style="font-size:18px;font-weight:600;">
        Already have an account?
        </span>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    if st.button("Login", use_container_width=True):
        st.switch_page("pages/5_Login.py")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.write("")

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;font-size:14px;'>

<b>Developed by Suhani Saxena</b><br>

AI Placement Predictor • Machine Learning • Streamlit • MySQL

</div>
""",
unsafe_allow_html=True
)