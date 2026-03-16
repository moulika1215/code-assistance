import streamlit as st
import base64

# Function to set background image
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Make all text bright */
    h1, h2, h3, p, div, label {{
        color: black !important;
        font-weight: bold;
    }}

    /* Chat message color */
    .stChatMessage {{
        color: black !important;
    }}

    </style>
    """

    st.markdown(bg_style, unsafe_allow_html=True)


# Call background function
set_bg("robo.jpg")   # put your image name here

st.title("Customer Support Chatbot")

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chatbot logic
def support_bot(question):

    question = question.lower()

    if "hi" in question or "hello" in question:
        return "Hello! How can I help you today?"

    elif "refund" in question:
        return "Our refund policy allows returns within 30 days."

    elif "shipping" in question:
        return "Shipping usually takes 3–5 business days."

    elif "order" in question:
        return "Please provide your order ID to check the status."

    else:
        return "Sorry, I didn't understand your question."


# User input
user_input = st.chat_input("Ask your question")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    reply = support_bot(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)