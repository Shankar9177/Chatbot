# chatbot_app.py file
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


# st.image("QG_logo3.png")  # Adjust width as needed
# st.header("QueryGenie🧞")

# Set page configuration with the genie image
# st.set_page_config(page_title="QueryGenie", page_icon="QG_logo3.png")
# st.image("QG_logo3.png")

# Placeholder for user profile in the sidebar
 
# st.sidebar.image("user_icon.png",  width=100)
# st.sidebar.header("Logged in as Shankar")


st.title("Chatbot : ChatGPT and Streamlit Chat")
st.subheader("AI Tutor:")

model = st.selectbox(
    "Select a model",
    ("gpt-3.5-turbo",)
)
# removed gpt-4 as it doesn't exist in OpenAI

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Query: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()
#we process the user's query and generate the AI response
if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

    # with st.expander("Show Messages"):
    #     st.write(messages)
