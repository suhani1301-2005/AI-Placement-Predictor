import streamlit as st
from utils.mentor import get_response
from utils.auth import check_login
from utils.sidebar import show_sidebar


check_login()
show_sidebar()

st.title("🤖 AI Career Mentor")
st.caption("Ask me anything about placements, DSA, SQL, resume or interviews.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """👋 Hello! I'm your AI Career Mentor.

I can help you with:

• Placement Preparation
• DSA Roadmap
• SQL Preparation
• Resume Tips
• Interview Preparation
• Project Ideas

Ask me anything! 🚀"""
        }
    ]

# Display previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_question = st.chat_input("Ask your placement-related question...")

if user_question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    # Generate AI response
    response = get_response(user_question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

