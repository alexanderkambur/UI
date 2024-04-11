import streamlit as st

# Hide the Streamlit menu
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

#Possible to add disclaimer above chatInput

with st.sidebar:
    st.markdown("Welcome! This page allows you to interact with the Chatbot.")

st.title("Chatbot")
st.caption("Powered by Mistral7B and RAG to provide context aware responses to user queries.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    msg = "Chatbot unavailable at the moment."
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
