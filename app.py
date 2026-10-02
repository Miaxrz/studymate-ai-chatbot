import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# ==========================================
# 1. Load API key
# ==========================================

load_dotenv()

if "OPENROUTER_API_KEY" in st.secrets:
    api_key = st.secrets["OPENROUTER_API_KEY"]
else:
    api_key = os.getenv("OPENROUTER_API_KEY")


# ==========================================
# 2. Check API key
# ==========================================

if not api_key:
    st.error("OpenRouter API key was not found.")
    st.stop()


# ==========================================
# 3. Create OpenRouter client
# ==========================================

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


# ==========================================
# 4. Page configuration
# ==========================================

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="centered"
)


# ==========================================
# 5. Application title
# ==========================================

st.title("StudyMate AI")

st.write(
    "Your AI-powered educational tutor"
)


# ==========================================
# 6. Sidebar
# ==========================================

with st.sidebar:

    st.header("About StudyMate AI")

    st.write(
        """
        StudyMate AI is an educational chatbot
        designed to help students understand
        academic and technical concepts.
        """
    )

    st.write("### Features")

    st.write(
        """
        - Academic explanations
        - Simple examples
        - Follow-up questions
        - Conversation history
        - Step-by-step explanations
        """
    )

    if st.button("Clear Conversation"):

        st.session_state.messages = []

        st.rerun()


# ==========================================
# 7. Create conversation history
# ==========================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==========================================
# 8. Display previous messages
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ==========================================
# 9. Get user input
# ==========================================

prompt = st.chat_input(
    "Ask me a question..."
)


# ==========================================
# 10. Process user question
# ==========================================

if prompt:

    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Display user message

    with st.chat_message("user"):

        st.write(prompt)


    # ======================================
    # 11. System instructions
    # ======================================

    system_instruction = """
    You are StudyMate AI, an educational tutor.

    Your purpose is to help students understand
    academic and technical concepts.

    Follow these rules:

    1. Explain concepts using simple and clear language.
    2. Provide examples when useful.
    3. Break difficult topics into smaller steps.
    4. Avoid unnecessary technical jargon.
    5. Use previous conversation context when answering
       follow-up questions.
    6. Give accurate and relevant answers.
    7. If you are uncertain about something, say so
       instead of making up information.
    8. Keep answers focused on the student's question.
    """


    # ======================================
    # 12. Prepare messages for AI
    # ======================================

    messages = [
        {
            "role": "system",
            "content": system_instruction
        }
    ]


    messages.extend(
        st.session_state.messages
    )


    # ======================================
    # 13. Generate AI response
    # ======================================

    try:

        with st.spinner("StudyMate AI is thinking..."):

            response = client.chat.completions.create(

                model="openrouter/free",

                messages=messages
            )


        # Get generated response

        answer = response.choices[0].message.content


        # ==================================
        # 14. Save AI response
        # ==================================

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        # ==================================
        # 15. Display AI response
        # ==================================

        with st.chat_message("assistant"):

            st.write(answer)


    except Exception as e:

        st.error(
            "Sorry, I was unable to generate a response. "
            "Please try again."
        )

        st.write(f"Error details: {e}")
