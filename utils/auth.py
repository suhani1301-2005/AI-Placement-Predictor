import streamlit as st


def check_login():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:

        st.warning("🔒 Please login to continue.")

        st.switch_page("pages/5_Login.py")