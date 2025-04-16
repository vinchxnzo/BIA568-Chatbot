import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Your FAQ bank
faq = {
    "application status": "You can check your application status via the portal.",
    "transcript": "A transcript is official if it is sealed and sent by your institution.",
    "academic calendar": "Stevens follows a 15-week semester system with fall and spring terms.",
}

# Match function using spaCy
def find_best_match(user_input):
    doc1 = nlp(user_input)
    best_match = None
    highest_score = 0
    for key in faq:
        doc2 = nlp(key)
        score = doc1.similarity(doc2)
        if score > highest_score:
            highest_score = score
            best_match = key
    if highest_score > 0.65:  # tweak this threshold if needed
        return faq[best_match]
    else:
        return "Sorry, I couldn’t understand that. Try rephrasing."

# Streamlit UI
st.title("Stevens Grad Admissions Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.chat.append(("You", user_input))
    reply = find_best_match(user_input)
    st.session_state.chat.append(("Bot", reply))

for sender, msg in st.session_state.chat:
    st.markdown(f"**{sender}:** {msg}")
