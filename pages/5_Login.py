import streamlit as st
from utils.database import login_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="wide"
)

# ---------------- CSS ----------------

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

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------

st.title("🔐 Welcome Back")

st.caption("Login to AI Placement Predictor")

st.write("")

left, center, right = st.columns([1,2,1])

with center:

    email = st.text_input("Email Address")

    password = st.text_input(
        "Password",
        type="password"
    )

    remember = st.checkbox("Remember Me")

    st.write("")

    c1, c2, c3 = st.columns([1,2,1])

    with c2:

        login = st.button(
            "🔑 Login",
            use_container_width=True
        )

    if login:

        if email == "" or password == "":

            st.error("Please enter Email and Password.")

        else:

            user = login_user(
                email,
                password
            )
            

            if user:

                st.session_state.logged_in = True
                st.session_state.user_name = user["name"]
                st.session_state.user_email = user["email"]

                st.success("Login Successful 🎉")

                st.switch_page("pages/1_Home.py")

            else:

                st.error("Invalid Email or Password.")

st.write("")
st.markdown("---")

col1, col2 = st.columns([4,1])

with col1:
    st.markdown("### Don't have an account?")

with col2:
    if st.button("Register", use_container_width=True):
        st.switch_page("register.py")

st.write("")
st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;'>

<b>Developed by Suhani Saxena</b><br>

AI Placement Predictor • Machine Learning • Streamlit • MySQL

</div>
""",
unsafe_allow_html=True
)