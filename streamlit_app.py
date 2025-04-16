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

    "check application status": "Once you've submitted your application, you can check updates through the online application status portal.",

    "admission decision notification": "Master’s applications are reviewed within 3–4 weeks, but timing may vary. You’ll get an email when there’s an update on your application status. Ph.D. decisions are generally made ~6 weeks after the deadline.",

    "official transcript": "A transcript is considered official if it is sent in a sealed envelope from the institution, provided by the student in a sealed unopened envelope, or sent electronically through a verified sender. It must also contain a seal/signature and legal translation if not in English.",

    "stevens graduate transcripts": "If you previously graduated from Stevens, you do not need to upload your transcripts again. The Graduate Admissions team will retrieve and upload them for you.",

    "academic calendar": "Stevens follows a traditional semester system with fall and spring semesters (15 weeks each). The full academic calendar is available on the Stevens website.",

    "pursuing two programs": "Yes, Stevens offers interdisciplinary graduate programs. To pursue two programs, you’ll need to submit a written proposal to the Dean of Graduate Academics. If approved, a committee will help you finalize a study plan."
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
