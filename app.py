import streamlit as st
from openaichatbot import TravelBot

# Initialize bot
bot = TravelBot()

st.set_page_config(page_title="Paris Travel Guide Bot")

st.title("Paris Travel Guide Bot")
st.markdown(
    "Ask questions about Paris landmarks or type `landmark: <name>` to get info from the local database."
)

# Conversation history stored in session state
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    if user_input.lower().startswith("landmark:"):
        landmark_name = user_input.split(":", 1)[1].strip()
        answer = bot.get_landmark_info(landmark_name)
    else:
        answer = bot.ask(user_input)

    # Store in history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", answer))

# Display conversation
for speaker, message in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
