pip install openai

import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]  # Or use os.getenv("OPENAI_API_KEY")

st.title("Smart FAQ Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask a question:", key="input")

if user_input:
    st.session_state.chat.append(("You", user_input))

    prompt = f"You are a helpful assistant for Stevens Graduate Admissions. Here’s a question: {user_input}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response['choices'][0]['message']['content']
    st.session_state.chat.append(("Bot", answer))

for sender, msg in st.session_state.chat:
    st.markdown(f"**{sender}:** {msg}")
