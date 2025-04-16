import streamlit as st

st.title("Stevens Graduate Admissions Chatbot")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", key="input")

# Define a simple FAQ dictionary
faq = {
    "application requirements": "Applicants must submit an online application, official transcripts, two letters of recommendation, a personal statement, a resume (for School of Business applicants), and a $60 application fee. GRE/GMAT scores and proof of English proficiency may also be required.",
    "application deadline": "Applications are accepted on a rolling basis, but it's recommended to apply by the suggested deadlines to ensure timely review.",
    "check application status": "You can check your application status by logging into the online application status portal.",
    "transcripts": "Submit official transcripts from all institutions attended. Unofficial transcripts can be uploaded for initial review, but official ones are required for final admission.",
    "funding": "Assistantships are limited. If not awarded initially, you may pursue opportunities within your department after arrival."
}

# Generate bot response
if user_input:
    st.session_state.messages.append(("You", user_input))
    response = "I'm sorry, I don't have information on that topic."
    for key in faq:
        if key in user_input.lower():
            response = faq[key]
            break
    st.session_state.messages.append(("Bot", response))

# Display conversation
for sender, message in st.session_state.messages:
    st.markdown(f"**{sender}:** {message}")
