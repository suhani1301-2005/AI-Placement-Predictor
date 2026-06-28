import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.markdown("---")

        st.success("👤 Logged In")

        st.write(f"**{st.session_state.user_name}**")

        st.caption(st.session_state.user_email)

        st.markdown("---")

        if st.button("🚪 Logout", use_container_width=True):

            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.user_email = ""

            st.switch_page("pages/5_Login.py")