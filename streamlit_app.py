import streamlit as st

# Page setup
st.set_page_config(page_title="Stevens Graduate Advisor Bot", page_icon="🎓")
st.title("🎓 Graduate Academics Advisor Chatbot")

# Inject custom CSS
st.markdown("""
    <style>
        .chat-message {
            padding: 0.8rem 1rem;
            border-radius: 12px;
            margin-bottom: 10px;
            max-width: 80%;
            word-wrap: break-word;
        }

        .user-msg {
            background-color: #dceeff;
            text-align: right;
            margin-left: auto;
        }

        .bot-msg {
            background-color: #eaeaea;
            text-align: left;
            margin-right: auto;
        }

        .chat-container {
            display: flex;
            flex-direction: column;
        }

        .stTextInput > div > input {
            background-color: #fff;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
Hi there! I'm **GradAdviserBot**, your virtual Graduate Academics Advisor here at Stevens.  
I'm here to help answer your questions about applications, transcripts, dual degrees, and more.  
Just ask me a question below — I’ll do my best to help! 👇
""")

# Session state to store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# FAQ knowledge base
faq = {
    "application requirements": "To apply, you'll need an online application, official transcripts, two letters of recommendation, a personal statement, a resume (for business programs), and a $60 fee. GRE/GMAT or English proficiency may also be required depending on your program.",
    
    "check application status": "You can check your status anytime by logging into the [application status portal](https://gradapp.stevens.edu/). You'll see updates from both yourself and the admissions office there.",
    
    "admissions decision": "Master's applications are typically reviewed within 3–4 weeks. Ph.D. decisions take about 6 weeks after the deadline. Once a decision is made, you’ll get an email notification to check your status portal.",
    
    "official transcript": "An official transcript is one sent directly from your institution in a sealed envelope or via a verified electronic sender. It must include a signature or seal and a certified English translation if needed.",
    
    "stevens graduate transcripts": "If you earned a degree at Stevens before, you don’t need to resubmit your transcripts. We’ll upload them for you automatically.",
    
    "academic calendar": "Stevens runs on a 15-week semester system for both fall and spring. You can view the full academic calendar [here](https://www.stevens.edu/academics/academic-calendar).",
    
    "pursuing two programs": "Yes! Stevens offers interdisciplinary graduate programs. Submit a written proposal to the Dean of Graduate Academics. If approved, a faculty committee will help you create a study plan. One faculty member will be your advisor throughout the process.",
    
    "funding": "Assistantships are limited and competitive. If you’re not awarded one in your first year, you can still pursue opportunities within your department after you arrive."
}

# Message formatter with styled HTML
def format_message(sender, message):
    css_class = "user-msg" if sender.lower() == "you" else "bot-msg"
    return f'<div class="chat-message {css_class}"><strong>{sender}:</strong> {message}</div>'

# User input
user_input = st.text_input("Type your question here:")

# Handle user interaction
if user_input:
    st.session_state.messages.append(("You", user_input))

    response = "I'm sorry, I couldn't find info on that. Try rephrasing or contact gradadmissions@stevens.edu."

    for keyword in faq:
        if keyword in user_input.lower():
            response = faq[keyword]
            break

    st.session_state.messages.append(("GradAdviserBot", response))

# Render conversation with styles
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, msg in st.session_state.messages:
    st.markdown(format_message(sender, msg), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
